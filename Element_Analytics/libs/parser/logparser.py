"""This module handles log file by parsing input logs
and return a condensed version of the logs with nonessential
information removed. The return data structures can be either
a list of entries or a dataframe supported by Pandas library"""

from libs.parser.tokenizer import LogTokenizer
import os.path
import multiprocessing as mp
import libs.parser.logfields as field


tokenizer = LogTokenizer().build()


def validate_path(path_to_file):
    """check if path is valid"""
    if not os.path.isfile(path_to_file):
        print("File does not exist. Exit")
        exit()


def parse_line(line):
    """parse a single line of log"""
    tokens = {
        field.DATE : None,
        field.NAME : None,
        field.TYPE : None,
        field.INFO : None,
        field.MSSG : None
    }
    tokenizer.input(line)
    for tok in tokenizer:
        tokens[tok.type] = tok.value
    return tokens


def parse_file(path_to_file):
    """parse a log file into a list of log entries in dictionaries"""
    validate_path(path_to_file)
    entries = []
    try:
        with open(path_to_file, 'r') as f:
            for l in f:
                entries.append(parse_line(l))
    except IOError as e:
        print("Couldn't read file. Error: ", e)
        exit()
    return entries


def worker_process(queue, l):
    """worker process, parse line and append to list"""
    while True:
        item = queue.get()
        if item is None:
            break
        l.append(parse_line(item))


def spawning_processes(q, l, n):
    """Spawns processes"""
    processes = []
    for i in range(n):
        p = mp.Process(target=worker_process, args=(q, l))
        p.start()
        processes.append(p)
    return processes


def join_processes(q, ps, n):
    """Join all terminated processes"""
    for i in range(n):
        q.put(None)
    q.close()
    for proc in ps:
        proc.join()


def parse_file_parallel(path_to_file):
    """Multi-processing parsing. Parse
    log file with multiple processes in
    parallel. The number of processes will
    depend on the number of CPU cores.
    WARNING: List order is not ensured."""
    validate_path(path_to_file)

    # Get number of physical CPU cores
    NUM_PROC = mp.cpu_count()
    if NUM_PROC <= 2:
        return parse_file(path_to_file)
    # Shared list
    entries = mp.Manager().list()
    # Shared queue
    queue = mp.Queue()
    try:
        with open(path_to_file, 'r') as f:
            # Spawning processes based on number of CPUs
            processes = spawning_processes(queue, entries, NUM_PROC)
            for l in f:
                queue.put(l)
    except IOError as e:
        print("Couldn't read file. Error: ", e)
        exit()

    # Joining procs
    join_processes(queue, processes, NUM_PROC)

    return entries._getvalue()

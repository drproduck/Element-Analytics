import ply.lex as lex

# List of token names.   This is always required
tokens = (
    'DATE',
    'SV_NAME',
    'TYPE',
    'CALLER',
    'MESSAGE'
)

# Token regex
t_DATE = r''
t_SV_NAME = r''
t_TYPE = r''
t_CALLER = r''
t_MESSAGE = r''


def t_NUMBER(t):
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)



t_ignore = ' \t'



def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

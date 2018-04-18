import ply.lex as lex

_DATE = 'date'
_NAME = 'sv_name'
_TYPE = 'type'
_INFO = 'metainfo'
_MSSG = 'message'


class DefaultTokenizer:

    def __init__(self):
        self.tokenizer = self.__Lexer().build()

    def parse_line(self,line):
        """parse a single line of log"""
        if not line:
            print("error: can't parse empty string")
            exit()
        tokens = {
            _DATE : None,
            _NAME : None,
            _TYPE : None,
            _INFO : None,
            _MSSG : None
        }
        self.tokenizer.input(line)
        for tok in self.tokenizer:
            tokens[tok.type] = tok.value
        return tokens

    class __Lexer(object):
        # List of token names.
        tokens = (
            _DATE,
            _NAME,
            _TYPE,
            _INFO,
            _MSSG
        )

        # Token regex and functions
        # IMPORTANT: never change the names of these functions
        t_date = r"[A-Za-z]{3}\s[0-9]{2}\s[0-9]{2}:[0-9]{2}:[0-9]+"
        t_sv_name = r"[A-Za-z_]+\[[0-9]+\]"
        t_type = r"INFO|DEBUG|WARN|ERROR"

        def t_metainfo(self,t):
            r"\s+(\.)?(?P<content>[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)+)"
            if t.value:
                t.value = t.lexer.lexmatch.group('content')
            return t

        def t_message(self,t):
            r"((\s(:|–|-\s-|\*|-)\s)|(:\s[^\[0-9]))(?P<content>.+)"
            if t.value:
                t.value = t.lexer.lexmatch.group('content')
            return t

        def t_error(self,t):
            # print("Illegal character '%s'" % t.value[0])
            t.lexer.skip(1)

        def build(self):
            self.lexer = lex.lex(module=self)
            return self.lexer


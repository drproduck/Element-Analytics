import ply.lex as lex


class LogTokenizer(object):
    # List of token names.   This is always required
    tokens = (
        'date',
        'sv_name',
        'type',
        'metainfo',
        'message'
    )

    # Token regex
    t_date = r"[A-Za-z]{3}\s[0-9]{2}\s[0-9]{2}:[0-9]{2}:[0-9]+"
    t_sv_name = r"[a-z_]+\[[0-9]+\]"
    t_type = r"INFO|DEBUG|WARNING|ERROR|EXCEPTION|CRITICAL"

    def t_metainfo(self,t):
        r"\s(?P<content>[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)+)"
        if t.value:
            t.value = t.lexer.lexmatch.group('content')
        return t

    def t_message(self,t):
        r"((\s(:|–|-\s-)\s)|(:\s\#))(?P<content>.+)"
        if t.value:
            t.value = t.lexer.lexmatch.group('content')
        return t

    def t_error(self,t):
        #print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def build(self):
        self.lexer = lex.lex(module=self)
        return self.lexer


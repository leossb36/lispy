from lark import Lark, InlineTransformer
from pathlib import Path

from .runtime import Symbol


class LispTransformer(InlineTransformer):
    def start(self, *args): 
        return [Symbol.BEGIN, *args]

    def case(self, *args):
        return [Symbol.IF, *args]

    def define(self, value):
        return [Symbol.DEFINE, value]

    def quote(self, *args):
        return [Symbol.QUOTE, *args]

    # def procedure(self, *args):
    #     return [Symbol.LET, *args]

    # def infix(self, *args):
    #     return [Symbol.COLON, *args]

    def inteiro(self, value):
        return int(value)

    def numerico(self, value):
        return float(value)

    def nome(self, value):
        return str(eval(value))

    def simbolo(self, value):
        return Symbol(value)

    def boolean(self, value):
        if (value == '#t'):
            return True
        elif(value == '#f'):
            return False

    def atomo(self, value):
        return Symbol(value)

    def lista(self, *args):
        return list(args)
    
def parse(src: int):
    """
    Compila string de entrada e retorna a S-expression equivalente.
    """
    return parser.parse(src)


def _make_grammar():
    """
    Retorna uma gramática do Lark inicializada.
    """

    path = Path(__file__).parent / 'grammar.lark'
    with open(path) as fd:
        grammar = Lark(fd, parser='lalr', transformer=LispTransformer())
    return grammar

parser = _make_grammar()
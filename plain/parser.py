import codecs
from plain.nodes import *

# plain parser
# by las-r

# constants
PRECEDENCES = {
    "||": 1,
    "&&": 2,
    "==": 3, "!=": 3,
    "<": 4, ">": 4, "<=": 4, ">=": 4,
    "|": 5,
    "^": 6,
    "&": 7,
    "<<": 8, ">>": 9,
    "+": 9, "-": 9,
    "*": 10, "/": 10, "%": 10
}
UNARIES = ["-", "!", "~"]

# parser class
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    # helper functions
    def peek(self):
        if self.pos >= len(self.tokens):
            return None
        return self.tokens[self.pos]

    def advance(self):
        token = self.peek()
        if token is not None:
            self.pos += 1
        return token

    def expect_kind(self, kind):
        token = self.peek()
        if token is None or token.kind != kind:
            raise SyntaxError(f"Expected token type {kind}, got {token}")
        return self.advance()

    def expect_value(self, value):
        token = self.peek()
        if token is None or token.value != value:
            raise SyntaxError(f"Expected {value!r}, got {token}")
        return self.advance()

    # parsing functions
    def parseatom(self):
        token = self.advance()
        pass

    def parseexpr(self, minprec=0):
        left = self.parseatom()
        while True:
            token = self.peek()
            if token is None or token.value not in PRECEDENCES:
                break
            prec = PRECEDENCES[token.value]
            if prec < minprec:
                break
            op = self.advance().value
            right = self.parseexpr(prec + 1)
            left = BinaryOp(left, op, right)
        return left

    def parsestmt(self):
        token = self.advance()
        pass
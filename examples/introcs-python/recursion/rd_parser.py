from typing import List, Tuple
from rd_nodes import Expr, Number, UnaryOp, BinOp

Token = Tuple[str, str]


# start: rd_parser
class Parser:
    """Recursive descent parser for arithmetic expressions.

    Grammar (each rule is one method):
        expr    -> term   (('+' | '-') term)*      left-associative
        term    -> unary  (('*' | '/') unary)*     left-associative
        unary   -> ('+' | '-') power | power
        power   -> primary ('^' power)?             right-associative
        primary -> NUMBER | '(' expr ')'
    """
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0

    def _current(self) -> Token:
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return ('EOF', '')

    def _advance(self) -> None:
        self.pos += 1

    def _match(self, tok_type: str, value: str = None) -> bool:
        t, v = self._current()
        if t == tok_type and (value is None or v == value):
            self._advance()
            return True
        return False

    def parse(self) -> Expr:
        result = self.expr()
        if self._current()[0] != 'EOF':
            raise SyntaxError(f"Unexpected token: {self._current()}")
        return result

    def expr(self) -> Expr:
        node = self.term()
        while self._match('OP', '+') or self._match('OP', '-'):
            op = self.tokens[self.pos - 1][1]
            node = BinOp(node, op, self.term())
        return node

    def term(self) -> Expr:
        node = self.unary()
        while self._match('OP', '*') or self._match('OP', '/'):
            op = self.tokens[self.pos - 1][1]
            node = BinOp(node, op, self.unary())
        return node

    def unary(self) -> Expr:
        if self._match('OP', '+') or self._match('OP', '-'):
            op = self.tokens[self.pos - 1][1]
            return UnaryOp(op, self.unary())
        return self.power()

    def power(self) -> Expr:
        node = self.primary()
        if self._match('OP', '^'):
            node = BinOp(node, '^', self.power())  # right-associative: recurse
        return node

    def primary(self) -> Expr:
        if self._match('NUMBER'):
            return Number(float(self.tokens[self.pos - 1][1]))
        elif self._match('OP', '('):
            node = self.expr()                      # mutual recursion
            if not self._match('OP', ')'):
                raise SyntaxError("Expected ')'")
            return node
        raise SyntaxError(f"Unexpected token: {self._current()}")
# end: rd_parser

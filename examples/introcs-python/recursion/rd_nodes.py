from typing import NamedTuple, Union


# start: rd_nodes
class Number(NamedTuple):
    value: float


class UnaryOp(NamedTuple):
    op: str
    operand: 'Expr'


class BinOp(NamedTuple):
    left: 'Expr'
    op: str
    right: 'Expr'


Expr = Union[Number, UnaryOp, BinOp]
# end: rd_nodes

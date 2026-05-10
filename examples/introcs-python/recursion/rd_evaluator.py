from rd_nodes import Expr, Number, UnaryOp, BinOp


# start: rd_evaluator
def eval_expr(node: Expr) -> float:
    """Recursively evaluate an expression AST and return a float."""
    match node:
        case Number(value):
            return value
        case UnaryOp(op, operand):
            val = eval_expr(operand)
            match op:
                case '+': return +val
                case '-': return -val
                case _: raise ValueError(f"Unknown unary op: {op}")
        case BinOp(left, op, right):
            lval = eval_expr(left)
            rval = eval_expr(right)
            match op:
                case '+': return lval + rval
                case '-': return lval - rval
                case '*': return lval * rval
                case '/': return lval / rval
                case '^': return lval ** rval
                case _: raise ValueError(f"Unknown binary op: {op}")
        case _:
            raise TypeError(f"Unknown AST node: {node}")
# end: rd_evaluator

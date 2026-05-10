from rd_tokenizer import tokenize_expr
from rd_parser import Parser
from rd_evaluator import eval_expr


# start: rd_calc
def calc(expression: str) -> float:
    """Tokenize, parse, and evaluate an arithmetic expression string."""
    tokens = tokenize_expr(expression)
    ast = Parser(tokens).parse()
    return eval_expr(ast)
# end: rd_calc


if __name__ == '__main__':
    print(calc("2 + 3 * 4"))      # 14.0
    print(calc("(2 + 3) * 4"))    # 20.0
    print(calc("2 ^ 3 ^ 2"))      # 512.0
    print(calc("-5 + 2"))          # -3.0

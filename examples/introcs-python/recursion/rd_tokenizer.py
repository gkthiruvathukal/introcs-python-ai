import tokenize
from io import BytesIO
from typing import List, Tuple

Token = Tuple[str, str]
ALLOWED_OPERATORS = {'+', '-', '*', '/', '(', ')', '^'}


# start: rd_tokenizer
def tokenize_expr(code: str) -> List[Token]:
    """Return a list of (type, value) tokens from an arithmetic expression."""
    tokens: List[Token] = []
    stream = BytesIO(code.encode('utf-8')).readline
    for tok in tokenize.tokenize(stream):
        if tok.type == tokenize.NUMBER:
            tokens.append(('NUMBER', tok.string))
        elif tok.type == tokenize.OP and tok.string in ALLOWED_OPERATORS:
            tokens.append(('OP', tok.string))
    return tokens
# end: rd_tokenizer

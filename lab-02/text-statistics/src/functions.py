import re

def count_sentences(text: str):
    reg_expr = r'(\.|\?|!)+'
    return len(re.findall(reg_expr, text))

import re

def count_sentences(text: str):
    reg_expr = r'(\.|\?|!)+'
    return len(re.findall(reg_expr, text))

def count_non_declarative_sentences(text: str):
    reg_expr = r'\.+'
    return count_sentences(text) - len(re.findall(reg_expr, text))

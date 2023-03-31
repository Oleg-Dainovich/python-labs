import re

ABBREVIATIONS = (
    'etc.', 'vs.', 'a.d.', 'b.c.', 'a.m.', 'p.m.', 'jr.',
    'sr.', 'v.i.p.', 'p.s.', 'p.p.s.', 'smth.', 'smb.', 'yr.',
    'jan.', 'feb.', 'mar.', 'jun.', 'jul.', 'aug.', 'sep.',
    'oct.', 'nov.', 'dec.', 'mon.', 'tue.', 'wed.', 'thu.',
    'fri.', 'sat.', 'sun.', 'mr.', 'mrs.', 'ms.', 'dr.',
    'st.', 'inc.', 'corp.', 'in.', 'lbs.', 'e.g.', 'i.e.'  
)

def replace_abbreviations(text: str):
    new_text = text
    for abbreviation in ABBREVIATIONS:
        new_text = re.sub(abbreviation, re.sub(r'\.', " ", abbreviation), new_text)
    return new_text

def find_words(text: str):
    words_list = re.findall(r'\w*[a-zA-Z]\w*', text)
    new_text = "".join(words_list)
    return new_text

def count_sentences(text: str):
    new_text = replace_abbreviations(text)
    print(new_text)
    reg_expr = r'(\.|\?|!)+'
    return len(re.findall(reg_expr, new_text))

def count_non_declarative_sentences(text: str):
    new_text = replace_abbreviations(text)
    reg_expr = r'\.+'
    return count_sentences(text) - len(re.findall(reg_expr, new_text))
 
def count_length_of_sentences(text: str):
    new_text = replace_abbreviations(text)
    print(new_text)
    #new_text = find_words(new_text)
    #print(new_text)
    reg_expr = r'(\w)+'
    return len(re.findall(reg_expr, new_text)) / count_sentences(text)

def count_length_of_words(text: str):
    reg_expr_letters = r'\w'
    reg_expr_words = r'(\w)+'
    return len(re.findall(reg_expr_letters, text)) / len(re.findall(reg_expr_words, text))

#def count_n_grams():

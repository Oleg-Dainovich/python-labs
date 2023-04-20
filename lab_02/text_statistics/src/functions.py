import re
from collections import defaultdict

ABBREVIATIONS = (
    ' etc.', ' vs.', ' a.d.', ' b.c.', ' a.m.', ' p.m.', ' jr.',
    ' sr.', ' v.i.p.', ' p.s.', ' p.p.s.', ' smth.', ' smb.', ' yr.',
    ' jan.', ' feb.', ' mar.', ' jun.', ' jul.', ' aug.', ' sep.',
    ' oct.', ' nov.', ' dec.', ' mon.', ' tue.', ' wed.', ' thu.',
    ' fri.', ' sat.', ' sun.', ' mr.', ' mrs.', ' ms.', ' dr.',
    ' st.', ' inc.', ' corp.', ' lbs.', ' e.g.', ' i.e.', ' in.'  
)

def replace_abbreviations(text: str):
    new_text = text
    for abbreviation in ABBREVIATIONS:
        new_text = re.sub(abbreviation, re.sub(r'\.', " ", abbreviation), new_text)     #change dots to spaces in abbreviations
    return new_text

def find_words(text: str):
    words_list = re.findall(r'\w*[a-zA-Z]\w*', text)                                    #remove numbers and punctuation
    new_text = " ".join(words_list)                                                     #join list to string
    return new_text

def count_sentences(text: str):
    new_text = replace_abbreviations(text)
    reg_expr = r'(\.|\?|!)+'
    return len(re.findall(reg_expr, new_text))

def count_non_declarative_sentences(text: str):
    new_text = replace_abbreviations(text)
    reg_expr = r'\.+'
    return count_sentences(text) - len(re.findall(reg_expr, new_text))
 
def count_length_of_sentences(text: str):
    new_text = find_words(text)
    reg_expr = r'(\w)+'
    try:
        return len(re.findall(reg_expr, new_text)) / count_sentences(text)
    except ZeroDivisionError:
        return 0

def count_length_of_words(text: str):
    new_text = find_words(text)
    reg_expr_letters = r'\w'
    reg_expr_words = r'(\w)+'
    try:
        return len(re.findall(reg_expr_letters, new_text)) / len(re.findall(reg_expr_words, new_text))
    except ZeroDivisionError:
        return 0

def get_n_grams(text: str, n: int):
    words_list = re.findall(r'\w*[a-zA-Z]\w*', text)
    n_grams_list: list[str] = []
    for word in words_list:
        if len(word) >= n:
            for i in range(0, len(word) - n + 1):
                n_grams_list.append("".join(word[i: i + n]))                            #add n-gram to list
    print(n_grams_list)
    return n_grams_list

def get_top_k_n_grams(text: str, k: int, n: int):
    n_grams_list = get_n_grams(text, n)
    top_k_n_grams = defaultdict(int)
    for n_gram in n_grams_list:
        top_k_n_grams[n_gram] += 1
    #top_k_n_grams = Counter(n_grams_list).most_common(k)                               #count most repeated n-grams and sort it
    return sorted(top_k_n_grams.items(), key = lambda item: item[1], reverse=True)      #sort dict by value

def print_top_k_n_grams(text: str, k: int = 10, n: int = 4):
    top_k_n_grams = get_top_k_n_grams(text, k, n)
    print("Top", k, "N-grams:")
    for n_gram, amount in top_k_n_grams:
        print("N-gram:", n_gram, "|", amount, "appearance(s)")
    return

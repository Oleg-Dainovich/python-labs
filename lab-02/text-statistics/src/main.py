from functions import (
    count_sentences, 
    count_non_declarative_sentences, 
    count_length_of_sentences,
    count_length_of_words,
    print_top_k_n_grams
)

text = input('Enter the text: ')
text = text.lower()

print('Amount of sentences in the text:', count_sentences(text))
print('Amount of non-declarative sentences in the text:', count_non_declarative_sentences(text))
print('Average length of the sentence:', count_length_of_sentences(text))
print('Average length of the word:', count_length_of_words(text))

k, n = map(int, input('Enter K and N for N-grams: ').split())
print_top_k_n_grams(text, k, n)

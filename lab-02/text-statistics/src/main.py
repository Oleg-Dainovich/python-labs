from functions import (
    count_sentences, 
    count_non_declarative_sentences, 
    count_length_of_sentences
)

text = input('Enter the text: ')

print('Amount of sentences in the text: ', count_sentences(text))
print('Amount of non-declarative sentences in the text: ', count_non_declarative_sentences(text))
print('Average length of the sentence: ', count_length_of_sentences(text))

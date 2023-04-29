import unittest
from ..src.functions import (
    replace_abbreviations,
    find_words,
    count_sentences,
    count_non_declarative_sentences,
    count_length_of_sentences,
    count_length_of_words,
    get_n_grams,
    get_top_k_n_grams
)

class ReplaceAbbreviationsTestCase(unittest.TestCase):
    def test_abbr_1(self):
        res = replace_abbreviations("Hello, World!")
        self.assertEqual(res, "Hello, World!")

    def test_abbr_2(self):
        res = replace_abbreviations("Hello, mr. Bond...")
        self.assertEqual(res, "Hello, mr  Bond...")

    def test_abbr_3(self):
        res = replace_abbreviations("Now is 11 p.m..")
        self.assertEqual(res, "Now is 11 p m .")

    def test_abbr_4(self):
        res = replace_abbreviations("")
        self.assertEqual(res, "")

    def test_abbr_5(self):
        res = replace_abbreviations("This is v.i.p. person!???!?!!?!?")
        self.assertEqual(res, "This is v i p  person!???!?!!?!?")

class FindWordsTestCase(unittest.TestCase):
    def test_find_words_1(self):
        res = find_words("")
        self.assertEqual(res, "")

    def test_find_words_2(self):
        res = find_words("abc a1b2c3 abc1 1abc 123 11b1")
        self.assertEqual(res, "abc a1b2c3 abc1 1abc 11b1")

    def test_find_words_3(self):
        res = find_words("adw12dqd2331!")
        self.assertEqual(res, "adw12dqd2331")

    def test_find_words_4(self):
        res = find_words("Hello, World!")
        self.assertEqual(res, "Hello World")

    def test_find_words_5(self):
        res = find_words("Hello,,,World!!??!??!?!?!?")
        self.assertEqual(res, "Hello World")

class CountSentencesTestCase(unittest.TestCase):
    def test_count_sent_1(self):
        res = count_sentences("What's in the box?")
        self.assertEqual(res, 1)

    def test_count_sent_2(self):
        res = count_sentences("Sentence")
        self.assertEqual(res, 0)

    def test_count_sent_3(self):
        res = count_sentences("Yeah buddy!Light weight baby!!!!!")
        self.assertEqual(res, 2)

    def test_count_sent_4(self):
        res = count_sentences(
            """ Welcome to Fight Club. 
            The first rule of Fight Club is: you do not talk about Fight Club. 
            The second rule of Fight Club is: you DO NOT talk about Fight Club! 
            Third rule of Fight Club: if someone yells “stop”, goes limp, or taps out, the fight is over. 
            Fourth rule: only two guys to a fight. 
            Fifth rule: one fight at a time, fellas. 
            Sixth rule: the fights are bare knuckle. No shirt, no shoes, no weapons. 
            Seventh rule: fights will go on as long as they have to. 
            And the eighth and final rule: if this is your first time at Fight Club, you have to fight.""")
        self.assertEqual(res, 10)

    def test_count_sent_5(self):
        res = count_sentences("""People... The whole world knows what pain is!!! 
        And this fear will be the medicine that will stop the war!?!?!?!?!? 
        This world has not yet reached a state of equilibrium, we can say that it is still growing. 
        Pain will make the world grow up, as it did me. After all, our world is just a child.""")
        self.assertEqual(res, 6)

class CountNonDeclarativeSetencesTestCase(unittest.TestCase):
    def test_count_non_decl_sent_1(self):
        res = count_non_declarative_sentences("")
        self.assertEqual(res, 0)

    def test_count_non_decl_sent_2(self):
        res = count_non_declarative_sentences("Man, this party stinks. I fucking hate these people!")
        self.assertEqual(res, 1)

    def test_count_non_decl_sent_3(self):
        res = count_non_declarative_sentences("See you space cowboy...")
        self.assertEqual(res, 0)

    def test_count_non_decl_sent_4(self):
        res = count_non_declarative_sentences("Believe in the me that believes in you!!!! Let's see you grit those teeth!???!!")
        self.assertEqual(res, 2)

    def test_count_non_decl_sent_5(self):
        res = count_non_declarative_sentences("""In this world, is the destiny of mankind controlled 
        by some transcendental entity or law? Is it like the hand of God hovering above? 
        At least it is true that man has no control, even over his own will. 
        Man takes up the sword in order to shield the small wound in his heart sustained in a far-off time beyond remembrance. 
        Man wields the sword so that he may die smiling in some far-off time beyond perception.""")
        self.assertEqual(res, 2)

class CountLengthOfSentencesTestCase(unittest.TestCase):
    def test_count_len_of_sent_1(self):
        res = count_length_of_sentences("")
        self.assertEqual(res, 0)

    def test_count_len_of_sent_2(self):
        res = count_length_of_sentences("Hello, World.")
        self.assertEqual(res, 2)

    def test_count_len_of_sent_3(self):
        res = count_length_of_sentences("""Nobody believes in you! 
        You have lost again, and again, and again. 
        The lights are cut off, but you still are looking at your dream, 
        reviewing it every day and say to yourself: It is not over until I win!!!""")
        self.assertAlmostEqual(res, 13.333333333333334)

    def test_count_len_of_sent_4(self):
        res = count_length_of_sentences("Ryan Gosling in Drive. This is mr. Ryan Gosling!")
        self.assertEqual(res, 4.5)

    def test_count_len_of_sent_5(self):
        res = count_length_of_sentences("Top G always wake up at 6 a.m.!")
        self.assertEqual(res, 8)

class CountLengthOfWordsTestCase(unittest.TestCase):
    def test_count_len_of_words_1(self):
        res = count_length_of_words("")
        self.assertEqual(res, 0)

    def test_count_len_of_words_2(self):
        res = count_length_of_words("How would you rate this girl from 1 to 10?")
        self.assertEqual(res, 3.625)

    def test_count_len_of_words_3(self):
        res = count_length_of_words("a1b2c3 123 111aaa abcd")
        self.assertEqual(res, 5.333333333333333)

    def test_count_len_of_words_4(self):
        res = count_length_of_words("I am Eikichi Onizuka, I am 22 years old. Single.")
        self.assertEqual(res, 3.7777777777777777)

    def test_count_len_of_words_5(self):
        res = count_length_of_words("Top G always goes to bed at 11 p.m.!")
        self.assertEqual(res, 2.5555555555555554)

class GetNGramsTestCase(unittest.TestCase):
    def test_get_n_grams_1(self):
        res = get_n_grams("", 0)
        self.assertEqual(res, [])

    def test_get_n_grams_2(self):
        res = get_n_grams("Hello, World!", 2)
        self.assertEqual(res, ['He', 'el', 'll', 'lo', 'Wo', 'or', 'rl', 'ld'])

    def test_get_n_grams_3(self):
        res = get_n_grams("Hello, World!", 10)
        self.assertEqual(res, [])

    def test_get_n_grams_4(self):
        res = get_n_grams("abc abcde abcde1 12345 a12345", 5)
        self.assertEqual(res, ['abcde', 'abcde', 'bcde1', 'a1234', '12345'])

    def test_get_n_grams_5(self):
        res = get_n_grams("dattebayo", 4)
        self.assertEqual(res, ['datt', 'atte', 'tteb', 'teba', 'ebay', 'bayo'])

class GetTopKNGramsTestCase(unittest.TestCase):
    def test_get_top_k_n_grams_1(self):
        res = get_top_k_n_grams("", 3, 2)
        self.assertEqual(res, [])

    def test_get_top_k_n_grams_2(self):
        res = get_top_k_n_grams("abc abcde abcde1 12345 a12345", 3, 2)
        self.assertEqual(res, [('ab', 3), ('bc', 3), ('cd', 2)])

    def test_get_top_k_n_grams_3(self):
        res = get_top_k_n_grams("abcde,,, a1b2c3!!! a1b2c3d4e5::: 123... abc??? a1?!?!?!", 10, 2)
        self.assertEqual(res, [('a1', 3), ('ab', 2), 
                               ('bc', 2), ('1b', 2), 
                               ('b2', 2), ('2c', 2), 
                               ('c3', 2), ('cd', 1), 
                               ('de', 1), ('3d', 1)])

    def test_get_top_k_n_grams_4(self):
        res = get_top_k_n_grams("abc abcd abc abcde abc abcdef", 15, 3)
        self.assertEqual(res, [('abc', 6), ('bcd', 3), ('cde', 2), ('def', 1)])

    def test_get_top_k_n_grams_5(self):
        res = get_top_k_n_grams("a", 100, 100)
        self.assertEqual(res, [])

if __name__ == "__main__":
    unittest.main()
        
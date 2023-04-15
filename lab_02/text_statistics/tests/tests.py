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
        res = find_words("abc a1b2c3 abc1 1abc 123 1b1")
        self.assertEqual(res, "abc a1b2c3 abc1 1abc 1b1")

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
        res = count_length_of_sentences("")
        self.assertEqual(res, 0)

    def test_count_len_of_sent_5(self):
        res = count_length_of_sentences("")
        self.assertEqual(res, 0)

if __name__ == "__main__":
    unittest.main()
        



#Nobody believes in you! You have lost again, and again, and again! The lights are cut off, but you still are looking at your dream, reviewing it every day and say to yourself: It is not over until I win!!!
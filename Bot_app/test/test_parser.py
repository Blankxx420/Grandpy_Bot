from Bot_app.stopword import STOPWORDS
from config import PUNCTUATION
import re


def test_remove_punctuation():
    question = "je suis là/ depuis bien longtemps !?"
    for char in question:
        if char in PUNCTUATION:
            assert question.replace(char, " ")


def test_sentence_lower():
    question = "A la recherche du Louvres"
    assert question.lower()


def test_remove_all_symbols():
    question = "@paris ="
    assert re.sub("r/W", " ", question)


def test_separate_word():
    question = "ou est paris"
    assert question.split(" ")


def test_remove_stopword():
    question = ["je suis à la recherche ainsi de paris"]
    for word in STOPWORDS:
        if word in question:
            assert question.remove(word)

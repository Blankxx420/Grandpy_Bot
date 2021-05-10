from Bot_app.stopword import STOPWORDS
import re


def test_sentence_lower():
    question = "A la recherche du Louvres"
    assert question.lower()


def test_remove_stopword():
    question = ["je suis à la recherche ainsi de paris"]
    for word in STOPWORDS:
        if word in question:
            assert question.remove(word)


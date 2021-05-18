"""Parser Module that will analyze question from user by:
    - removing symbols
    - removing punctuation
    - make it lower
    - separate word
    - removing word from list of stopword
"""
import re
from Bot_app.stopword import STOPWORDS
from config import PUNCTUATION


class Parser:
    """represent the parser"""

    def __init__(self, question):
        self.stop_word = STOPWORDS
        self.question = question
        self.delete_all_symbols()
        self.question_lower()
        self.remove_punctuation()
        self.separate_word()
        self.remove_stop_word()

    def delete_all_symbols(self):
        """ Remove all symbols"""
        self.question = re.sub('r/W', " ", self.question)

    def question_lower(self):
        """Makes the question in lower case"""
        self.question = self.question.lower()

    def remove_punctuation(self):
        """Removes punctuation in question"""
        for char in self.question:
            if char in PUNCTUATION:
                self.question = self.question.replace(char, " ")

    def separate_word(self):
        """Separate word in question to create list of word"""
        self.question = self.question.split()

    def remove_stop_word(self):
        """removes stopword contains in question to get relevant word"""
        for words in self.stop_word:
            if words in self.question:
                self.question.remove(words)
        print(self.question)

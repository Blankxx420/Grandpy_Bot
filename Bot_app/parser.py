import json
import re



class Parser:

    def __init__(self, question_ask):
        self.stop_word = 'stopword.json'
        self.question_ask = question_ask

    def delete_all_symbols(self, question):
        re.sub('r/W " "', question)
        print(question)

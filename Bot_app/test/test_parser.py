from Bot_app.parser import Parser


question_1 = "où se trouve Paris ?"
question_2 = "montre-moi Bordeaux"


def test_parser_question_1():
    parser = Parser(question_1)
    assert parser.parsed_question == ["trouve", 'paris']


def test_parser_question_2():
    parser = Parser(question_2)
    assert parser.parsed_question == ["montre-moi", "bordeaux"]



"""
    Código para executar pré-processamento dos textos

"""

import spacy
from unidecode import unidecode


class PreProcessText:
    def __init__(self, model):
        self.nlp_model = spacy.load(model)

    def is_date_format(self, text):
        return (
            len(text) == 10
            and text[2] == "/"
            and text[5] == "/"
            and text[:2].isdigit()
            and text[3:5].isdigit()
            and text[6:].isdigit()
        )

    DEBUG = True

    def process_text(self, text):
        print("entrou")
        doc_ = self.nlp_model(text)
        # Adicionei "" para remover as palavras vazias e len(token.lemma_.strip()) > 3 para remover palavras com 3 caracter
        tokens = []
        for token in doc_:
            if (
                not token.lemma_.is_stop
                and not token.lemma_.is_punct
                and token.lemma_.strip() != ""
                and len(token.lemma_.strip()) > 3
            ):
                if not (
                    any(char.isdigit() for char in token.lemma_.text)
                    and not self.is_date_format(token.text)
                ):
                    tokens.append(unidecode(token.lemma_.lower().strip()))
                    print(token.lemma_.lower().strip())
                    print("saiu")

        return tokens

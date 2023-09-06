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

    # def process_text(self, text):
    #     doc_ = self.nlp_model(text)
    #     # adicionei "" para remover as palavras vazias e len(token.lemma_.strip()) > 1 para remover palavras com 1 caracter
    #     tokens = [
    #         unidecode(token.lemma_.lower().strip())
    #         for token in doc_
    #         if not token.is_stop
    #         and not token.is_punct
    #         and token.lemma_.strip() != ""
    #         and len(token.lemma_.strip()) > 3
    #         # and not any(char.isdigit() for char in token.text)
    #     ]

    #     return tokens

    def process_text(self, text):
        doc_ = self.nlp_model(text)
        # Adicionei "" para remover as palavras vazias e len(token.lemma_.strip()) > 1 para remover palavras com 1 caracter
        tokens = []
        for token in doc_:
            if (
                not token.is_stop
                and not token.is_punct
                and token.lemma_.strip() != ""
                and len(token.lemma_.strip()) > 3
            ):
                if not (
                    any(char.isdigit() for char in token.text)
                    and not self.is_date_format(token.text)
                ):
                    tokens.append(unidecode(token.lemma_.lower().strip()))

        return tokens

import spacy
from unidecode import unidecode


class PreProcessText:
    def __init__(self, model):
        self.nlp_model = spacy.load(model)

        # def is_date_format(self, text):
        #     return (
        #         len(text) == 10
        #         and text[2] == "/"
        #         and text[5] == "/"
        #         and text[:2].isdigit()
        #         and text[3:5].isdigit()
        #         and text[6:].isdigit()
        #     )

    def process_text(self, text):
        doc_ = self.nlp_model(text.lower())
        tokens = [
            token.text.lower()
            for token in doc_
            if not (
                token.is_stop
                or token.is_punct
                or token.lemma_.strip() == ""
                or len(token.lemma_.strip()) <= 5
                or any(char.isdigit() for char in token.text)
            )
        ]
        return " ".join(tokens)


if __name__ == "__main__":
    # Para testar esse código, use via terminal na raiz do projeto: python -m modules.preprocess.pre_process_text

    pp = PreProcessText("pt_core_news_lg")
    tokens = pp.process_text(
        "Os ARTIGOS foram publicados na última conferência. A administração emitiu um ato administrativo."
    )
    print(tokens)

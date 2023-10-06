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
        
        tokens = []
        words = []
        for token in doc_:
            words.append(token)
            if (
                not token.is_stop # Remove stopwords
                and not token.is_punct # Remove pontuação
                and token.lemma_.strip() != "" # Remove palavras vazias
                and len(token.lemma_.strip()) > 5 # Remove falavras de tamanaho menor que 5
            ):
                if not (
                    any(char.isdigit() for char in token.text)
                    # and not self.is_date_format(token.text)
                ):
                    tokens.append(unidecode(token.lemma_.strip()))
                    
        return tokens


if __name__ == "__main__":

    # Para testar esse código, use via terminal na raiz do projeto: python -m modules.preprocess.pre_process_text

    pp = PreProcessText("pt_core_news_lg")
    tokens = pp.process_text("Os ARTIGOS foram publicados na última conferência. A administração emitiu um ato administrativo.")
    print(tokens)
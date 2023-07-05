'''
    Código para executar pré-processamento dos textos

'''

import spacy 
from unidecode import unidecode


class PreProcessText():

    def __init__(self, model):
        
        self.nlp_model = spacy.load(model)    


    def process_text(self, text):

        doc_ = self.nlp_model(text)
        
        tokens = [unidecode(token.lemma_.lower()) for token in doc_ if not token.is_stop and not token.is_punct]

        return tokens
        
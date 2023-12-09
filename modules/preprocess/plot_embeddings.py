import spacy
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE


class PlotEmbeddings:
    def __init__(self, model):
        self.nlp_model = spacy.load(model)

    def plot_embeddings(self, palavras):
        
        word_embeddings = []
        for palavra in palavras:
            token = self.nlp_model(palavra)[
                0
            ]  
            embedding = token.vector  # Obter o vetor de embedding da palavra
            word_embeddings.append(embedding)

        # Convertendo a lista de embeddings em um array numpy
        word_embeddings = np.array(word_embeddings)

       
        tsne = TSNE(n_components=2, random_state=0)
        embeddings_tsne = tsne.fit_transform(word_embeddings)

        
        plt.scatter(embeddings_tsne[:, 0], embeddings_tsne[:, 1])

        
        for i, palavra in enumerate(palavras):
            plt.annotate(palavra, (embeddings_tsne[i, 0], embeddings_tsne[i, 1]))

        # Exibir o gráfico
        plt.show()

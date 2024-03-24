from bertopic import BERTopic

class ExtractTopics():

    def __init__(self,model='default'):

        if model == 'default':
            self.bert_model = BERTopic(language='portuguese', min_topic_size=2, nr_topics="auto")

        elif model == 'gpt':
            import openai
            from bertopic.backend import OpenAIBackend

            client = openai.OpenAI(api_key="sk-...")
            embedding_model = OpenAIBackend(client, "text-embedding-ada-002")

            topic_model = BERTopic(embedding_model=embedding_model, language='portuguese', min_topic_size=2, nr_topics="auto")

        elif model == 'zeroshot':
            from bertopic.representation import KeyBERTInspired

            zeroshot_topic_list = ["Aquisições Diretas",
                                    "Contratações Emergenciais",
                                    "Dispensas de Licitação"]

            self.bert_model = BERTopic(
                embedding_model="thenlper/gte-small",
                language="portuguese",
                nr_topics="auto",
                min_topic_size=2,
                zeroshot_topic_list=zeroshot_topic_list,
                zeroshot_min_similarity=.85,
                representation_model=KeyBERTInspired())


    def extract_topics(self, text):

        self.bert_model.fit_transform(text)
        topics = self.bert_model.get_topics()
        topics_info = self.bert_model.get_topic_info()
        #new_topics = topic_model.reduce_outliers(abstracts, topics)
        #topic_model.update_topics(docs, topics=new_topics)
        

        return topics, topics_info
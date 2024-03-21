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



    def extract_topics(self, text):

        self.bert_model.fit_transform(text)
        topics = self.bert_model.get_topics()
        topics_info = self.bert_model.get_topic_info()
        

        return topics, topics_info
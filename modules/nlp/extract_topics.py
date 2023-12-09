from bertopic import BERTopic

class ExtractTopics:

    def __init__(self):
        self.bert_model = BERTopic(language='portuguese', min_topic_size=2)

    def extract_topics(self, text):
        model_ = self.bert_model.fit_transform(text)
        topics = model_.get_topics()
        return topics

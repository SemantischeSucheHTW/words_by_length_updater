from kafka import KafkaConsumer

import json
from datetime import datetime

class KafkaSource:

    def __init__(self, config):

        config["key_deserializer"] = lambda k: k.decode("utf-8")
        config["value_deserializer"] = lambda k: json.loads(k)
        topic = config.pop("topic")

        self.consumer = KafkaConsumer(topic, **config)

    def getWordList(self):
        kv = next(self.consumer)
        assert isinstance(kv.value, list)
        return kv.value
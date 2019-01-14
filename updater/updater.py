#from kafka import KafkaConsumer

import json
from datetime import datetime

class Updater:

    def __init__(self, dao):
        self.dao = dao

    def put(self, new_words):
        word_len_dict = {}
        for word in new_words:
            try:
                values = word_len_dict[len(word)]
                values.append(word)
            except:
                values = [word]
            word_len_dict[len(word)] = values
        #print(word_len_dict)
        self.dao.updateWordsByLengthMatrix(word_len_dict)
        return word_len_dict
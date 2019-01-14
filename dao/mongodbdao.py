from pymongo import MongoClient

import datetime

class MongoDBDao():

    def __init__(self, config):

        conf_copy = dict(config)
        db = conf_copy.pop("db")
        words_by_length_collection_name = conf_copy.pop("words_by_length_collection")

        self.client = MongoClient(**conf_copy)
        self.db = self.client[db]
        self.words_by_length_collection = self.db[words_by_length_collection_name]

    def updateWordsByLengthMatrix(self, new_word_len_dict):
        for key in new_word_len_dict.keys():
            #print(f"checking for key {key}")
            old_value = self.words_by_length_collection.find_one({"len":key})
            #print(f"old list is {old_value}")
            new_value = new_word_len_dict[key]
            if (old_value):
                new_value.extend(old_value["words"])
            #print(f"new list will be {new_value}")
            self.words_by_length_collection.update_one({"len":key}, {"$set": {"words":new_value}}, upsert=True)
    
    def get_all(self):
        d = {}
        for l in self.words_by_length_collection.find({}):
            d[l["len"]]=l["words"]
        return d
        
    def delete_all(self):
        self.words_by_length_collection.delete_many({})
        
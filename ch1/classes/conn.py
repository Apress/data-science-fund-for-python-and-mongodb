class conn:
    from pymongo import MongoClient
    client = MongoClient('localhost', port=27017)
    def __init__(self, dbname):
        self.db = conn.client[dbname]
    def getDB(self):
        return self.db

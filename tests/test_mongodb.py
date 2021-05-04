from unittest import TestCase

from pymongo import MongoClient

from alexandria.repository.mongodb import Shelf, ShelfInterfaceMongo
from alexandria.utils.logger import logger

logger.off = True
HOST = "mongodb://0.0.0.0"
PORT = "27017"
TEST_DATA = [
    Shelf(name="Cinema", book_ids=[1, 2]),
    Shelf(name="Anime", book_ids=[4]),
    Shelf(name="Python", book_ids=[3, 5, 6]),
]
TEST_ID = [None] * len(TEST_DATA)

def _get_db():
    client = MongoClient(host=HOST, port=int(PORT))
    return client["test"]

testdb = _get_db()
shelves = ShelfInterfaceMongo(testdb)



class TestShelfInterfaceMongo(TestCase):
    def test_create(self):
        res = shelves.create(TEST_DATA[0])
        id = res.inserted_id
        TEST_ID[0] = id
        cursor = testdb.shelves.find()
        flag = False
        for doc in cursor:
            if doc["_id"] == id:
                flag = True
        self.assertTrue(flag, "create function should update collection in mongodb!")

    def test_get(self):
        res = shelves.get(TEST_ID[0])
        self.assertEqual(TEST_ID[0], res["_id"], "get should return object with id equal to %s!" % TEST_ID[0])

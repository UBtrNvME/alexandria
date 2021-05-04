"""Mongodb implementation of the Repository Interfaces."""

from pymongo import MongoClient
from pymongo.collection import Collection

from alexandria.domain.interfaces import ShelfInterface
from alexandria.domain.models import Shelf
from alexandria.utils.logger import logger

try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus


def new_client(config):
    """Construct new client for MongoDB."""
    try:
        host = config["host"]
        user = config["user"]
        password = config["password"]
        dbname = config["dbname"]
    except KeyError:
        return None
    uri = "mongodb+srv://%s:%s@%s" % (quote_plus(user), quote_plus(password), host)

    return getattr(MongoClient(uri), dbname)


class ShelfInterfaceMongo(ShelfInterface):
    """MongoDB implementation of the ShelfInterface."""

    def delete(self, _id):
        """Delete shelf by id from Mongo Database."""

    def list(self):
        """Get all shelves from Mongo Database."""

    def update(self, _id, data):
        """Update shelf with id equal _id with data provided."""

    def get(self, _id):
        """Get shelf with id equal _id from Mongo Database."""
        collection: Collection = self._db.shelves
        shelf = collection.find_one({"_id": _id})
        return shelf

    def create(self, data: Shelf):
        """Create new shelf in Mongo Database with parameters provided in data."""
        try:
            return self._db.shelves.insert_one(data.dict())
        except Exception as e:  # pylint: disable=W0703
            logger.error("an exception occurred :: %s", e)
            return False

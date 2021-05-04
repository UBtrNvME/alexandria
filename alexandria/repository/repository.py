"""
Provides Repository layer of the application.

Design and implementation of the Repository object,
which is the innermost layer of the application.

Job of the repository object is to provide interface for data source manipulation.

Adapters that already has been implemented are:
    - MongoDB Adapter
"""
from .mongodb import ShelfInterfaceMongo


class Repository:
    """Repository class that provides interface for data source manipulation."""

    def __init__(self, db):
        """Initialise repository object."""
        self.shelves = ShelfInterfaceMongo(db)
        # self.books = BookInterfaceMongo(db)

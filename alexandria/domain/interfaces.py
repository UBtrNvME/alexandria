"""Interfaces provides abstractions for communication between layers of alexandria."""
from abc import ABC, abstractmethod


class ShelfInterface(ABC):
    """Shelf Interface Abstraction."""

    def __init__(self, db):
        """Initialise Shelf Interface."""
        self._db = db

    @abstractmethod
    def create(self, data):
        """Create shelf."""

    @abstractmethod
    def get(self, _id):
        """Get shelf by _id."""

    @abstractmethod
    def update(self, _id, data):
        """Update shelf with _id with data."""

    @abstractmethod
    def delete(self, _id):
        """Delete shelf by _id."""

    @abstractmethod
    def list(self):
        """Get all shelves."""


class BookInterface:
    """Book Interface abstraction."""

    def __init__(self, db):
        """Initialise BookInterface."""
        self._db = db

    @abstractmethod
    def create(self, data):
        """Create book."""

    @abstractmethod
    def get(self, _id):
        """Get book by _id."""

    @abstractmethod
    def update(self, _id, data):
        """Update book with _id with data."""

    @abstractmethod
    def delete(self, _id):
        """Delete book by _id."""

    @abstractmethod
    def list(self):
        """Get all books."""

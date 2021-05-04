"""Models provide inner layer entities of the alexandria application."""
from typing import List

from pydantic import BaseModel


class Shelf(BaseModel):
    """Model that describes Shelf object."""

    name: str
    book_ids: List[int]

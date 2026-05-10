

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab04.interfaces import Displayable


class ResidentialComplex:
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def get_all(self):
        return self._items.copy()

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __str__(self):
        if not self._items:
            return "Жилой комплекс пуст"
        result = f"Жилой комплекс ({len(self._items)} шт.)\n"
        for i, item in enumerate(self._items):
            result += f"{i+1}. {item.address}\n"
        return result.strip()

    def get_displayable(self):
        """Вернуть новую коллекцию только из Displayable объектов"""
        new_collection = ResidentialComplex()
        for item in self._items:
            if isinstance(item, Displayable):
                new_collection.add(item)
        return new_collection
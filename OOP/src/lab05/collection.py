
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
            result += f"{i+1}. {item.address} - {item.price} руб.\n"
        return result.strip()

    def sort_by(self, key_func, reverse=False):
        """Сортировка по переданной стратегии"""
        self._items.sort(key=key_func, reverse=reverse)
        return self

    def filter_by(self, predicate):
        """Фильтрация по переданному условию"""
        self._items = list(filter(predicate, self._items))
        return self

    def apply(self, func):
        """Применение функции к каждому элементу"""
        self._items = list(map(func, self._items))
        return self

    def copy(self):
        """Создание копии коллекции"""
        new_collection = ResidentialComplex()
        for item in self._items:
            new_collection.add(item)
        return new_collection
from typing import List
from lab06.container import TypedCollection
from lab07.models import ApartmentRent
from lab07.exceptions import DuplicateApartmentError, ApartmentNotFoundError


class ApartmentApp:
    """Бизнес-логика приложения для управления квартирами."""

    def __init__(self) -> None:
        self._collection: TypedCollection[ApartmentRent] = TypedCollection()

    def add_apartment(self, price: float, price_month: float, address: str, square: float, available: bool = True) -> None:
        """Добавляет квартиру в коллекцию. Проверяет дубликаты по адресу."""
        for apt in self._collection.get_all():
            if apt.address == address:
                raise DuplicateApartmentError(f"Квартира по адресу '{address}' уже существует")

        apt = ApartmentRent(int(price), int(price_month), address, int(square), available)
        self._collection.add(apt)

    def remove_by_address(self, address: str) -> None:
        """Удаляет квартиру по адресу."""
        to_remove = [apt for apt in self._collection.get_all() if apt.address == address]
        if not to_remove:
            raise ApartmentNotFoundError(f"Квартира по адресу '{address}' не найдена")

        for apt in to_remove:
            self._collection.remove(apt)

    def get_all(self) -> List[ApartmentRent]:
        """Возвращает все квартиры."""
        return self._collection.get_all()

    def find_by_address(self, address: str) -> List[ApartmentRent]:
        """Поиск квартир по адресу."""
        return self._collection.find_by_address(address)

    def filter_by_price(self, min_price: float, max_price: float) -> List[ApartmentRent]:
        """Фильтрация квартир по диапазону цен."""
        return self._collection.find_by_price_range(min_price, max_price)

    def sort_by_price(self, reverse: bool = False) -> None:
        """Сортировка квартир по цене."""
        self._collection.sort_by_price(reverse)

    def get_collection(self):
        """Возвращает коллекцию (для storage)."""
        return self._collection

    def __len__(self) -> int:
        return len(self._collection)
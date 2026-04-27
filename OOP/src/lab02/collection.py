from src.lab03.model import Apartment

class ResidentialComplex:
    def __init__(self):
        self._items = []

    def add(self, item: Apartment):
        if not isinstance(item, Apartment):
            raise TypeError(f"Ожидался Apartment, получен {type(item).__name__}")
        if item in self._items:
            raise ValueError("Такая квартира уже есть в комплексе")
        self._items.append(item)

    def remove(self, item: Apartment):
        if item not in self._items:
            raise ValueError("Квартира не найдена в списке")
        self._items.remove(item)

    def get_all(self) -> list[Apartment]:
        return list(self._items)

    def find_by_address(self, address: str):
        """Поиск по точному совпадению адреса"""
        for item in self._items:
            if item.address == address:
                return item
        return None
    
    def remove_at(self, index):
        """ Удаление по индексу """
        if not (0 <= index < len(self._items)):
            raise IndexError("Индекс вне диапазона")
        return self._items.pop(index)
    
    def sort_by_price(self):
        """Сортиртировка по цене"""
        self._items.sort(reverse=True)

    def get_available(self):
        """Возвращает новый объект того же класса только с доступными квартирами"""
        new_collection = ResidentialComplex()
        
        for item in self._items:
            if item.available:
                new_collection.add(item)
                
        return new_collection

    def __len__(self):
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]
    
    def __repr__(self) -> str:
        return f"ResidentialComplex(items={self._items!r})"
    
    def __str__(self):
        if not self._items:
            return "Жилой комплекс пуст."
        
        header = f"В комплексе {len(self)} объектов:"
        items_str = "\n".join(f"  {i+1}. {item.__class__.__name__} {item.address} ({item.price} р.)" 
                             for i, item in enumerate(self._items))
        return f"{header}\n{items_str}"
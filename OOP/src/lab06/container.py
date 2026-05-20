
from typing import TypeVar, Generic, Callable, Optional, List, Protocol



# PROTOCOLS


class Displayable(Protocol):
    def display(self) -> str:
        ...


class Scorable(Protocol):
    def score(self) -> float:
        ...


# TYPEVAR

T = TypeVar('T')
D = TypeVar('D', bound=Displayable)
S = TypeVar('S', bound=Scorable)
R = TypeVar('R')


# GENERIC-КОЛЛЕКЦИЯ

class TypedCollection(Generic[T]):
    
    def __init__(self) -> None:
        self._items: List[T] = []
    
    # БАЗОВЫЕ ОПЕРАЦИИ
    
    def add(self, item: T) -> None:
        self._items.append(item)
    
    def remove(self, item: T) -> None:
        self._items.remove(item)
    
    def remove_at(self, index: int) -> T:
        if index < 0 or index >= len(self._items):
            raise IndexError("Неверный индекс")
        return self._items.pop(index)
    
    def get_all(self) -> List[T]:
        return self._items.copy()
    
    def clear(self) -> None:
        self._items.clear()
    
    # ПОИСК 
    
    def find_by_address(self, address: str) -> List[T]:
        result = []
        for item in self._items:
            if hasattr(item, 'address') and item.address == address:
                result.append(item)
        return result
    
    def find_by_price_range(self, min_price: float, max_price: float) -> List[T]:
        result = []
        for item in self._items:
            if hasattr(item, 'price') and min_price <= item.price <= max_price:
                result.append(item)
        return result
    
    #  СОРТИРОВКА 
    
    def sort_by_price(self, reverse: bool = False) -> None:
        self._items.sort(key=lambda x: x.price if hasattr(x, 'price') else 0, reverse=reverse)
    
    def sort_by_square(self, reverse: bool = False) -> None:
        self._items.sort(key=lambda x: x.square if hasattr(x, 'square') else 0, reverse=reverse)
    
    #  ФИЛЬТРАЦИЯ
    
    def get_available(self) -> 'TypedCollection[T]':
        new = TypedCollection[T]()
        for item in self._items:
            if hasattr(item, 'available') and item.available:
                new.add(item)
        return new
    
    def filter_by_min_level(self, min_level: int) -> 'TypedCollection[T]':
        new = TypedCollection[T]()
        for item in self._items:
            if hasattr(item, 'level') and item.level >= min_level:
                new.add(item)
        return new
    
    # МАГИЧЕСКИЕ МЕТОДЫ 
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
    def __getitem__(self, index):
        if isinstance(index, slice):
            return self._items[index]
        if index < 0:
            index = len(self._items) + index
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс вне диапазона")
        return self._items[index]
    
    def __contains__(self, item: T) -> bool:
        return item in self._items
    
    def __str__(self) -> str:
        if not self._items:
            return "Коллекция пуста"
        lines = [f"{i+1}. {item}" for i, item in enumerate(self._items)]
        return f"Коллекция ({len(self._items)} шт.)\n" + "\n".join(lines)
    
    def __repr__(self) -> str:
        return f"TypedCollection({self._items})"
    
   
    
    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for item in self._items:
            if predicate(item):
                return item
        return None
    
    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        return [item for item in self._items if predicate(item)]
    
    def map(self, transform: Callable[[T], R]) -> List[R]:
        return [transform(item) for item in self._items]
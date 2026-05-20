

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab04.models import ApartmentRent, ApartmentSale
from lab06.container import TypedCollection, Displayable, Scorable


def patch_classes():
    """Добавляем методы display() и score() в классы для Protocol"""
    def display(self):
        return f"{self.address} ({self.square}м², {self.price} руб.)"
    
    def score(self):
        return float(self.price) / 1_000_000
    
    for cls in (ApartmentRent, ApartmentSale):
        if not hasattr(cls, 'display'):
            cls.display = display
        if not hasattr(cls, 'score'):
            cls.score = score


def main():
    patch_classes()
    
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА №6 - GENERICS И TYPING")
    print("=" * 60)
    
    # =========================================================================
    # СЦЕНАРИЙ 1: БАЗОВАЯ РАБОТА С GENERIC-КОЛЛЕКЦИЕЙ (все методы из ЛР-2)
    # =========================================================================
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 1: БАЗОВАЯ РАБОТА С GENERIC-КОЛЛЕКЦИЕЙ")
    print("=" * 60)
    
    col: TypedCollection[ApartmentRent] = TypedCollection()
    
    a1 = ApartmentRent(5_000_000, 30_000, "ул. Ленина, 10", 45, True)
    a2 = ApartmentRent(7_200_000, 42_000, "ул. Пушкина, 5", 60, True)
    a3 = ApartmentRent(3_500_000, 25_000, "ул. Гагарина, 15", 35, True)
    
    col.add(a1)
    col.add(a2)
    col.add(a3)
    
    print("\n1.1 get_all() - все элементы:")
    for item in col.get_all():
        print(f"   {item.address} - {item.price} руб.")
    
    print(f"\n1.2 Длина коллекции: {len(col)}")
    
    print("\n1.3 sort_by_price() - сортировка по цене (по возрастанию):")
    col.sort_by_price()
    for item in col:
        print(f"   {item.address} - {item.price} руб.")
    
    print("\n1.4 find_by_address() - поиск по адресу 'ул. Пушкина, 5':")
    found = col.find_by_address("ул. Пушкина, 5")
    for item in found:
        print(f"   {item}")
    
    print("\n1.5 get_available() - только доступные квартиры:")
    available = col.get_available()
    print(f"   Доступно: {len(available)} шт.")
    
    # =========================================================================
    # СЦЕНАРИЙ 2: МЕТОДЫ FIND, FILTER, MAP
    # =========================================================================
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 2: МЕТОДЫ FIND, FILTER, MAP")
    print("=" * 60)
    
    col2: TypedCollection[ApartmentRent] = TypedCollection()
    col2.add(a1)
    col2.add(a2)
    col2.add(a3)
    
    print("\n2.1 find() - поиск первой квартиры дороже 6 млн:")
    result = col2.find(lambda x: x.price > 6_000_000)
    if result:
        print(f"   Найдено: {result.address} - {result.price} руб.")
    
    print("\n2.2 find() - поиск того, чего нет (цена > 10 млн):")
    result = col2.find(lambda x: x.price > 10_000_000)
    print(f"   Результат: {result}")
    
    print("\n2.3 filter() - все квартиры дороже 4 млн:")
    filtered = col2.filter(lambda x: x.price > 4_000_000)
    for item in filtered:
        print(f"   {item.address} - {item.price} руб.")
    
    print("\n2.4 map() - преобразование в адреса (list[str]):")
    addresses = col2.map(lambda x: x.address)
    print(f"   {addresses}")
    
    print("\n2.5 map() - преобразование в цену в млн (list[float]):")
    prices_in_millions = col2.map(lambda x: x.price / 1_000_000)
    print(f"   {prices_in_millions}")
    
    # =========================================================================
    # СЦЕНАРИЙ 3: PROTOCOLS И STRUCTURAL TYPING
    # =========================================================================
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 3: PROTOCOLS И STRUCTURAL TYPING")
    print("=" * 60)
    
    print("\n3.1 TypedCollection с ограничением Displayable:")
    displayable_col: TypedCollection[D] = TypedCollection()
    displayable_col.add(a1)
    displayable_col.add(a2)
    
    for item in displayable_col:
        print(f"   {item.display()}")
    
    print("\n3.2 TypedCollection с ограничением Scorable:")
    scorable_col: TypedCollection[S] = TypedCollection()
    scorable_col.add(a1)
    scorable_col.add(a2)
    
    for item in scorable_col:
        print(f"   {item.address}: {item.score():.2f} млн")
    
    print("\n3.3 Проверка соответствия протоколам:")
    print(f"   ApartmentRent имеет display()? {hasattr(a1, 'display')}")
    print(f"   ApartmentRent имеет score()? {hasattr(a1, 'score')}")
    
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 60)


if __name__ == "__main__":
    main()
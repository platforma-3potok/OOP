

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab04.models import ApartmentRent, ApartmentSale
from lab04.collection import ResidentialComplex
from lab04.interfaces import Displayable


def print_all_displayable(items):
    for item in items:
        if isinstance(item, Displayable):
            print(f"   {item.display_info()}")


def main():
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА №4 - ИНТЕРФЕЙСЫ (ABC)")
    print("=" * 60)

    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 1: СОЗДАНИЕ ОБЪЕКТОВ И ИНТЕРФЕЙСНЫЕ МЕТОДЫ")
    print("=" * 60)

    rent_apt = ApartmentRent(5000000, 30000, "ул. Ленина, 10", 45, True)
    sale_apt = ApartmentSale(8000000, 50000, "ул. Пушкина, 5", 60, True)

    print("\n1.1 Displayable метод display_info():")
    print(f"   {rent_apt.display_info()}")
    print(f"   {sale_apt.display_info()}")

    print("\n1.2 Rentable метод rent():")
    rent_apt.rent(6, 200000)

    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 2: ИНТЕРФЕЙС КАК ТИП И ПРОВЕРКА isinstance")
    print("=" * 60)

    items = [rent_apt, sale_apt]

    print("\n2.1 Проверка через isinstance():")
    for item in items:
        print(f"   {item.__class__.__name__}: Displayable? {isinstance(item, Displayable)}")

    print("\n2.2 Универсальная функция print_all_displayable():")
    print_all_displayable(items)

    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 3: КОЛЛЕКЦИЯ И ФИЛЬТРАЦИЯ ПО ИНТЕРФЕЙСУ")
    print("=" * 60)

    collection = ResidentialComplex()
    collection.add(rent_apt)
    collection.add(sale_apt)

    print("\n3.1 Исходная коллекция:")
    print(collection)

    print("\n3.2 Фильтрация: только Displayable объекты:")
    for item in collection.get_displayable():
        print(f"   {item.display_info()}")

    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 60)


if __name__ == "__main__":
    main()
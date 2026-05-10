

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab05.collection import ResidentialComplex
from lab05.strategies import *
from lab04.models import ApartmentRent, ApartmentSale


def create_sample_collection():
    collection = ResidentialComplex()
    collection.add(ApartmentRent(5000000, 30000, "ул. Ленина, 10", 45, True))
    collection.add(ApartmentRent(8000000, 40000, "ул. Пушкина, 5", 60, True))
    collection.add(ApartmentRent(3500000, 20000, "ул. Гагарина, 15", 35, True))
    collection.add(ApartmentRent(10000000, 50000, "ул. Советская, 1", 80, True))
    collection.add(ApartmentRent(6500000, 35000, "ул. Мира, 8", 55, True))
    return collection


def main():
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА №5 - СТРАТЕГИИ И ДЕЛЕГАТЫ")
    print("=" * 60)

    # СЦЕНАРИЙ 1: СОРТИРОВКА ТРЁМЯ СТРАТЕГИЯМИ
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 1: СОРТИРОВКА ТРЁМЯ СТРАТЕГИЯМИ")
    print("=" * 60)

    col = create_sample_collection()
    print("\n1.1 Исходная коллекция:")
    print(col)

    print("\n1.2 Сортировка по цене:")
    col2 = col.copy()
    col2.sort_by(by_price)
    print(col2)

    print("\n1.3 Сортировка по площади:")
    col3 = col.copy()
    col3.sort_by(by_square)
    print(col3)

    print("\n1.4 Сортировка по адресу:")
    col4 = col.copy()
    col4.sort_by(by_address)
    print(col4)

    # СЦЕНАРИЙ 2: ФИЛЬТРАЦИЯ ДВУМЯ ФУНКЦИЯМИ
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 2: ФИЛЬТРАЦИЯ")
    print("=" * 60)

    col5 = create_sample_collection()
    print("\n2.1 Фильтрация: только доступные квартиры:")
    filtered = list(filter(is_available, col5.get_all()))
    for item in filtered:
        print(f"   {item.address} - {item.price} руб.")

    print("\n2.2 Фильтрация: только дорогие (цена > 6000000):")
    filtered2 = list(filter(is_expensive, col5.get_all()))
    for item in filtered2:
        print(f"   {item.address} - {item.price} руб.")

    # СЦЕНАРИЙ 3: MAP, ЦЕПОЧКА, CALLABLE
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 3: MAP, ЦЕПОЧКА, CALLABLE")
    print("=" * 60)

    col6 = create_sample_collection()
    print("\n3.1 Применение map() с lambda для увеличения цены:")
    new_prices = list(map(lambda x: x.price * 1.1, col6.get_all()))
    print(f"   Новые цены: {[int(p) for p in new_prices]}")

    print("\n3.2 Фабрика фильтров make_price_filter(6000000):")
    price_filter = make_price_filter(6000000)
    filtered_cheap = list(filter(price_filter, col6.get_all()))
    print(f"   Квартир с ценой <= 6000000: {len(filtered_cheap)}")

    print("\n3.3 Цепочка операций filter -> sort -> apply:")
    col7 = create_sample_collection()
    result = (col7
              .copy()
              .filter_by(is_expensive)
              .sort_by(by_price)
              .apply(lambda x: x))
    print(f"   Результат: {len(result.get_all())} дорогих квартир")

    print("\n3.4 Callable-объект DiscountStrategy(10):")
    col8 = create_sample_collection()
    discount = DiscountStrategy(10)
    print(f"   Цена до: {col8.get_all()[0].price}")
    col8.apply(discount)
    print(f"   Цена после скидки 10%: {col8.get_all()[0].price}")

    print("\n3.5 Сортировка через lambda:")
    col9 = create_sample_collection()
    col9.sort_by(lambda x: x.address.lower(), reverse=True)
    print(col9)

    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 60)


if __name__ == "__main__":
    main()
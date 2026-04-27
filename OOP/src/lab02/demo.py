from src.lab01.model import Apartment
from src.lab02.collection import ResidentialComplex

def main():
    # 1. Инициализация коллекции
    complex_vostok = ResidentialComplex()
    print("=== [1] Создание объектов и валидация ===")

    # Создаем несколько квартир
    apt1 = Apartment(price=5_000_000, price_month=30_000, address="ул. Ленина, 1", square=45, available=True)
    apt2 = Apartment(price=8_500_000, price_month=50_000, address="пр. Мира, 15", square=75, available=True)
    apt3 = Apartment(price=3_200_000, price_month=20_000, address="ул. Садовая, 5", square=30, available=True)
    
    # Демонстрация валидации
    try:
        print("Попытка создать квартиру с отрицательной ценой...")
        invalid_apt = Apartment(price=-100, price_month=10, address="Ошибка", square=10, available=True)
    except ValueError as e:
        print(f" Перехвачена ошибка валидации: {e}")

    # 2. Работа с коллекцией
    print("\n=== [2] Наполнение коллекции ===")
    complex_vostok.add(apt1)
    complex_vostok.add(apt2)
    complex_vostok.add(apt3)
    
    try:
        print("Попытка добавить дубликат квартиры...")
        complex_vostok.add(apt1)
    except ValueError as e:
        print(f" Система не дала добавить дубликат: {e}")

    print(f"\nТекущее состояние комплекса:\n{complex_vostok}")

    # 3. Поиск и доступ по индексу
    print("\n=== [3] Поиск и доступ ===")
    address_to_find = "пр. Мира, 15"
    found = complex_vostok.find_by_address(address_to_find)
    print(f"Найден объект по адресу '{address_to_find}':\n{found}")

    # 4. Сортировка
    print("\n=== [4] Сортировка по цене (от дорогих к дешевым) ===")
    complex_vostok.sort_by_price()
    print(complex_vostok)

    # 5. Бизнес-логика и фильтрация
    print("\n=== [5] Бизнес-логика и фильтрация ===")
    print("Сдаем квартиру на ул. Садовая, 5 в аренду...")
    apt_to_rent = complex_vostok.find_by_address("ул. Садовая, 5")
    if apt_to_rent:
        apt_to_rent.rent(months=2, money=40000) # Успешная аренда

    print("\nПолучаем список только ДОСТУПНЫХ квартир:")
    available_only = complex_vostok.get_available()
    print(available_only)
    print(f"Всего доступно: {len(available_only)} из {len(complex_vostok)}")

    # 6. Удаление
    print("\n=== [6] Удаление объектов ===")
    removed_apt = complex_vostok.remove_at(0)
    print(f"Удалена самая дорогая квартира: {removed_apt.address}")
    print(f"Осталось в комплексе: {len(complex_vostok)}")

if __name__ == "__main__":
    main()
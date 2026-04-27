from src.lab01.model import Apartment

def main():
    print("=== [Сценарий 1] Создание объектов и магические методы ===")
    apt1 = Apartment(20_000_000, 80_000, "Крымская 15 к. 1 п.3", 100, True)
    apt2 = Apartment(15_000_000, 80_000, "Крымская 17 к. 1 п.3", 70, False)

    print("\n-- Вывод __str__ --")
    print(apt1)
    
    print("\n-- Вывод __repr__ --")
    print(repr(apt1))
    
    print("\n-- Сравнение __eq__ --")
    print(f"Квартиры одинаковые? -> {apt1 == apt2}")

    print("\n=== [Сценарий 2] Ошибки валидации (Тип данных) ===")
    try:
        # Передаем строку вместо числа
        apt_invalid_type = Apartment("15_000_000", 80_000, "Крымская", 70, False)
    except TypeError as e:
        print(f"Успешно перехвачена ошибка типа: {e}")

    print("\n===[Сценарий 3] Ошибки валидации (Логика/Значение) ===")
    try:
        # Передаем отрицательную цену
        apt_invalid_value = Apartment(-200, 80_000, "Крымская", 70, False)
    except ValueError as e:
        print(f"Успешно перехвачена ошибка значения: {e}")

    print("\n===[Сценарий 4] Смена свойства через setter ===")
    print(f"Старая цена apt1: {apt1.price:,} руб.")
    apt1.price = 10_000_000
    print(f"Новая цена apt1: {apt1.price:,} руб.")

    print("\n=== [Сценарий 5] Бизнес-логика (Покупка и Аренда) ===")
    apt3 = Apartment(12_000_000, 60_000, "ул. Пушкина 10", 50, True)
    
    print("\nПопытка купить apt1:")
    apt1.buy(15_000_000_000)
    
    print("Попытка арендовать apt3:")
    apt3.rent(2, 200_000)

    # Демонстрация того, что купленную квартиру нельзя арендовать заново
    print("\nПопытка арендовать уже купленную apt1:")
    try:
        apt1.rent(1, 100_000)
    except ValueError as e:
        print(f"Перехвачена ошибка бизнес-логики: {e}")

if __name__ == "__main__":
    main()

from src.lab03.base import StudioApartment, Penthouse
from src.lab02.collection import ResidentialComplex

def main():
    print("=== [Сценарий 1] Создание объектов разных типов и интеграция с коллекцией ===")
    
    # Создаем студию (Дочерний класс 1)
    studio = StudioApartment(
        price=5_000_000, 
        price_month=30_000, 
        address="ул. Пушкина, 10", 
        square=30, 
        available=True, 
        is_furnished=True, 
        max_tenants=2
    )
    
    # Создаем пентхаус (Дочерний класс 2)
    penthouse = Penthouse(
        price=35_000_000, 
        price_month=150_000, 
        address="пр. Мира, 1", 
        square=150, 
        available=True, 
        terrace_square=50, 
        has_smart_home=True
    )

    # Работа с разными типами через ОДНУ коллекцию (Единый список)
    catalog = ResidentialComplex()
    catalog.add(studio)
    catalog.add(penthouse)
    print(catalog)

    print("===[Сценарий 2] Демонстрация полиморфизма (Один метод — разное поведение) ===")
    for apt in catalog:
        # 1. Вывод объектов (полиморфный вызов переопределенного __str__)
        print(apt)
        
        # 2. Вызов одинаковых методов для разных типов -> разные результаты
        utility_bill = apt.calculate_utility_bills()
        reg_status = apt.check_registration()
        
        print(f"Расчет ЖКУ: {utility_bill} руб.")
        print(f"Статус: {reg_status}\n")

    print("=== [Сценарий 3] Использование методов базового класса ===")
    # Вызываем методы rent() и buy(), которые были унаследованы от абстрактного Apartment
    print("Попытка арендовать студию на 3 месяца...")
    try:
        studio.rent(months=3, money=100_000)
    except ValueError as e:
        print(f"Ошибка: {e}")
        
    print("\nПопытка купить пентхаус...")
    try:
        penthouse.buy(money=40_000_000)
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\n=== [Сценарий 4] Фильтрация по типу через isinstance() ===")
    print("Ищем в каталоге только элитную недвижимость (Пентхаусы):")
    for apt in catalog:
        if isinstance(apt, Penthouse):
            print(f"   Найден пентхаус по адресу: {apt.address}.")
            print(f"   Площадь террасы: {apt.terrace_square} м², Умный дом: {apt.has_smart_home}")

if __name__ == "__main__":
    main()
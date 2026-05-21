

from lab07.app import ApartmentApp
from lab07.exceptions import DuplicateApartmentError, ApartmentNotFoundError


def print_menu() -> None:
    """Выводит главное меню."""
    print("\n" + "=" * 50)
    print("УПРАВЛЕНИЕ КОЛЛЕКЦИЕЙ КВАРТИР")
    print("=" * 50)
    print("1. Добавить квартиру")
    print("2. Показать все квартиры")
    print("3. Найти квартиру по адресу")
    print("4. Фильтровать по цене")
    print("5. Сортировать по цене")
    print("6. Удалить квартиру по адресу")
    print("0. Выход")
    print("-" * 50)


def get_int(prompt: str) -> int:
    """Безопасный ввод целого числа."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("   Ошибка: введите число")


def get_float(prompt: str) -> float:
    """Безопасный ввод числа с плавающей точкой."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("   Ошибка: введите число")


def get_bool(prompt: str) -> bool:
    """Ввод подтверждения (y/n)."""
    while True:
        val = input(prompt + " (y/n): ").lower()
        if val in ('y', 'yes', 'да', 'д'):
            return True
        if val in ('n', 'no', 'нет', 'н'):
            return False
        print("   Введите y или n")


def run(app: ApartmentApp) -> None:
    """Запуск основного цикла CLI."""
    while True:
        print_menu()
        choice = get_int("Выберите пункт: ")

        if choice == 1:
            price = get_float("   Цена покупки: ")
            price_month = get_float("   Аренда в месяц: ")
            address = input("   Адрес: ").strip()
            square = get_float("   Площадь (м²): ")

            try:
                app.add_apartment(price, price_month, address, square, True)
                print("   Квартира добавлена")
            except DuplicateApartmentError as e:
                print(f"   Ошибка: {e}")

        elif choice == 2:
            items = app.get_all()
            print(f"\n   Всего квартир: {len(items)}")
            for i, apt in enumerate(items, 1):
                print(f"   {i}. {apt.address} | {apt.price:,} руб. | {apt.square} м²")

        elif choice == 3:
            address = input("   Адрес: ").strip()
            found = app.find_by_address(address)
            if found:
                for apt in found:
                    print(f"   {apt}")
            else:
                print("   Не найдено")

        elif choice == 4:
            min_price = get_float("   Мин. цена: ")
            max_price = get_float("   Макс. цена: ")
            filtered = app.filter_by_price(min_price, max_price)
            print(f"\n   Найдено: {len(filtered)}")
            for apt in filtered:
                print(f"   {apt.address} | {apt.price:,} руб.")

        elif choice == 5:
            rev = get_bool("   По убыванию")
            app.sort_by_price(rev)
            print("   Сортировка выполнена")
    
            items = app.get_all()
            if items:
                print("\n   Отсортированные квартиры:")
                for i, apt in enumerate(items, 1):
                    print(f"   {i}. {apt.address} | {apt.price:,} руб. | {apt.square} м²")
            else:
                print("   Нет квартир для отображения")


        elif choice == 6:
            address = input("   Адрес для удаления: ").strip()
            if not get_bool(f"   Удалить '{address}'"):
                print("   Удаление отменено")
                continue

            try:
                app.remove_by_address(address)
                print("   Квартира удалена")
            except ApartmentNotFoundError as e:
                print(f"   Ошибка: {e}")

        elif choice == 0:
            print("   До свидания")
            break

        else:
            print("   Неверный пункт меню")
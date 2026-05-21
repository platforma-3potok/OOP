
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab07.app import ApartmentApp
from lab07.cli import run
from lab07.storage import save, load

DATA_FILE = "apartments.json"


def main() -> None:
    """Главная функция приложения."""
    app = ApartmentApp()

    load(DATA_FILE, app.get_collection())
    print(f"Загружено {len(app)} квартир(ы)")

    run(app)

    save(app.get_collection(), DATA_FILE)
    print(f"Сохранено {len(app)} квартир(ы)")


if __name__ == "__main__":
    main()
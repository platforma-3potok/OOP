

import json
from typing import List, Dict, Any
from lab07.models import ApartmentRent


def apartment_to_dict(apt: ApartmentRent) -> Dict[str, Any]:
    """Преобразует квартиру в словарь для JSON."""
    return {
        "price": apt.price,
        "price_month": apt.price_month,
        "address": apt.address,
        "square": apt.square,
        "available": apt.available
    }


def dict_to_apartment(data: Dict[str, Any]) -> ApartmentRent:
    """Восстанавливает квартиру из словаря."""
    return ApartmentRent(
        data["price"],
        data["price_month"],
        data["address"],
        data["square"],
        data["available"]
    )


def save(collection, filepath: str) -> None:
    """Сохраняет коллекцию в JSON-файл."""
    data = [apartment_to_dict(item) for item in collection.get_all()]
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load(filepath: str, collection) -> None:
    """Загружает коллекцию из JSON-файла (если существует)."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            for item_data in data:
                apt = dict_to_apartment(item_data)
                collection.add(apt)
    except FileNotFoundError:
        pass
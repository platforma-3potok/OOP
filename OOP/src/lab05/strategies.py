


def by_price(item):
    """Стратегия: сортировка по цене"""
    return item.price


def by_square(item):
    """Стратегия: сортировка по площади"""
    return item.square


def by_address(item):
    """Стратегия: сортировка по адресу"""
    return item.address.lower()


def make_price_filter(max_price):
    """Фабрика фильтров: создаёт функцию для фильтрации по максимальной цене"""
    def price_filter(item):
        return item.price <= max_price
    return price_filter


def is_available(item):
    """Фильтр: оставляет только доступные квартиры"""
    return item.available


def is_expensive(item):
    """Фильтр: оставляет только дорогие квартиры (цена > 6000000)"""
    return item.price > 6000000


class DiscountStrategy:
    """Callable-объект: стратегия для применения скидки"""
    
    def __init__(self, percent):
        self.percent = percent
    
    def __call__(self, item):
        item._price = int(item.price * (1 - self.percent / 100))
        return item
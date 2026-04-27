from src.lab01.validate import (
    validate_price,
    validate_price_month,
    validate_address,
    validate_square,
    validate_available
)

class Apartment:
    currency = "₽"

    def __init__(self, price, price_month, address, square, available):
        self.price = price
        self.price_month = price_month
        self.address = address
        self.square = square
        self.available = available

    @property
    def price(self):
        return self._price 
    
    @price.setter
    def price(self, value: int):
        validate_price(value)
        self._price = value

    @property
    def price_month(self):
        return self._price_month 
    
    @price_month.setter
    def price_month(self, value: int):
        validate_price_month(value)
        self._price_month = value

    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, value: str):
        validate_address(value)
        self._address = value

    @property
    def square(self):
        return self._square 
    
    @square.setter
    def square(self, value: int):
        validate_square(value)
        self._square = value

    @property
    def available(self):
        return self._available
    
    @available.setter
    def available(self, value: bool):
        validate_available(value)
        self._available = value

    def rent(self, months, money):
        if not isinstance(months, int):
            raise TypeError("кол-во месяцев должно быть числом")
        if months <= 0:
            raise ValueError("Кол-во месяцев не может быть отрицательным или равно нулю")
        if not isinstance(money, int): 
            raise TypeError("Кол-во денег должно быть числом")
        if money < 0: 
            raise ValueError("Кол-во денег не может быть отрицательным")
        if not self.available: 
            raise ValueError("Квартира уже сдается")
        cost = self.price_month * months
        if money < cost: 
            raise ValueError("У вас недостаточно средств")
        self.available = False
        print("Вы успешно арнедовали квартиру")

    def buy(self, money):
        if not isinstance(money, int):
            raise TypeError("Кол-во денег должно быть числом")
        if money < 0:
            raise ValueError("Кол-во денег не может быть отрицательным")
        if not self.available:
            raise ValueError("Квартира сдается, пока что вы не можете её купить")
        if self.price > money:
            raise ValueError(f"Недостаточно средств для покупки, вам не хватает {self.price - money} р.")
        print("Вы успешно купили квартиру")
        self.available = False

    def __str__(self):
        status = "сдана" if not self.available else "доступна"
        return (
            f"Квартира по адресу: {self.address}\n"
            f"Площадь: {self.square} м²\n"
            f"Стоимость: {self.price:,} {self.currency}\n"
            f"Арендная цена в месяц: {self.price_month:,} р.\n"
            f"Состояние: {status}"
        )
        
    def __eq__(self, other):
        if not isinstance(other, Apartment):
            return NotImplemented
        return (
            self.price == other.price and
            self.price_month == other.price_month and
            self.address == other.address and
            self.square == other.square and
            self.available == other.available
        )

    def __repr__(self):
        return (
            f"Apartment(price={self.price}, price_month={self.price_month}, "
            f"address='{self.address}', square={self.square}, available={self.available})"
        )   

    def __lt__(self, other):
        if not isinstance(other, Apartment):
            return NotImplemented
        
        return self.price < other.price 
# src/lab04/models.py

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab03.model import Apartment
from lab04.interfaces import Displayable, Rentable


class ApartmentRent(Apartment, Displayable, Rentable):
    """Квартира с возможностью аренды и отображения"""
    
    def display_info(self) -> str:
        status = "доступна" if self.available else "сдана"
        return f"Квартира: {self.address}, {self.square}м², {self.price} руб., {status}"
    
    def rent(self, months: int, money: int) -> bool:
        if not self.available:
            raise ValueError("Квартира уже сдана")
        cost = self.price_month * months
        if money < cost:
            raise ValueError(f"Не хватает {cost - money} руб.")
        self.available = False
        print(f"Квартира сдана на {months} месяцев")
        return True
    
    def calculate_utility_bills(self) -> float:
        return self.square * 50
    
    def check_registration(self) -> bool:
        return True


class ApartmentSale(Apartment, Displayable):
    """Квартира только для продажи (без аренды)"""
    
    def display_info(self) -> str:
        status = "доступна" if self.available else "продана"
        return f"Квартира: {self.address}, {self.square}м², {self.price} руб., {status}"
    
    def calculate_utility_bills(self) -> float:
        return self.square * 50
    
    def check_registration(self) -> bool:
        return True
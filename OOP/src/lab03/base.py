from src.lab03.model import Apartment

class StudioApartment(Apartment):
    def __init__(self, price, price_month, address, square, available, is_furnished: bool, max_tenants: int):
        super().__init__(price, price_month, address, square, available)

        self._is_furnished = is_furnished
        self._max_tenants = max_tenants

    @property
    def is_furnished(self):
        return self._is_furnished

    @property
    def max_tenants(self):
        return self._max_tenants

    def calculate_utility_bills(self):
        """Коммуналка считается по пониженному тарифу (100 руб за квадратный метр)"""
        return self.square * 100.0

    def check_registration(self):
        """Разрешает постоянную прописку (так как это жилой фонд)"""
        return f"Прописка в Студии разрешена"
    
    def __str__(self):
        furnished_status = "Да" if self.is_furnished else "Нет"
        return (
            f"[СТУДИЯ] {super().__str__()}\n"
            f"Меблировка: {furnished_status}\n"
            f"Макс. жильцов: {self.max_tenants} чел."
        )

class Penthouse(Apartment):
    def __init__(self, price, price_month, address, square, available, terrace_square: int, has_smart_home: bool):
        super().__init__(price, price_month, address, square, available)

        self._terrace_square = terrace_square
        self._has_smart_home = has_smart_home

    @property
    def terrace_square(self):
        return self._terrace_square

    @property
    def has_smart_home(self):
        return self._has_smart_home
    
    def calculate_utility_bills(self):
        """Наценка за элитное обслуживание террасы и умный дом"""
        base_bill = self.square * 200.0 
        terrace_bill = self.terrace_square * 500.0 
        smart_home_fee = 5000 if self.has_smart_home else 0 
        
        return base_bill + terrace_bill + smart_home_fee

    def check_registration(self):
        """Разрешает постоянную прописку (так как это жилой фонд)"""
        return f"Прописка в Пентхаусе разрешена"
    
    def __str__(self):
        smart_status = "Установлен" if self.has_smart_home else "Отсутствует"
        return (
            f"[ПЕНТХАУС] {super().__str__()}\n"
            f"Площадь террасы: {self.terrace_square} м²\n"
            f"Умный дом: {smart_status}"
        )
from abc import ABC, abstractmethod


class Displayable(ABC):
    @abstractmethod
    def display_info(self) -> str:
        pass


class Rentable(ABC):
    @abstractmethod
    def rent(self, months: int, money: int) -> bool:
        pass
    
    @abstractmethod
    def calculate_utility_bills(self, rate: float) -> float:
        pass
    
    @abstractmethod
    def check_registration(self) -> bool:
        pass
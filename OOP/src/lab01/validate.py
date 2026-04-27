def validate_price(value):
    if not isinstance(value, int):
        raise TypeError("Цена должна быть числом")
    if value <= 0:
        raise ValueError("Цена должна быть больше нуля")    

def validate_price_month(value):
    if not isinstance(value, int):
        raise TypeError("Цена должна быть числом")
    if value <= 0:
        raise ValueError("Цена должна быть больше нуля")    

def validate_address(value):
    if not isinstance(value, str): 
        raise ValueError("Адрес должен быть строкой")
    if not value.strip(): 
        raise ValueError("Адрес не может быть пустым")

def validate_square(value):
    if not isinstance(value, int): 
        raise TypeError("Площадь должна быть числом")
    if value <= 0: 
        raise ValueError("Площадь не может быть отрицательной или равна нулю")

def validate_available(value):
    if not isinstance(value, bool): 
        raise TypeError("available должно быть True или False")
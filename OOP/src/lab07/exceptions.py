

class ApartmentNotFoundError(Exception):
    """Квартира не найдена в коллекции."""
    pass


class DuplicateApartmentError(Exception):
    """Квартира с таким адресом уже существует."""
    pass
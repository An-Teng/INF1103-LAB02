class OrderLineClass:
    def __init__(self, product, quantity):
        self.__product = product
        self.__quantity = quantity

    def calculate_subtotal(self):
        return self.__product.get_price() * self.__quantity
    def set_quantity(self, quantity):
        self.__quantity = quantity
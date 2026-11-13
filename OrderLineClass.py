from ProductClass import Product
class OrderLineClass:
    def __init__(self, product: Product, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.__product: Product = product
        self.__quantity = quantity

    def get_product(self):
        return self.__product

    def calculate_subtotal(self):
        return self.__product.get_price() * self.__quantity

    def display_information(self):
        subtotal = self.calculate_subtotal()
        self.__product.display_information()
        print(f"Quantity: {self.__quantity}, Subtotal: ${subtotal:.2f}")
    
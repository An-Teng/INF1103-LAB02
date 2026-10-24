class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, name):
        for product in self.__products:
            if name.lower() == product.get_name().lower():
                return product
        return None

    def display_products(self):
        for product in self.__products:
            product.display_information()

    def to_list(self):
        return [product.to_dict() for product in self.__products]

    def count(self):
        return len(self.__products)
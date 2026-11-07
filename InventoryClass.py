from ProductClass import Product


class Inventory:
    def __init__(self):
        self.__products: list[Product] = []

    def get_products(self):
        return self.__products

    def add_product(self, product):
        self.__products.append(product)

    def remove_product(self, product_id):
        product=self.find_product(product_id)
        if product:
            self.__products.remove(product)
            return product
        return None
    
    def find_product(self, product_id):
        for product in self.__products:
            if product.get_id() == product_id:
                return product
        return None
    
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
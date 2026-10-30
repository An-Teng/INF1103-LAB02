from abc import ABC, abstractmethod
class Product(ABC):
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def update_stock(self,quantity):
        if quantity < 0 :
            print("Stock cannot be negative.")
            return
        self.__stock = quantity

    def display_information(self):
        return (f"ID: {self.__product_id}, Name: {self.__name}, Price: ${self.__price:.2f}, Stock: {self.__stock}")

    def to_dict(self):
        return {"id": self.__product_id, "name": self.__name,
                "price": self.__price, "stock": self.__stock}
    @abstractmethod
    def get_fulfilment_method(self):
        pass
class CanbeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass
class PhysicalProduct(Product,CanbeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight
        self.__shipping_cost=self.calculate_shipping_cost()
    def get_weight(self):
        return self.__weight

    def display_information(self):
        result=super().display_information()
        print(result+f" Weight: {self.__weight} kg"+f" Shipping Cost: ${self.__shipping_cost:.2f}")

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Physical"
        data["weight"] = self.__weight
        data["shipping_cost"] = self.__shipping_cost
        return data

    def get_fulfilment_method(self):
        print("This is a physical product and will be shipped.")

    def calculate_shipping_cost(self):
        base_cost = 5.0  # Base shipping cost
        cost_per_kg = 2.0  # Cost per kilogram
        return base_cost + (cost_per_kg * self.__weight)


class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def get_file_size(self):
        return self.__file_size

    def display_information(self):
        result=super().display_information() 
        print(result+f" Download Size: {self.__download_size} MB")
    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Digital"
        data["download_size"] = self.__download_size
        return data

    def get_fulfilment_method(self):
        print("This is a digital product and will be delivered digitally.")

# test=PhysicalProduct("P001", "Laptop", 999.99, 10, 2.5)
# test.display_information()
# test.get_fulfilment_method()
# test2=DigitalProduct("D001", "E-book", 9.99, 100, 5)
# test2.display_information()
# test2.get_fulfilment_method()
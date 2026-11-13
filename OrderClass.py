from OrderLineClass import OrderLineClass
from ProductClass import Product
from DiscountStrategyClass import DiscountStrategy, NoDiscount
class Order:
    def __init__(self, order_id, discount: DiscountStrategy | None=None):
        self.__order_id = order_id
        self.__order_lines: list[OrderLineClass] = []
        self.__discount: DiscountStrategy = discount if discount is not None else NoDiscount()

    def set_discount(self, discount: DiscountStrategy):
        self.__discount = discount

    def get_order_lines(self):
        return self.__order_lines

    def add_order_line(self, product: Product, quantity: int):
        order_line = OrderLineClass(product, quantity)
        self.__order_lines.append(order_line)

    def remove_order_line(self, product_id):
        for order_line in self.__order_lines:
            if order_line.get_product().get_id() == product_id:
                self.__order_lines.remove(order_line)
                return True
        return False

    def calculate_total(self):
        total = 0
        for order_line in self.__order_lines:
            total += order_line.calculate_subtotal()
        return self.__discount.apply(total)

    def display_information(self):
        print(f"Order ID: {self.__order_id}")
        for order_line in self.__order_lines:
            order_line.display_information()
        print(f"Total: ${self.calculate_total():.2f}")
from ProductClass import PhysicalProduct,DigitalProduct
from SupplierClass import Supplier
from OrderClass import Order
from OrderLineClass import OrderLineClass
from DiscountStrategyClass import BulkDiscount, PercentageDiscount, StudentDiscount
from ProductFactory import ProductFactory
from OOP import load_products
from InventoryClass import Inventory

inventory = Inventory()
supplier = Supplier("S001", "TechCorp", "tech@corp.com")
desk = PhysicalProduct("P001", "Desk", 150.0, 5, 12.0, supplier)


order = Order("O001")                   
order.add_order_line(desk, 1)
print("No discount:", order.calculate_total())

order.set_discount(BulkDiscount(200, 20))
print("Bulk(200, 20):", order.calculate_total())

order.set_discount(PercentageDiscount(10))
print("Percentage(10):", order.calculate_total())

order.set_discount(StudentDiscount())
print("Student:", order.calculate_total())

shared = PercentageDiscount(10)
order_a = Order("A", shared)
order_b = Order("B", shared)

attempts = {
    "price 0":            lambda: PhysicalProduct("P002", "X", 0, 5, 1.0, supplier),
    "negative price":     lambda: DigitalProduct("D002", "X", -5, 5, 1.0, supplier),
    "negative stock":     lambda: PhysicalProduct("P003", "X", 10.0, -1, 1.0, supplier),
    "update stock to -3": lambda: desk.update_stock(-3),
    "order quantity 0":   lambda: OrderLineClass(desk, 0),
    "order quantity -2":  lambda: OrderLineClass(desk, -2),
}

for label, attempt in attempts.items():
    try:
        attempt()
        print(f"{label}: NO ERROR (something is wrong)")
    except ValueError as err:
        print(f"{label}: rejected -> {err}")

load_products("products.csv", inventory, supplier)
inventory.display_products()

print("--- missing file ---")
load_products("does_not_exist.csv", inventory, supplier)

from ProductClass import PhysicalProduct
from SupplierClass import Supplier
from OrderClass import Order
from DiscountStrategyClass import BulkDiscount, PercentageDiscount, StudentDiscount

supplier = Supplier("S001", "TechCorp", "tech@corp.com")
desk = PhysicalProduct("P100", "Desk", 250.0, 10, 5.0, supplier)

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

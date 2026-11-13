from ProductClass import Product,PhysicalProduct, DigitalProduct
from SupplierClass import Supplier
class ProductFactory:
    @staticmethod
    def create_product(product_type, product_id: str, name:str, price:float, stock_quantity:int, supplier:Supplier, extra: float = 0.0):
        product_type = product_type.strip().lower()
        if product_type == "physical":
            return PhysicalProduct(product_id, name, price, stock_quantity, extra, supplier)
        elif product_type == "digital":
            return DigitalProduct(product_id, name, price, stock_quantity, extra, supplier)
        else:
            raise ValueError(f"Unknown product type: {product_type}")
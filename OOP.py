import json
from InventoryClass import Inventory
from SupplierClass import Supplier
from ProductFactory import ProductFactory
import csv

def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number, e.g. 12.50")

def get_non_negative_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Stock cannot be negative.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number, e.g. 12")

def load_inventory():
    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
            print("Inventory file not found. Starting with an empty inventory.")
            return Inventory()
    inventory = Inventory()
    for item in data:
            s=item["supplier"]
            supplier=Supplier(s["supplier_id"], s["name"], s["contact_email"])
            extra = item.get("weight", item.get("download_size", 0.0))
            product=ProductFactory.create(item["type"], item["product_id"], item["name"], item["price"], item["stock_quantity"], supplier, extra)
            inventory.add_product(product)
    return inventory
    
def save_inventory(data):
      with open("inventory.json", "w") as file:
            json.dump(data.to_list(), file, indent=4)
      print("Inventory saved successfully.")

def start():
    inventory = load_inventory()
    while True:
        print("=========Menu=========")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Remove Product")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            inventory.display_products()
        elif choice == "2":
            print("1. Physical Product")
            print("2. Digital Product")
            product_type = {"1": "physical", "2": "digital"}.get(
                input("Enter Product type (1 or 2): ").strip())
            if product_type is None:
                print("Invalid product type. Please try again.")
                continue
            new_id = f"{product_type[0].upper()}{inventory.count() + 1:03d}"
            name = input("Enter Product name: ")
            price = get_positive_float("Enter Product price: ")
            stock_quantity = get_non_negative_int("Enter Product stock quantity: ")
            prompts = {"physical": "Enter Product weight(kg): ",
                    "digital": "Enter Product download size(MB): "}
            extra = get_positive_float(prompts[product_type])
            supplier_id = input("Enter Supplier ID: ")
            supplier_name = input("Enter Supplier Name: ")
            supplier_email = input("Enter Supplier Contact Email: ")
            supplier = Supplier(supplier_id, supplier_name, supplier_email)
            inventory.add_product(ProductFactory.create(
                product_type, new_id, name, price, stock_quantity, supplier, extra))
            print(f"{product_type.capitalize()} product {name} added successfully.")
        
        elif choice == "3":
            product = inventory.search_product(input("Enter the product name: "))
            if product:
                try:
                    product.update_stock(int(input("Enter the new stock quantity: ")))
                    print("Stock updated.")
                except ValueError as err:
                    print(err)
            else:
                print("No products found with that name.")
        elif choice == "4":
            product = inventory.search_product(input("Enter the product name: "))
            if product:
                product.display_information()
            else:
                print("No products found with that name.")
        elif choice == "5":
            save_inventory(inventory)
        elif choice == "6":
            product_id = input("Enter the product ID to remove: ")
            product = inventory.remove_product(product_id)
            if product:
                print(f"Product with ID {product_id} removed.")
            else:
                print("No products found with that ID.")
        elif choice == "7":
            print("Exiting the program.")
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    start()
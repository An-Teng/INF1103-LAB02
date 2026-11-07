import json
from ProductClass import Product, PhysicalProduct, DigitalProduct
from InventoryClass import Inventory
from SupplierClass import Supplier

def load_inventory():
    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)
            inventory = Inventory()
            for item in data:
                s=item["supplier"]
                supplier=Supplier(s["supplier_id"], s["name"], s["contact_email"])
                if item.get("type") == "Physical":
                    product = PhysicalProduct(item["id"], item["name"], item["price"], item["stock"], item["weight"],supplier)
                elif item.get("type") == "Digital":
                    product = DigitalProduct(item["id"], item["name"], item["price"], item["stock"], item["download_size"],supplier)
                inventory.add_product(product)
            return inventory
    except FileNotFoundError:
        print("Inventory file not found. Starting with an empty inventory.")
        return Inventory()
    
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
            product_type = input("Enter Product type (1 or 2): ")
            if product_type == "1":
                new_id = f"P{inventory.count() + 1:03d}"
                name = input("Enter the product name: ")
                price = float(input("Enter the product price: "))
                stock = int(input("Enter the stock quantity: "))
                weight = float(input("Enter the product weight (in kg): "))
                supplier_id = input("Enter the supplier ID: ")
                supplier_name = input("Enter the supplier name: ")
                supplier_email = input("Enter the supplier contact email: ")
                supplier = Supplier(supplier_id, supplier_name, supplier_email)
                inventory.add_product(PhysicalProduct(new_id, name, price, stock, weight, supplier))
                print(f"Physical Product '{name}' added with ID {new_id}.")
            elif product_type == "2":
                new_id = f"D{inventory.count() + 1:03d}"
                name = input("Enter the product name: ")
                price = float(input("Enter the product price: "))
                stock = int(input("Enter the stock quantity: "))
                download_size = float(input("Enter the download size (in MB): "))
                supplier_id = input("Enter the supplier ID: ")
                supplier_name = input("Enter the supplier name: ")
                supplier_email = input("Enter the supplier contact email: ")
                supplier = Supplier(supplier_id, supplier_name, supplier_email)
                inventory.add_product(DigitalProduct(new_id, name, price, stock, download_size, supplier))
                print(f"Digital Product '{name}' added with ID {new_id}.")
            else:
                print("Invalid product type selection.")
                continue
        elif choice == "3":
            product = inventory.search_product(input("Enter the product name: "))
            if product:
                product.update_stock(int(input("Enter the new stock quantity: ")))
                print("Stock updated.")
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

start()
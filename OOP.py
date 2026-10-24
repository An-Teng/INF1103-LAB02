import json
from ProductClass import Product
from InventoryClass import Inventory

def load_inventory():
    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)
            inventory = Inventory()
            for item in data:
                product = Product(item["id"], item["name"], item["price"], item["stock"])
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
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            inventory.display_products()
        elif choice == "2":
            new_id = f"P{inventory.count() + 1:03d}"
            name = input("Enter the product name: ")
            price = float(input("Enter the product price: "))
            stock = int(input("Enter the stock quantity: "))
            inventory.add_product(Product(new_id, name, price, stock))
            print(f"Product '{name}' added with ID {new_id}.")
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
            print("Exiting the program.")
            break
        else:
            print("Invalid selection. Please try again.")

start()
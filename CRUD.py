import json
def start():
    print("================================")
    print("  Inventory Management System")
    print("================================")
    try:
         with open("inventory.json", "r") as file:
                print("Inventory loaded successfully.")
                # Inventory = data.get("Inventory", 0)
                # item = data.get("item", [])
                menu()
    except FileNotFoundError:
        print("Inventory file not found. Starting with 0 inventory.")
        with open("inventory.json", "w") as file:
              print()
        menu()
def menu():
    print("=========Menu=========")
    print("1. Display All Products")
    print("2. Add products")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    selection=input("Enter your choice (1-6): ")
    if selection=="1":
         display_products()
    elif selection=="2":
         add_product()
    elif selection=="3":
            print()
    elif selection=="4":
            print()
    elif selection=="5":
            print()
    elif selection=="6":
            print("Exiting the program.")
    else:
            print("Invalid selection. Please try again.")
            menu()

def display_products():
      with open("inventory.json", "r") as file:
            data = json.load(file)
            print("=========Current Inventory=========")
            for product in data:
                print(f"ID: {product['id']}, Name: {product['name']}, Price: ${product['price']:.2f}, Stock: {product['stock']}")
            menu() 
def add_product():
      with open("inventory.json", "r") as file:
            data = json.load(file)
            new_id = len(data) + 1
            name = input("Enter the product name: ")
            price = float(input("Enter the product price: "))
            stock = int(input("Enter the product stock quantity: "))
            new_product = {"id": new_id, "name": name, "price": price, "stock": stock}
            data.append(new_product)
            print(data)
      with open("inventory.json", "w") as file:
            json.dump(data, file, indent=4)
      print(f"Product '{name}' added successfully.")
      menu()
start()

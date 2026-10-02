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
         print()
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
                print(f"ID: {product['id']}, Name: {product['name']}, Price: {product['price']}, Stock: {product['stock']}")   

start()

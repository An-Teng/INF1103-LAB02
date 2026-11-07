class Supplier:
    def __init__(self, supplier_id, name, contact_email):
        self.__supplier_id = supplier_id
        self.__name = name
        self.__contact_email = contact_email

    def get_supplier_id(self):
        return self.__supplier_id

    def display_information (self):
        print(f"Supplier ID: {self.__supplier_id}, Name: {self.__name}, Contact Email: {self.__contact_email}")

    def to_dict(self):
        return {"supplier_id": self.__supplier_id, "name": self.__name, "contact_email": self.__contact_email}
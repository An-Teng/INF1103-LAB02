class Supplier:
    def __init__(self, supplier_id, name, contact_email):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_email = contact_email

    def get_supplier_id(self):
        return self.supplier_id

    def display_information (self):
        print(f"Supplier ID: {self.supplier_id}, Name: {self.name}, Contact Email: {self.contact_email}")
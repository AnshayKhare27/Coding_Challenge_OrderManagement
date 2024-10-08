class Product:
    def __init__(self,product_id,product_name,description,price,quantity_in_stock,type):
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock
        self.type = type

    #Getters
    def get_product_id(self):
        return self.product_id
    def get_product_name(self):
        return self.product_name
    def get_description(self):
        return self.description
    def get_price(self):
        return self.price
    def get_quantity_in_stock(self):
        return self.quantity_in_stock
    def get_type(self):
        return self.type

    #Setters
    def set_product_id(self,product_id):
        self.product_id = product_id
    def set_product_name(self,product_name):
        self.product_name = product_name 
    def set_description(self,description):
        self.description = description  
    def set_price(self,price):
        self.price = price
    def set_quantity_in_stock(self,quantity_in_stock):
        self.quantity_in_stock = quantity_in_stock
    def set_type(self,type):
        self.type = type 
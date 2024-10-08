from entity.product import Product

class Clothing(Product):
    def __init__(self,product_id,product_name,description,price,quantity_in_stock,size,color):
        super().__init__(product_id,product_name,description,price,quantity_in_stock,"Clothing")     
        self.size = size
        self.color = color

    #Getters
    def get_size(self):
        return self.size
    def get_color(self):
        return self.color

    #Setters
    def set_size(self,size):
        self.size = size
    def set_color(self, color):
        self.color = color 
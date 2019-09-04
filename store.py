from products import Product
class Store:
    def __init__ (self):
        self.name = 'Supermart'
        self.products = []
        self.product_id = 0
    def add_product(self, name, price, category):
        self.products.append(Product(name, price, category)) 
        self.product_id += 1
        return self
    def sell_product(self, product_id):
        del self.products[product_id]
        print(self.products[product_id])
        return self
    def change_price(self, name, percent_change, is_increased):
        for product in self.products:
            if product.item_name == name:
                product.update_price(percent_change, is_increased)
    def product_info(self, name):
        for product in self.products:
            if product.item_name == name:
                product.print_info()
    def inflation(self, name, percent_increase):
        for product in self.products:
            if product.item_name == name:
                product.update_price(percent_increase, True)
    def set_clearence(self, category, percent_increase):
        for product in self.products:
            if product.item_category == category:
                product.update_price(percent_increase, False)





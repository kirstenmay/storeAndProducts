class Product:
    def __init__ (self, name, price, category):
            self.item_name = name 
            self.item_price = price
            self.item_category = category
    def update_price (self, percent_change, is_increased):
        if is_increased == True:
            self.item_price += self.item_price * percent_change
            return self
        else:
            self.item_price -= self.item_price * percent_change
            return self
    def print_info(self):
        print(self.item_name, self.item_price, self.item_category)
        return self


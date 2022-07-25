from operator import itemgetter


class Course:
    list_of_course = ("sandwich", "croissant", "donut", "baguette")
    #stuff is an option apply for sandwich/baget
    list_of_stuffed = ("sausage", "Ham", "Salad")
    #topping applyfor donut/croissant
    list_of_topping = ("Chocolate", "Chip")
    def __init__(self,item, option) -> None:
        self.item_name = item
        self.option = option
        self.price = self.cal_price()
        

    def add_course(self):
        pass

    def add_stuff(self):
        pass

    def add_topping(self):
        pass
    
    def cal_price(self):
        if self.item_name == "sandwich":
            if self.option == "sausage":
                price = 10
        if self.item_name == "sandwich":
            if self.option == "Ham":
                price = 9
        if self.item_name == "sandwich":
            if self.option == "Salad":
                price = 8
        else:
            print("Has not handled")
        return price 

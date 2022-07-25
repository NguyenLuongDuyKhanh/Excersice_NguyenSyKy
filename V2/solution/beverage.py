class Beverage:
    list_of_beverage = ("Coffee", "Smoothies", "Tea")
    # Hot or cold is an option that apply for Coffee and Tea
    # seasonal_fruits = ("Pine Apple", "Babana", "Water Melon", "Strawberry")
    hot_or_cold = ("Hot", "Cold")

    def __init__(self, item, option) -> None:
        self.item_name = item
        self.option = option # hot_or_cold
        self.price = self.cal_price()

    def cal_price(self):
        price = 0
        if self.item_name == "coffee":
            if self.option == "cold":
                price = 8
        if self.item_name == "coffee":
            if self.option == "hot":
                price = 10
        else:
            print("Has not handled")
        return price 

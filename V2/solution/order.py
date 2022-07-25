class Order:
    def __init__(self,customer) -> None:
        self.items = []          # L
        self.customer = customer # Membership
    def add(self, new, quantity):
        self.items.append(
            {
                "item": str(new.item_name) + str(new.option),
                "quantity": quantity,
                "price": new.price
            }
        )
    def total(self):
        total_cost = 0
        print(self.items)
        for x in self.items:
            total_cost += x["price"]*x["quantity"]
        #self.customer.check()
        print(f"Apply discount {self.customer.discount}%")
        total_cost *= (100 - self.customer.discount)/100
     
        print("total cost ", total_cost)

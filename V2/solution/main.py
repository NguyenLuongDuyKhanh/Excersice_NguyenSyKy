from unittest import loader
import beverage
import course
import order
import membership
import yaml

print("Welcome to ABC Cafeteria, could you tell us your name?! ")

name = input()
new_customer = membership.Membership(name)
new_order = order.Order(new_customer)

with open("menu.yml") as f:
    menu = yaml.load_all(f, Loader = yaml.FullLoader)
    for items in menu:
        #print(items)
        option = int(input("Select menu: 1 for food; 2 for beverage: "))
        #order_flag = True
        while option == 1:
            #print([item for item in enumerate(items["food"], 1)])
            temp_items = [item for item in enumerate(items["food"], 1)]
            print("food menu: ")
            print(temp_items)
            
            food_selection = int(input("Select food options: "))
            selected_food = [item for item in enumerate(items["food"], 1) if food_selection == item[0]]
            print(selected_food)
            #print(items["food"][selected_food[0][1]]["stuffed"])
            if selected_food[0][1] == "sandwich":
                print("Choose stuff below: ")
                print(items["food"][selected_food[0][1]]["stuffed"])
                stuff_selection = int(input("Select stuff options: "))
                selected_stuff = [item for item in enumerate(items["food"][selected_food[0][1]]["stuffed"], 1) if stuff_selection == item[0]]
                print(selected_stuff)
                quantity = input("How many sandwichs do you want: ")
                            
                new_order.add(selected_food[0][1], quantity)
            
            elif selected_food[0][1] == "croissant":
                print("Choose topping below: ")
                print(items["food"][selected_food[0][1]]["topping"])
                stuff_selection = int(input("Select topping options: "))
                selected_stuff = [item for item in enumerate(items["food"][selected_food[0][1]]["topping"], 1) if stuff_selection == item[0]]
                print(selected_stuff)  
                quantity = input("How many croissants do you want: ")

            elif selected_food[0][1] == "donut":
                print("Choose topping below: ")
                print(items["food"][selected_food[0][1]]["topping"])
                stuff_selection = int(input("Select topping options: "))
                selected_stuff = [item for item in enumerate(items["food"][selected_food[0][1]]["topping"], 1) if stuff_selection == item[0]]
                print(selected_stuff)
                quantity = input("How many donuts do you want: ")

            elif selected_food[0][1] == "baguette":
                print("Choose stuff below: ")
                print(items["food"][selected_food[0][1]]["stuffed"])
                stuff_selection = int(input("Select stuff options: "))
                selected_stuff = [item for item in enumerate(items["food"][selected_food[0][1]]["stuffed"], 1) if stuff_selection == item[0]]
                print(selected_stuff)
                quantity = input("How many baguettes do you want: ")             

            #add_new_order = input("Do you want to order more food? Y/N")
            #if add_new_order.upper == "N":
            #    order_flag = False
            
        while option == 2:
            #print([item for item in enumerate(items["food"], 1)])
            temp_items = [item for item in enumerate(items["beverage"], 1)]
            print("beverage menu: ")
            print(temp_items)
            
            beverage_selection = int(input("Select beverage options: "))
            selected_beverage = [item for item in enumerate(items["beverage"], 1) if beverage_selection == item[0]]
            print(selected_beverage)
            #print(items["food"][selected_beverage[0][1]]["stuffed"])
            
            if selected_beverage[0][1] == "coffee":
                print("Choose variants below: ")
                print(items["beverage"][selected_beverage[0][1]]["variants"])
                variants_selection = int(input("Select variants options: "))
                selected_variants = [item for item in enumerate(items["beverage"][selected_beverage[0][1]]["variants"], 1) if variants_selection == item[0]]
                print(selected_variants)

                milk_selection = int(input("Add milk ? 1 : yes, 2 : no "))
                selected_milk = [item for item in enumerate(items["beverage"][selected_beverage[0][1]]["milk"], 1) if milk_selection == item[0]]
                print(selected_milk)
                quantity = input("How many cups do you want: ")   

            elif selected_beverage[0][1] == "tea":
                print("Choose variants below: ")
                print(items["beverage"][selected_beverage[0][1]]["variants"])
                variants_selection = int(input("Select variants options: "))
                selected_variants = [item for item in enumerate(items["beverage"][selected_beverage[0][1]]["variants"], 1) if variants_selection == item[0]]
                print(selected_variants)

                milk_selection = int(input("Add milk ? 1 : yes, 2 : no "))
                selected_milk = [item for item in enumerate(items["beverage"][selected_beverage[0][1]]["milk"], 1) if milk_selection == item[0]]
                print(selected_milk)
                quantity = input("How many cups do you want: ") 
                
            elif selected_beverage[0][1] == "smoothies":
                print("Choose fruit below: ")
                print(items["beverage"][selected_beverage[0][1]]["fruit"])
                variants_selection = int(input("Select fruit options: "))
                selected_variants = [item for item in enumerate(items["beverage"][selected_beverage[0][1]]["fruit"], 1) if variants_selection == item[0]]
                print(selected_variants)

                milk_selection = int(input("Add milk ? 1 : yes, 2 : no "))
                selected_milk = [item for item in enumerate(items["beverage"][selected_beverage[0][1]]["milk"], 1) if milk_selection == item[0]]
                print(selected_milk)
                quantity = input("How many cups do you want: ") 



new_order.total()
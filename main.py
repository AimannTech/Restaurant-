#  define the menu of restaurant use dict
menu = {
    'Pizza' : 80,
    'Coffee' : 50,
    'Sandwich' : 60,
    'Juice' : 40,
    'Tea' : 30,
}
# Greet
print("Welcome to Aiman's Restaurant")
print(f"The menu is {menu}")

class restaurant:
    order_total = 0
# pizza:80+0=80
# pizza:80+ Tea:30 =110

    item_1 = input("Enter your first order : ")
    
    if item_1 in menu:
     order_total +=menu [item_1] # 0 + pizza :80 = 80
     print(f"Your first order {item_1} has been added.")
    else:
        if item_1 not in menu:
         print(f"Your order {item_1} is not in the menu")

    anotherOrder = input("Do you want something more? (yes / no)")

    if anotherOrder == "yes":
        item_2 = input("Enter your second order:")
        if item_2 in menu:
            order_total +=menu[item_2]
            print(f"Your Order {item_2} has been added.")

        else:
         print(f"Your order {anotherOrder} is not in the menu")

    print(f"Your total bill is {order_total}")

# print(menu)
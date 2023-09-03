#import saving loading functions

import warehousefunctions

from ManagerDECO import Manager



manager=Manager()

option = ""



#rewrite def sale function
@manager.assign("sale")
def sales_func(manager):
    #define objects 
        key = input("Provide the name of product sold: ").lower()
        unit_price = float(input("Provide the unit price: "))
        quantity = int(input("Provide the quantity sold: "))
        #check if sale matches inventory
        if key not in manager.inventory.keys():
            print("This product does not exist.")
            return
        #selling activity 
        sales = unit_price * quantity
        manager.inventory[key]["amount"] -= quantity
        manager.account = manager.account + sales
        print(f"This deal- {key} brought you {sales} euros revenue.")
        #save the change
        change = (f"This deal -{key} brought you {sales} euros revenue.")
        manager.history.append(change) 

@manager.assign("purchase")
def purchase_func(manager):
      #define objects 
     key = input("Provide the name of product bought: ").lower()
     unit_price = float(input("Provide the unit price: "))
     quantity = int(input("Provide the quantity purchased: "))
     #calculate purchase
     purchase = unit_price * quantity
     manager.account = manager.account - purchase
     print(f"This deal - {key} cost you {purchase} euros.")
     change = (f"This deal-{key} cost you {purchase} euros.")
     manager.history.append(change)
    #set up filter 
     if purchase > manager.account:
            print("Current balance is not enough to purchase these products.")
            return
    
     if key not in manager.inventory:
        manager.inventory[key] = {"amount": 0, "unit_price":0}
        manager.inventory[key]['unit_price'] = unit_price
        manager.inventory[key]['amount'] += quantity
        print(key) 
        print(manager.inventory[key]['unit_price'])
        print(manager.inventory[key]['amount'])

@manager.assign("account")
def account_func(manager):
    print(manager.account)

@manager.assign("balance")
def balance_func(manager):
        balance_command = input("Enter 'add' to add money or 'subtract' to subtract money: ")

        if balance_command == "add":
            amount = float(input("Enter an amount to add: "))
            manager.account = manager.account + amount
            print(f"You have added {amount} euros onto the account")
            change = (f"You have added {amount} euros onto the account")
            manager.history.append(change)
        elif balance_command == "subtract":
            amount = float(input("Enter an amount to subtract: "))
            if amount > manager.account:
                print("It's invalid input! Money you wish to subtract cannot exceed current balance.")
            else:
                manager.account = manager.account - amount
                print(f"You have withdrawn {amount} euros from the account")
                change = (f"You have withdrawn {amount} euros from the account")
                manager.history.append(change)
        else:
            print("It's invalid input! Please try again. ")

@manager.assign("history")
def history_func(manager):
        from_value = input("Please enter the from value: ")
        to_value = input("Please enter the to value: ")
    
        if from_value == "" and to_value == "":
            for i in manager.history:
                print(i)
        elif from_value != "" and to_value == "":
            for i in manager.history[int(from_value)-1:]:
                print(i)
        elif from_value == "" and to_value !="":
            for i in manager.history[:int(to_value)+1]:
                print(i)
        else:
            for i in manager.history[int(from_value)-1:int(to_value)]:
                print(i)

@manager.assign("inventory")
def inventory_func(manager):
        print("Inventory status:\n")
        print(manager.inventory)

@manager.assign("warehouse")
def warehouse_func(manager):
        key = input("Enter the name of the product: ")
        print(key)
        print(manager.inventory[key]['unit_price'])
        print(manager.inventory[key]['amount'])

#Insert while loop to run commands
while True:
    print("Hiya user, welcome to warehouse system! See the available commands:\n ")
    print("exit -to log out\n")
    print("sale -record the sales of your products")
    print("purchase -record the purchase of your products")
    print("inventory -to display inventory")
    print("balance -the money in and out of your account")
    print("account- balance on the current account")
    print("history - the update record in the system\n")
    command = input("Provide a command: ").lower()

#Enter'sale': command entered for selected product name -  unit price, quantity
#display sales record and updated- sale quantity should not exceed the inventory
    if command == "sale":
        manager.execute("sale")


    elif command == "purchase":
        manager.execute("purchase")
      
        
    elif command == "account":
        manager.execute("account")
    
    elif command == "balance":
        manager.execute("balance")

    elif command == "history":
        manager.execute("history")
    
    elif command == "inventory":
        manager.execute("inventory")

    elif command == "warehouse":
        manager.execute("warehouse")

    elif command == "exit":
        print("You will exit the system.")
        manager.exit()
        break


    else:
        print("It's invalid input! Please try again or enter exit to leave. ")


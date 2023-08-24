#structure - class manager - 2 functions:assign & execute 
import warehousefunctions

file_name1= input("Please enter a name for inventory (i.e. .txt): ")
file_name2= input("Please enter a name for balance (i.e. .txt): ")
file_name3= input("Please enter a name for history (i.e. .txt): ")
class Manager:
    def __init__(self):
        self.actions = {}
        self.account = warehousefunctions.loading_balance(file_name2)
        self.inventory = warehousefunctions.loading_inventory(file_name1)
        self.history = warehousefunctions.loading_history(file_name3)
        
    #- For the `assign` method, consider how tasks can be mapped to methods in your class. 
    # This might involve using a dictionary or similar data structure to map string task names to methods.
    #using Python decorators. These decorators should provide additional functionalities to these operations
    def assign(self, name):
        def inner_function(func):
           self.actions[name] = func
        return inner_function
    

    #executing various operations like `sale`, `purchase`, `balance
    def execute(self, name, *args, **kwargs):
        if name not in self.actions:
            print("Action not defined")
        else:
            self.actions[name](self, *args, **kwargs)
            
manager = Manager ()

 
 
#@manager.assign("sale")
def printer(manager):
    print("yes")

 #how to match commands/functions with my codes????
 #QQ: Extend sale, purchase etc?? 
while True:
    action = input("See the available commands [sale/purchase/inventory/balance/account/history]: \n ")
    if action == "sale":
        manager.execute("sales_func")
    elif action == "purchase":
        manager.execute("purchase")
    elif action == "inventory":
        manager.execute("inventory")
    elif action == "balance":
        manager.execute("balance")
    elif action == "account":
        manager.execute("account")
    elif action == "history":
        manager.execute("history")
    else:
        print("Exit the program.")
        break



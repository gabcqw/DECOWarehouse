#structure - class manager - 2 functions:assign & execute 
import warehousefunctions

file_name1= input("Please enter a name for inventory (i.e. .txt): ")
file_name2= input("Please enter a name for balance (i.e. .txt): ")
file_name3= input("Please enter a name for history (i.e. .txt): ")


class Manager:
    def __init__(self):
        self.actions = {}
        self.inventory_file = file_name1
        self.balance_file = file_name2
        self.history_file = file_name3
        self.account = warehousefunctions.loading_balance(self.balance_file)
        self.inventory = warehousefunctions.loading_inventory(self.inventory_file)
        self.history = warehousefunctions.loading_history(self.history_file)
    
    def exit(self):

        warehousefunctions.saving_inventory(file_name1, self.inventory)
        warehousefunctions.saving_balance(file_name2, self.account)
        warehousefunctions.saving_history(file_name3, self.history )
        
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
            

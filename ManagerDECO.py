# structure - class manager - 2 functions:assign & execute
class Manager:
    def __init__(self):
        self.actions = {}

    # - For the `assign` method, consider how tasks can be mapped to methods in your class.
    # This might involve using a dictionary or similar data structure to map string task names to methods.
    # using Python decorators. These decorators should provide additional functionalities to these operations
    
    def assign(self, name):
        def inner_function(func):
            self.actions[name] = func

        return inner_function

    # executing various operations like `sale`, `purchase`, `balance
    def execute(self, name, *args, **kwargs):
        if name not in self.actions:
            print("Action not defined")
        else:
            self.actions[name](self, *args, **kwargs)


manager = Manager()


# @manager.assign("sale")
# def printer(manager):
# print("yes")

# how to match commands/functions with my codes????
# QQ: Extend sale, purchase etc??
# while True:
#     action = input("See the available commands [sale/purchase/inventory/balance/account/history]: \n ")
#     if action == "sale":
#         manager.execute("sale")
#     elif action == "purchase":
#         manager.execute("purchase")
#     elif action == "inventory":
#         manager.execute("inventory")
#     elif action == "balance":
#         manager.execute("balance")
#     elif action == "account":
#         manager.execute("account")
#     elif action == "history":
#         manager.execute("history")
#     else:
#         print("Exit the program.")
#         break

from ast import literal_eval


def loading_inventory(file_name):
    try:
        with open(file_name, "r") as file1:
            return literal_eval(file1.read())
    except FileNotFoundError:
        print("This file does not exist. Please create new file. ")
        return {}


def saving_inventory(file_name, inventory):
    with open(file_name, "w") as file1:
        file1.write(str(inventory))


def loading_balance(file_name):
    try:
        with open(file_name, "r") as file2:
            return literal_eval(file2.read())

    except FileNotFoundError:
        print("This file does not exist. Please create new file. ")
        return {}


def saving_balance(file_name, balance):
    with open(file_name, "w") as file2:
        file2.write(str(balance))


def loading_history(file_name):  # history is a list ?how to use it? loke -.readline() ?
    try:
        with open(file_name, "r") as file3:
            return literal_eval(file3.read())
    except FileNotFoundError:
        print("This file does not exist. Please create new file. ")
        return []


def saving_history(file_name, history):
    with open(file_name, "w") as file3:
        file3.write(str(history))

checklist = list()

def create(item):
    checklist.append(item)
    print("You added {} to the list".format(item))

def read(index):
    return "reading index {}: {}".format(index, checklist[int(index)])

def update(index, item):
    prev_item = checklist[item]
    checklist[index] = item
    print("You updated {} to {}".format(prev_item, item))

def destroy(index):
    del_item = checklist[index]
    checklist.pop(int(index))
    print("You removed {} from the list.".format(del_item))

def list_all_items():
    print("Printing all items: ")
    index = 0
    for item in checklist:
        print("{} {}".format(index, item))
        index += 1

def mark_completed(index):
    checklist[index] = "√ {}".format(checklist[index])

def user_input(prompt):
    user_input = input(prompt).upper()
    return user_input

def check_index(index):
    if index >= len(checklist):
        if len(checklist) == 1:
            print("There is only one item in the list. Please choose index 0 to view item.")
        else:
            print("The list has only {} items. Please enter a number between 0 to {}".format(len(checklist), len(checklist) - 1))
        return False
    return True

def select(function_code):
    if function_code == "1":
        input_item = user_input("Input item: ")
        create(input_item)

    elif function_code == "2":
        if len(checklist) == 0:
            print("There are no items in the list.")
        else:
            item_index = int(user_input("Index Number: "))
            if check_index(item_index):
                print(read(item_index))

    elif function_code == "5":
        list_all_items()

    elif function_code == "Q":
        return False

    else:
        print("Unknown Option")

    print()
    return True

# def test():
    # create("purple sox") # checklist == ["purple sox"]
    # create("red cloak") # checklist == ["purple sox", "red cloak"]

    # print(read(0)) # return "purple sox"
    # print(read(1)) # return "red cloak"

    # update(0, "purple socks") # checklist == ["purple socks", "red cloak"]
    # destroy(1) # checklist == ["purple socks"]

    # print(read(0)) # return "purple socks"
    # print(read(1)) # error
    # print(checklist)

    # list_all_items()

    # select("C")
    # list_all_items()
    # select("R")
    # list_all_items()
    # select("P")
    # list_all_items()
    # select("A")
    # list_all_items()

# test()

prompt = """Choose one:
[1] add an item to the list
[2] read an item from the list
[3] update an item
[4] delete an item
[5] display the list
[Q] quit

Your input: """

user_select = True
while user_select == True:
    selection = user_input(prompt)
    print()
    user_select = select(selection)

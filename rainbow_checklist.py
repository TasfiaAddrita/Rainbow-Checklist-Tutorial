from termcolor import colored
from os import system, name
from time import sleep

checklist = list()

# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    return checklist[int(index)]

# UPDATE
def update(index, new_item):
    checklist[index] = new_item

# DESTROY
def destroy(index):
    checklist.pop(int(index))

# LIST ALL ITEMS
def list_all_items():
    print("Printing all items: ")
    index = 0
    for item in checklist:
        print("Index {} - {}".format(index, color_text(item)))
        index += 1

# MARK ITEM AS COMPLETED
def mark_complete(index):
    checklist[index] = "√ {}".format(checklist[index])

# MARK ITEM AS UNCOMPLETED
def mark_uncomplete(index):
    checklist[index] = "{}".format(checklist[index].replace("√ ", ""))

# CHECK IF ITEM IS COMPLETE
def check_complete(index):
    if "√" in checklist[index]:
        return True
    return False

# GET USER INPUT
def user_input(prompt):
    user_input = input(prompt)
    return user_input

# CHECK IF INDEX IS VALID (not negative, within list's bounds)
def check_index(index):
    if index >= len(checklist):
        if len(checklist) == 1:
            print("There is only one item in the list. Please choose index 0.")
        else:
            print("The list has only {} items. Please enter a number between 0 to {}.".format(len(checklist), len(checklist) - 1))
        return False
    if index < 0:
        print("Please enter positive numbers.")
        return False
    return True

# COLOR WORDS THAT ARE "COLORS"
def color_text(item):
    colors = ["grey", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
    item_list = item.split(" ")
    for index in range(len(item_list)):
        if item_list[index] in colors:
            item_list[index] = colored(item_list[index], item_list[index])
    return " ".join(item_list)

# CREDITS GO TO GEEKS FOR GEEKS: https://www.geeksforgeeks.org/clear-screen-python/
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# SELECT MENU
def select(function_code):
    print("----------------------------------------------------------------------")

    # only CREATE and QUIT options should be available if there are no items in the checklist
    if (function_code != "C" and function_code != "Q") and (len(checklist) == 0):
        print("Please pick an option from the list.")

    # CREATE ITEM
    elif function_code == "C":
        input_item = user_input("Add item: ")
        create(input_item)
        print("You added {} to the list.".format(color_text(input_item)))

    # READ ITEM
    elif function_code == "R":
        item_index = int(user_input("Item's index number to read: "))
        if check_index(item_index):
            read(item_index)
            print("Reading index {}: {}".format(item_index, color_text(checklist[item_index])))

    # UPDATE ITEM
    elif function_code == "U":
        item_index = int(user_input("Item's index number to update: "))
        if check_index(item_index):
            item_update = user_input("Replace index {} with: ".format(item_index))
            prev_item = checklist[item_index]
            update(item_index, item_update)
            print("You updated {} to {}".format(color_text(prev_item), color_text(checklist[item_index])))

    # DELETE ITEM
    elif function_code == "D":
        item_index = int(user_input("Item's index number to delete: "))
        if check_index(item_index):
            del_item = checklist[item_index]
            destroy(item_index)
            print("You removed {} from the list.".format(color_text(del_item)))

    # MARK ITEM AS COMPLETE
    elif function_code == "M":
        item_index = int(user_input("Item's index number to mark complete: "))
        if check_index(item_index):
            if check_complete(item_index) == False:
                print("You marked {} as complete.".format(color_text(checklist[item_index])))
                mark_complete(item_index)
            else:
                print("{} is already marked complete".format(color_text(checklist[item_index][2:])))

    # MARK ITEM AS UNCOMPLETE
    elif function_code == "N":
        item_index = int(user_input("Item's index number to mark uncomplete: "))
        if check_index(item_index):
            if check_complete(item_index):
                mark_uncomplete(item_index)
                print("You marked {} as uncomplete.".format(color_text(checklist[item_index])))
            else:
                print("{} is already marked uncomplete".format(color_text(checklist[item_index])))

    # PRINT ALL ITEMS
    elif function_code == "P":
        list_all_items()

    # QUIT PROGRAM
    elif function_code == "Q":
        return False

    # USER DIDN'T CHOOSE AN OPTION FROM MENU
    else:
        print("Please pick an option from the list.")

    return True

def main():
    clear()
    print("Hi! Welcome to Captain Rainbow's Color Checklist! Here you can add, read, update, and delete items in the checklist. Lets get started!")
    prompt_begin = "----------------------------------------------------------------------\nChoose one:\n"
    create_choice_prompt = "[C] Add an item to the list \n"
    read_choice_prompt = "[R] Read an item from the list \n"
    update_choice_prompt = "[U] Update an item \n"
    delete_choice_prompt = "[D] Delete an item \n"
    mark_complete_choice_prompt = "[M] Mark an item as complete \n"
    mark_uncomplete_choice_prompt = "[N] Mark an item as uncomplete \n"
    print_choice_prompt = "[P] Display all items \n"
    quit_choice_prompt = "[Q] Quit \n"
    prompt_end = "\nYour input: "

    # CONTINUOUS LOOP UNTIL USER QUITS
    user_select = True
    while user_select == True:
        if len(checklist) == 0:
            selection = user_input(prompt_begin + create_choice_prompt + quit_choice_prompt + prompt_end).upper()
        else:
            selection = user_input(prompt_begin + create_choice_prompt + read_choice_prompt + update_choice_prompt + delete_choice_prompt + mark_complete_choice_prompt + mark_uncomplete_choice_prompt + print_choice_prompt + quit_choice_prompt + prompt_end).upper()
        if selection != 'Q':
            sleep(1)
            clear()
        user_select = select(selection.upper())

    print("Goodbye! Thanks for using the Rainbow Checklist!")

def test():
    create("purple sox") # ["purple sox"]
    create("red cloak") # ["purple sox", "red cloak"]
    create("blue jeans") # ["purple sox", "red cloak", "blue jeans"]
    create("green tie") # ["purple sox", "red cloak", "blue jeans", "green tie"]

    print()
    print(checklist)

    print()
    print(read(0)) # return "purple sox"
    print(read(1)) # return "red cloak"

    update(0, "purple socks") # ["purple socks", "red cloak", "blue jeans", "green tie"]
    destroy(1) # deletes "red cloak", ["purple socks", "blue jeans", "green tie"]

    print()
    print(checklist)

    print()
    print(read(1)) # return "blue jeans"

    # all should return errors
    print()
    try:
        print(update(6, "grey blouse"))
    except:
        print("error")

    print()
    list_all_items()

    select("C") # add magenta glasses
    list_all_items()
    select("R") # put in index 3, return magenta glasses
    select("R") # put in index 4, should return error message
    select("R") # put in index -1, should return error message

    for index in range(len(checklist) - 1): # remove red, blue, and green items
        select("D")
        print()
        list_all_items()

    select("R") # any number other than 0 should result in error

    select("U") # 0, red tie
    select("U") # any number other than 0 should result in error

    select("M") # 0, check red tie
    select("M") # 0, error
    select("M") # 2, error
    print()
    list_all_items()

    select("N") # 0, uncheck red tie
    select("N") # 0, error
    select("N") # 2, error
    print()
    list_all_items()

    select("P") # print items

    select("C") # add grey blouse
    select("M") # index 1
    select("M") # index 2
    select("M") # index 1

    select("Q")

# test()

main()

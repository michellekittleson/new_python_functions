# Task 1: Write a function that lets the user add items to a list.

shopping_list = []

def add_item():
    global shopping_list
    item = input("Enter the item to add to the list: ")
    shopping_list.append(item)

# Task 2: Include a function to remove items from the list.

def remove_item():
    global shopping_list
    item = input("Enter the item to remove from the list: ")
    shopping_list.remove(item)

# Task 3: Add a function that prints out the entire list in a formatted way.

def display_list():
    print("\nShopping List: ")
    for item in shopping_list:
        print(item)

while True:
    choice = input("What would you like to do? [A]dd item, [R]emove item, [D]isplay list, or [Q]uit? ")
    if choice == 'A':
        add_item()
    elif choice == 'R':
        remove_item()
    elif choice == 'D':
        display_list()
    elif choice == 'Q':
        break
    else:
        print("Please make a valid choice. ")
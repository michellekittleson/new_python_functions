# Task 1: Create functions for each arithmetic operation

def addition():
    a = float(input("Enter the first number to add: "))
    b = float(input("Enter the second number to add: "))
    sum = a + b
    print(f"{a} + {b} = {sum}")

def subtraction():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the number to subtract from the previous number: "))
    difference = a - b
    print(f"{a} - {b} = {difference}")

def multiplication():
    a = float(input("Enter the first number to multiply: "))
    b = float(input("Enter the second number to multiply: "))
    product = a * b
    print(f"{a} x {b} = {product}")

def division():
    a = float(input("Enter the first number of the quotient: "))
    b = float(input("Enter the number to divide the first number by: "))
    # Task 3: Ensure your code can handle division by zero and other potential errors.
    if b == 0:
        print("Cannot divide by zero. Please choose a different number.")
    else:
        quotient = a / b
        print(f"{a} / {b} = {quotient}")

# Task 2: Use inputs to ask the user what operations they want to perform, and what numbers they want to use.
while True:
    operation = input("Enter which operation to perform: [A]ddition, [S]ubtraction, [M]ultiplication, [D]ivision, or [Q]uit: ")
    if operation == 'A':
        addition()
    elif operation == 'S':
        subtraction()
    elif operation == 'M':
        multiplication()
    elif operation == 'D':
        division()
    elif operation == 'Q':
        break
    else:
        print("Please enter a valid choice.")

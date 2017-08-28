'''
Testing a basic calculator
'''

print("This is a basic calculator.")
print("To perform a calculation, choose from the options below:")
print("Add")
print("Subtract")
print("Multiply")
print("Divide")

operation = input("> ")

if str.lower(operation) == 'add':
    print("Ok, you've chosen to add two numbers")
    print("Enter the first number:")
    add_first_number = input("> ")
    print("Enter the second number:")
    add_second_number = input("> ")
    result = int(add_first_number) + int(add_second_number)
    print(f"{add_first_number} plus {add_second_number} equals {result}")

elif str.lower(operation) == 'subtract':
    print("Ok, you've chosen to subtract two numbers")
    print("Enter the first number:")
    subtract_first_number = input("> ")
    print("Enter the second number:")
    subtract_second_number = input("> ")
    result = int(subtract_first_number) - int(subtract_second_number)
    print(f"{subtract_first_number} minus {subtract_second_number} equals {result}")

elif str.lower(operation) == 'multiply':
    print("Ok, you've chosen to multiply two numbers")
    print("Enter the first number:")
    multiply_first_number = input("> ")
    print("Enter second number:")
    multiply_second_number = input("> ")
    result = int(multiply_first_number) * int(multiply_second_number)
    print(f"{multiply_first_number} multiplied by {multiply_second_number} equals {result}")

elif str.lower(operation) == 'divide':
    print("Ok, you've chosen to divide two numbers")
    print("Enter the first number:")
    divide_first_number = input("> ")
    print("Enter second number")
    divide_second_number = input("> ")
    result = int(divide_first_number) / int(divide_second_number)
    print(f"{divide_first_number} divided by {divide_second_number} equals {result}")

else:
    print("I don't understand that...")

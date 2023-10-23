# Get user input for two numbers and the operation
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
opr = input("Enter the operation (+, -, *, /): ")

# Perform the selected operation and print the result
if opr == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif opr == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif opr == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif opr == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
else:
    print("Invalid operation. Please enter one of the allowed operations: +, -, *, /")


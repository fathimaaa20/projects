operator = input("Enter the operator (+, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == '+':
    result = num1 + num2
    print(f"The result of {num1} + {num2} is {round(result, 3)}")
elif operator == '-':
    result = num1 - num2
    print(f"The result of {num1} - {num2} is {round(result, 3)}")
elif operator == '*':
    result = num1 * num2
    print(f"The result of {num1} * {num2} is {round(result, 3)}")
elif operator == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is {round(result, 3)}")
else:
    print("Invalid operator! Please use +, -, *, or /.")

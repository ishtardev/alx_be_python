num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
op = input("Choose the operation (+, -, *, /): ").strip()

result = None

match op:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
    case _:
        print("Invalid operation.")

if result is not None:
    print(f"The result is {result}")
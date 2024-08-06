def calculator():
   
    try:
        num1 = float(input("Enter the first number: "))
    except ValueError:
        return "Invalid input for the first number. Please enter a numeric value."

    
    try:
        num2 = float(input("Enter the second number: "))
    except ValueError:
        return "Invalid input for the second number. Please enter a numeric value."

    
    print("Choose an operation:")
    print("Addition (+)")
    print("Subtraction (-)")
    print("Multiplication (*)")
    print("Division (/)")

    operation = input("Enter the operation (+, -, *, /): ").strip()

   
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        result = num1 / num2
    else:
        return "Invalid operation. Please enter one of +, -, *, /."

    return f"The result of {num1} {operation} {num2} is {result}"


print(calculator())



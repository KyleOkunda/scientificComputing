def calculator():
    """
    A simple calculator program that takes two numbers and an operator
    from the user and performs the corresponding calculation.
    """
    try:
        # Get the first number from the user.
        num1 = float(input("Enter the first number: "))
        
        # Get the operator from the user.
        operator = input("Enter an operator (+, -, *, /): ")
        
        # Get the second number from the user.
        num2 = float(input("Enter the second number: "))
        
        result = 0

        # Perform the calculation based on the operator.
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            # Handle division by zero to prevent an error.
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operator. Please use one of: +, -, *, /")
            return

        # Print the formatted result.
        print(f"{num1} {operator} {num2} = {result}")

    except ValueError:
        # Handle cases where the user enters non-numeric input.
        print("Invalid input. Please enter valid numbers.")

# Run the calculator program.
if __name__ == "__main__":
    calculator()

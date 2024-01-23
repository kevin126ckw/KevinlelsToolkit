# model_calc.py

def calc():

    # Define functions
    def add(x, y):
        """Addition"""

        return x + y

    def subtract(x, y):
        """Subtraction"""

        return x - y

    def multiply(x, y):
        """Multiplication"""

        return x * y

    def divide(x, y):
        """Division"""

        return x / y

    # User input
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1/2/3/4):")

    num1 = input("Enter the first number: ")
    try:
        num1 = int(num1)
    except ValueError:
        print("Invalid input")

    num2 = input("Enter the second number: ")
    try:
        num2 = int(num2)
    except ValueError:
        print("Invalid input")

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid input")

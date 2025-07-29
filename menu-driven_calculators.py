def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed"
    
while True:
    print("\nMenu:")
    print("1. Addition")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose a number:")
    if choice == "5":
        print("Existing Calculator")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == "1":
        print("Result: ", add(num1, num2))
    elif choice == "2":
        print("Result:", subtract(num1, num2))
    elif choice == "3":
        print("Result: ", multiply(num1, num2))
    elif choice == "4":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice. Please pick from the menu and try again")
# TASK 2 - CALCULATOR   

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Display menu
print("Select operation : ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take input from user
choice = input("Enter choice (1/2/3/4) : ")

try:
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))

    if choice == '1':
        print("Result :", add(num1, num2))
    elif choice == '2':
        print("Result :", subtract(num1, num2))
    elif choice == '3':
        print("Result :", multiply(num1, num2))
    elif choice == '4':
        print("Result :", divide(num1, num2))
    else:
        print("Invalid input! Please select a valid option.")

except ValueError:
    print("Invalid input! Please enter numeric values.")
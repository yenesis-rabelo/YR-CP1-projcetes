#Yenesis Rabelo Calculator SkillPractice

def calculator():
    # asking user for input
    try:
        num1 = float(input("Enter the first number: "))  # cnvert input to float
        num2 = float(input("Enter the second number: "))  # convert input to float
    except ValueError:  # catch invalid inputs
        print("Invalid input! Please enter numeric values.")
        return  # exit the function if input is not valid

    # asking for the operation
    operation = input("Enter the operation (+, -, *, /): ").strip()

    # performing the selected operation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        # checking for division by zero
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
            return  # exiting the function to avoid invalid operation
        result = num1 / num2
    else:
        print("Invalid operation! Please choose +, -, *, or /.")
        return  # exit if the operation is not valid

    # printing the result
    print(f"The result of {num1} {operation} {num2} is: {result}")

# call the calculator function
calculator()

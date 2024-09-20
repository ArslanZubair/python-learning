
print("------------ Calculater using functions --------------")
def add(num1:int,num2:int):
    return num1 + num2


def subtract(num1:int,num2:int):
    return num1 - num2



def multiply(num1:int,num2:int):
    return num1 * num2


def divide(num1:int,num2:int):
    if num2 == 0:
        print("Error: Division can not be apply by zero")
        return
    return num1 / num2


def main():
    user_input1 = int(input("Enter your first number:"))
    user_input2 = int(input("Enter your second: "))
    operator = input("Enter the operator (+, -, *, /): ")
    if operator == '+':
        result = add(user_input1,user_input2)
    elif operator == '-':
        result = subtract(user_input1,user_input2)
    elif operator == '*':
        result = multiply(user_input1, user_input2)
    else:
        result = divide(user_input1, user_input2)

    print("The result is: ",result)

main()

# infinite loop to keep the calculator running until user decides to exit
print("Do you want to continue? (y/n):")
user_choice = input().lower()
while user_choice == 'y':
    main()
    

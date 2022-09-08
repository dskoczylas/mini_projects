def mainMenu():
    print("1. ADD")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVIDE")
    print("5. EXIT")
    print("CHOOSE OPTION:")

def addition():
    num1 = input("Please enter first number: ")
    num2 = input("Please enter second number: ")
    res = int(num1)+int(num2)
    print("Sum is: %d" %res)
def substraction():
    num1 = input("Please enter first number: ")
    num2 = input("Please enter second number: ")
    res = int(num1)-int(num2)
    print("Substraction is: %d" %res)
def multiply():
    num1 = input("Please enter first number: ")
    num2 = input("Please enter second number: ")
    res = int(num1)*int(num2)
    print("Multiply is: %d" %res)
def division():
    num1 = input("Please enter first number: ")
    num2 = input("Please enter second number: ")
    res = float(num1)/float(num2)
    print("Division is: %f" %res)


print("WELCOME TO MY CALCULATOR APP!")

while True:
    mainMenu()
    option = input()
    if option == "1":
        addition()
    elif option == "2":
        substraction()
    elif option == "3":
        multiply()
    elif option == "4":
        division()
    elif option == "5":
        print("Thanks for using program, see you next time!")
        break
    else:
        print("Please enter correct number!")

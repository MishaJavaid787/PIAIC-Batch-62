# Basic Calculator Operations User input
num1 =input("enter first number: ")
num2 = input("enter second number: ")
operator = input("Enter the operator (+, -, *, /): ")
if operator == "+":
    print("Output: " + str(int(num1) + int(num2)))
elif operator == "-":
    print("Output: "  + str(int(num1) - int(num2)))
elif operator == "*":
    print("Output: " + str(int(num1) * int(num2)))
elif operator == "/":
    print("Output: " + str(int(num1) / int(num2)))
    # check for division by 0
else :
    print ("invalid entry") 

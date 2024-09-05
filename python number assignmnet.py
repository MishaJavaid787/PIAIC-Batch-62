name = input ("enter your name: ")
print (f"Hello, {name}, Let's play a game using your favourite numbers: ")
num1 =input("enter first number: ")
num2 = input("enter second number: ")
num3 = input("enter third number: ")
numbers = [num1, num2, num3]
print (numbers)
fave_numbers= [4,7,12]
my_tuple1 = tuple (fave_numbers)
print (my_tuple1)
even_numbers = []
odd_numbers =[]
even_numbers = [num for num in fave_numbers if num % 2 == 0]
odd_numbers = [num for num in fave_numbers if num % 2 != 0]

print ("Even numbers:", even_numbers)
print ("Odd numbers:",odd_numbers)

tuple1 = ("The number", num1, "is an odd number.")
tuple2 = ("The number", num2, "is an even number.")
tuple3 = ("The number", num3, "is again an odd number.")
print(tuple1)
print(tuple2)
print(tuple3)

squares= []
for number in fave_numbers:
    squares.append(number ** 2)

#print (squares)
my_tuple2 = tuple (squares)
print (my_tuple2)
combined = my_tuple1 + my_tuple2
#print (combined)
for num in my_tuple1:
    squares.append(num ** 2)
    my_tuple3= (num, num**2)
    print ("The number", num, "and its square:", my_tuple3)
operator = input("Enter the operator (+, -, *, /): ")
if operator == "+":
    Output = ("Well, the sum of your favorite numbers is: " + str (int(num1) + int(num2)+ int (num3)))
    print(Output)
Output = 23
if Output ==1:
        print ("not prime")
if Output >1:
    for i in range (2, Output):
        if (Output) % i == 0:
            print (f" Wow, {Output}, is not a prime number: ")
            break
    else:
        print(f"Wow, {Output}, is a prime number.")

















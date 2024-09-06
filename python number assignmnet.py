name = input("Enter your name: ")
print(f"Hello, {name}, let's play a game using your favourite numbers:")

# Input numbers as integers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

numbers = [num1, num2, num3]
print(numbers)

even_numbers = []
odd_numbers = []
tuple_list = []
tuple_squares = []

# Determine if numbers are even or odd
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
        tuple_list.append(f"The number {num} is even.")
    else:
        odd_numbers.append(num)
        tuple_list.append(f"The number {num} is odd.")

for num in tuple_list:
    print(num)

# Calculate squares and store in tuples
for num in numbers:
    my_tuple = (num, num ** 2)
    tuple_squares.append(my_tuple)
    print(f"The number {num} and its square: {my_tuple}")

# Calculate the total sum of the numbers
total_sum = sum(numbers)
print("Well, the sum of your favorite numbers is: " + str(total_sum))

# Check if the total_sum is a prime number
is_Prime=True
if total_sum == 1:
    print("1 is not prime.")
    is_Prime=False
elif total_sum > 1:
    for i in range(2, total_sum):
        if total_sum % i == 0:
            print(f"Wow, {total_sum} is not a prime number.")
            is_Prime=False
            break

if is_Prime:
    print(f"Wow, {total_sum} is a prime number.")

















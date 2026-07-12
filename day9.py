#print("Hello world")

# age = 18
# if age >= 18:
#     print("You can vote")
# else:
#     print("You cannot vote")

# for i in range(1, 7):
#     print(i)

# i = 1
# while i <= 5:
#     print(i)
#     i = i + 1

# print("Welcome to python!")

# name = input("Enter your name:")
# age = int(input("Enter your age:"))
# if age >= 18:
#     print("Hello", name)
#     print("You can vote")
# else:
#     print("Hello", name)
#     print("You cannot vote")

#     print("\ncounting from 1 to 5:")
#     for i in range(1, 6):
#         print(i)

# number = int(input("Enter a number:"))
# if number % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

# num1 = int(input("Enter first number:"))
# num2 = int(input("Enter second number:"))
# sum = num1 + num2
# print("The sum is:", sum)

# print("------ Multiplication Table ------")
# number = int(input("Enter a number:"))
# for i in range(1, 11):
#     print(number, "x", i, "=", number * i)

# print("------ Calculator ------")
# num1 = int(input("Enter first number:"))
# num2 = int(input("Enter second number:"))

# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")
# choice = int(input("Enter your choice:"))
# if choice == 1:
#     print("Answer =", num1 + num2)
# elif choice == 2:
#     print("Answer =", num1 - num2)
# elif choice == 3:
#     print("Answer =", num1 * num2)
# elif choice == 4:
#     print("Answer =", num1 / num2)
# else:
#     print("Invalid choice")

print("------ Login ------")
username = input("Enter your username:")
password = int(input("Enter your password:"))

if username == "Rohit" and password == 1234:
    print("Login successful")
else:
    print("invalid username or password")
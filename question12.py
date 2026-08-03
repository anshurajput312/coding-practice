# Write a program to generate a menu which will have options of 
# 1. sum of n natural numbers 
# 2. reverse of given number 
# 3. Count how many times a input number is repeated
# 4. Lcm of two digits
# 5. exit
# ask value form user
from math import gcd


while True:
    print("1. Sum of n natural numbers")
    print("2. Reverse of given number")
    print("3. Count how many times a input number is repeated")
    print("4. Lcm of two digits")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter a number: "))
        sum_n = n * (n + 1) // 2
        print("The sum of first", n, "natural numbers is:", sum_n)

    elif choice == 2:
        number = int(input("Enter a number: "))
        reverse = 0
        while number != 0:
            digit = number % 10
            reverse = reverse * 10 + digit
            number //= 10
        print("The reverse of the given number is:", reverse)

    elif choice == 3:
        num = int(input("Enter a number: "))
        count = 0
        while num != 0:
            digit = num % 10
            count += 1
            num //= 10
        print("The numberis repeated", count, "times.")

    elif choice == 4:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        lcm = (num1 * num2) // gcd(num1, num2)
        print("The LCM of", num1, "and", num2, "is:", lcm)

    elif choice == 5:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")
        
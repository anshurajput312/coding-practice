# write a program to find the number of digits in a given number.
number = int(input("Enter a number: "))
count = 0
while number != 0:
    number //= 10
    count += 1
print("The number of digits in the given number is:", count)
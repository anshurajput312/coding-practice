# WRP to find the number of digits in given number
n = int(input("Enter a number: "))
count = 0
while n > 0:
    count += 1
    n //= 10
print("Number of digits:", count) 

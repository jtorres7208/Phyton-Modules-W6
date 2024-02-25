#Julian Torres
#2/24/2024
import math

num = int(input("Enter a number: "))

# Calculate factorial using for loop
factorial = 1
for i in range(1, num+1):
    factorial *= i

print("Factorial by for loop:", factorial) 

# Calculate factorial using math.factorial
print("Factorial by math.factorial:", math.factorial(num))

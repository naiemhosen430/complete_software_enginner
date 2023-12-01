# Task 4: Function Practice

# Write a Python program that defines a function to calculate the factorial of a number. 
# Test the function by calculating the factorial of 5.

def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


print("So result is ", factorial(5))


# Completed
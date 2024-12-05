def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Input from the user
number = int(input("Enter a number: "))

# Calculate and display the factorial
print(f"The factorial of {number} is {factorial(number)}.")

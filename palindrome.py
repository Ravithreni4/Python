def is_palindrome_number(number):
    # Convert the number to a string
    str_number = str(number)
    # Check if the string is the same when reversed
    return str_number == str_number[::-1]

# Input from the user
number = int(input("Enter a number: "))

# Check if the number is a palindrome
if is_palindrome_number(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")

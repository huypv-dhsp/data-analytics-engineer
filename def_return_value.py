def calculate_factorial(number):
    if number <= 1:
        return 1

    i = 1
    result = 1
    while i <= number:
        result = result * i
        i = i + 1

    return result


factorial_of_5 = calculate_factorial(5)
print(f"The factorial of 5 is: {factorial_of_5}")
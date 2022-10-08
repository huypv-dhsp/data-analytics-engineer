# Exercise 1: Check a number odd or even
def check_odd_or_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

my_number = -10
if check_odd_or_even(my_number):
    print(f"{my_number} is an even number")
else:
    print(f"{my_number} is an odd number")

# Excercise 2: Get the sum of all even numbers less than or equal a number

def calculate_sum_of_even_numbers(number):
    if number < 0:
        print("Number must be larger than 0.")
        pass

    i = 0
    result = 0
    while i <= number:
        if check_odd_or_even(i):
            result = result + i
        i = i + 1

    return result


sum_of_even_of_my_number = calculate_sum_of_even_numbers(my_number)
print(f"The sum of even numbers less than or equal to {my_number} is: {sum_of_even_of_my_number}")
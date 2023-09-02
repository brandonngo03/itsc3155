def get_valid_int_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter an integer.")

def sum_five_integers():
    total = 0
    for _ in range(5):
        num = get_valid_int_input("Enter an integer: ")
        total += num
    return total

# Call the function to sum 5 integers
result = sum_five_integers()
print("The sum of the entered integers is:", result)
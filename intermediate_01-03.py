def count_letters(input_string):
    letter_count = {}
    
    for char in input_string:
        if char.isalpha():  # Check if the character is a letter
            char = char.lower()  # Convert to lowercase
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    
    return letter_count

# Take user input and test the function
user_input = input("Enter a string: ")
result = count_letters(user_input)
print(result)
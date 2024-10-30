#Write a Python code to accept a string from the user and display characters present at an even index number.
#For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.

user_input = input("Please enter a string: ")
print("You entered:", user_input)
string_length = len(user_input)
print("The length of the string is:", string_length)
for i in range(0, len(user_input), 2):
    print(f"Character at even index {i} is: {user_input[i]}")
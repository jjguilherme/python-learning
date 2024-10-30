number_one = int(input("What is the first number? "))
number_two = int(input("What is the second number? "))

rest = number_one % number_two  # Store the remainder

if rest % 2 == 1:  # Checking if the remainder is odd
    print(f"The remainder {rest} is odd!")
else:
    print(f"The remainder {rest} is even!")

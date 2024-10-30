previous_num = 0
for i in range(1, 11):  # To include the first 10 numbers
    current_sum = previous_num + i
    print(f"Current number: {i}, Previous number: {previous_num}, Sum: {current_sum}")
    previous_num = i  # Update the previous number
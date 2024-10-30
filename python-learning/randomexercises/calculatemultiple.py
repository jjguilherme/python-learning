#Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

def multiple_numbers(num1,num2):

    var = num1 * num2
    if var >= 1000:
        return print("Impossible")
    elif var <= 1000:
        return print("The result is", var)


print(multiple_numbers(100,3000))

def multiple_numbers(num1, num2):
    result = num1 * num2
    if result >= 1000:
        return "Impossible"
    return f"The result is {result}"

print(multiple_numbers(10, 30))
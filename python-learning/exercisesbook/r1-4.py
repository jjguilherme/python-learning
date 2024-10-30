#Write a short Python function that takes a positive integer n and returns
#the sum of the squares of all the positive integers smaller than n

def sum_squares(n):
    total=0
    for i in range(1, n):
        total += i ** 2
    return total

print(sum_squares(5))

    


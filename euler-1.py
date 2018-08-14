# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


n = 999


def sum_divisible(x):
    return (x + (n // x) * x) * (n // x) / 2


sum = int(sum_divisible(3) + sum_divisible(5) - sum_divisible(15))
print(sum)

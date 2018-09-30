# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome(x):
    x = str(x)
    y = ''
    i = 1
    while i <= len(x):
        y += x[len(x) - i]
        i += 1
    if x == y:
        return True
    else:
        return False


z = 0
x = 999
while x >= 100:
    y = 999
    while y >= x:
        if x * y <= z:
            break
        if is_palindrome(x * y):
            if x * y > z:
                z = x * y
        y -= 1
    x -= 1


print(z)

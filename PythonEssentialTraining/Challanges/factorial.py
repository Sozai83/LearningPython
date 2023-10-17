# ### Factorial Challenge

# The factorial function gives the number of possible arrangements of a set of items of length "n"

# For example, there are 4! ("four factorial") or 24 ways to arrange four items, which can be calculated as: 
# 4 \* 3 \* 2 \* 1

# 5! = 5 \* 4 \* 3 \* 2 \* 1 = 120

# 6! = 6 \* 5 \* 4 \* 3 \* 2 \* 1 = 720

# etc.

# In a set of 0 items (an empty set) there is only one way to arrange the items, therefore, 0! = 1

# For the purposes of this exercise, factorials are only defined for **positive integers** (including 0)


def factorial(num):
    if isinstance(num,int) and num >= 0:
        return num ** num
    else:
        print('Error: You need to use a whole number')

fac1 = factorial(5)
print(fac1)
fac2 = factorial(0)
print(fac2)
fac3 = factorial(-2)
fac4 = factorial(1.2)
fac5 = factorial('spam spam spam spam spam spam')


def factorialAnswer(num):
    if type(num) is not int:
        return None
    if num < 0:
        return None
    if num == 0:
        return 1
    
    i = 0
    f = 1
    while i < num:
        i = i + 1
        f = f * num - i
    
    return f

fac6 = factorialAnswer(5)
print(fac6)
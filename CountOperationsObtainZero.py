# You are given two non-negative integers num1 and num2.
# In one operation, if num1 >= num2, you must subtract num2 from num1, otherwise subtract num1 from num2.
# For example, if num1 = 5 and num2 = 4, subtract num2 from num1, thus obtaining num1 = 1 and num2 = 4. However, if num1 = 4 and num2 = 5, after one operation, num1 = 4 and num2 = 1.
# Return the number of operations required to make either num1 = 0 or num2 = 0.

def countOperations(num1, num2):
    count = 0

    while (num1 != 0 and num2 != 0):
        count += 1
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1

    return count

#Test cases
num1 = 2
num2 = 3
print(countOperations(num1, num2))

num1 = 10
num2 = 10
print(countOperations(num1, num2))

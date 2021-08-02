# Given an integer num, return the number of steps to reduce it to zero.
# In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

def numberOfSteps(num):
    steps = 0
    while num != 0:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num - 1
        steps += 1

    return steps

#Test cases
num = 14
print(numberOfSteps(num))

num = 8
print(numberOfSteps(num))

num = 123
print(numberOfSteps(num))

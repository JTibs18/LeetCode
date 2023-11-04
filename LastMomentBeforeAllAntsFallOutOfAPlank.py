# We have a wooden plank of the length n units. Some ants are walking on the plank, each ant moves with a speed of 1 unit per second. Some of the ants move to the left, the other move to the right.
# When two ants moving in two different directions meet at some point, they change their directions and continue moving again. Assume changing directions does not take any additional time.
# When an ant reaches one end of the plank at a time t, it falls out of the plank immediately.
# Given an integer n and two integer arrays left and right, the positions of the ants moving to the left and the right, return the moment when the last ant(s) fall out of the plank.

def getLastMoment(n, left, right):
    if len(left) > 0 and len(right) > 0: 
        if max(left) > n - min(right): 
            return max(left)
        return n - min(right)

    if len(left) > 0:
        return max(left)
    
    return n - min(right)

# Test cases 
n = 4
left = [4, 3]
right = [0, 1]
print(getLastMoment(n, left, right))

n = 7
left = []
right = [0, 1, 2, 3, 4, 5, 6, 7]
print(getLastMoment(n, left, right))

n = 7
left = [0, 1, 2, 3, 4, 5, 6, 7]
right = []
print(getLastMoment(n, left, right))

n = 9 
left = [5]
right = [4]
print(getLastMoment(n, left, right))

n = 1000
left = [0]
right = []
print(getLastMoment(n, left, right))

n = 11
left = [1, 4, 5, 10, 9]
right = [2, 7, 6, 3]
print(getLastMoment(n, left, right))

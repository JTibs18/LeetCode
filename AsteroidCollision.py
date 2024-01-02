# We are given an array asteroids of integers representing asteroids in a row.
# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

def asteroidCollision(asteroids):
    stack = []
    returnedAsteroids = []

    for a in asteroids:
        if a < 0 and len(stack) == 0:
            returnedAsteroids.append(a)
        elif a < 0:
            while len(stack) > 0 and abs(a) > abs(stack[-1]):
                stack.pop()
            
            if len(stack) > 0 and abs(a) == abs(stack[-1]):
                stack.pop()
            elif len(stack) == 0:
                returnedAsteroids.append(a)
        else:
            stack.append(a)

    return returnedAsteroids + stack

# Test cases
asteroids = [5,10,-5]
print(asteroidCollision(asteroids))

asteroids = [8,-8]
print(asteroidCollision(asteroids))

asteroids = [10,2,-5]
print(asteroidCollision(asteroids))

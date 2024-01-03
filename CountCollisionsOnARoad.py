# There are n cars on an infinitely long road. The cars are numbered from 0 to n - 1 from left to right and each car is present at a unique point.
# You are given a 0-indexed string directions of length n. directions[i] can be either 'L', 'R', or 'S' denoting whether the ith car is moving towards the left, towards the right, or staying at its current point respectively. Each moving car has the same speed.
# The number of collisions can be calculated as follows:
#   When two cars moving in opposite directions collide with each other, the number of collisions increases by 2.
#   When a moving car collides with a stationary car, the number of collisions increases by 1.
# After a collision, the cars involved can no longer move and will stay at the point where they collided. Other than that, cars cannot change their state or direction of motion.
# Return the total number of collisions that will happen on the road.

def countCollisions(directions):
    collisionCount = 0 
    stack = []

    for i in directions:
        if i == "L" and len(stack):
            collisionCount += 1

            while len(stack) and stack[-1] == "R":
                stack.pop()
                collisionCount += 1

            stack.append("S")
        elif i == "R": 
            stack.append(i)
        elif i == "S":
            while len(stack) and stack[-1] == "R":
                stack.pop()
                collisionCount += 1 
            stack.append(i)

    return collisionCount

# Test cases
directions = "RLRSLL"
print(countCollisions(directions))

directions = "LLRR"
print(countCollisions(directions))

directions = "LLRLRLLSLRLLSLSSSS"
print(countCollisions(directions))

directions = "SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR"
print(countCollisions(directions))

directions = "SRRLRLRSRLRSSRRLSLRLLRSLSLLSSRRLSRSLSLRRS"
print(countCollisions(directions))

directions = "LSSSLLSSSSLRRSLLLSLSLRRLLLLLRSSRSRRSLLLSSS"
print(countCollisions(directions))


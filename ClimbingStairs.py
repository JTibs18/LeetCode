# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def climbStairs(n):
    possibleSteps = [0, 1, 2]

    for _ in range(n - 2):
        possibleSteps.append(possibleSteps[-1] + possibleSteps[-2])

    return possibleSteps[n]

# Test cases
n = 1 
print(climbStairs(n))

n = 2 
print(climbStairs(n))

n = 3 
print(climbStairs(n))
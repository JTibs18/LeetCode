# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.

def minCostClimbingStairs(cost):
    costAtStep = dict()
    costAtStep[len(cost)] = 0 
    costAtStep[len(cost) - 1] = cost[-1]

    for i in range(len(cost) - 2, -1, -1):
        costAtStep[i] = cost[i] + min(costAtStep[i + 1], costAtStep[i + 2])

    return min(costAtStep[0], costAtStep[1])

# Test cases
cost = [10, 15, 20]
print(minCostClimbingStairs(cost))

cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(minCostClimbingStairs(cost))

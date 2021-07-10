# Today, the bookstore owner has a store open for customers.length minutes.
# Every minute, some number of customers (customers[i]) enter the store, and all those customers leave after the end of that minute.
# On some minutes, the bookstore owner is grumpy.
# If the bookstore owner is grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.
# When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise they are satisfied.
# The bookstore owner knows a secret technique to keep themselves not grumpy for minutes minutes straight, but can only use it once.
# Return the maximum number of customers that can be satisfied throughout the day.

def maxSatisfied(customers, grumpy, minutes):
    maxHappy = 0
    happyCount = 0

    for indx, val in enumerate(grumpy):
        if val == 0:
            happyCount += customers[indx]
    minHappy = happyCount
    happyCount = 0

    for val in range(minutes):
        if grumpy[val] == 1:
            happyCount += customers[val]

    if happyCount + minHappy > maxHappy:
        maxHappy = happyCount + minHappy

    p1 = 0
    p2 = minutes

    while p2 < len(customers):
        if grumpy[p1] == 1:
            happyCount -= customers[p1]
        p1 += 1
        if grumpy[p2] == 1:
            happyCount += customers[p2]
        p2 += 1
        if happyCount + minHappy > maxHappy:
            maxHappy = happyCount + minHappy
    return maxHappy

#Test casses
customers =  [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3
print(maxSatisfied(customers, grumpy, minutes))

customers =  [4, 10, 10]
grumpy = [1, 1, 0]
minutes = 2
print(maxSatisfied(customers, grumpy, minutes))

# Today, the bookstore owner has a store open for customers.length minutes.
# Every minute, some number of customers (customers[i]) enter the store, and all those customers leave after the end of that minute.
# On some minutes, the bookstore owner is grumpy.
# If the bookstore owner is grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.
# When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise they are satisfied.
# The bookstore owner knows a secret technique to keep themselves not grumpy for minutes minutes straight, but can only use it once.
# Return the maximum number of customers that can be satisfied throughout the day.

# Example 1:
# Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
# Output: 16
# Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes.
# The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.


#PROBLEM: TOO SLOW WITH NESTED LOOP

def gBookOwner(customers, grumpy, minutes):
    # wSum = sum(customers)
    happy = 0
    # maxHappy = 0
    addDiff = 0
    for index, value in enumerate(customers):
        # happyMins = 0
        diff = 0
        if (grumpy[index] == 0):
            happy = happy + value
        for i in range(minutes):
            if (index <= len(customers) - minutes):
                if (grumpy[index + i] != 0):
                    diff = diff + customers[index + i]
                # happyMins = happyMins + customers[index + i]
        if (diff > addDiff):
            # maxHappy = happyMins
            addDiff = diff
    happy = happy + addDiff
    return happy


#Test casses
customers =  [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3
print(gBookOwner(customers, grumpy, minutes))

customers =  [4, 10, 10]
grumpy = [1, 1, 0]
minutes = 2
print(gBookOwner(customers, grumpy, minutes))

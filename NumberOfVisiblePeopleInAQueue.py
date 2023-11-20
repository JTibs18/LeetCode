# There are n people standing in a queue, and they numbered from 0 to n - 1 in left to right order. You are given an array heights of distinct integers where heights[i] represents the height of the ith person.
# A person can see another person to their right in the queue if everybody in between is shorter than both of them. More formally, the ith person can see the jth person if i < j and min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1]).
# Return an array answer of length n where answer[i] is the number of people the ith person can see to their right in the queue.

def canSeePersonsCount(heights):
    stack = []
    answer = []

    for i in range(len(heights) - 1, -1, -1):
        canSee = 0 
        
        while len(stack) and stack[-1] < heights[i]:
            stack.pop()
            canSee += 1 

        if len(stack):
            canSee += 1 

        answer.append(canSee)
        stack.append(heights[i])
    
    answer.reverse()
    return answer

# Test cases
heights = [10, 6, 8, 5, 11, 9]
print(canSeePersonsCount(heights))

heights = [5, 1, 2, 3, 10]
print(canSeePersonsCount(heights))

heights = [4, 3, 2, 1]
print(canSeePersonsCount(heights))
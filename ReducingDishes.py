# A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.
# Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level  i.e.  time[i]*satisfaction[i]
# Return the maximum sum of Like-time coefficient that the chef can obtain after dishes preparation.
# Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.

def maxSatisfaction(satisfaction):
    s = sorted(satisfaction, reverse=True)
    timeC = 0

    for indx, dish in enumerate(s):
        if timeC < timeC + int(dish) + sum(s[:indx]):
            timeC = timeC + int(dish) + sum(s[:indx])
        else:
            return timeC

    return timeC
    
#Test cases
satisfaction = [-1,-8,0,5,-9]
print(maxSatisfaction(satisfaction))

satisfaction = [4,3,2]
print(maxSatisfaction(satisfaction))

satisfaction = [-1,-4,-5]
print(maxSatisfaction(satisfaction))

satisfaction = [-2,5,-1,0,3,-3]
print(maxSatisfaction(satisfaction))

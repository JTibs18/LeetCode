# You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.
# The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:
# The 1st place athlete's rank is "Gold Medal".
# The 2nd place athlete's rank is "Silver Medal".
# The 3rd place athlete's rank is "Bronze Medal".
# For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
# Return an array answer of size n where answer[i] is the rank of the ith athlete.

def findRelativeRank(score):
    sortedScore = sorted(score, reverse = True)
    placement = []

    for i in score:
        indx = sortedScore.index(i)
        if indx == 0:
            placement.append("Gold Medal")
        elif indx == 1:
            placement.append("Silver Medal")
        elif indx == 2:
            placement.append("Bronze Medal")
        else:
            placement.append(str(indx + 1))

    return placement

#Test cases
score = [5,4,3,2,1]
print(findRelativeRank(score))

score = [10,3,8,9,4]
print(findRelativeRank(score))

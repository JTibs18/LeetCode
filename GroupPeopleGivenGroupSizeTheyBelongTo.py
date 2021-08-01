# There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.
# You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.
# Return a list of groups such that each person i is in a group of size groupSizes[i].
# Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.

def groupThePeople(groupSizes):
    groups = dict()
    ans = []

    for indx, g in enumerate(groupSizes):
        if g not in groups:
            groups[g] = [indx]
        else:
            groups[g].append(indx)

    for key, val in groups.items():
        while val != []:
            ans.append(val[:key])
            val = val[key:]
    return ans

#Test cases
groupSizes = [3,3,3,3,3,1,3]
print(groupThePeople(groupSizes))

groupSizes = [2,1,3,3,3,2]
print(groupThePeople(groupSizes))

# You are given the logs for users' actions on LeetCode, and an integer k. The logs are represented by a 2D integer array logs where each logs[i] = [IDi, timei] indicates that the user with IDi performed an action at the minute timei.
# Multiple users can perform actions simultaneously, and a single user can perform multiple actions in the same minute.
# The user active minutes (UAM) for a given user is defined as the number of unique minutes in which the user performed an action on LeetCode. A minute can only be counted once, even if multiple actions occur during it.
# You are to calculate a 1-indexed array answer of size k such that, for each j (1 <= j <= k), answer[j] is the number of users whose UAM equals j.
# Return the array answer as described above.

def findingUsersActiveMinutes(logs, k):
    ans = [0] * k
    UAM = dict()

    for l in logs:
        if l[0] not in UAM:
            UAM[l[0]] = [l[1]]
        elif l[1] not in UAM[l[0]]:
            UAM[l[0]].append(l[1])

    for key, val in UAM.items():
        ans[len(val) - 1] += 1

    return ans

#Test cases
logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
k = 5
print(findingUsersActiveMinutes(logs, k))

logs = [[1,1],[2,2],[2,3]]
k = 4
print(findingUsersActiveMinutes(logs, k))

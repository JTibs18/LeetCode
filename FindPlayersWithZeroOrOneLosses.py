# You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.
# Return a list answer of size 2 where:
# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.
# The values in the two lists should be returned in increasing order.
# Note:
# You should only consider the players that have played at least one match.
# The testcases will be generated such that no two matches will have the same outcome.
# Q2 of Weekly Contest 287

def findWinners(matches):
    winCount = dict()
    lossCount = dict()
    gameCount = dict()
    winArray = []
    loseArray = []

    for i in matches:
        if i[0] in winCount:
            winCount[i[0]] += 1
        else:
            winCount[i[0]] = 1

        if i[1] in lossCount:
            lossCount[i[1]] += 1
        else:
            lossCount[i[1]] = 1

        if i[0] in gameCount:
            gameCount[i[0]] += 1
        else:
            gameCount[i[0]] = 1

        if i[1] in gameCount:
            gameCount[i[1]] += 1
        else:
            gameCount[i[1]] = 1

    for key, val in winCount.items():
        if gameCount[key] == winCount[key]:
            winArray.append(key)

    for key, val in lossCount.items():
        if 1 == lossCount[key]:
            loseArray.append(key)

    winArray = sorted(winArray)
    loseArray = sorted(loseArray)

    return [winArray, loseArray]

#Test Cases
matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
print(findWinners(matches))

matches = [[2,3],[1,3],[5,4],[6,4]]
print(findWinners(matches))

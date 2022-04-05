# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
# If the town judge exists, then:
# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.
# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

def findJudge(n, trust):
    trustGraph = dict()
    trustingPeople = set()

    if n == 1 and trust == []:
        return 1

    for i in trust:
        if i[1] in trustGraph:
            trustGraph[i[1]].append(i[0])
        else:
            trustGraph[i[1]] = [i[0]]
        trustingPeople.add(i[0])

    for i in range(1, n + 1):
        if i in trustGraph and len(trustGraph.get(i)) == n - 1 and i not in trustingPeople:
            return i

    return -1

#Test cases
n = 2
trust = [[1,2]]
print(findJudge(n, trust))

n = 3
trust = [[1,3],[2,3]]
print(findJudge(n, trust))

n = 3
trust = [[1,3],[2,3],[3,1]]
print(findJudge(n, trust))

n = 1
trust = []
print(findJudge(n, trust))

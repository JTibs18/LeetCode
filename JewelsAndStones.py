# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

def numJewelsInStones(jewels, stones):
    j = dict()
    count = 0

    for s in stones:
        if s in j:
            j[s] += 1
        else:
            j[s] = 1

    for i in jewels:
        if i in j:
            count += j.get(i)
    return count

#Test cases
jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))

jewels = "z"
stones = "ZZ"
print(numJewelsInStones(jewels, stones)) 

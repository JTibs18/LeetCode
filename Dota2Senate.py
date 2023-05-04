# In the world of Dota2, there are two parties: the Radiant and the Dire.
# The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:
# Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
# Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.
# Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n senators, the size of the given string will be n.
# The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.
# Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".
# Note: memory and speed performance can improve still 

def predictPartyVictory1(senate):
    voteCount = 0 
    queue = list(senate)
    winningChar = senate[0]
    rCount = senate.count("R")
    dCount = senate.count("D")

    while queue and dCount > 0 and rCount > 0: 
        if voteCount == 0: 
            voteCount += 1 
            winningChar = queue[0]
            queue.append(winningChar)
        elif voteCount > 0 and queue[0] == winningChar: 
            voteCount += 1 
            queue.append(winningChar)
        else: 
            voteCount -= 1
            if queue[0] == "R":
                rCount -= 1 
            else:
                dCount -= 1
        
        queue.pop(0)
        
    if winningChar == "D": 
        return "Dire"
    else:
        return "Radiant"

# worse memory and speed than previous example
def predictPartyVictory(senate):
    queue = list(senate)
    rCount = senate.count("R")
    dCount = senate.count("D")

    while queue and dCount > 0 and rCount > 0: 
        curLetter = queue.pop(0)

        if curLetter == "D": 
            queue.remove("R")
            rCount -= 1 
        else: 
            queue.remove("D")
            dCount -= 1 
        
        queue.append(curLetter)
        
    if dCount > 0: 
        return "Dire"
    else:
        return "Radiant"

# Test cases
senate = "RD"
print(predictPartyVictory(senate))

senate = "RDD"
print(predictPartyVictory(senate))

senate = "DDRRR"
print(predictPartyVictory(senate))

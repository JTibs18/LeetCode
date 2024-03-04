# You start with an initial power of power, an initial score of 0, and a bag of tokens given as an integer array tokens, where each tokens[i] donates the value of tokeni.
# Your goal is to maximize the total score by strategically playing these tokens. In one move, you can play an unplayed token in one of the two ways (but not both for the same token):
#   Face-up: If your current power is at least tokens[i], you may play tokeni, losing tokens[i] power and gaining 1 score.
#   Face-down: If your current score is at least 1, you may play tokeni, gaining tokens[i] power and losing 1 score.
# Return the maximum possible score you can achieve after playing any number of tokens.

def bagOfTokenScore(tokens, power):
    score = 0 
    tokens.sort()
    ptr1 = 0
    ptr2 = len(tokens) - 1

    while ptr1 <= ptr2:
        if tokens[ptr1] <= power:
            power -= tokens[ptr1]
            score += 1 
            ptr1 += 1 
        elif score >= 1 and ptr2 - 1 > ptr1:
            power += tokens[ptr2] 
            ptr2 -= 1 
            score -= 1
        else:
            break
    
    return score

# Test cases
tokens = [100]
power = 50
print(bagOfTokenScore(tokens, power))

tokens = [200,100]
power = 150
print(bagOfTokenScore(tokens, power))

tokens = [100,200,300,400]
power = 200
print(bagOfTokenScore(tokens, power))

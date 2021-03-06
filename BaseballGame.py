# You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.
# At the beginning of the game, you start with an empty record. You are given a list of strings ops, where ops[i] is the ith operation you must apply to the record and is one of the following:
# An integer x - Record a new score of x.
# "+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.
# "D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
# "C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.
# Return the sum of all the scores on the record.

def calPoints(ops):
    score = []

    for i in ops:
        if i == "+":
            score.append(score[len(score) - 1] + score[len(score) - 2])
        elif i == "D":
            score.append(score[len(score) - 1] * 2)
        elif i == "C":
            score.pop()
        else:
            score.append(int(i))

    return sum(score)

#Test Cases
ops = ["5","2","C","D","+"]
print(calPoints(ops))

ops = ["5","-2","4","C","D","9","+","+"]
print(calPoints(ops))

ops = ["1"]
print(calPoints(ops))

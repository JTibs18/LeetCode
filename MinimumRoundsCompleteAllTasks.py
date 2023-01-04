# You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task. In each round, you can complete either 2 or 3 tasks of the same difficulty level.
# Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.

def minimumRounds(tasks):
    taskCount = dict()
    rounds = 0 

    for i in tasks: 
        if i in taskCount: 
            taskCount[i] += 1
        else: 
            taskCount[i] = 1

    for value in taskCount.values(): 
        while value > 1: 
            if value >= 3 and value - 3 != 1: 
                rounds += 1
                value = value - 3 
            elif value >= 2: 
                rounds += 1
                value = value - 2
        if value == 1: 
            return -1 
        
    return rounds 

# Test cases
tasks = [2,2,3,3,2,4,4,4,4,4]
print(minimumRounds(tasks))

tasks = [2,3,3]
print(minimumRounds(tasks))

tasks = [5,5,5,5]
print(minimumRounds(tasks))

tasks = [69,65,62,64,70,68,69,67,60,65,69,62,65,65,61,66,68,61,65,63,60,66,68,66,67,65,63,65,70,69,70,62,68,70,60,68,65,61,64,65,63,62,62,62,67,62,62,61,66,69]
print(minimumRounds(tasks))

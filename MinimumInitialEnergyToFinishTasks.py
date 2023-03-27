# You are given an array tasks where tasks[i] = [actuali, minimumi]:
# actuali is the actual amount of energy you spend to finish the ith task.
# minimumi is the minimum amount of energy you require to begin the ith task.
# For example, if the task is [10, 12] and your current energy is 11, you cannot start this task. However, if your current energy is 13, you can complete this task, and your energy will be 3 after finishing it.
# You can finish the tasks in any order you like.
# Return the minimum initial amount of energy you will need to finish all the tasks.

def minimumEffort(tasks): 
    tasks = sorted(tasks, key=lambda i: i[1] - i[0], reverse=True)
    totalEnergy = 0 
    energy = 0 

    for actual, minimum in tasks: 
        diff = minimum - energy 

        if diff > 0: 
            totalEnergy += diff 
            
        energy = max(minimum, energy) - actual 

    return totalEnergy

# Test cases
tasks = [[1,2],[2,4],[4,8]]
print(minimumEffort(tasks))

tasks = [[1,3],[2,4],[10,11],[10,12],[8,9]]
print(minimumEffort(tasks))

tasks = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]
print(minimumEffort(tasks))

tasks = [[1,1],[1,3]]
print(minimumEffort(tasks))

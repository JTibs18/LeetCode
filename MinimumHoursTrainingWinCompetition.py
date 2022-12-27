# You are entering a competition, and are given two positive integers initialEnergy and initialExperience denoting your initial energy and initial experience respectively.
# You are also given two 0-indexed integer arrays energy and experience, both of length n.
# You will face n opponents in order. The energy and experience of the ith opponent is denoted by energy[i] and experience[i] respectively. When you face an opponent, you need to have both strictly greater experience and energy to defeat them and move to the next opponent if available.
# Defeating the ith opponent increases your experience by experience[i], but decreases your energy by energy[i].
# Before starting the competition, you can train for some number of hours. After each hour of training, you can either choose to increase your initial experience by one, or increase your initial energy by one.
# Return the minimum number of training hours required to defeat all n opponents.

def minNumberHours(initialEnergy, initialExperience, energy, experience): 
    trainingHours = 0 

    for indx, val in enumerate(energy): 
        if val >= initialEnergy: 
            trainingHours += (val - initialEnergy) + 1
            initialEnergy += (val - initialEnergy) + 1
        if experience[indx] >= initialExperience: 
            trainingHours += (experience[indx] - initialExperience) + 1
            initialExperience += (experience[indx] - initialExperience) + 1
        initialExperience += experience[indx]
        initialEnergy -= val
    
    return trainingHours

# Test cases 
initialEnergy = 5
initialExperience = 3
energy = [1,4,3,2]
experience = [2,6,3,1]
print(minNumberHours(initialEnergy, initialExperience, energy, experience))

initialEnergy = 2
initialExperience = 4
energy = [1]
experience = [3]
print(minNumberHours(initialEnergy, initialExperience, energy, experience))

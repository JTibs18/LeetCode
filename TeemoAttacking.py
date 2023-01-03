# Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets poisoned for a exactly duration seconds. More formally, an attack at second t will mean Ashe is poisoned during the inclusive time interval [t, t + duration - 1]. If Teemo attacks again before the poison effect ends, the timer for it is reset, and the poison effect will end duration seconds after the new attack.
# You are given a non-decreasing integer array timeSeries, where timeSeries[i] denotes that Teemo attacks Ashe at second timeSeries[i], and an integer duration.
# Return the total number of seconds that Ashe is poisoned.

def findPoisonedDuration(timeSeries, duration): 
    time = 0 

    for indx, val in enumerate(timeSeries): 
        if indx + 1 < len(timeSeries) and (val + duration) - 1 >= timeSeries[indx + 1]: 
            time += timeSeries[indx + 1] - val 
        else: 
            time += duration 
    
    return time

# Test cases 
timeSeries = [1,4]
duration = 2
print(findPoisonedDuration(timeSeries, duration))

timeSeries = [1,2]
duration = 2
print(findPoisonedDuration(timeSeries, duration))

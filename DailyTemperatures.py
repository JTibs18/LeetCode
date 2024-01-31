# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

# naive solution results in TLE
def dailyTemperatures1(temperatures): 
    indx1 = 0
    indx2 = 1 
    days = 0
    answer = []

    while indx1 < len(temperatures) - 1: 
        days += 1
        if temperatures[indx1] < temperatures[indx2]: 
            answer.append(days)
            days = 0
            indx1 += 1 
            indx2 = indx1 + 1 
        elif indx2 + 1 > len(temperatures) - 1: 
            answer.append(0)
            indx1 += 1 
            indx2 = indx1 + 1 
            days = 0
        else: 
            indx2 += 1

    answer.append(0)
    return answer

# monotonic stack solution is much faster and memory efficient 
def dailyTemperatures(temperatures): 
    output = [0 for _ in range(len(temperatures))]
    stack = []

    for indx, val in enumerate(temperatures):
        while stack and stack[-1][0] < val: 
            _, i = stack.pop()
            output[i] = indx - i
        
        stack.append((val, indx))

    return output 

# Test cases 
temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures))

temperatures = [30,40,50,60]
print(dailyTemperatures(temperatures))

temperatures = [30,60,90]
print(dailyTemperatures(temperatures))

# There are n employees in a company, numbered from 0 to n - 1. Each employee i has worked for hours[i] hours in the company.
# The company requires each employee to work for at least target hours.
# You are given a 0-indexed array of non-negative integers hours of length n and a non-negative integer target.
# Return the integer denoting the number of employees who worked at least target hours.

# faster runtime, more memory
def numberOfEmployeesWhoMetTarget(hours, target):
    hours.sort(reverse=True)
    count = 0 

    for i in hours:
        if i >= target:
            count += 1
        else:
            return count 
        
    return count

# slower runtime, less memory 
def numberOfEmployeesWhoMetTarget(hours, target):
    hours.sort(reverse=True)

    for indx in range(len(hours)):
        if hours[indx] < target:
            return indx 
        
    return len(hours)

# Test cases
hours = [0,1,2,3,4]
target = 2
print(numberOfEmployeesWhoMetTarget(hours, target))

hours = [5,1,4,2,2]
target = 6
print(numberOfEmployeesWhoMetTarget(hours, target))

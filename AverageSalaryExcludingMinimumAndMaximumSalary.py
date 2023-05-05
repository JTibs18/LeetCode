# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
# Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

def average(salary): 
    max = 0 
    min = 1000000000000
    total = 0 

    for i in salary: 
        if i < min: 
            min = i 
        if i > max: 
            max = i 
        
        total += i
    
    total -= min + max 
    return total / (len(salary) - 2)

# Test cases
salary = [4000,3000,1000,2000]
print(average(salary))

salary = [1000,2000,3000]
print(average(salary))

# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

def subtractProductAndSum(n):
   s = sum([int(d) for d in str(n)])
   multi = 1

   for d in str(n):
       multi *= int(d)

   return(multi - s)

#Test cases
n = 234
print(subtractProductAndSum(n))

n = 4421
print(subtractProductAndSum(n))

# At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
# Note that you do not have any change in hand at first.
# Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

def lemonadeChange(bills): 
    change = {5: 0, 10: 0, 20: 0} 

    for i in bills: 
        change[i] += 1
        
        if i == 10: 
            if change[5] > 0: 
                change[5] -= 1 
            else: 
                return False 
        elif i == 20: 
            if change[5] > 0 and change[10] > 0: 
                change[5] -= 1 
                change[10] -= 1 
            elif change[5] > 2:
                change[5] -= 3  
            else: 
                return False 

    return True

# Test cases
bills = [5,5,5,10,20]
print(lemonadeChange(bills))

bills = [5,5,10,10,20]
print(lemonadeChange(bills))

bills = [5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]
print(lemonadeChange(bills))

bills = [5,5,5,5,20,20,5,5,20,5]
print(lemonadeChange(bills))

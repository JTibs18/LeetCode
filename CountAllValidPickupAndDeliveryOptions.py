# Given n orders, each order consists of a pickup and a delivery service.
# Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 
# Since the answer may be too large, return it modulo 10^9 + 7.

# theory: 
# Usually when n = 1: you will have 2 spots to fill _ _ and you need to fill P1 and D1. So 1 choice for those 2 spots.
# When n = 2: you will have 4 spots to fill _ _ _ _. Now for the 1st spot, you have 2 choices P1, P2. Then for the next 3 spots, if you chose P1 for the spot then you will have 3 places to chose D1. And for the rest of the 2 spaces you will fill P2 and D2. Here if you observe, After fixing the first spot with P1, you have 3 choices for D1 and 2 spots for P and D "P1 D1 _ _" or P1 _ D1 _" or P1 _ _ D1". This 2 spots for a P and D is similar to n = 1. Two fill those 2 spots you will have same number of chances like n = 1 which is 1 in this case. Hence P1 D1 [P2 D2] or P1 [P2 D2] D1 or P1 [P2] D1 [D2]. That is like 3 * 1 choices when P1 took first spot. Similarly, when P2 take the first spot, it is again 3 * 1 choices. Hence totally there are 2 numbers which can occupy first spot so it is 2*3*1 choices.
# When n = 3, we have 6 spots _ _ _ _ _ _ . Now We have 3 choices for first spot P1 P2 and P3. After choosing the first spot P, Again for its D we have 5 choices and 4 spots left with 2 Ps and 2 Ds which is again n=2 question where we have 2 Ps and 2 Ds for 4 spots. Hence we already know its answer is 6. Hence as we have 5 choices for D and 6 choices each time, we have 5*6 choices for each P at 1st spot. This will end up with 3*5*6 choices for n = 3.

def countOrders(n): 
    if n == 1: 
        return 1

    return n * ((n * 2) - 1) * countOrders(n - 1) % ((10 ** 9) + 7)
    
# Test cases
n = 1
print(countOrders(n))

n = 2
print(countOrders(n))

n = 3
print(countOrders(n))

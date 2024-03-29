# Given an integer array arr of distinct integers and an integer k.
# A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]). In each round of the game, we compare arr[0] with arr[1], the larger integer wins and remains at position 0, and the smaller integer moves to the end of the array. The game ends when an integer wins k consecutive rounds.
# Return the integer which will win the game.
# It is guaranteed that there will be a winner of the game.

# initial attempt with array manipulation, slow but memory efficient 
def getWinner1(arr, k):
    if k > len(arr): 
        return max(arr)
    
    consecutiveCount = 0

    while consecutiveCount != k:
        loser = min(arr[0], arr[1])

        if loser != arr[0]:
            consecutiveCount += 1 
        else: 
            consecutiveCount = 1

        arr.remove(loser)
        arr.append(loser)
        
    return arr[0]

# using pointers and maintaining a winner, fast but requires more memory 
def getWinner(arr, k):
    consecutiveCount = 0 
    winner = arr[0]
    ptr = 1

    while consecutiveCount < k and ptr < len(arr):
        if winner > arr[ptr]:
            consecutiveCount += 1 
        else:
            winner = arr[ptr]
            consecutiveCount = 1 
        
        ptr += 1 

    return winner 

# Test cases
arr = [2, 1, 3, 5, 4, 6, 7]
k = 2
print(getWinner(arr, k))

arr = [3, 2, 1]
k = 10 
print(getWinner(arr, k))

arr = [1, 25, 35, 42, 68, 70]
k = 2
print(getWinner(arr, k))

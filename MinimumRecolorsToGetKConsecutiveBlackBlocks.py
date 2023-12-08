# You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.
# You are also given an integer k, which is the desired number of consecutive black blocks.
# In one operation, you can recolor a white block such that it becomes a black block.
# Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

def minimumRecolors(blocks, k):
    blocks = list(blocks)
    indx = 0 
    whiteCount = len([b for b in blocks[indx:indx + k - 1] if b == "W"])
    minChange = k

    while indx + k <= len(blocks): 
        if blocks[indx + k - 1] == "W":
            whiteCount += 1 

        if whiteCount < minChange: 
            minChange = whiteCount
        
        if blocks[indx] == "W": 
            whiteCount -= 1
        
        indx += 1
    
    return minChange

# Test cases
blocks = "WBBWWBBWBW"
k = 7
print(minimumRecolors(blocks, k))

blocks = "WBWBBBW"
k = 2
print(minimumRecolors(blocks, k))

blocks = "WBB"
k = 1
print(minimumRecolors(blocks, k))

blocks = "BWWWBB"
k = 6
print(minimumRecolors(blocks, k))

blocks = "WWBBBWBBBBBWWBWWWB"
k = 16
print(minimumRecolors(blocks, k))

blocks = "BWWBWBBBWBBBWBBWWWBBBWBWBWBBBWWBWWWBWBBBWBBW"
k = 27
print(minimumRecolors(blocks, k))

blocks = "W"
k = 1
print(minimumRecolors(blocks, k))

# You are given four integers sx, sy, fx, fy, and a non-negative integer t.
# In an infinite 2D grid, you start at the cell (sx, sy). Each second, you must move to any of its adjacent cells.
# Return true if you can reach cell (fx, fy) after exactly t seconds, or false otherwise.
# A cell's adjacent cells are the 8 cells around it that share at least one corner with it. You can visit the same cell several times.

def isReachableAtTime(sx, sy, fx, fy, t):
    if max(abs(fy - sy), abs(fx - sx)) <= t and not ((t == 1) and (sy == fy) and (sx == fx)): 
        return True 
    return False 

# Test cases
sx = 2 
sy = 4
fx = 7
fy = 7 
t = 6
print(isReachableAtTime(sx, sy, fx, fy, t))

sx = 3
sy = 1
fx = 7
fy = 3
t = 3
print(isReachableAtTime(sx, sy, fx, fy, t))

sx = 1
sy = 1
fx = 2
fy = 2
t = 1 
print(isReachableAtTime(sx, sy, fx, fy, t))

sx = 1
sy = 2
fx = 1
fy = 2 
t = 1 
print(isReachableAtTime(sx, sy, fx, fy, t))

sx = 5
sy = 1 
fx = 1 
fy = 4 
t = 4
print(isReachableAtTime(sx, sy, fx, fy, t))

sx = 1
sy = 4
fx = 1 
fy = 2
t = 1
print(isReachableAtTime(sx, sy, fx, fy, t))

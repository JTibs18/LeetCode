# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively.
# You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
# Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

#Example 1:
# Input: path = "NES"
# Output: false
# Explanation: Notice that the path doesn't cross any point more than once.

#Example 2:
# Input: path = "NESWW"
# Output: true
# Explanation: Notice that the path visits the origin twice.

def pathCrossing(path):
    location = [0, 0]
    travelled = set()
    travelled.add(tuple(location))
    for index, value in enumerate(path):
        if (value == "N"):
            location[1] += 1
        elif (value == "S"):
            location[1] -= 1
        elif (value == "E"):
            location[0] += 1
        elif (value == "W"):
            location[0] -= 1
        if (tuple(location) in travelled):
            return True
        else:
            travelled.add(tuple(location))
    return False

#test cases
path = "NES"
print(pathCrossing(path))

path = "NESWW"
print(pathCrossing(path))

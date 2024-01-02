# There are n 1-indexed robots, each having a position on a line, health, and movement direction.
# You are given 0-indexed integer arrays positions, healths, and a string directions (directions[i] is either 'L' for left or 'R' for right). All integers in positions are unique.
# All robots start moving on the line simultaneously at the same speed in their given directions. If two robots ever share the same position while moving, they will collide.
# If two robots collide, the robot with lower health is removed from the line, and the health of the other robot decreases by one. The surviving robot continues in the same direction it was going. If both robots have the same health, they are both removed from the line.
# Your task is to determine the health of the robots that survive the collisions, in the same order that the robots were given, i.e. final heath of robot 1 (if survived), final health of robot 2 (if survived), and so on. If there are no survivors, return an empty array.
# Return an array containing the health of the remaining robots (in the order they were given in the input), after no further collisions can occur.
# Note: The positions may be unsorted.

def survivedRobotsHealths(positions, healths, directions):
    robots = []
    updatedRobots = []
    stack = []

    for i in range(len(positions)):
        robots.append({"position": positions[i], "health": healths[i], "direction": directions[i], "index": i})
    
    sortedRobots = sorted(robots, key=lambda x:x["position"])

    for robot in sortedRobots:
        if robot["direction"] == "L" and len(stack) > 0:
            while len(stack) > 0 and stack[-1]["health"] < robot["health"]:
                stack.pop()
                robot["health"] -= 1

            if len(stack) > 0 and stack[-1]['health'] > robot['health']:
                stack[-1]['health'] -= 1 
            elif len(stack) > 0 and stack[-1]['health'] == robot['health']:
                stack.pop()
            else:
                updatedRobots.append(robot)
        elif robot["direction"] == "R":
            stack.append(robot)
        else:
            updatedRobots.append(robot)

    for i in stack:
        updatedRobots.append(i)

    return [x['health'] for x in sorted(updatedRobots, key=lambda x:x["index"])]

# Test cases
positions = [5,4,3,2,1]
healths = [2,17,9,15,10]
directions = "RRRRR"
print(survivedRobotsHealths(positions, healths, directions))

positions = [3,5,2,6]
healths = [10,10,15,12]
directions = "RLRL"
print(survivedRobotsHealths(positions, healths, directions))

positions = [1,2,5,6]
healths = [10,10,11,11]
directions = "RLRL"
print(survivedRobotsHealths(positions, healths, directions))

positions = [1, 40]
healths = [10, 11]
directions = "RL"
print(survivedRobotsHealths(positions, healths, directions))

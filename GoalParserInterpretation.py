# You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.
# Given the string command, return the Goal Parser's interpretation of command.

def interpret(command):
    pretation = ""

    for indx, val in enumerate(command):
        if val == "G":
            pretation += "G"
        elif val == "(" and command[indx + 1] == ")":
            pretation += "o"
        elif val == "(" and command[indx + 1] == "a":
            pretation += "al"

    return pretation

#Test cases
command = "G()(al)"
print(interpret(command))

command = "G()()()()(al)"
print(interpret(command))

command = "(al)G(al)()()G"
print(interpret(command))

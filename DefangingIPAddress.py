# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".

def defangIPaddr(address):
    newString = ""
    for index, value in enumerate(address):
        if value == ".":
            newString = newString + "[.]"
        else:
            newString = newString + value
    return newString

address = "1.1.1.1"
print(defangIPaddr(address))

# You are given the strings key and message, which represent a cipher key and a secret message, respectively. The steps to decode message are as follows:
# Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
# Align the substitution table with the regular English alphabet.
# Each letter in message is then substituted using the table.
# Spaces ' ' are transformed to themselves.
# For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet), we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
# Return the decoded message.

def decodeMessage(key, message):
    mapping = dict()
    alphabetNum = 97
    decode = ""

    for i in key: 
        if i != " " and i not in mapping: 
            mapping[i] = alphabetNum
            alphabetNum += 1 

    for i in message:
        if i == " ": 
            decode += i 
        else: 
            decode += chr(mapping[i])
    
    return decode

# Test cases 
key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
print(decodeMessage(key, message))

key = "eljuxhpwnyrdgtqkviszcfmabo"
message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
print(decodeMessage(key, message))

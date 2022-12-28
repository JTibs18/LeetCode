# You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.
# The ith item is said to match the rule if one of the following is true:
# ruleKey == "type" and ruleValue == typei.
# ruleKey == "color" and ruleValue == colori.
# ruleKey == "name" and ruleValue == namei.
# Return the number of items that match the given rule.

def countMatches(items, ruleKey, ruleValue): 
    matches = 0 

    if ruleKey == "type":
        indx = 0
    elif ruleKey == "color": 
        indx = 1
    else: 
        indx = 2 
    
    for i in items: 
        if i[indx] == ruleValue: 
            matches += 1
    
    return matches

# Test cases 
items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"
print(countMatches(items, ruleKey, ruleValue))

items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"
print(countMatches(items, ruleKey, ruleValue))


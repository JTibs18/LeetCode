# LeetCode company workers use key-cards to unlock office doors. Each time a worker uses their key-card, the security system saves the worker's name and the time when it was used. The system emits an alert if any worker uses the key-card three or more times in a one-hour period.
# You are given a list of strings keyName and keyTime where [keyName[i], keyTime[i]] corresponds to a person's name and the time when their key-card was used in a single day.
# Access times are given in the 24-hour time format "HH:MM", such as "23:51" and "09:49".
# Return a list of unique worker names who received an alert for frequent keycard use. Sort the names in ascending order alphabetically.
# Notice that "10:00" - "11:00" is considered to be within a one-hour period, while "22:51" - "23:52" is not considered to be within a one-hour period.

def alertNames(keyName, keyTime):
    keyUsagePerPerson = dict()
    allAlertNames = []

    for i in range(len(keyName)):
        time = keyTime[i].split(":")
        
        if keyName[i] in keyUsagePerPerson:
            keyUsagePerPerson[keyName[i]].append((int(time[0]), int(time[1])))
        else:
            keyUsagePerPerson[keyName[i]] = [(int(time[0]), int(time[1]))]

    for key, value in keyUsagePerPerson.items():
        if len(value) < 3:
            continue
        
        value = sorted(value)
        ptr = 0

        while ptr + 2 < len(value):
            if ((value[ptr + 2][0] - value[ptr][0]) * 60) + (value[ptr + 2][1] - value[ptr][1]) <= 60:
                allAlertNames.append(key)
                break
            else:
                ptr += 1

    return sorted(allAlertNames)

# Test cases
keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"]
keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
print(alertNames(keyName, keyTime))

keyName = ["alice","alice","alice","bob","bob","bob","bob"]
keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]
print(alertNames(keyName, keyTime))

keyName = ["a","a","a","a","a","a","b","b","b","b","b"]
keyTime = ["23:27","03:14","12:57","13:35","13:18","21:58","22:39","10:49","19:37","14:14","10:41"]
print(alertNames(keyName, keyTime))

# A transaction is possibly invalid if:
# the amount exceeds $1000, or;
# if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
# You are given an array of strings transaction where transactions[i] consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.
# Return a list of transactions that are possibly invalid. You may return the answer in any order.

def invalidTranaction(transactions):
    names = []
    time = []
    amount = []
    city = []
    invalid = []

    for t in transactions:
        details = t.split(",")
        names.append(details[0])
        time.append(details[1])
        amount.append(details[2])
        city.append(details[3])

    for indx, t in enumerate(transactions):
        try:
            indices = [i for i, x in enumerate(names) if x == names[indx]]
            for i in indices:
                if (city[i] != city[indx] and abs(int(time[i]) - int(time[indx])) <= 60):
                    invalid.append(t)
                    break
                elif (int(amount[indx]) > 1000):
                    invalid.append(t)
                    break
        except ValueError:
            if int(amount[indx]) > 1000:
                invalid.append(t)

    return invalid

#Test cases
transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
print(invalidTranaction(transactions))

transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
print(invalidTranaction(transactions))

transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
print(invalidTranaction(transactions))

transactions = ["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"]
print(invalidTranaction(transactions))

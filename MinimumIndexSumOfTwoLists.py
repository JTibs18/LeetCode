# Given two arrays of strings list1 and list2, find the common strings with the least index sum.
# A common string is a string that appeared in both list1 and list2.
# A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.
# Return all the common strings with the least index sum. Return the answer in any order.

def findRestaurant(list1, list2):
    names = dict()

    for indx, val in enumerate(list1):
        if val in list2:
            names[val] = indx + list2.index(val)

    return [key for key, val in names.items() if val == min(names.values())]  

# Test cases
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
print(findRestaurant(list1, list2))

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]
print(findRestaurant(list1, list2))

list1 = ["happy","sad","good"]
list2 = ["sad","happy","good"]
print(findRestaurant(list1, list2))

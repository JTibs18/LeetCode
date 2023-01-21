# You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.
# To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.
# If k > 0, replace the ith number with the sum of the next k numbers.
# If k < 0, replace the ith number with the sum of the previous k numbers.
# If k == 0, replace the ith number with 0.
# As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].
# Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

def decrypt(code, k): 
    newArray = []
    
    if k > 0: 
        count = sum(code[1:k+1]) 
        newArray.append(count)

        for i in code[1:]: 
            count -= i 
            k += 1 
            if k == len(code): 
                k = 0 
            count += code[k]
            newArray.append(count)
    elif k < 0: 
        k = abs(k)
        count = sum(code[len(code) - k:len(code)]) 
        newArray.append(count)
        
        for indx, val in enumerate(code): 
            if indx == len(code) - 1: 
                break 
            count += val 
            count -= code[len(code) - k]
            k -= 1 
            if k == 0: 
                k = len(code)
            newArray.append(count)
    else: 
        newArray = [0] * len(code)
     
    return newArray

# Test cases
code = [5,7,1,4]
k = 3
print(decrypt(code, k))

code = [1,2,3,4]
k = 0
print(decrypt(code, k))

code = [2,4,9,3]
k = -2
print(decrypt(code, k))

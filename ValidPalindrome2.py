# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

def validPalidrome(s):
    delete = False

    def helperFun(s, delete):
        ptr1 = 0
        ptr2 = len(s) - 1

        while ptr1 <= ptr2:
            if s[ptr1] != s[ptr2] and delete == False:
                delete = True

                if s[ptr1 + 1] == s[ptr2] and s[ptr1] == s[ptr2 - 1]:
                    return helperFun(s[ptr1 + 1: ptr2 + 1], delete) or helperFun(s[ptr1: ptr2], delete)

                elif s[ptr1 + 1] == s[ptr2]:
                    ptr1 += 1
                else:
                    ptr2 -= 1
            elif s[ptr1] == s[ptr2]:
                ptr1 += 1
                ptr2 -= 1
            else:
                return False

        return True

    return helperFun(s, delete)

#Test Cases
s = "aba"
print(validPalidrome(s))

s = "abca"
print(validPalidrome(s))

s = "abc"
print(validPalidrome(s))

s = "cbbcc"
print(validPalidrome(s))

s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
print(validPalidrome(s))

s = "yd"
print(validPalidrome(s))

s = "aydmda"
print(validPalidrome(s))

s = "acxcybycxcxa"
print(validPalidrome(s))

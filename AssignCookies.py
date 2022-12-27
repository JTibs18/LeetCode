# Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.
# Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

def findContentChildren(g, s): 
    happyChildren = 0 
    g = sorted(g, reverse=True)
    s = sorted(s, reverse=True)

    for i in g: 
        for cookie in s: 
            if i <= cookie: 
                happyChildren += 1 
                s.remove(cookie)
                break
            
    return happyChildren

# Test cases 
g = [1,2,3]
s = [1,1]
print(findContentChildren(g, s))

g = [1,2]
s = [1,2,3]
print(findContentChildren(g, s))

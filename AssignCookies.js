// Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.
// Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

// First Attempt: less memory but slow runtime 
function findContentChildren1(g, s){
    g.sort(function(a, b) {return a - b}).reverse()
    s.sort(function(a, b) {return a - b}).reverse()
    previousCookieIndx = 0
    cookieIndx = 0 
    count = 0

    for (i of g){
        while (s[cookieIndx] < i && cookieIndx < s.length){
            cookieIndx += 1
        }

        if (s[cookieIndx] >= i){
            cookieIndx += 1
            previousCookieIndx = cookieIndx
            count += 1
        }else{
            cookieIndx = previousCookieIndx
        }
    }

    return count
};

// Second Attempt: worse memory usage and still slow runtime  
function findContentChildren(g, s){
    g.sort(function(a, b) {return a - b}).reverse()
    s.sort(function(a, b) {return a - b}).reverse()
    happyChildren = 0

    for (greed of g){
        for (cookieIndx = 0; cookieIndx < s.length; cookieIndx++){
            if (greed <= s[cookieIndx]){
                happyChildren += 1
                s.splice(cookieIndx, 1)
                break
            }
        }
    }

    return happyChildren
};

// Test cases
g = [1, 2, 3]
s = [1, 1]
console.log(findContentChildren(g, s))

g = [1, 2]
s = [1, 2, 3]
console.log(findContentChildren(g, s))

g = [10,9,8,7,10,9,8,7]
s = [10,9,8,7]
console.log(findContentChildren(g, s))

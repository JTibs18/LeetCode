# website domain "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com" and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.
# A count-paired domain is a domain that has one of the two formats "rep d1.d2.d3" or "rep d1.d2" where rep is the number of visits to the domain and d1.d2.d3 is the domain itself.
# For example, "9001 discuss.leetcode.com" is a count-paired domain that indicates that discuss.leetcode.com was visited 9001 times.
# Given an array of count-paired domains cpdomains, return an array of the count-paired domains of each subdomain in the input. You may return the answer in any order.

def subdomainVisits(cpdomains):
    subCount = dict()
    ans = []

    for domain in cpdomains:
        d = domain.split()
        subs = d[1].split(".")
        prev = ""

        for s in reversed(subs):
            if prev != "":
                prev = s + "." + prev
            else:
                prev = s
            if prev not in subCount:
                subCount[prev] = int(d[0])
            else:
                subCount[prev] += int(d[0])

    for key, val in subCount.items():
        ans.append(str(val) + " " + key)

    return ans

#Test cases
cpdomains = ["9001 discuss.leetcode.com"]
print(subdomainVisits(cpdomains))

cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print(subdomainVisits(cpdomains))

# Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.
# The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

def shortestDistance(s, c):
    distance = []
    prev = -1000

    for indx, char in enumerate(s):
        
        d = s[indx:].find(c)
        if d == 0:
            prev = indx
            distance.append(d)
        elif indx - prev < d or d < 0:
            distance.append(indx - prev)
        else:
            distance.append(d)
    return distance

#Test cases
s = "loveleetcode"
c = "e"
print(shortestDistance(s, c))

s = "aaab"
c = "b"
print(shortestDistance(s, c))

s = "aaba"
c = "b"
print(shortestDistance(s, c))

s = "abhshmmilugfpqugcxkixyiyylahuimjcspqdlpstsfifvkzlveheymjyxbribtwyhpjhnwizwaqvnckjpdjdchcnletbxldtrskqzjmofisxhiodwepxpmcfxjblemjqpegrenbcdlnqdqqpsyhmsounqmseumlivyuwsajzrmjtpfmmsrxpggvwrgtevnhtbxzednufjcbgoowsnolofgldwpfrrmwuvypeifwjtodvnazttujrhkecfnoxmedpbkazplarkduzebuxaucmvkjqerdldelpxsojxqfgnwbvbutkqgsoozdixtgdqqioslpbpqguagmfnvzyfkinlrhiqtenocpsyenusifkplmnqvliespunolnfpbftvtleifzbpqzckbjzhrwokrjiqipnzynyrsntyeklneqkrtizominzxvafokwsknnidelmguolvrtoibxgpcnqzovahxakqykdfzllzdqciskyiaqmkowxzwbwgnizqixaqypjbbpdxztgpyddcrtemwcbkvxqymwpukdgzfwrmbqtsjmxzzjuarnwtuczqbfufocyyewlaajkptwdoxpudbviihqftzwiplmetdnawzllwpmjafnhhgzqmtwbcbqbekbwkpdawhdhncedzvescmqnctvsofmontvbajywmawynyzucwiufqziiurzpmydwptrdliolrcbjnsoustvswwhbzyogoialbvayefdfwvhhgwwlckumrzrjcxuxzqxcifyirynybrwgzyqisarlnflfzyuxmepwneyunyjremkzgblsfsrtmomdydeshldqxmwikjtfnupbcwhfcipzvuciehpelkmtnuttectqzeaeswritrfrrchkuqswcgsuoshkxvthzjjcxfgtcezgxblhkdgubhempnaoossyypewihccbzbkdjjxbqvnzqycdlwmrjjfykuitkzfhchuambdagictmjatwnttpce"
c = "o"
print(shortestDistance(s, c))

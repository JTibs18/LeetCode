# A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.
# Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.
#   For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
# There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.
# Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.
# Note that the starting point is assumed to be valid, so it might not be included in the bank.

def minMutation(startGene, endGene, bank):
    possibleGenes = ["A", "C", "G", "T"]
    q = [(list(startGene), 0)]
    traversed = []
    bank = [list(x) for x in bank]

    while q:
        curGene, curCount = q.pop(0)
        traversed.append(curGene)

        if curGene == list(endGene):
            return curCount

        for i in range(len(curGene)):
            for g in possibleGenes:
                newGene = curGene[:]
                newGene[i] = g 
                if newGene in bank and newGene not in traversed:
                    q.append((newGene, curCount + 1))

    return -1

# Test cases
startGene = "AACCGGTT"
endGene = "AACCGGTA"
bank = ["AACCGGTA"]
print(minMutation(startGene, endGene, bank))

startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
print(minMutation(startGene, endGene, bank))

startGene = "AACCTTGG"
endGene = "AATTCCGG"
bank = ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]
print(minMutation(startGene, endGene, bank))

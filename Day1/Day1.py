import time

input = open("input.txt", "r", encoding="utf-8").read()

freqStrings = input.splitlines()

freqs = [int(s) for s in freqStrings]

##Part 1:
## Solution to first subquestion, that returns array for the sake of dynamic programming in part 2:
def sumOfFrequencies(freqs):
    s = 0
    res = [0]
    for freq in freqs:
        s += freq
        res.append(s)
    return res

print(sumOfFrequencies(freqs)[-1])

## Part 2:
## Solution to second subquestion that is quadratic in input length,
## and uses dynamic programming in calculating sums of subsequences.
## Algorithm correctness: Finding the subsequence of which the numeric sum is lowest among
## subsequences where the sum wholly divides the sum of the entire input of frequency changes.
## When summing the inputs (applying frequence changes), the first reoccuring value
## will be present in the very first "round", at the index where
##  the above mentioned sum starts or ends (depending on sign; see line 51-53).

def firstCycle2(freqs):

    sumArr = sumOfFrequencies(freqs)
    sum = sumArr[-1]
    candidateIndices = (0,0)
    candidateSum = 0
    for i in range(0,len(freqs)):
        for j in range(i+1,len(freqs)):
            s = sumArr[j]-sumArr[i]
            if sum==0 or s%sum == 0:
                if candidateSum == 0 or abs(s)<abs(candidateSum):
                    candidateIndices = (i,j-1)
                    candidateSum = s
    if sum*candidateSum > 0:
        return sumArr[candidateIndices[1]+1]
    return sumArr[candidateIndices[0]+1]


#Printing solution
print("exercise solution:")
start = time.time()
print(firstCycle2(freqs))
print("{} seconds".format(time.time() - start))

## Solution to second subquestion. First simple algorithm.
#  Algorithm is linear in cycle length, and performs better than the above on our input.
#  Uses Set for expected O(1), i.e. constant, time insertion and search (membership check).

def firstCycle1(freqs, seen, current):
    seen.add(current)
    for freq in freqs:
        current += freq
        if current in seen:
            return current
        seen.add(current)
    return firstCycle1(freqs, seen, current)

#Pringting solution using naive algorithm
print("Using naive algorithm")
start = time.time()
print(firstCycle1(freqs,set(),0))
print("{} seconds".format(time.time() - start))


## Test cases:

# Tests:
# t1 = [+1,-1] #0
# t2 = [+3,+3,+4,-2,-4] # first reaches 10 twice.
# t3 = [-6, +3, +8, +5, -6] # first reaches 5 twice.
# t4 = [+7, +7, -2, -7, -4] # first reaches 14 twice.
# t5 = [+1,-2,+3,+1] #2
# t6 = [+7, +3, +1, -13] # first reaches 11

# print("t1 (should be 0) : " + str(firstCycle2(t1)))
# print("t2 (should be 10) : " + str(firstCycle2(t2)))
# print("t3 (should be 5) : " + str(firstCycle2(t3)))
# print("t4 (should be 14) : " + str(firstCycle2(t4)))
# print("t5 (should be 2) : " + str(firstCycle2(t5)))

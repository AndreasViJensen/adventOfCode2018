import time
input = open("input.txt", "r", encoding="utf-8").read()

freqStrings = input.splitlines()

freqs = [int(s) for s in freqStrings]

#Tests:
t1 = [+1,-1] #0
t2 = [+3,+3,+4,-2,-4] # first reaches 10 twice.
t3 = [-6, +3, +8, +5, -6] # first reaches 5 twice.
t4 = [+7, +7, -2, -7, -4] # first reaches 14 twice.
t5 = [+1,-2,+3,+1] #2
t6 = [+7, +3, +1, -13] # first reaches 11

def sumOfFrequencies(freqs):
    s = 0
    res = [0]
    for freq in freqs:
        s += freq
        res.append(s)
    return res

print(sumOfFrequencies(freqs)[-1])


#First cycle optimized:
def firstCycle2(freqs):

    sum = sumOfFrequencies(freqs)
    candidateIndices = (0,0)
    candidateSum = 0
    for i in range(0,len(freqs)):
        for j in range(i+1,len(freqs)):
            s = sumOfFrequencies(freqs[i:j])
            if sum==0 or s%sum == 0:
                if candidateSum == 0 or abs(s)<abs(candidateSum):
                    candidateIndices = (i,j-1)
                    candidateSum = s
    if sum*candidateSum > 0:
        return sumOfFrequencies(freqs[:candidateIndices[1]+1])
    return  sumOfFrequencies(freqs[:candidateIndices[0]+1])

#Printing solution
print("exercise solution:")

start = time.time()
print(firstCycle2(freqs))
print("{} seconds".format(time.time() - start))

#Tests
print("t1 (should be 0) : " + str(firstCycle2(t1)))
print("t2 (should be 10) : " + str(firstCycle2(t2)))
print("t3 (should be 5) : " + str(firstCycle2(t3)))
print("t4 (should be 14) : " + str(firstCycle2(t4)))
print("t5 (should be 2) : " + str(firstCycle2(t5)))


#First cycle naive:
def firstCycle(freqs, seen):
    current = seen[-1]
    for freq in freqs:
        current += int(freq)
        if current in seen:
            print(seen)
            return current
        seen.append(current)
    return firstCycle(freqs, seen)

#Solution using naive algorithm
print("Using naive algorithm")
start = time.time()
print(firstCycle(freqs,[0]))
print("{} seconds".format(time.time() - start))

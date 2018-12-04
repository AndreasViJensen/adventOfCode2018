import re

# Method: Filling a dict of minutes slept using stateful runthrough:
def findGuardWithMostSleep(events):

    guards = dict()
    currentGuard = 0
    asleep = False
    fallAsleepTime = None
    guardID_re = re.compile("#[0-9]+")

    for event in events:
        match = guardID_re.search(event)

        if match: #Shift start event
            currentGuard = int(match.group()[1:])

        elif not asleep: #Fall asleep event
            fallAsleepTime = int(event[15:17])
            asleep = True

        else: #Wake up event
            wakeTime = int(event[15:17])
            if currentGuard in guards:
                guards[currentGuard] += (wakeTime-fallAsleepTime)
            else:
                guards.update({currentGuard: wakeTime-fallAsleepTime})
            asleep = False
    return max(guards, key=lambda x: guards.get(x))


# Method: Extract all events relating to a guard, using stateful runthrough

def extract_guard_events(guardID, events):
    thisGuard = False
    res = []
    for event in events:
        if "#"+str(guardID) in event:
            thisGuard = True
        elif "#" in event:
            thisGuard = False
        elif thisGuard:
            res.append(event)
    return res

    # make 60-entry array of 0's
    # iterate through all the sleep/wake events of guard
    #   and add/subtract 1 at the minute-position of the event under consid.
    #  return max position in sum-array
def findMostSleepyMinute(guardID, guardEvents):
    minutes = []
    for i in range(0,60):
        minutes.append(0)
    for event in guardEvents:
        if "falls asleep" in event:
            minutes[int(event[15:17])] += 1
        if "wakes up" in event:
            minutes[int(event[15:17])] += -1
    current = 0
    max = 0
    maxIndex = 0
    for i in range(0, 60):
        current += minutes[i]
        if current > max:
            max = current
            maxIndex = i
    return (maxIndex, max)

#Part 1: Solution:
print("part 1:")
input = open("input.txt", "r", encoding="utf-8").read()
unsortedEvents = input.splitlines()
events = sorted(unsortedEvents)
maxGuard = findGuardWithMostSleep(events)
print("max guard is #" + str(maxGuard))
guardEvents = extract_guard_events(maxGuard, events)
mostSleepyMinute = findMostSleepyMinute(maxGuard,guardEvents)[0]
print("his most sleepy minute is " + str(mostSleepyMinute))
print("answer is " + str(maxGuard*mostSleepyMinute))



##PART 2:

# Method: Assign each event to corresponding guard in a dictionnary. Uses stateful runthrough.
def makeGuardEventDict(events):
    guardEventDict = dict()
    currentGuard = 0
    currentEventList = []
    guardID_re = re.compile("#[0-9]+")
    for event in events:
        match = guardID_re.search(event)
        if match:
            if currentGuard in guardEventDict:
                guardEventDict[currentGuard].extend(currentEventList)
            else:
                guardEventDict.update({currentGuard:currentEventList})
            currentEventList = []
            currentGuard = int(match.group()[1:])
        else:
            currentEventList.append(event)

    if currentGuard in guardEventDict:
        guardEventDict[currentGuard].extend(currentEventList)
    else:
        guardEventDict.update({currentGuard: currentEventList})

    return guardEventDict

def findGuardByStrategy2(events):
    maxGuard = 0
    maxFreq = 0
    maxMinute = 0

    guardEventDict = makeGuardEventDict(events)

    for guard in guardEventDict:
        res = findMostSleepyMinute(guard,guardEventDict[guard])
        if res[1]>maxFreq:
            maxFreq = res[1]
            maxGuard = guard
            maxMinute = res[0]
    return (maxGuard,maxMinute)


#Part 2 Solution:
print("Part 2:")
input = open("input.txt", "r", encoding="utf-8").read()
unsortedEvents = input.splitlines()
events = sorted(unsortedEvents)

(resGuard,resMinute) = findGuardByStrategy2(events)

print("max guard is #" + str(resGuard))
print("His most sleepy minute is " + str(resMinute))
print("answer is " + str(resGuard*resMinute))

states = int(input("How many states are there?"))

i = 1

statesarray = []
mainarray = []
sidearray = []

while i < states + 1:
    statesarray.append(i)
    i += 1

h = 0
f = 0

while h < len(statesarray):
    while f < len(statesarray):
        probability = input("Probability of transitioning from" + str(statesarray[h]) + "to" + str(statesarray[f]))
        sidearray.append(probability)
        if len(sidearray) == len(statesarray):
            mainarray.append(sidearray)
            sidearray.clear()
    f += 1
h += 1

# categorized such that probability of state 1 transitioning to stage 4 is mainarray[0][3]
# probability of transitioning from state m to state n is mainarray[m-1][n-1]

result = 1

# we want to calculate the probability of n state transitions

transitions = int(input("Enter the number of transitions involved:"))

i = 0

while i < transitions:
    firststate = int(input("Enter the state you're transitioning from:"))
    secondstate = int(input("Enter the state you're transitioning to:"))
    result *= mainarray[firststate - 1][secondstate - 1]
i += 1

print(result)

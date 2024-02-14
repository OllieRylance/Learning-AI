import random

def f(inputS):
    if inputS > 0:
       return 1 
    elif inputS < 0:
        return -1
    return 0

E = [ # Training Set
    [1,1,4],-1,
    [1,2,9],1,
    [1,5,6],1,
    [1,4,5],1,
    [1,6,0.7],-1,
    [1,1,1.5],-1,
]

ro = 0.01

def randint ():
    number = random.uniform(-1, 1)
    return number

W = [randint(), randint(), randint()]

ecrons = 0
while ecrons < 500:
    ecrons += 1
    for i in range(int(len(E)/2)):
        currentPredictors = E[2*i]
        currentPredictand = E[2*i + 1]
        S = currentPredictors[0] * W[0] + currentPredictors[1] * W[1] + currentPredictors[2] * W[2]
        W[0] += ro * (currentPredictand - S) * currentPredictors[0]
        W[1] += ro * (currentPredictand - S) * currentPredictors[1]
        W[2] += ro * (currentPredictand - S) * currentPredictors[2]

print(W)
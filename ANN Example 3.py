def f(inputS):
    if inputS > 0:
       return 1 
    elif inputS < 0:
        return -1
    return 0

E = [ # Training Set
    [1,1.7,1,4],-1,
    [1,5.5,2,9],1,
    [1,2.2,5,6],1,
    [1,1.3,4,5],1,
    [1,1.4,6,0.7],-1,
    [1,4.2,1,1.5],-1,
]

W = [0,0,0,0]

allCorrect = False
while allCorrect == False:
    allCorrect = True
    for i in range(int(len(E)/2)):
        currentPredictors = E[2*i]
        currentPredictand = E[2*i + 1]
        S = currentPredictors[0] * W[0] + currentPredictors[1] * W[1] + currentPredictors[2] * W[2] + currentPredictors[3] * W[3]
        if f(S) != currentPredictand:
            allCorrect = False
            W[0] += currentPredictand * currentPredictors[0]
            W[1] += currentPredictand * currentPredictors[1]
            W[2] += currentPredictand * currentPredictors[2]
            W[3] += currentPredictand * currentPredictors[3]
print(W)
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

W = [0,0,0]

allCorrect = False
x = 0
while allCorrect == False and x < 1000:
   x += 1
   allCorrect = True
   for i in range(int(len(E)/2)):
       currentPredictors = E[2*i]
       currentPredictand = E[2*i + 1]
       S = currentPredictors[0] * W[0] + currentPredictors[1] * W[1] + currentPredictors[2] * W[2]
       if f(S) != currentPredictand:
           allCorrect = False
       W[0] += currentPredictand * currentPredictors[0]
       W[1] += currentPredictand * currentPredictors[1]
       W[2] += currentPredictand * currentPredictors[2]
print(W)

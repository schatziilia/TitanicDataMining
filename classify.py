from numpy import *
from normalization import normalization
from kNN import kNN

def classify(trainSet, trainLabels, testSet):
    trainSet = normalization(trainSet)
    testSet = normalization(testSet)    
   
    #k  sqrt(testSet.shape[0]).astype(int)
    k=4
   # print k
    predictedLabels = zeros(testSet.shape[0])

    for i in range(testSet.shape[0]):
       # print Current Test Instance  str(i1)
        predictedLabels[i] = kNN(k, trainSet, trainLabels, testSet[i,:])
        
    return predictedLabels
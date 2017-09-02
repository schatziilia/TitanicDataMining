from numpy import *
import operator
import collections
from euclideanDistance import euclideanDistance

def kNN(k, X, labels, y):
    # Assigns to the test instance the label of the majority of the labels of the k closest 
	# training examples using the kNN with euclidean distance.

   
    
    m = X.shape[0] # number of training examples
    n = X.shape[1] # number of attributes

    closest = zeros((k,2)) # stores the k closest to the test instance training examples
 
            
 
#Calculate the distance betweet y and each row of X  
    distances = []
    
    for i in range(m):
        
        distance = euclideanDistance(y, X[i,:])
        
        distances.append(distance)
        
       
    
    
    sortedDistances, sortedLabels = zip(*sorted(zip(distances, labels),key=operator.itemgetter(0), reverse=False))
   
 #find the k closest observations   
    
    neighbors = []
    
    for i in range(k):
        
        neighbors.append(sortedDistances[i])
        
   
  
#give y the class of the majority of them.  
    classVotes = {}
    for j in range(k):
        response = sortedLabels[j]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
            
    sortedVotes = collections.OrderedDict(sorted(classVotes.items()))
    keys = sortedVotes.keys()
    values = sortedVotes.values()
    
    label = keys[values.index(max(values))]
   # print label
     
    
    
	
	
    # =============================================================

    
    return label

 

from numpy import *

def normalization(X) :
    #0,7,9,10
    X = delete(X,10,1)
    X = delete(X,9,1)
    X  delete(X,8,1)
    X = delete(X,7,1)
    X = delete(X,0,1)
   
    
    for i in range(X.shape[0]):
        if X[i,2] == 'female':
            X[i,2] = -1
        else:
            X[i,2] = 1
    
        
    
    #miss1, mrs2,master3,mll:4
    for i in range(X.shape[0]):
        if "Miss." in X[i,1] : #contains 
            X[i,1] = 1
        elif "Mrs." in X[i,1]:
            X[i,1] = 2
        elif "Master." in X[i,1]:
            X[i,1] = 3
        elif "Mlle." in X[i,1]:
            X[i,1] = 1
        elif "Mr." in X[i,1]:
            X[i,1] = 4
        elif "Dr." in X[i,1]:
            X[i,1] = 4
        elif "Rev." in X[i,1]:
            X[i,1] = 4
        elif "Mme." in X[i,1]:
            X[i,1] = 2
        elif "Ms." in X[i,1]:
            X[i,1] = 1
        elif "Major." in X[i,1]:
            X[i,1] = 4
        elif "Lady." in X[i,1]:
            X[i,1] = 2
        elif "Sir." in X[i,1]:
            X[i,1] = 4
        elif "Col." in X[i,1]:
            X[i,1] = 4
        elif "Capt." in X[i,1]:
            X[i,1] = 4
        elif "Countess." in X[i,1]:
            X[i,1] = 2
        elif "Jonkheer." in X[i,1]:
            X[i,1] = 4
        elif "Don." in X[i,1]:
            X[i,1] = 4
        
    for i in range(X.shape[0]):
        if X[i,3] == '':
            X[i,3] = 0
    
    X=X.astype(float)    
       
        #ages
    avg1=0
    avg2=0
    avg3=0
    avg4=0
    c1=0
    c2=0
    c3=0
    c4=0
    for i in range(X.shape[0]):
        if X[i,1] == 1:
            if X[i,3] != 0:
                avg1 = avg1+X[i,3]
                c1=c1+1
        if X[i,1] == 2:
            if X[i,3] != 0:
                avg2 = avg2+X[i,3]
                c2=c2+1
        if X[i,1] == 3:
            if X[i,3] != 0:
                avg3 = avg3+X[i,3]
                c3=c3+1
        if X[i,1] == 4:
            if X[i,3] != 0:
                avg4 = avg4+X[i,3]
                c4=c4+1
      
    if c1 != 0:
        avg1 = avg1/c1
    if c2 != 0:
        avg2 = avg2/c2
    if c3 != 0:
        avg3 = avg3/c3
    if c4 != 0:
        avg4 = avg4/c4
    
    for i in range(X.shape[0]):
        if X[i,3] == 0:
            if X[i,1] == 1:
                X[i,3] = avg1
            elif X[i,1] == 2:
                X[i,3] = avg2
            elif X[i,1] == 3:
                X[i,3] = avg3
            elif X[i,1] == 4:
                X[i,3] = avg4
     
    
    X = delete(X,1,1)
   
    


    return X                
            
    
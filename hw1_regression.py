import numpy as np
import sys

lambda_input = int(sys.argv[1])
sigma2_input = float(sys.argv[2])
X_train = np.genfromtxt(sys.argv[3], delimiter = ",")
y_train = np.genfromtxt(sys.argv[4])
X_test = np.genfromtxt(sys.argv[5], delimiter = ",")

## Make diagonal matrix of ones
def diag1(ncol, lambdax=1):
    #INPUT: number of columns in square matrix
    #OUTPUT: diagonal matrix of ones times lambda
    c = [1*lambdax]*ncol
    I = np.diag(c)
    return(I)
    
## Solution for Part 1
def part1(X = X_train,Y = y_train, L = lambda_input, S2 = sigma2_input):
    ## Input : Arguments to the function
    ## Return : wRR, Final list of values to write in the file
    ncolx = X.shape[1]
    constLamda = L
    I = diag1(ncolx, constLamda)
    lhs = np.linalg.inv(I + np.matmul(X.transpose(),X)) ##(s2*L*I + x^t*x) inverted
    rhs = np.matmul(X.transpose(),Y) ## xty
    w = np.matmul(lhs,rhs)
    pass
    return (w)
#end def part1()
    
wRR = part1()  # Assuming wRR is returned from the function
np.savetxt("wRR_" + str(lambda_input) + ".csv", wRR, delimiter="\n") # write output to file

## check if number is in list
def ifExist(List1, Elem1):
    if Elem1 in List1:
        return(1)
    else:
        return(0)
##finished ifExist

## Solution for Part 2
def part2(X = X_train, Xnew = X_test, L = lambda_input, S2 = sigma2_input):
    ## Input : Arguments to the function
    ## Return : active, Final list of values to write in the file
    ncolx = X.shape[1]
    I = diag1(ncolx,L)
    XTX = np.matmul(X.transpose(),X)
    Cov = np.linalg.inv(np.add(I,XTX*(S2**(-1))))
    storage1 = [0]*10
    storage2 = [0]*10
    keke = []
    for i in range(0,10,1):
        ## Pick the 10 Xi to store                    
        temp = -1
        tempMax = -99999
        tempRow = 0
        tempVec = Xnew[1,]
        for j in Xnew:
            temp += 1
            temp2 = S2 + np.matmul(np.matmul(j.transpose(),Cov),j)
           
            if ifExist(keke,temp) == 0 and temp2 > tempMax:
                tempMax = temp2
                tempRow = temp
                tempVec = j
            #end if
        #end for j
        
        #update the covariance matrix   
        #XTX = np.add(np.matmul(tempVec,tempVec.transpose()),XTX)
        X = np.vstack([X,tempVec]) ##stacks matrix by rows
        XTX = np.matmul(X.transpose(),X)
        Cov = np.linalg.inv(np.add(I,XTX*(S2**(-1))))
        storage1[i] = tempRow+1
        keke.append(tempRow)
        storage2[i] = tempMax   
        #Xnew = np.delete(Xnew,tempRow,0)
    #end for i
    pass
    print(storage1)
    print(storage2)
    return (storage1)
#end def part2()

active = part2()  # Assuming active is returned from the function
np.savetxt("active_" + str(lambda_input) + "_" + str(int(sigma2_input)) + ".csv", active, delimiter=",") # write output to file

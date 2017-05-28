import hashlib
import binascii
import random
import numpy as np
from matplotlib import pyplot as plt
from numpy import zeros_like
from math import factorial as fact


max_nonce = 2**32

def hash_exp(num_zeros):
    b1 = 'wubba lubba'
    b2 = 'dub dub'
    for nonce in xrange(max_nonce):
        hashResult = hashlib.sha256(b1+b2+str(nonce)).hexdigest()
        s = ("1"+ hashResult)
        binary = str("{0:020b}".format(int(s,16)))
        if (int(binary[1:num_zeros+1]) == 0):
            return (hashResult,nonce)
    return 0

########################################################################
#Done 21
def fake_hash_exp(num_zeros):
    b1 = 'wubba lubba'
    b2 = 'dub dub'
    r = random.randint(0,pow(2,256)-1) # range from 0 to [2^256 -1]
    # s -> 'int', convert this to binary. [DONE]
    # check leading zero from this with [num_zeros]
    hashResult = hashlib.sha256(b1+b2+str(r)).hexdigest()
    string = "1" + hashResult
    binary = str("{0:020b}".format(int(string,16)))
    #print(binary)
    #print(binary[1:num_zeros+1])
    
    if ( int(binary[1:num_zeros+1]) ) == 0:
        #print("Goes In")
        return 1
    else:
        return 0
    
########################################################################
# Done 21 and 22
def run_fake_hash_exp(num_zeros):
    arr = []
    counter = 0
    v2 = []
    for i in range(0,500000):
        arr += [fake_hash_exp(num_zeros)]
        if arr[i] == 0:
            counter +=1
        else:
            v2 += [counter]
            counter = 0
    return(arr,v2)

########################################################################
#Done 23
def histogram(num_zeros):
    (arr,v2) = run_fake_hash_exp(num_zeros)
    print(v2)
    plt.figure(1)
    plt.hist(v2,bins = 20,rwidth=.4,align ='mid',weights = np.zeros_like(v2)+1./len(v2))
    plt.xlim(0,200)
    plt.title("Histogram")
    plt.xlabel("x")
    plt.ylabel("Pr")
    plt.show()

########################################################################
# 24
def run_fake_10min(num_zeros):
    (arr,v2) = run_fake_hash_exp(num_zeros)
    n = 0
    v3 = []
    # slicing 1000 elements and summing it to simulate 10 minutes.
    # v3 = [sum(arr[0:1001]) ,sum(arr[1000:2001]),......,sum(arr[n,(2*n)+1])]
    for j in range(0,500):
        v3 += [sum(arr[n:n+1001])]
        n += 1000
    return(v3)
#=======================================================================
def histogram_1000trials(num_zeros):
    (v3) = run_fake_10min(num_zeros)
    #print(v3)
    plt.figure(1)
    plt.hist(v3,bins = 1000,rwidth=.4,align ='mid',weights = np.zeros_like(v3)+1./len(v3))
    plt.xlim(0,35)
    plt.title("Histogram")
    plt.xlabel("x")
    plt.ylabel("Pr")
    plt.show()    
########################################################################   
#25
def histogram_q25(num_zeros):
    
    (v3) = run_fake_10min(num_zeros)
    l = sum(v3)/len(v3)
    y_value=[]
    x_value=[]
    
    for k in range(0,35):
        y_value += [((2.7)**-l * l**k)/fact(k)]
        x_value += [k]
    print(y_value)
    
    plt.figure(1)
    plt.hist(v3,bins = len(v3),rwidth=.4,align ='mid',weights = np.zeros_like(v3)+1./len(v3))

    plt.xlim(0,35)
    plt.draw()
    plt.title("Histogram")
    plt.xlabel("x")
    plt.ylabel("Pr")
    plt.plot(x_value,y_value)
    plt.show()
    
########################################################################    

        
    
    
    

    
    


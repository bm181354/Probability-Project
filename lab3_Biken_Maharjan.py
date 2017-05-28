import numpy as np
from matplotlib import pyplot as plt
from numpy import zeros_like
from numpy.random import randint
from math import factorial as fact
import pylab
import hashlib
import binascii
import random
import pandas as pd

#Q1 n Q2

def flip(p):
    return 1 if np.random.uniform(0.0,1.0) < p else 0
##############################################################################################

def Bernoulli_hist(p,m):
    array = [0]*(m+1) 
    for i in range(0,m):
        array[i] = flip(p)   
    plt.figure(1)
    plt.hist(array,bins =2,rwidth=.4,align ='mid',weights = np.zeros_like(array)+1./len(array))
    plt.xlim(0,1)
    plt.title("Bernoulli Histogram")
    plt.xlabel("x")
    plt.ylabel("Pr")
    plt.show()

##############################################################################################    
#[5]
def binomial_draw(n,p):
    array = []
    store_success = []
    for i in range(0,n):
        array += [flip(p)]   
       
    for i in range(0,n):    
        if array[i] == 1:
            store_success += [array[i]]
    return len(store_success)

##############################################################################################
#[6]
def binom_trials(n,p,numExpts):
    var = []
    for i in range(0,numExpts):
        var +=[binomial_draw(n,p)]
    return var

##############################################################################################
#[7]
def binom_hist(n,p,numExpts):
    array = [0]*(numExpts+1) 
    array = binom_trials(n,p,numExpts)   
    plt.figure(1)
    plt.hist(array,bins = numExpts,rwidth=.4,align ='mid',weights = np.zeros_like(array)+1./len(array))
    plt.xlim(0,100)
    plt.title("Bernoulli Histogram")
    plt.xlabel("No# of Head")
    plt.ylabel("Pr")
    plt.show()
##############################################################################################
#8 -> G
def histogram():
    
    array = []
    s =[]
    length = 4
    
    for i in range(length):
        array += [3-2*i]
    
    for x in array:
        k = ((3-x)/2)
        s += [( (fact(3)/(fact(3-k)*fact(k))) *(1.0/8))]
    plt.bar(array,s,align='center', color='red')
    plt.xlabel('s')
    plt.ylabel(' pr[S = s] ')

###########################################################################################
#9 -> B
def histogram_q8():
    
    array = []
    s =[]
    length = 9
    
    for i in range(length):
        array += [8-2*i]
    
    for x in array:
        k = ((8-x)/2)
        s += [( (fact(8)/(fact(8-k)*fact(k))) *(1.0/pow(2,8)))]
    plt.figure(1)
    plt.bar(array,s,align='center', color='blue')
    plt.xlabel('s')
    plt.ylabel(' pr[S = s] ')
#===================================================================
def call_histograms():
    histogram_q8()
    histogram()
    plt.show()


##############################################################################################
#14

def histogram1():
    
    array = []
    s =[]
    length = 101
    
    for i in range(length):
        array += [100-2*i]
    
    for x in array:
        k = ((100-x)/2)
        s += [( (fact(100)/(fact(100-k)*fact(k))) *(1.0/pow(2,100)))]
    plt.bar(array,s,align='center', color='red')
    plt.xlabel('s')
    plt.ylabel(' pr[S = s] ')

###############################################################################################
def histogram_q14():
    
    array = []
    s =[]
    length = 201
    
    for i in range(length):
        array += [200-2*i]
    
    for x in array:
        k = ((200-x)/2)
        s += [( (fact(200)/(fact(200-k)*fact(k))) *(1.0/pow(2,200)))]
    
    plt.figure(1)
    plt.bar(array,s,align='center', color='blue')
    plt.xlabel('s')
    plt.ylabel(' pr[S = s] ')
#===================================================================
def call_histograms1():
    histogram1()
    histogram_q14()
    plt.show()

####################################################################################################
def find_p():
    p=0
    for s in range(-100,101):
        p+= ((((fact(200)/(fact(200-((200-(s))/2))*fact((200-(s))/2))) *(1.0/pow(2,200)))+
              (((fact(200)/(fact(200-((200-(s-2))/2))*fact((200-(s-2))/2))) *(1.0/pow(2,200)))+
               +(((fact(200)/(fact(200-((200-(s+2))/2))*fact((200-(s+2))/2))) *(1.0/pow(2,200)))))) *
             ((fact(100)/(fact(100-((100-(s))/2))*fact((100-(s))/2))) *(1.0/pow(2,100))))
    return(p)

#################################################################################################


#Q.19

data_frame = pd.read_csv('real_bitcoin.csv', delim_whitespace=True, header=None)
def histogram_poisson():
    y_series = []
    
    for i in xrange(59):
        y_series +=[(data_frame.iat[i+1, 2]-data_frame.iat[i, 2])/12.5]

    plt.figure (1)
    plt.hist(y_series,bins=6,rwidth = 0.5 ,align='mid',
             weights=np.zeros_like (y_series) + 1. /len(y_series))
    plt.xlim (100,190)
    plt.title ("PMF")
    plt.xlabel ("x")
    plt.ylabel("Pr[ X = x]")
    plt.show()

##################################################################################################

max_nonce = pow(2,32)

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

###################################################################################################

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

#####################################################################################################
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

#####################################################################################################
#Done 23
def histogram2(num_zeros):
    (arr,v2) = run_fake_hash_exp(num_zeros)
    print(v2)
    plt.figure(1)
    plt.hist(v2,bins = 20,rwidth=.4,align ='mid',weights = np.zeros_like(v2)+1./len(v2))
    plt.xlim(0,200)
    plt.title("Histogram")
    plt.xlabel("x")
    plt.ylabel("Pr")
    plt.show()

####################################################################################################
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
#===================================================================================================
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
####################################################################################################
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

#######################################################################################


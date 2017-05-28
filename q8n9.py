from matplotlib import pyplot as plt
import numpy as np
from numpy.random import randint
from numpy import zeros_like
from math import factorial as fact

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
 
#####################################################################
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
#####################################################################    
    
    
    
     

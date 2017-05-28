from matplotlib import pyplot as plt
import numpy as np
from numpy.random import randint
from numpy import zeros_like
from math import factorial as fact

#14
def histogram():

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
 
#####################################################################
def histogram_q8():

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
def call_histograms():
    
    histogram()
    histogram_q8()
    plt.show()
#####################################################################
def find_p():
    p=0
    for s in range(-100,101):
     p+= ((((fact(200)/(fact(200-((200-(s))/2))*fact((200-(s))/2))) *(1.0/pow(2,200)))+
          (((fact(200)/(fact(200-((200-(s-2))/2))*fact((200-(s-2))/2))) *(1.0/pow(2,200)))+
          +(((fact(200)/(fact(200-((200-(s+2))/2))*fact((200-(s+2))/2))) *(1.0/pow(2,200)))))) *
          ((fact(100)/(fact(100-((100-(s))/2))*fact((100-(s))/2))) *(1.0/pow(2,100))))
    return(p)

    

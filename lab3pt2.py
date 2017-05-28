#Q.19

from matplotlib import pyplot as plt
import numpy as np
from numpy.random import randint
from numpy import zeros_like
import pylab

import pandas as pd
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
##################################################################################    
    

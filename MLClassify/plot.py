# -*- coding: utf-8 -*-
"""
Created on Mon May  4 21:30:08 2020

@author: Nitish Ranjan
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import label_binarize

def plotCM(cm):
    
    accuracy = np.trace(cm) / np.sum(cm).astype('float')
    misclass = (1 - accuracy) 
    accuracy = accuracy * 100
    misclass = misclass * 100
    sns.heatmap(cm/np.sum(cm), annot=True, fmt='.2%', cmap='Blues')

    # labels, title and ticks
    ax.set_xlabel('Predicted labels');
    ax.set_ylabel('True labels'); 
    ax.set_title('Confusion Matrix for Cricket Data'); 
    ax.xaxis.set_ticklabels(['Negative', 'Neutral','Positive']); ax.yaxis.set_ticklabels(['Negative', 'Neutral','Positive']);
    plt.xlabel('Predicted label\naccuracy={:0.2f}%; misclass={:0.2f}%'.format(accuracy, misclass))


ax= plt.subplot()

cfMain = [[374, 12, 31],
       [33, 2, 12],
       [73, 9, 50]]

cmTest = [[367, 2, 20],
       [20, 9, 12],
       [68, 5, 93]]


cmTestRestaurantUnigram = [[58, 3, 62],
                           [2, 4, 6],
                           [16, 2, 259]]



cmTestRestaurantBigram = [[61, 4, 58],
                          [1, 6, 5],
                          [9, 3, 265]]

cmTestCricketBigram = [[372, 3, 14],
                       [16, 15, 10],
                       [59, 4, 103]]

plotCM(cmTest)



####### Cricket ##########

"""

cfMain = [[374, 12, 31],
       [33, 2, 12],
       [73, 9, 50]]

cmTest = [[367, 2, 20],
       [20, 9, 12],
       [68, 5, 93]]

"""
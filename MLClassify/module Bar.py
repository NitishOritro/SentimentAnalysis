# -*- coding: utf-8 -*-
"""
Created on Tue May  5 22:02:15 2020

@author: Nitish Ranjan
"""
import chart_studio.plotly as py
from plotly.graph_objs import *
py.sign_in('nitish.ranjan51', 'ZUrihULi2FJYxY3ZJ9GP')
trace1 = {
  "name": "Accuracy", 
  "type": "bar", 
  "x": ["SVM_Linear", "SVM_RBF", "SVM_Polynomial k=3", "Random Forest", "Naive Bayes"], 
  "y": [63, 57, 70, 71, 69]
}
trace2 = {
  "name": "Precision", 
  "type": "bar", 
  "x": ["SVM_Linear", "SVM_RBF", "SVM_Polynomial k=3", "Random Forest", "Naive Bayes"], 
  "y": [63, 57, 73, 71, 75]
}
trace3 = {
  "name": "Recall", 
  "type": "bar", 
  "x": ["SVM_Linear", "SVM_RBF", "SVM_Polynomial k=3", "Random Forest", "Naive Bayes"], 
  "y": [63, 58, 71, 71, 68]
}
trace4 = {
  "name": "F1 Score", 
  "type": "bar", 
  "x": ["SVM_Linear", "SVM_RBF", "SVM_Polynomial k=3", "Random Forest", "Naive Bayes"], 
  "y": [62, 55, 70, 71, 66]
}
data = Data([trace1, trace2, trace3, trace4])
layout = {"barmode": "group"}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 22:13:03 2020

@author: Nitish Ranjan
""
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['SVM', 'Logistic Regresiion', 'KNN', 'Random Forest']
#men_means = [77.91, 70.41 , 69.41, 67.23]
#women_means = [78.61, 67.07, 66.13, 45.21]

men_means = [78.69, 72.81 , 63.25, 65.26]
women_means = [80, 70.36, 56.60, 42.59]

x = np.arange(len(labels))
  # the label locations
print(x)
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Accuracy')
rects2 = ax.bar(x + width/2, women_means, width, label='Precision')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Classification Algorithm')
ax.set_ylabel('Accuracy & Precision')
ax.set_title('Accuracy & Precision of Cricket Data with Different Classifier')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        print(height)
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 0.5),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()



import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

data1 = [23,85, 72, 43, 52]
data2 = [42, 35, 21, 16, 9]
width =0.3
plt.bar(np.arange(len(data1)), data1, width=width)
plt.bar(np.arange(len(data2))+ width, data2, width=width)
plt.show()
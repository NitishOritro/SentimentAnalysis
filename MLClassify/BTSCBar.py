# -*- coding: utf-8 -*-
"""
Created on Sun May 17 23:22:22 2020

@author: Nitish Ranjan
"""


"""
Created on Wed May  6 22:13:03 2020

@author: Nitish Ranjan
""
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['Positive(Restaurant)', 'Positive(Cricket)', 'Negative(Restaurant)', 'Negative(Cricket)', 'Neutral(Restaurant)', 'Neutral(Cricket)']
#men_means = [77.91, 70.41 , 69.41, 67.23]
#women_means = [78.61, 67.07, 66.13, 45.21]

#men_means = [77.91, 80.58, 78.69, 82.21]
#women_means = [78.61, 81.26, 80.00, 81.64]


TPR = [0.87, 0.88, 0.83, 0.90, 0.16, 0.60] 
TNR = [0.87, 0.89, 0.87, 0.89, 0.99, 0.99]
FPR = [0.37, 0.10, 0.12, 0.12, 0.008, 0.008]

x = np.arange(len(labels))
  # the label locations
print(x)
width = 0.20  # the width of the bars

#fig, ax = plt.subplots()
fig, ax = plt.subplots(figsize=(10, 4))
rects1 = ax.bar(x - (width), TPR, width, label='TPR')
rects2 = ax.bar(x + (width/20), TNR, width, label='TNR')
rects3 = ax.bar(x + (1.1*width), FPR, width, label='FPR')
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('TPR, TNR & FPR in Restaurant & Cricket Dataset')
ax.set_ylabel('TPR, TNR & FPR')
ax.set_title('TPR, TNR & FPR for positive, negative & neutral polarity in Restaurant & Cricket Dataset')
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
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

fig.tight_layout()
# Setting the x-axis and y-axis limits
#plt.xlim(1, 5)
plt.ylim([0, 1.5] )
plt.show()



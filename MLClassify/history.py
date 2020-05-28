#women_means = [78.61, 67.07, 66.13, 45.21]

men_means = [69, 76.72 , 83.20, 85, 80.48, 82.21,80.58]
#women_means = [80, 70.36, 56.60, 42.59]

x = np.arange(len(labels))
  # the label locations
print(x)
width = 0.50  # the width of the bars

fig, ax = plt.subplots(figsize=(7, 4.5))
rects1 = ax.bar(x , men_means, width, label='Accuracy')
#rects2 = ax.bar(x + width/2, women_means, width, label='Precision')

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
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')



autolabel(rects1)
#autolabel(rects2)

fig.tight_layout()
plt.ylim([0, 110] )

plt.show()
"""
Created on Fri May 22 16:39:36 2020

@author: Nitish Ranjan
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['Paper [16]\nUniGram\n+\nNegation\n+\nSVM', 'Paper [18]\nUniGram\n+\nStemmer\n+\nNaive Base', 
          'Paper [18]\nBiGram\n+\nStemmer\n+\nNaive Base', 'Paper [20]\nUniGram\n+\nPOS',
          'Paper [28]\nMultinomial\nNaive Base', 'Proposed\nMethod\nBiGram\nCricket','Proposed\nMethod\nBiGram\nRestaurant']
#men_means = [77.91, 70.41 , 69.41, 67.23]
#women_means = [78.61, 67.07, 66.13, 45.21]

men_means = [69, 76.72 , 83.20, 85, 80.48, 82.21,80.58]
#women_means = [80, 70.36, 56.60, 42.59]

x = np.arange(len(labels))
  # the label locations
print(x)
width = 0.50  # the width of the bars

fig, ax = plt.subplots(figsize=(7, 4.5))
rects1 = ax.bar(x , men_means, width, label='Accuracy')
#rects2 = ax.bar(x + width/2, women_means, width, label='Precision')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Different Classification Approach')
ax.set_ylabel('Accuracy')
ax.set_title('Comapare Accuracy Between Existing and Proposed System')
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
#autolabel(rects2)

fig.tight_layout()
plt.ylim([0, 110] )

plt.show()

## ---(Sat May 23 13:47:51 2020)---
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['Paper [16]\nUniGram\n+\nNegation\n+\nSVM', 'Paper [18]\nUniGram\n+\nStemmer\n+\nNaive Base', 
          'Paper [18]\nBiGram\n+\nStemmer\n+\nNaive Base', 'Paper [20]\nUniGram\n+\nPOS',
          'Paper [27]\nMultinomial\nNaive Base', 'Proposed\nMethod\nBiGram\nCricket','Proposed\nMethod\nBiGram\nRestaurant']
#men_means = [77.91, 70.41 , 69.41, 67.23]
#women_means = [78.61, 67.07, 66.13, 45.21]

men_means = [69, 76.72 , 83.20, 85, 80.48, 82.21,80.58]
#women_means = [80, 70.36, 56.60, 42.59]

x = np.arange(len(labels))
  # the label locations
print(x)
width = 0.50  # the width of the bars

fig, ax = plt.subplots(figsize=(7, 4.5))
rects1 = ax.bar(x , men_means, width, label='Accuracy')
#rects2 = ax.bar(x + width/2, women_means, width, label='Precision')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Different Classification Approach')
ax.set_ylabel('Accuracy')
ax.set_title('Comapare Accuracy Between Existing and Proposed System')
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
#autolabel(rects2)

fig.tight_layout()
plt.ylim([0, 110] )

plt.show()
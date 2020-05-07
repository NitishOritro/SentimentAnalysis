
"""
Created on Wed May  6 22:13:03 2020

@author: Nitish Ranjan
""
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['Restaurant(UniGram + SVM)', '(BiGram + SVM)', 'Cricket(UniGram + SVM)', '(BiGram + SVM)']
#men_means = [77.91, 70.41 , 69.41, 67.23]
#women_means = [78.61, 67.07, 66.13, 45.21]

#men_means = [77.91, 80.58, 78.69, 82.21]
#women_means = [78.61, 81.26, 80.00, 81.64]


accuracy = [77.91, 80.58, 78.69, 82.21]
precision = [78.61, 80.92, 80.00, 81.64]
reecall = [77.16, 78.48, 77.89, 79.56]

x = np.arange(len(labels))
  # the label locations
print(x)
width = 0.20  # the width of the bars

#fig, ax = plt.subplots()
fig, ax = plt.subplots(figsize=(10,5))
rects1 = ax.bar(x - (width), accuracy, width, label='Accuracy')
rects2 = ax.bar(x + (width/20), precision, width, label='Precision')
rects3 = ax.bar(x + (1.1*width), reecall, width, label='Recall')
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('SVM Classification Algorithm')
ax.set_ylabel('Accuracy, Precision & Recall')
ax.set_title('Accuracy & Precision in Suport Vector Machine with Tf-Idf Model')
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
plt.ylim([0, 120] )
plt.show()



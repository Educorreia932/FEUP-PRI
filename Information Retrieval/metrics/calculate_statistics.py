"""
Q0
W0 - NNNNNNRNNN NRRNNRNRNR
W1 - NNNNRRRRRR RNRRRNNRRR
W2 - NNNNNNRNNN NRRNNRNRNN
W3 - NNNNNNRNNN NRRNNRNRNN

Q1
W0 - NNNRNNRNRN RNRNNNRRRN
W1 - NRNRRRNRRR RRRRNNNNNN
W2 - NNNNNNNNRN NNNNNNRNNR
W3 - NRNRRRNRRR RRRRNNNNNN

Q2
W0 - NNNNNNNRNR NNNNNNNNNR
W1 - RRNNNNNRRN RRRNNRRRRR
W2 - NNNNNNNRNN NNNNRNRRNN
W3 - NNNRNNNNNN RNNNRNRNNN

Q3
W0 - RRNNNNRRNN RRRNRNNNRN
W1 - RNRNNNNNNN RNNNNNNNNN
W2 - RRRRRNRRRR RRNRRRRRRN
W3 - RNNRNRNNNN NNNNNNNNNN

Q4
W0 - RRNNNNRRNN RRRNRNNNRN
W1 - RNRNNNNNNN RNNNNNNNNN
W2 - RRRRRNRRRR RRNRRRRRRN
W3 - RNNRNRNNNN NNNNNNNNNN
"""

import math
import matplotlib.pyplot as plt
from sklearn.metrics import PrecisionRecallDisplay
import numpy as np
import json
import requests
import pandas as pd


N_RETRIEVED = 10
UNIVERSE_SIZE = 20


relevance_string = ""
relevance_list = ["NNNNNNRNNN NRRNNRNRNR", "NNNNRRRRRR RNRRRNNRRR", "NNNNNNRNNN NRRNNRNRNN", "NNNNNNRNNN NRRNNRNRNN", "NNNRNNRNRN RNRNNNRRRN", "NRNRRRNRRR RRRRNNNNNN", "NNNNNNNNRN NNNNNNRNNR", "NRNRRRNRRR RRRRNNNNNN", "NNNNNNNRNR NNNNNNNNNR", "RRNNNNNRRN RRRNNRRRRR", "NNNNNNNRNN NNNNRNRRNN", "NNNRNNNNNN RNNNRNRNNN", "RRNNNNRRNN RRRNRNNNRN", "RNRNNNNNNN RNNNNNNNNN", "RRRRRNRRRR RRNRRRRRRN", "RNNRNRNNNN NNNNNNNNNN", "RRNNNNRRNN RRRNRNNNRN", "RNRNNNNNNN RNNNNNNNNN", "RRRRRNRRRR RRNRRRRRRN", "RNNRNRNNNN NNNNNNNNNN"]










# Precision
# documents from the first 10 / 10
# Input: String (size 10) of relevant documents
def calc_precision(relevance_string, num):
    precision = 0
    for i in range(0, num):
        if relevance_string[i] == 'R':
            precision += 1
    return precision / num



# Recall  
# documents from the first 10 / relevant documents from the 20
# Input: String (size 20) of relevant documents
def calc_recall(relevance_string, num):
    relevant_count = 0
    rel_total_count = 0
    for i in range(0, num):
        if relevance_string[i] == 'R':
            relevant_count += 1
    for i in range(0, UNIVERSE_SIZE):
        if relevance_string[i] == 'R':
            rel_total_count += 1
    return relevant_count / rel_total_count

# Average precision 
# From i in range(0, 10): Precision at i * wether i is relevant
# All of that divided by the number of relevant documents (first 10)
# Input: String (size 20) of relevant documents
def calc_AP(relevance_string):
    relevant_count = 0
    AP_score = 0
    for i in range(0, N_RETRIEVED):
        if relevance_string[i] == 'R':
            relevant_count += 1
    for i in range(0, N_RETRIEVED):
        if relevance_string[i] == 'R':
            AP_score += calc_precision(relevance_string, i + 1)
    return AP_score / relevant_count


# Mean AP
# Only doable when I have all the average precisions (?)

# Mean reciprocal rank
# Average of all queries
# For each query, find the first relevant result (at place n) and the result is 1/n
# Input: String (size 20) of relevant documents

# Discounted cumulative gain @p=10
# sum of:
# for i in range(0, p): wether i is relevant / log2(i + 1)
# Input: String (size 20) of relevant documents
def calc_DCG(relevance_string):
    score = 0
    for i in range(0, N_RETRIEVED):
        if relevance_string[i] == 'R':
            score += 1 / math.log2(i + 2)
    return score


# Good for finding the best ranking functions
# "The authors show that for every pair of substantially different ranking functions, the NDCG can decide which one is better in a consistent manner."


with open('search_names_and_jsons/statistics.txt','w') as tf:
    for q in range(0, 5):
        relevance_string = ""
        for w in range(0, 4):
            relevance_string = relevance_list[w + q * 4]
            tf.write("Querry " + str(q) + ":\n")
            tf.write("Weight system " + str(w) + ":\n")
            tf.write("Precision: " + str(calc_precision(relevance_string, N_RETRIEVED)) + "\n")
            tf.write("Recall: " + str(calc_recall(relevance_string, N_RETRIEVED)) + "\n")
            tf.write("Average Precision: " + str(calc_AP(relevance_string)) + "\n")
            tf.write("Discounted cumulative gain: " + str(calc_DCG(relevance_string)) + "\n" + "\n")


for q in range(0, 5):
    _, ax = plt.subplots(figsize=(10, 10))
    relevance_string = ""
    for w in range(0, 4):
        relevance_string = relevance_list[w + q * 4]
        # PRECISION-RECALL CURVE
        # Calculate precision and recall values as we move down the ranked list
        precision_values = list()
        recall_values = list()

        for i in range(0, UNIVERSE_SIZE):
            precision_values.append(calc_precision(relevance_string, i + 1))

        for i in range(0, UNIVERSE_SIZE):
            recall_values.append(calc_recall(relevance_string, i + 1))

        '''
        precision = [
            calc_precision(relevance_string, idx)
            for idx, _ in enumerate(relevance_string, start=1)
        ]

        precision = [
            calc_precision(relevance_string, idx)
            for idx, _ in enumerate(relevance_string, start=1)
        ]'''


        precision_recall_match = dict(zip(recall_values, precision_values))
        #precision_recall_match = {k: v for k,v in zip(recall_values, precision_values)}

        # Extend recall_values to include traditional steps for a better curve (0.1, 0.2 ...)
        recall_values.extend([step for step in np.arange(0.1, 1.1, 0.1) if step not in recall_values])
        recall_values = sorted(set(recall_values))

        # Extend matching dict to include these new intermediate steps
        for idx, step in enumerate(recall_values):
            if step not in precision_recall_match:
                if recall_values[idx-1] in precision_recall_match:
                    precision_recall_match[step] = precision_recall_match[recall_values[idx-1]]
                else:
                    precision_recall_match[step] = precision_recall_match[recall_values[idx+1]]

        disp = PrecisionRecallDisplay([precision_recall_match[r] for r in recall_values], recall_values)
        #plt.savefig('precision_recall_q' + str(q) + '_w' + str(w) + '.pdf')
        disp.plot(ax=ax, name=f"WF{w}")

    ax.legend(loc="upper left")
    ax.set_xlabel("Recall")
    ax.set_ylabel("Precision")

    plt.savefig('precision_recall_q' + str(q) + '.pdf')
    plt.close()


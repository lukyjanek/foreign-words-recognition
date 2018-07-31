#!/usr/bin/env python3
# coding: utf-8

"""Count Precision, Recall and F1 score of recogFW script."""

import sys

sys.path.append('../')
from recogFW import recog_foreign_word

# load manual annotated data - gold data
gold_data = list()
with open(sys.argv[1], mode='r', encoding='utf-8') as f:
    for line in f:
        line = line.rstrip('\n').split('\t')
        gold_data.append(line)

# measure precision and recall
fn = 0  # false negatives
tn = 0  # true negatives
fp = 0  # false positives
tp = 0  # true positives

for entry in gold_data:
    alg_res = recog_foreign_word(entry[1])
    if entry[0] == '+' and alg_res:
        tp += 1
    elif entry[0] == '' and not alg_res:
        fp += 1
    elif entry[0] == '+' and not alg_res:
        tn += 1
    elif entry[0] == '' and alg_res:
        fn += 1
    else:
        print('Problem with:', entry)

precision = (tp + fp) / len(gold_data)
recall = tp / (tp + fn)

# measure F1 score
f1_score = 2 * (precision * recall) / (precision + recall)

# print measured results
print(10*'-', 'RESULTS', 10*'-')
print('Gold data:', sys.argv[1], sep='\t')
print('Compared to:', 'recogFW.py', sep='\t')

print()

print('Prec:', precision, sep='\t')
print('Rec:', recall, sep='\t')

print('F1:', f1_score, sep='\t')

print()

print('More details')
print('Size of data:', len(gold_data), sep='\t')
print('True-Posit:', tp, sep='\t')
print('True-Negat:', tn, sep='\t')
print('False-Posit:', fp, sep='\t')
print('False-Negat:', fn, sep='\t')

print(29*'-')

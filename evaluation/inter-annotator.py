#!/usr/bin/env python3
# coding: utf-8

"""Count Cohen's kappa (inter-annotator agreement) between annotations."""

import sys

# load manual annotated data
data1 = list()
with open(sys.argv[1], mode='r', encoding='utf-8') as f:
    for line in f:
        line = line.rstrip('\n').split('\t')
        data1.append(line)

data2 = list()
with open(sys.argv[2], mode='r', encoding='utf-8') as f:
    for line in f:
        line = line.rstrip('\n').split('\t')
        data2.append(line)

# measure Cohen's kappa
# probability of agreement by chance (Pe)
T1 = 0
F1 = 0
for entry in data1:
    if entry[0] == '':
        F1 += 1
    else:
        T1 += 1

T2 = 0
F2 = 0
for entry in data2:
    if entry[0] == '':
        F2 += 1
    else:
        T2 += 1

Pe = T1/len(data1) * T2/len(data2) + F1/len(data2) * F2/len(data2)

# probability of relative observer agreement between annoators (Pa)
number_same = 0
number_diff = 0

merged = list(zip(data1, data2))
for entries in merged:
    if entries[0] == entries[1]:
        number_same += 1
    else:
        number_diff += 1

Pa = number_same/len(merged)

# Cohen's kappa
K = (Pa - Pe) / (1 - Pe)

# print measured results
print(10*'-', 'RESULTS', 10*'-')
print('Data 1:', sys.argv[1], sep='\t')
print('Data 2:', sys.argv[2], sep='\t')

print()

print("Cohen's kappa:", K, sep='\t')

print(29*'-')

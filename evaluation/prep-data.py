#!/usr/bin/env python3
# coding: utf-8

"""Build evaluation data."""

import sys
import string
import random
from collections import defaultdict


# read freq-word-list and create freq-lemma-list
lemmas_freq = defaultdict(int)
with open(sys.argv[1], mode='r', encoding='utf-8') as f:
    for line in f:
        entry = line.strip().split('\t')
        pos = entry[2][0] + entry[2][14]  # pos and number for abbrev (8)
        lemmas_freq[(entry[1], pos)] += int(entry[0].split()[0])


# remove propriums, interpunctions, abbreviations, and lemmas with numbers or
# punctuations from freq-lemma-list
remove_from_list = set()
for lemma in lemmas_freq:
    if lemma[0][0].isupper():  # propriums
        remove_from_list.add(lemma)

    if 'Z' in lemma[1]:  # interpunctions
        remove_from_list.add(lemma)

    if '8' in lemma[1]:  # abbreviations
        remove_from_list.add(lemma)

    for num in '0123456789':  # numbers
        if num in lemma[0]:
            remove_from_list.add(lemma)
            break

    for punct in string.punctuation:  # punctuations
        if punct in lemma[0]:
            remove_from_list.add(lemma)
            break

for lemma in remove_from_list:
    del lemmas_freq[lemma]


# split input frequency list of all lemmas according to four intervals
interval1 = list()  # freq 1-2
interval2 = list()  # freq 3-10
interval3 = list()  # freq 11-100
interval4 = list()  # freq 101-max


for lemma, freq in lemmas_freq.items():
    if freq <= 2:
        interval1.append(lemma)
    elif 3 <= freq <= 10:
        interval2.append(lemma)
    elif 11 <= freq <= 100:
        interval3.append(lemma)
    else:
        interval4.append(lemma)


# create random samples of evaluation
evaluation_data = list()

n = 1000  # size of evaluation data
i = 4     # number of intervals

lpi = n/i  # lemmas per interval
evaluation_data.append(random.sample(interval4, round(lpi)))
evaluation_data.append(random.sample(interval3, round(lpi)))
evaluation_data.append(random.sample(interval2, round(lpi)))
evaluation_data.append(random.sample(interval1, round(lpi)))


# save evaluation data
with open(sys.argv[2], mode='w', encoding='utf-8') as f:
    for interval in evaluation_data:
        for lemma in interval:
            f.write('\t' + lemma[0] + '\n')

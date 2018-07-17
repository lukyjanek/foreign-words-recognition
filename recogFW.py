#!usr/bin/env python3
# coding: utf-8

'''Script for the recognition of foreign words in the Czech language.'''

import sys
import itertools as it


# function for the recognition of foreign word
# can be imported and used in any project
def recog_foreign_word(word, pos=None):
    '''Return True statement if given word (and pos optionaly) is foreign.'''
    word = word.lower()

    # PART1: universal rules for all pos
    # foreign letters
    for letter in 'gxwqóf':
        if letter in word:
            return word, True

    # combinations of vowels (except 'ou' and 'oo')
    vowels = 'aeiyouáéěíýůú'

    combinations = list(it.product(vowels, repeat=2))
    del combinations[combinations.index(('o', 'u'))]
    del combinations[combinations.index(('o', 'o'))]

    for pair in combinations:
        comb = pair[0] + pair[1]
        if comb in word:
            return word, True

    # unrespected palatalization
    palatal_vowels = 'eéií'
    for pair in list(it.product(('k', 'h', 'ch', 'r'), palatal_vowels)):
        comb = pair[0] + pair[1]
        if comb in word:
            return word, True

    # unrespected soft and hard consonants
    hard_consonants = ('h', 'ch', 'k', 'r')
    for pair in list(it.product(hard_consonants, 'ií')):
        comb = pair[0] + pair[1]
        if comb in word:
            return word, True

    soft_consonants = 'žščřcj'
    for pair in list(it.product(soft_consonants, 'yý')):
        comb = pair[0] + pair[1]
        if comb in word:
            return word, True

    # unrespected mixed consonants

    # borrowed nasalisation pattern
    consonants = 'cdghjklrstvzščřžďťň'
    vowels = 'aeiyouáéěíýůú'

    transcribed = ''
    for letter in word:
        if letter in consonants:
            transcribed += 'C'
        elif letter in vowels:
            transcribed += 'V'
        else:
            transcribed += letter

    if 'VnC' in transcribed or 'Vmb' in transcribed or 'Vmp' in transcribed:
        return word, True

    # PART2: rules according to a specific pos
    if pos == 'N' or pos is None:  # nouns and unspecific
        pass

    if pos == 'V' or pos is None:  # verbs and unspecific
        pass

    if pos == 'A' or pos is None:  # adjectives and unspecific
        pass

    if pos == 'D' or pos is None:  # adverbs and unspecific
        pass

    return word, False


# internal function for splitting input data if script is used in shell
def split_data(line):
    '''Return word and pos splited from stdin/file line. Separator is \t.'''
    word = None
    pos = None

    if len(line.split('\t')) == 1:
        word = line.split('\t')[0]
        pos = None
    else:
        word, pos = line.split('\t')

    if pos not in ('V', 'N', 'D', 'A'):  # allowed pos
        pos = None

    return word, pos


# running script if it is used in shell (with stdin or path to file)
if __name__ == '__main__':

    if not sys.stdin.isatty():  # read from stdin
        for line in sys.stdin:
            word, pos = split_data(line.strip())
            print(recog_foreign_word(word, pos))

    else:  # read from file
        if len(sys.argv) == 2:
            with open(sys.argv[1], mode='r', encoding='utf-8') as f:
                for line in f:
                    word, pos = split_data(line.strip())
                    print(recog_foreign_word(word, pos))
        else:
            print('Error: Use script in pipeline or give the path '
                  'to the relevant file in the first argument.')

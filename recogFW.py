#!usr/bin/env python3
# coding: utf-8

'''Script for the recognition of foreign words in the Czech language.'''

import sys


# function for the recognition of foreign word
# can be imported and used in any project
def recog_foreign_word(word, pos=None):
    '''Return True statement if given word (and pos optionaly) is foreign.'''
    return word, pos


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

    if not sys.stdin.isatty():  # read from stdin (pipeline)
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

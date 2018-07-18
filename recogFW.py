#!usr/bin/env python3
# coding: utf-8

'''Script for the recognition of foreign words in the Czech language.'''

import sys
import itertools as it


# function for the recognition of foreign word
# can be imported and used in any project
def recog_foreign_word(word, pos=None):
    '''Return T/F statement if given word (and pos optionaly) is foreign.'''
    word = word.lower()

    # foreign letters
    for letter in 'gxwqóf':
        if letter in word:
            return word, 1, True

    # combinations of vowels (except 'ou' and 'oo')
    vowels = 'aeiyouáéěíýůú'

    combinations = list(it.product(vowels, repeat=2))
    del combinations[combinations.index(('o', 'u'))]
    del combinations[combinations.index(('o', 'o'))]

    for pair in combinations:
        comb = pair[0] + pair[1]
        if comb in word:
            return word, 2, True

    # unrespected palatalization
    palatal_vowels = 'eéií'
    for pair in list(it.product(('k', 'h', 'ch', 'r'), palatal_vowels)):
        comb = pair[0] + pair[1]
        if comb in word:
            return word, 3, True

    # unrespected soft and hard consonants
    hard_consonants = ('h', 'ch', 'k', 'r')
    for pair in list(it.product(hard_consonants, 'ií')):
        comb = pair[0] + pair[1]
        if comb in word:
            return word, 4, True

    soft_consonants = 'žščřcj'
    for pair in list(it.product(soft_consonants, 'yý')):
        comb = pair[0] + pair[1]
        if comb in word:
            return word, 5, True

    # unrespected y followed by mixed consonants (b, l, m, p, s, v, z)
    vowels_long = 'áéíýůú'
    vowels_all = 'aeiyouáéěíýůú'

    all_patterns = {'by': ['byt', 'byl', 'aby', 'kdyby', 'čby', 'bych',
                           'bys@', 'byste', 'byv', 'bydl', 'byč', 'byst',
                           'bysl'],

                    'ly': ['slyš', 'mlyn', 'lyka', 'lyká', 'plyn', 'vzlyk',
                           'lysý', 'lysi', 'lyso', 'lysic', 'lyž', 'lyň',
                           'plyš'],

                    'my': ['myd', 'myt', 'myč', 'myc', 'myj', 'mysl', 'myšl',
                           'myl', 'hmyz', 'myš', 'myk', 'mych'],

                    'py': ['pych', 'pyt', 'pyl', 'pysk', 'pyka', 'pyká'],

                    'sy': ['syn@', 'synVA', 'sysl', 'syse', 'sytVA', 'syt@',
                           'syre', 'syro', 'sychr', 'sycha', 'syč', 'syk',
                           'syp'],

                    'vy': ['vys', 'vyš', 'vyk', 'vyd', 'vyž', '#vy'],

                    'zy': ['brzy', 'jazyk', 'jazyl', 'zýv']}

    for name, patterns in all_patterns.items():
        checked = word
        if checked.endswith('y'):
            checked = checked[:-1]

        for pattern in patterns:
            if 'VD' in pattern:  # long vowel insted 'VD'
                for letter in vowels_long:
                    checked = checked.replace(pattern[:-2] + letter, '$')
            elif 'VA' in pattern:  # vowel instead 'VA'
                for letter in vowels_all:
                    checked = checked.replace(pattern[:-2] + letter, '$')
            elif '@' in pattern:  # word ends with this pattern
                if checked.endswith(pattern[:-1]):
                    checked = checked[:-len(pattern)-1]
            elif '#' in pattern:  # word starts with this pattern
                if checked.startswith(pattern[1:]):
                    checked = checked[len(pattern[1:]):]
            else:
                checked = checked.replace(pattern, '$')

        if name in checked:
            return word, 6, True

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
        return word, 7, True

    # ends with long vowel or consists of 'ú' inside
    vowels_long = 'áéóůú'
    for letter in vowels_long:
        if word.endswith(letter):
            return word, 8, True

    if 'ú' in word[1:]:
        return word, 9, True

    # foreign morphemes
    # TODO: increase accuracy (add derivations as 'áž-ní', 'áž-ně';
        # check short pre-/suf-fixes; segmentation); invent testing data
        # and evaluate (preccision, recall, F1 score)
    suffixes = ['áž', 'ce', 'en', 'én', 'er', 'ér', 'ie', 'ik', 'in', 'ín',
                'ns', 'on', 'ón', 'or', 'oř', 'os', 'sa', 'se', 'ta', 'um',
                'us', 'za', 'ze', 'ace', 'ant', 'bal', 'bus', 'ent', 'eus',
                'fil', 'fob', 'for', 'ice', 'ida', 'ika', 'ina', 'ína', 'ing',
                'ink', 'ism', 'ita', 'log', 'man', 'men', 'nom', 'ona', 'óna',
                'tel', 'tor', 'una', 'úna', 'ura', 'úra', 'urg', 'ální',
                'álný', 'ánní', 'ánný', 'ární', 'árný', 'átní', 'átný',
                'átor', 'énní', 'énný', 'erie', 'érie', 'érní', 'érný',
                'ézní', 'ézný', 'ický', 'ilní', 'ilný', 'ista', 'itor',
                'ivní', 'ívní', 'ivný', 'ívný', 'orní', 'orný', 'ózní',
                'ózný', 'stor', 'teka', 'téka', 'tura', 'antní', 'antný',
                'asmus', 'atura', 'bilní', 'bilný', 'dozer', 'entní', 'entný',
                'eskní', 'eskný', 'esmus', 'fobie', 'iální', 'iálný', 'ismus',
                'itura', 'izace', 'izmus', 'logie', 'vální', 'válný',
                'fikace', 'írovat', 'izovat', 'ýrovat', 'ebilita', 'ekalita',
                'ibilita', 'ikalita']

    prefixes = ['ab', 'an', 'bi', 'de', 'di', 'em', 'en', 'ex', 'im',
                'in', 'ko', 're', 'ana', 'ant', 'apo', 'des', 'dez', 'dia',
                'dis', 'dys', 'epi', 'kom', 'kon', 'non', 'par', 'per', 'pre',
                'pro', 'sub', 'sur', 'aero', 'ante', 'anti', 'arci', 'fero',
                'foto', 'hypo', 'kata', 'kino', 'maxi', 'meta', 'mini',
                'para', 'tele', 'gramo', 'hyper', 'infra', 'inter', 'intra',
                'intro', 'makro', 'mikro', 'radio', 'rádio', 'super', 'supra',
                'tacho', 'trans', 'ultra', 'kontra', 'pseudo', 'techno',
                'elektro', 'magneto']

    for suffix in suffixes:
        if word.endswith(suffix):
            if len(word.replace(suffix, '')) > 2:
                return word, 10, True

    for prefix in prefixes:
        if word.startswith(prefix):
            if len(word.replace(prefix, '')) > 2:
                return word, 11, True

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

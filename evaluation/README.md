# Evaluation of script for the RFW in the Czech language
This part of the repository contains scripts and brief tutorial for evaluation of implemented rule-based script for recognition of foreign words in the Czech language.

## Creating of evaluation data
The evaluation data comes from the corpus [SYN2015](http://wiki.korpus.cz/doku.php/en:cnk:syn2015) Czech National Corpus (ČNK).

1. This corpus is downloadable [here](http://hdl.handle.net/11234/1-1593) after confirmation of the (academic non-commercial) license.
2. The list of word forms with their lemmatization, tag and frequency was created by running shell script:
```bash
zgrep -v '^<' 'syn2015.gz' | cut -d $'\t' -f 1,2,3 | sort | uniq -c | sort -nr > 'word-list.tsv'
```
3. The list of lemmas with their frequency was created. Propriums, interpunctions, abbreviations, numbers and lemmas containing punctuation were removed from the list of lemmas. From this list, the random sample according to four intervals (by frequencies of lemmas) was generated. Intervals were: *1-2*, *3-10*, *11-100*, *101-max*. Two hundred and fifty lemmas were randomly chosen from each interval, so the evaluation data consists of 1 thousand lemmas. This all was processed by running python script:
```python
python3 prep-data.py 'data/word-list.tsv' 'data/eval-data-for-annot.tsv'
```
5. After that, the manual parallel annotation was made (**+** in the first column means foreign word). First annotator *a1* had no linguistic background (except traditional language courses at the secondary school). Second annotator *a2* had the linguistic background. Both annotated data are available in `data/eval-data-annot-a1.tsv` and `data/eval-data-annot-a2.tsv`.

## Evaluation
The measurement of [Precision and Recall](https://en.wikipedia.org/wiki/Precision_and_recall) (and recalculating them to [F1 score](https://en.wikipedia.org/wiki/F1_score)) was used for evaluation of implemented recognition of foreign words.
```bash
python3 -B evaluate.py 'data/eval-data-annot-a1.tsv'
python3 -B evaluate.py 'data/eval-data-annot-a2.tsv'
```

## Results
The automatic recognition of foreign words in the Czech language achieved around 80% success.
| Gold data     | `eval-data-annot-a1.tsv`  | `eval-data-annot-a2.tsv`  |
| :---          | :---                      | :---                      |
| Compared to   | `recogFW.py`              | `recogFW.py`              |
| Prec          | 0.809                     | 0.858                     |
| Rec           | 0.7938388625592417        | 0.7962085308056872        |
| **F1**        | **0.8013477272256867**    | **0.8259501830746223**    |
| ---           | ---                       | ---                       |
| Size of data  | 1000                      | 1000                      |
| True-Posit    | 335                       | 336                       |
| True-Negat    | 104                       | 56                        |
| False-Posit   | 474                       | 522                       |
| False-Negat   | 87                        | 86                        |

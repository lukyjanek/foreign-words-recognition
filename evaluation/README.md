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
```bash
python3 prep-data.py 'data/word-list.tsv' 'data/eval-data-for-annot.tsv'
```

4. After that, the manual parallel annotation was made (**+** in the first column means foreign word). First annotator *a1* had no linguistic background (except traditional language courses at the secondary school). Second annotator *a2* had the linguistic background. Both annotated data are available in `data/eval-data-annot-a1.tsv` and `data/eval-data-annot-a2.tsv`.

## Evaluation
First, the inter-annotator agreement (so called [Cohens's kappa](https://en.wikipedia.org/wiki/Cohen%27s_kappa)) was measured to compare parallel annotations.
```bash
python3 inter-annotator.py 'data/eval-data-annot-a1.tsv' 'data/eval-data-annot-a2.tsv'
```

Second, the measurement of [Precision and Recall](https://en.wikipedia.org/wiki/Precision_and_recall) (and recalculating them to [F1 score](https://en.wikipedia.org/wiki/F1_score)) was used for evaluation of implemented recognition of foreign words.
```bash
python3 -B evaluate.py 'data/eval-data-annot-a1.tsv'
python3 -B evaluate.py 'data/eval-data-annot-a2.tsv'
```

## Results
The inter-annotator agreement achieved 76 % success. It corresponds to the linguistic theory that the foreign words vary for each annotator, but there still exists the certain degree of compliance between annotators.

| | |
| --- | --- |
| Data 1 | data/eval-data-annot-a1.tsv |
| Data 2 | data/eval-data-annot-a2.tsv |
| **Cohen's kappa** | **0.760027566064206** |

The automatic recognition of foreign words in the Czech language achieved around 80 % success.

| Gold data | `eval-data-annot-a1.tsv` | `eval-data-annot-a2.tsv` |
| :--- | :--- | :--- |
| Compared to | `recogFW.py` | `recogFW.py` |
| Prec | 0.8428927680798005 | 0.85785536159601 |
| Rec | 0.7699316628701595 | 0.864321608040201 |
| **F1** | **0.8047619047619047** | **0.8610763454317897** |
| --- | --- | --- |
| Size of data | 1000 | 1000 |
| True-Posit | 338 | 344 |
| True-Negat | 498 | 545 |
| False-Posit | 63 | 57 |
| False-Negat | 101 | 54 |

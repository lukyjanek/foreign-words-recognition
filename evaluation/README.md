# Evaluation of script for the RFW in the Czech language
This part of the repository contains scripts and brief tutorial for evaluation of implemented rule-based script for recognition of foreign words in the Czech language in **version 2**.

## Creating of data for evaluation
Data for manual annotation comes from the corpus [SYN2015](http://wiki.korpus.cz/doku.php/en:cnk:syn2015) Czech National Corpus (ČNK). The whole process of obtaining random data is described bellow, but it can be simply processed calling:
```bash
make prepare
```

1. Corpus SYN2015 is downloadable [here](http://hdl.handle.net/11234/1-1593) after confirmation of the (academic non-commercial) license.

2. The list of word forms with their lemmatization, tag and frequency was created by running shell script:
```bash
zgrep -v '^<' 'syn2015.gz' | cut -d $'\t' -f 1,2,3 | sort | uniq -c | sort -nr > 'word-list.tsv'
```

3. The list of lemmas with their frequency was created. Propriums, interpunctions, abbreviations, numbers and lemmas containing punctuation were removed from the list of lemmas. From this list, the random sample according to four intervals (by frequencies of lemmas) was generated. Intervals were according to frequencies of lemmas: *1-2*, *3-10*, *11-100*, *101-max*. 250 lemmas were randomly chosen from each interval, so the data for manual annotations consists of 1 thousand lemmas. This all was processed by running python script:
```bash
python3 prep-data.py 'data/word-list.tsv' 'data/eval-data-for-annot.tsv'
```

# Manual annotation
Two rounds of manual annotations were done.

**First annotation round** was made for final SFG report, so it consists of parallel annotation (**+** in the first column means foreign word) of two annotators *a1* (`data/eval-data-annot-a1.tsv`) and *a2* (`data/eval-data-annot-a2.tsv`). After that, an inter-annotator agreement was measured, both data were merged (`data/gold-data-prep.tsv`) and the annotator *a2* annotated unclear cases (unclear cases are marked by **?**) according to *Nový akademický slovník cizích slov* (Kraus et al., 2005, Praha: Academia). Complete annotated gold data are available in `data/gold-data-prep-annot-a2.tsv`.

**Second annotation round** was made with new versions of script for recognition of foreign words in the Czech language. Annotator *a2* annotated data (**+** in the first column means foreign word). The name of files with data of second annotation round are named `data/eval-data[2,3,4,...]-annot-a2.tsv`.

Annotator *a1* was educated at high school in economics. Annotator *a2* was educated at university in linguistics.

## Evaluation
The whole process of evaluation (described bellow) can be simply processed calling:
```bash
make evaluation
```

Inter-annotator agreement (so called [Cohens's kappa](https://en.wikipedia.org/wiki/Cohen%27s_kappa)) was measured to compare parallel annotations. `data/gold-data-prep.tsv` was created with this measurement.
```bash
python3 inter-annotator.py 'data/eval-data-annot-a1.tsv' 'data/eval-data-annot-a2.tsv' 'data/gold-data-prep.tsv'
```

Measurement of [Precision and Recall](https://en.wikipedia.org/wiki/Precision_and_recall) (and recalculating them to [F1 score](https://en.wikipedia.org/wiki/F1_score)) was used for evaluation of implemented recognition of foreign words.
```bash
python3 -B evaluate.py 'data/eval-data-annot-a1.tsv'
python3 -B evaluate.py 'data/eval-data-annot-a2.tsv'
python3 -B evaluate.py 'data/gold-data-prep-annot-a2.tsv'
python3 -B evaluate.py '[...]'
```

## Results
The inter-annotator agreement for parallel annotations achieved 76 % success. It corresponds to the linguistic theory that the foreign words vary for each annotator, but there still exists the certain degree of compliance between annotators.

| | |
| --- | --- |
| Data 1 | data/eval-data-annot-a1.tsv |
| Data 2 | data/eval-data-annot-a2.tsv |
| **Cohen's kappa** | **0.760027566064206** |

The automatic recognition of foreign words in the Czech language reached an average of 84 % (F1 score) success. Table bellow shows results of all evaluated files.

| Annotated data | `eval-data-annot-a1.tsv` | `eval-data-annot-a2.tsv` | `data/gold-data-prep-annot-a2.tsv` | `data/eval-data2-annot-a2.tsv` |
| :--- | :--- | :--- | :--- | :--- |
| Compared to | `recogFW.py` | `recogFW.py` | `recogFW.py` | `recogFW.py` |
| Prec | 0.83871 | 0.85608 | 0.86352 | 0.83416 |
| Rec | 0.76993 | 0.86683 | 0.86352 | 0.87760 |
| **F1** | **0.80285** | **0.86142** | **0.86352** | **0.85533** |
| --- | --- | --- | --- | --- |
| Size of data | 1000 | 1000 | 1000 | 1000 |
| True-Posit | 338 | 345 | 348 | 337 |
| True-Negat | 496 | 544 | 542 | 549 |
| False-Posit | 65 | 58 | 55 | 67 |
| False-Negat | 101 | 53 | 55 | 47 |

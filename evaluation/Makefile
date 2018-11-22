SHELL=/bin/bash

syn2015.gz:
	echo 'You need syn2015.gz corpus from Czech National Corpus Institution.'

word-list.tsv: syn2015.gz
	zgrep -v '^<' 'syn2015.gz' | cut -d $$'\t' -f 1,2,3 | sort | uniq -c | sort -nr > 'word-list.tsv'

# create new data for manual annotation
prepare: word-list.tsv
	python3 prep-data.py 'word-list.tsv' 'data/eval-data-for-annot.tsv'

# evaluate all annotated data
evaluation:
	# first round of evaluation (SFG evaluation; without part-of-speech)
	python3 inter-annotator.py 'data/eval-data-annot-a1.tsv' 'data/eval-data-annot-a2.tsv' 'data/gold-data-prep.tsv'
	python3 -B evaluate.py 'data/eval-data-annot-a1.tsv'
	python3 -B evaluate.py 'data/eval-data-annot-a2.tsv'
	python3 -B evaluate.py 'data/gold-data-prep-annot-a2.tsv'
	# second round of evaluation (several others manualy annotated [by one person] data; with part-of-speech)
	python3 -B evaluate.py 'data/eval-data2-annot-a2.tsv'

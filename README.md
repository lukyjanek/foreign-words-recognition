# Recognition of foreign words in the Czech language
This repository contains codes of rule-based approach to the recognition of foreign words in the Czech language. Used rules are based on the study of so far published linguistic papers.

*Supported by Student's Faculty Grant (SFG) at [Faculty of Mathematics and Physics, Charles University](https://www.mff.cuni.cz/), in the academic year 2017/2018.*

**Still under construction.**

## Usage
This script can be used both as imported in any project, and as shell script. Bellow, three ways (with examples) how to use this script are described.

**1. Download and import as the function to your Python3 project.**
Allowed part-of-speech tags are: N (*noun*), A (*adjective*), V (*verb*), D (*adverb*). It can be also empty.
```python
from recogFW import recog_foreign_word

statement1 = recog_foreign_word('automatický', 'A')
statement2 = recog_foreign_word('automatický')
print(statement1, statement2)
```
**2. Download and use in the shell pipeline.**
Separator must be *\t*. Allowed part-of-speech tags are: N (*noun*), A (*adjective*), V (*verb*), D (*adverb*). Other (or empty) tags are processed automaticaly as *None*. Each word must be on a separate line.
```bash
echo -e 'automatický\tA' | python3 recogFW.py
echo -e 'automatický' | python3 recogFW.py
cat path-to-file | python3 recogFW.py
```
**3. Download and use in the shell for file only.**
Separator betwen word ang tag must be *\t*. Allowed part-of-speech tags are: N (*noun*), A (*adjective*), V (*verb*), D (*adverb*). Other (or empty) tags are processed automaticaly as *None*. Each word must be on a separate line.
```bash
python3 recogFW.py 'path-to-file'
```

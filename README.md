# Recognition of foreign words in the Czech language
This repository contains codes of rule-based approach to the recognition of borrowed foreign words in the Czech language. Used rules are based on the study of so far published linguistic papers (listed bellow).

--
*Supported by Student's Faculty Grant (SFG) at [Faculty of Mathematics and Physics, Charles University](https://www.mff.cuni.cz/), in the academic year 2017/2018.*

## Usage
This script can be used both as imported in any project, and as shell script. Bellow, three ways (with examples) how to use this script are described.

**1. Download and import as the function to your Python3 project.**
Given word must be lemmatized.
```python
from recogFW import recog_foreign_word

statement1 = recog_foreign_word('automatický')
print(statement1)
```

**2. Download and use in the shell pipeline.**
Given word must be lemmatized. If you want to use this way for more words, each word must be on a separate line.
```bash
echo -e 'automatický' | python3 recogFW.py
cat 'path-to-input-file' | python3 recogFW.py > 'results.tsv'
```

**3. Download and use in the shell for file only.**
Given word must be lemmatized. Each word must be on a separate line.
```bash
python3 recogFW.py 'path-to-input-file' > 'results.tsv'
```

## Based on these studies and resources
- POGNAN, Patrice. **Une reconnaissance automatique des mots étrangers dans les textes scientifiques**: Un essai en langue tchéque. The Prague Bulletin of Mathematical Linguistics. Prague: Charles University, 1983, 40(1), 31-42. ISSN 0032-6585.
- DOKULIL, Miloš & Jaroslav KUCHAŘ. **Slovotvorná charakteristika cizích slov**. Naše řeč. Prague: Czech Language Institute, Academy of Science, 1977, 60(4), 196-185. ISSN 2571-0893.
--
- **Mluvnice češtiny 1**: *Fonetika, fonologie, morfonologie a morfematika, tvoření slov*. Prague: Academia, 1986.
- **Mluvnice češtiny 2**: *Tvarosloví*. Prague: Academia, 1986.
- MARTINCOVÁ, Olga & Nikolaj SAVICKÝ. **Hybridní slova a některé obecné otázky neologie**.  *Slovo a slovesnost*. Prague: Czech Language Institute, Academy of Science, 1987,  48(2), 124-139. ISSN 0037-7031.
- MEJSTŘÍK, Vladimír. **Tzv. hybridní složeniny a jejich stylová platnost**.  *Naše řeč*. Prague: Czech Language Institute, Academy of Science, 1965,  48(1), 1-15. ISSN 0027-8203.
- MRAVINACOVÁ, Jitka. **Přejímání cizích lexémů**. MARTINCOVÁ, Olga, ed.  *Neologizmy v dnešní češtině*. Prague: Czech Language Institute, Academy of Science, 2005, s. 187-211. ISBN 80-200-0607-9.
- MARTINCOVÁ, Olga. **Internacionalizace**. KARLÍK, Petr, Marek NEKULA a Jana PLESKALOVÁ, ed. *Nový encyklopedický slovník češtiny*. Prague: NLN, Nakladatelství Lidové noviny, 2016. ISBN 978-80-7422-482-9.
- MARTINCOVÁ, Olga. **Prefixoid**. KARLÍK, Petr, Marek NEKULA a Jana PLESKALOVÁ, ed.  *Nový encyklopedický slovník češtiny*. Prague: NLN, Nakladatelství Lidové noviny, 2016. ISBN 978-80-7422-482-9.
- MARTINCOVÁ, Olga. **Sufixoid**. KARLÍK, Petr, Marek NEKULA a Jana PLESKALOVÁ, ed.  *Nový encyklopedický slovník češtiny*. Prague: NLN, Nakladatelství Lidové noviny, 2016. ISBN 978-80-7422-482-9.
- NEKULA, Marek. **Adaptace výpůjček**. KARLÍK, Petr, Marek NEKULA a Jana PLESKALOVÁ, ed.  *Nový encyklopedický slovník češtiny*. Prague: NLN, Nakladatelství Lidové noviny, 2016. ISBN 978-80-7422-482-9.
- NEKULA, Marek. **Hierarchie výpůjček**. KARLÍK, Petr, Marek NEKULA a Jana PLESKALOVÁ, ed.  *Nový encyklopedický slovník češtiny*. Prague: NLN, Nakladatelství Lidové noviny, 2016. ISBN 978-80-7422-482-9.
- NEKULA, Marek. **Výpůjčka (přejímka)**. KARLÍK, Petr, Marek NEKULA a Jana PLESKALOVÁ, ed.  *Nový encyklopedický slovník češtiny*. Prague: NLN, Nakladatelství Lidové noviny, 2016. ISBN 978-80-7422-482-9.
- PRAVDOVÁ, Markéta & Ivana SVOBODOVÁ, ed.  **Akademická příručka českého jazyka**. Prague: Academia, 2014. ISBN 978-80-200-2327-8.
--
- KŘEN, Michal, Václav CVRČEK, Tomáš ČAPKA, et al.  **SYN2015**: *reprezentativní korpus psané češtiny*. Prague: Ústav Českého národního korpusu FF CUNI, 2015.
- VIDRA, Jonáš, Zdeněk ŽABOKRTSKÝ, Magda ŠEVČÍKOVÁ, et al.  **DeriNet**: *Word-Formation Network for Czech*. Prague: Institute of Formal and Applied Linguistics, MFF CUNI, 2017.

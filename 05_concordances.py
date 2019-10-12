# -*- coding: utf-8 -*-
"""
Kitconc examples
@author: jlopes@usp.br
"""
from kitconc.kit_corpus import Corpus 
corpus = Corpus('kitconc-examples/workspace','ads','english')
concordances = corpus.concordance('experience',show_progress=True)
print(concordances.df.head(10))
concordances.save_excel(corpus.output_path + 'concordances.xlsx',highlight='R1 R2 R3')
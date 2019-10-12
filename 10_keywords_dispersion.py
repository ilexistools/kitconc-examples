# -*- coding: utf-8 -*-
"""
Kitconc examples
@author: jlopes@usp.br
"""
from kitconc.kit_corpus import Corpus 
corpus = Corpus('kitconc-examples/workspace','ads','english')
wordlist = corpus.wordlist(show_progress=True)
keywords = corpus.keywords(wordlist,show_progress=True)
keywords_dispersion = corpus.keywords_dispersion(keywords,show_progress=True)
print(keywords_dispersion.df.head(10))
keywords_dispersion.save_excel(corpus.output_path+'keywords_dispersion.xlsx')
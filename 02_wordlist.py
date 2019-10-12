# -*- coding: utf-8 -*-
"""
Kitconc examples
@author: jlopes@usp.br
"""
from kitconc.kit_corpus import Corpus 
# reference to the corpus
corpus = Corpus('kitconc-examples/workspace','ads','english')
# make wordlist
wordlist = corpus.wordlist(show_progress=True)
# print the top 10 
print(wordlist.df.head(10))
# save Excel file
wordlist.save_excel(corpus.output_path + 'wordlist.xlsx') 

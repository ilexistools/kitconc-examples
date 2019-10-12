# -*- coding: utf-8 -*-
"""
Kitconc examples
@author: jlopes@usp.br
"""
from kitconc.kit_corpus import Corpus 
corpus = Corpus('kitconc-examples/workspace','ads','english')
collocates = corpus.collocates('skills',left_span=3,right_span=3,coll_pos='NN JJ',show_progress=True)
print(collocates.df.head(10))
collocates.save_excel(corpus.output_path + 'collocates.xlsx')
# plot collocates
collocates.plot_collgraph(node='skills')
# -*- coding: utf-8 -*-
"""
Kitconc examples
@author: jlopes@usp.br
"""
from kitconc.kit_corpus import Corpus 
# reference to the corpus
corpus = Corpus('kitconc-examples/workspace','ads','english')
# add texts from source folder
corpus.add_texts('kitconc-examples/ads',show_progress=True)
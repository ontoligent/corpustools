#! /usr/bin/env python

from poloCorpus import *

# Get the source fille
src_file = 'projects/demo/corpus/corpus.csv'

# Get the destination db
dst_db = 'projects/demo/corpus/demo-default-corpus.db'

# Get the dictfilecho
dictfile = None

pc = PoloCorpus(src_file,dst_db)
pc.produce()
pc.update_word_freqs()
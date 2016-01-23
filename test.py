#! /usr/bin/env python

from poloCorpus import *

# Get the source fille
# Get the destination db
# Get the dictfilecho

src_file = 'projects/demo/corpus/corpus.csv'
dst_db = 'projects/demo/corpus/demo-default-corpus.db'
dictfile = None

# Make sure the above resources exist before calling object

pc = PoloCorpus(src_file,dst_db)
pc.produce()
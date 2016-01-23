#! /usr/bin/env python

from poloCorpus import *

project = 'neuromancer'
# Get the source fille
src_file = 'projects/{}/corpus/corpus.csv'.format(project)

# Get the destination db
dst_db = 'projects/{0}/corpus/{0}-corpus.db'.format(project)

# Get the dictfilecho
dictfile = None

pc = PoloCorpus(src_file,dst_db)
pc.produce()
pc.update_word_freqs()
pc.update_word_stems()
pc.pull_corpus_as_words()
#print(pc.doc_words)
pc.insert_bigrams()

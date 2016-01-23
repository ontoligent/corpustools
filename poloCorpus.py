from corpus import Corpus

'''
This corpus subclass expects to find a comma-delimitted corpus file
with three columns -- a unique doc_id, a doc_tag, and doc_content 
'''

class PoloCorpus(Corpus):
    
    def __init__(self,src_file,dst_db,dictfile=None):
        self.src_file = src_file
        Corpus.__init__(self,dst_db,dictfile)

    def src_doc_generator(self):
        with open(self.src_file) as src:
            for line in src.readlines():
                (doc_id,doc_label,doc_content) = line.split(',')
                yield doc_content.strip().lower()

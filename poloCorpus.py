from corpus import Corpus

class PoloCorpus(Corpus):

    def __init__(self,src_file,dst_db,dictfile):
        Corpus.__init__(self,dst_db,dictfile)

    def src_doc_generator(self):
        with open(src_file) as src:
            for line in src.readlines():
                yield line[2]

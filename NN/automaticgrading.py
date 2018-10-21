import numpy as np
import random
import re 
import nltk
import pandas as pd
text = open("/Users/savita/Desktop/computeCost.txt","r") 

file_contents = text.read()

nltk.download('punkt')

clean_text = re.sub(r'%(.*)\n','',file_contents)
clean_text = re.sub(r'\s+',' ',clean_text)

words = nltk.word_tokenize(clean_text)
n=5
ngrams ={}
for i in range(len(words)-n):
    gram =' '.join(words[i:i+n])
    if gram not in ngrams.keys():
        ngrams[gram] = []
    ngrams[gram].append(words[i+n])
    
from gensim import corpora
from gensim.models import TfidfModel
from gensim.models import LsiModel
from gensim.similarities import MatrixSimilarity

dictionary = corpora.Dictionary(clean_text)
corpus_gensim = [dictionary.doc2bow(doc) for doc in clean_text]
tfidf_text= TfidfModel(corpus_gensim)
corpus_tfidf_text = tfidf_text[corpus_gensim]
lsi_text = LsiModel(corpus_tfidf_text,
                        id2word=dictionary, num_topics=10)
lsi_index_text = MatrixSimilarity(lsi_text[corpus_tfidf_text])
sims['clean_text']['LSI'] = np.array([lsi_index_text[lsi_text[corpus_tfidf_text[i]]]
                                    for i in range(len(clean_text))])

    
    
    
    
    
    
    
    
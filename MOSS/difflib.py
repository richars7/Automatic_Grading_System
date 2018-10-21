import numpy as np
import re 
import nltk
import pandas as pd
import difflib

text1 = open("/Users/savita/Desktop/computeCost.txt","r") 
text2 = open("/Users/savita/Desktop/gradientDescent.txt","r") 
file_contents1 = text1.read()
file_contents2 = text2.read()

clean_text1 = re.sub(r'%(.*)\n','',file_contents1)
clean_text1 = re.sub(r'\s+',' ',clean_text1)

clean_text2 = re.sub(r'%(.*)\n','',file_contents2)
clean_text2 = re.sub(r'\s+',' ',clean_text2)

seq=difflib.SequenceMatcher(None,clean_text1,clean_text2)

d=seq.ratio()*100
print(d)

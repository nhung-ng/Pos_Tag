from PosT import *
import re
import random
from sklearn.model_selection import train_test_split
import sklearn_crfsuite
from sklearn_crfsuite import scorers
from sklearn_crfsuite import metrics
#sent2label()
def sent2labels(sent):
    return [label for token, label in sent]
#process
sentences=[]
data=open('data.txt','r',encoding="utf-8")
for line in data:
    sentence=[]
    line=line.strip()
    line=re.sub(r"_+", "_", line)
    if not line:
        continue
    tokens = line.strip().split(" ")
    try:
        for token in tokens:
            if token.startswith("//"):
                word = "/"
                tag = token[2:]
            else:
                word, tag = token.split("/")
            word = word.replace("_", " ")
            sentence.append([word, tag])
    except:
        continue
    sentences.append(sentence)

datas=[sent2features(sent,True) for sent in sentences]
labels=[sent2labels(sent) for sent in sentences]

X_train,X_test,y_train,y_test=train_test_split(datas,labels,test_size=0.2,random_state=42)

assert len(X_train) == len(y_train)
assert len(X_test) == len (y_test)

print("Number of Data: ",len(datas))
print("Number of X_train, X_test: ",len(y_train), "/",len(y_test))

##############


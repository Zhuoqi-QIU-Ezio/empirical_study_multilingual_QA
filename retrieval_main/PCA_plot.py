#!/usr/bin/env python
# coding=utf-8
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from gensim.models import word2vec
# load the word2vec model
model = word2vec.Word2Vec.load('/ANU_project/question_retrieval_tool/body_model/mymodel30000000')
rawWordVec = model.v

# reduce the dimension of word vector
X_reduced = PCA(n_components=2).fit_transform(rawWordVec)

# show some word(center word) and it's similar words
index1,metrics1 = model.most_similar_cosmul('image')
index2,metrics2 = model.most_similar_cosmul('javascript')
index3,metrics3 = model.most_similar_cosmul('python')
index4,metrics4 = model.most_similar_cosmul('tuple')
index5,metrics5 = model.most_similar_cosmul('c')

# add the index of center word
index01=np.where(model.vocabulary=='image')
index02=np.where(model.vocabulary=='javascript')
index03=np.where(model.vocabulary=='python')
index04=np.where(model.vocabulary=='tuple')
index05=np.where(model.vocabulary=='c')

index1=np.append(index1,index01)
index2=np.append(index2,index03)
index3=np.append(index3,index03)
index4=np.append(index4,index04)
index5=np.append(index5,index05)

# plot the result
zhfont = matplotlib.font_manager.FontProperties(fname='/usr/share/fonts/truetype/wqy/wqy-microhei.ttc')
fig = plt.figure()
ax = fig.add_subplot(111)

for i in index1:
    ax.text(X_reduced[i][0],X_reduced[i][1], model.vocabulary[i], fontproperties=zhfont,color='r')

for i in index2:
    ax.text(X_reduced[i][0],X_reduced[i][1], model.vocabulary[i], fontproperties=zhfont,color='b')

for i in index3:
    ax.text(X_reduced[i][0],X_reduced[i][1], model.vocabulary[i], fontproperties=zhfont,color='g')

for i in index4:
    ax.text(X_reduced[i][0],X_reduced[i][1], model.vocabulary[i], fontproperties=zhfont,color='k')

for i in index5:
    ax.text(X_reduced[i][0],X_reduced[i][1], model.vocabulary[i], fontproperties=zhfont,color='c')

ax.axis([0,0.8,-0.5,0.5])
plt.show()
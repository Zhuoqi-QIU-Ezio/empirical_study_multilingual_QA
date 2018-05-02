from gensim.models import word2vec
import gensim
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# sentences = word2vec.Text8Corpus('/ANU_project/question_retrieval_tool/en_title_trainset_utf8')
# model = word2vec.Word2Vec(sentences, size=200, iter=10)
# model.save('/ANU_project/question_retrieval_tool/en_title_model/en_title.model')
# print('model1 trained DONE')
#
# sentences_ste = word2vec.Text8Corpus('/ANU_project/question_retrieval_tool/en_title_trainset_utf8_ste')
# model2 = word2vec.Word2Vec(sentences_ste, size=200, iter=10)
# model2.save('/ANU_project/question_retrieval_tool/en_title_ste_model/en_title.model')
# print('model2 trained DONE')
#
model = word2vec.Word2Vec.load('/ANU_project/question_retrieval_tool/body_model/mymodel30000000')
#model = word2vec.Word2Vec.load('/ANU_project/question_retrieval_tool/en_title_ste_model/en_title.model')
print(model.most_similar('javascript'))
print(model.most_similar('c'))
print(model.most_similar('code'))
print(model.most_similar('algorithm'))
print(model.most_similar('image'))
print(model.most_similar('bug'))
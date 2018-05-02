import pickle
from nltk.stem import SnowballStemmer


f0 = open("D://ANU_project//question_retrieval_tool//test_dataset//python_test_title_utf8_ste", "r", encoding='utf-8')
line = f0.readline()
a = 1
while line:
    line = f0.readline()
    a += 1
print(a)
f0.close()
#
# fuck
# print('\n')
# print(':::RESULT on TAG:::')
# print('---------------------------------------------------------------------')
# print('TAG || Test_pairs_num || Corpus_size || ACC(rel_value in top10) || words>4_ACC ')
# print('android | 573 | 892361 | 19.72% | 12.04%')
# print('c# | 327 | 979276 | 26.91% | 29.36% ')
# print('java | 315 | 1142565 | 17.74% | 23.49% ')
# print('javascript | 231 | 1301125 | 21.65% | 14.29% ')
# print('php | 192 | 969791 | 35.42% |  31.77% ')


# snowball_stemmer = SnowballStemmer('english')
# stop_ws = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']
# # stop_ws_ste = []
# # for item3 in stop_ws:
# #     stop_ws_ste.append(snowball_stemmer.stem(item3))
# # print(stop_ws_ste)
# sentence = "this is a foo bar sentence!?"
# sentence = [i for i in sentence.lower().split() if i not in stop_ws]
# print(sentence)



# f0 = open("D://ANU_project//question_retrieval_tool//en_title_data_utf8", "r", encoding='utf-8')
# target_titles = f0.readlines()
# print('load target titles data successfully')
# titles_list = []
# a = 0
# for line in target_titles:
#     line = line.replace('\r\n', '')
#     line = line.replace('\n', '')
#     line = line.replace('?', '')
#     line = line.replace(';', '')
#     line = line.replace(':', '')
#     line = line.replace(',', '')
#     line = line.replace('!', '')
#     line = line.replace('-', '')
#     words = line.split(' ')
#     titles_list.append(words)
#     a += 1
#     # if a > 15:
#     #     break

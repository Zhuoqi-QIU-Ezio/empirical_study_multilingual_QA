import requests
import time
import hashlib
import json
from nltk.stem import SnowballStemmer
from gensim.models import word2vec
# import string
# import gensim


import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# ######### init ##############################

# set up Baidu translation logging info.
api_url = "http://api.fanyi.baidu.com/api/trans/vip/translate"   # baidu developer account
my_appid = '20180311000134261'
cyber = 'Yp3vRSB_0_HjSuikUA3n'

# choose word2vec model
# model = word2vec.Word2Vec.load('/ANU_project/question_retrieval_tool/en_title_model/en_title.model')
model = word2vec.Word2Vec.load('/ANU_project/question_retrieval_tool/en_title_ste_model/en_title.model')
# model = word2vec.Word2Vec.load('/ANU_project/question_retrieval_tool/body_model/mymodel30000000')   #  use body trained model

# loading the query list, corpus and model
#fq_path = "D://ANU_project//question_retrieval_tool//test_dataset//python_test_query_utf8"
#fq_path = "D://ANU_project//question_retrieval_tool//ru_python_scorehigh_query"
fq_path = "D://ANU_project//question_retrieval_tool//ru_python_scorehigh_query_2"
f_ori_path = "D://ANU_project//question_retrieval_tool//test_dataset//python_test_title_utf8"

f_tran_path = "D://ANU_project//question_retrieval_tool//test_dataset//python_test_title_utf8_ste"  # when use ste model
# f_tran_path = "D://ANU_project//question_retrieval_tool//test_dataset//python_test_title_utf8"    # when use non-ste model

#flog_path = "D://ANU_project//question_retrieval_tool//test_dataset//python_test_log_2"

# pre-checked diff dataset to save memo
# total_titles = 14987178     # all title
# total_titles = 892361  # android only
total_titles = 779370    # python only

# result_show_num_control
show_top = 10

# symbol operation and stopwords list
remove_list = ['\r\n', '\n', '&quot;', ';', ',', '-', '?', ':']
isolate_list = ['=', '*', '{', '}', '[', ']', '&', '$', '.', '!', '/', '\\', '(', ')', "'"]
stop_ws = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']
# stop_ws_ste = ['ourselv', 'her', 'between', 'yourself', 'but', 'again', 'there', 'about', 'onc', 'dure', 'out', 'veri', 'have', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'it', 'your', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselv', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'abov', 'both', 'up', 'to', 'our', 'had', 'she', 'all', 'no', 'when', 'at', 'ani', 'befor', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'doe', 'yourselv', 'then', 'that', 'becaus', 'what', 'over', 'whi', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'onli', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'be', 'if', 'their', 'my', 'against', 'a', 'by', 'do', 'it', 'how', 'further', 'was', 'here', 'than']

print(':::INFO:::initial process executed successfully')

# ############# function: call the baidu translate API #################################


def requests_for_dst(word):
    # init salt and final_sign
    salt = str(time.time())[:10]
    final_sign = str(my_appid) + word + salt + cyber
    final_sign = hashlib.md5(final_sign.encode("utf-8")).hexdigest()
    paramas = {                                             # baidu translate parameters
                 'q': word,
                 'from': 'ru',
                 'to': 'en',
                 'appid': '%s' % my_appid,
                 'salt': '%s' % salt,
                 'sign': '%s' % final_sign
             }

    response = requests.get(api_url, params=paramas).content
    content = str(response, encoding="utf-8")
    json_reads = json.loads(content)
    #print(':::INFO:::translated_query --- %s' % json_reads['trans_result'][0]['dst'])
    return json_reads['trans_result'][0]['dst']   # return translated query in english

# ###########  main process starts #########################

# while True:                  # manual input
# ru_query = input("please type your query (russian): ")


fq = open(fq_path, "r", encoding='utf-8')
#flog = open(flog_path, "a+", encoding='utf-8')

query_count = 0  # show how many query has been processed

all_both_query = fq.readlines()
break_point = 96  # starting from this point if suffered break before

for both_query in all_both_query:
    query_count += 1

    if query_count < break_point:  # jump to break point
        continue

    f_ori = open(f_ori_path, "r", encoding='utf-8')
    f_tran = open(f_tran_path, "r", encoding='utf-8')

    both_query = both_query.replace('\n', '')
    query = both_query.split('\t')[0].replace('\n', '')
    #answer = both_query.split('\t')[1].replace('\n', '')

    ru_query = query
    print(':::INFO:::original_query --- %s' % ru_query)

    translated = requests_for_dst(ru_query)
    tran_q = requests_for_dst(ru_query)      # call translate function
    print(':::INFO:::translated_query --- %s' % tran_q)
    tran_q = tran_q.lower()                  # lower the str

    #  remove noise symbols
    for item1 in remove_list:
        tran_q = tran_q.replace(item1, ' ')

    # isolate non-english symbols
    for item2 in isolate_list:
        tran_q = tran_q.replace(item2, ' %s ' % item2)

    q_terms = tran_q.split()

    # remove stop_words
    q_terms = [i for i in q_terms if i not in stop_ws]

    # stemming ################################################
    snowball_stemmer = SnowballStemmer('english')
    q_terms_ste = []
    for item in q_terms:
        q_terms_ste.append(snowball_stemmer.stem(item))

    # ########### n^2 loop matching ###########################

    #q_terms_final = q_terms      # switch on ste or not
    q_terms_final = q_terms_ste

    print(':::INFO:::input query terms list is as following')
    print(q_terms_final)

    # initial final result lists
    top_title_rel_value_list = []
    top_title_list = []
    top_limit = 0
    line_check = 0

    print(':::INFO:::start matching on query %d' % query_count)

    title_ori = f_ori.readline()
    title_tran = f_tran.readline()

    while title_tran:

        title_ori = title_ori.replace('\n', '')
        title_terms = title_tran.split()

        q_word_rel_values = []
        final_qt_rel_value = 0

        for word1 in q_terms_final:

            qt_word_rel_values = []

            for word2 in title_terms:

                try:
                    c_simi = model.similarity(word1, word2)  # use model to calculate similarity
                except KeyError:                             # if checking word is not in vocabulary then set similarity to 0
                    c_simi = 0

                qt_word_rel_values.append(c_simi)

            q_word_rel_values.append(max(qt_word_rel_values))

        final_qt_rel_value = sum(q_word_rel_values)

        if top_limit < show_top:
            top_title_rel_value_list.append(final_qt_rel_value)
            top_title_list.append(title_ori)
            top_limit += 1
        elif final_qt_rel_value > min(top_title_rel_value_list):
            c_index = top_title_rel_value_list.index(min(top_title_rel_value_list))
            top_title_rel_value_list[c_index] = final_qt_rel_value
            top_title_list[c_index] = title_ori
        elif final_qt_rel_value == min(top_title_rel_value_list):
            top_title_rel_value_list.append(final_qt_rel_value)
            top_title_list.append(title_ori)

        #  progress watching on single matching
        # line_check += 1
        # if line_check % 10000 == 0:  # progress report
        #     print(':::INFO::: %d lines checked' % line_check)
        #     print(':::INFO::: current progress %.2f%%' % (line_check / total_titles * 100))

        title_ori = f_ori.readline()   # continue on next title in corpus
        title_tran = f_tran.readline()

    print(':::INFO:::%d query have been checked $$$$$$$$$$$$$$$$$$$$$' % query_count)

    for i in range(1, show_top + 1):  # control output num
        max_index = top_title_rel_value_list.index(max(top_title_rel_value_list))
        print('RANK:   %d' % i)
        print('TITLE:   %s' % top_title_list[max_index])
        print('Rel_VALUE:   %f' % top_title_rel_value_list[max_index])
        print('------------------------------------------------------')
        del top_title_list[max_index]
        del top_title_rel_value_list[max_index]

    # if answer in top_title_list:
    #     #flog.write('T ')
    #     print(':::RESULT OUUUUUUUUUUUUUUUT::: %d query is ---T--- with link pairs' % query_count)
    # else:
    #     #flog.write('F ')
    #     print(':::RESULT OUUUUUUUUUUUUUUUT::: %d query is ---F--- with link pairs' % query_count)

    f_ori.close()
    f_tran.close()


print(':::INFO:::all query list checked')


# ##### result output #################

# result_limit = len(top_title_rel_value_list)
#
# print('------------------------------------------------------')
# print(':::INFO:::RESULT_OUTPUT')
# print('QUERY:   %s' % ru_query)
# print('TRANSLATED_QUERY:   %s' % translated)
# print('------------------------------------------------------')
# for i in range(1, result_limit):
#     max_index = top_title_rel_value_list.index(max(top_title_rel_value_list))
#     print('RANK:   %d' % i)
#     print('TITLE:   %s' % top_title_list[max_index])
#     print('Rel_VALUE:   %f' % top_title_rel_value_list[max_index])
#     print('------------------------------------------------------')
#     del top_title_list[max_index]
#     del top_title_rel_value_list[max_index]

#!/usr/bin/python
# -*- coding: UTF-8 -*-
from nltk.stem import SnowballStemmer

fo = open("D://ANU_project//question_retrieval_tool//en_title_data_utf8", "rb")
line = fo.readline()
f1 = open("D://ANU_project//question_retrieval_tool//en_title_trainset_utf8", "a+", encoding='utf-8')
f2 = open("D://ANU_project//question_retrieval_tool//en_title_trainset_utf8_ste", "a+", encoding='utf-8')
a = 0
snowball_stemmer = SnowballStemmer('english')
total_titles = 14987178

while line:
    #print(line)
    #print(a)
    line = line.decode('utf-8','ignore')
    line = line.lower()
    #print(line)
    #remove
    remove_list = ['\r\n', '\n', '&quot;', ';', ':', ',', '"']
    for item1 in remove_list:
        line = line.replace(item1, ' ')
    #isolate
    isolate_list = ['=', '*', '{', '}', '[', ']', '&', '$', '?', '.', '!', "'", '/', '\\', '(', ')', '@', '%', '^', '+', '|', '<', '>', '`', '~']
    for item2 in isolate_list:
        line = line.replace(item2, ' %s ' % item2)

    # line = line.replace('     ', ' ')  # remove extra blanks
    # line = line.replace('    ', ' ')
    # line = line.replace('   ', ' ')
    # line = line.replace('  ', ' ')

    l_terms = line.split()
    l_terms_ste = []

    for item3 in l_terms:
        l_terms_ste.append(snowball_stemmer.stem(item3))
    #print(l_terms_ste)

    line_new = ' '.join(l_terms_ste)
    line = ' '.join(l_terms)

    f1.write(line)
    f1.write('\n')
    f2.write(line_new)
    f2.write('\n')
    a += 1
    if a % 10000 == 0:  # progress report
        print(':::INFO::: %d lines checked' % a)
        print(':::INFO::: current progress %.2f%%' % (a / total_titles * 100))
    line = fo.readline()
    #if a > 10:
       #break

print(a)
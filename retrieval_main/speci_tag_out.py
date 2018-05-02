from nltk.stem import SnowballStemmer

# f0 = open("D://ANU_project//question_retrieval_tool//ru_post_repo.txt", "r")
# f1 = open("D://ANU_project//question_retrieval_tool//ru_title_js", "a+")
# line = f0.readline()
# a = 0
# target_tag = 'javascript'
# while line:
#     terms = line.split('\t')
#     title = terms[0]
#     tags = terms[2].lower()
#     tag_list = tags.split('|')
#     if target_tag  in tag_list:
#         content = title + '\t' + tags
#         f1.write(content)
#         f1.write('\n')
#         a += 1
#
#     line = f0.readline()
#
# print(a)

#   ############title and tag out ########

fo = open("D://ANU_project//question_retrieval_tool//en_post_repo.txt", "rb")

line = fo.readline()
f1 = open("D://ANU_project//question_retrieval_tool//en_title+tag_data_utf8", "a+", encoding='utf-8')
f2 = open("D://ANU_project//question_retrieval_tool//en_title+tag_data_utf8_ste", "a+", encoding='utf-8')
a = 0
snowball_stemmer = SnowballStemmer('english')
total_titles = 14987178

while line:
    #print(line)
    #print(a)
    line = line.decode('utf-8','ignore')
    terms = line.split('\t')
    title = terms[0]
    tag = terms[2]
    data = title + '\t' + tag
    data = data.replace('\n','')
    data = data.replace('\r\n','')

    title = title.lower()
    #remove
    remove_list = ['\r\n', '\n', '&quot;', ';', ':', ',', '"']
    for item1 in remove_list:
        title = title.replace(item1, ' ')
    #isolate
    isolate_list = ['=', '*', '{', '}', '[', ']', '&', '$', '?', '.', '!', "'", '/', '\\', '(', ')', '@', '%', '^', '+', '|', '<', '>', '`', '~']
    for item2 in isolate_list:
        title = title.replace(item2, ' %s ' % item2)

    # line = line.replace('     ', ' ')  # remove extra blanks
    # line = line.replace('    ', ' ')
    # line = line.replace('   ', ' ')
    # line = line.replace('  ', ' ')

    l_terms = title.split()
    l_terms_ste = []

    for item3 in l_terms:
        l_terms_ste.append(snowball_stemmer.stem(item3))
    #print(l_terms_ste)

    title_new = ' '.join(l_terms_ste)

    tag_ste_list = []
    tag_list = tag.split('|')
    for item4 in tag_list:
        tag_ste_list.append(snowball_stemmer.stem(item4))

    tag_new = '|'.join(tag_ste_list)

    data_ste = title_new + '\t' + tag_new
    data_ste = data_ste.replace('\n', '')
    data_ste = data_ste.replace('\r\n', '')


    f1.write(data)
    #f1.write('\n')
    f2.write(data_ste)
    #f2.write('\n')
    a += 1
    if a % 10000 == 0:  # progress report
        print(':::INFO::: %d lines checked' % a)
        print(':::INFO::: current progress %.2f%%' % (a / total_titles * 100))
    line = fo.readline()
    # if a > 10:
    #    break

print(a)


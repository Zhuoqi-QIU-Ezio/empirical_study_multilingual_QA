target_tag = 'python'


# make test database #####################################################
f1 = open("D://ANU_project//question_retrieval_tool//en_title+tag_data_utf8", "r", encoding='utf-8')
f2 = open("D://ANU_project//question_retrieval_tool//en_title+tag_data_utf8_ste", "r", encoding='utf-8')
f3 = open("D://ANU_project//question_retrieval_tool//test_dataset//%s_test_title_utf8" % target_tag, "a+", encoding='utf-8')
f4 = open("D://ANU_project//question_retrieval_tool//test_dataset//%s_test_title_utf8_ste" % target_tag, "a+", encoding='utf-8')

a = 0
write_count = 0
line1 = f1.readline()
line2 = f2.readline()
total_titles = 14987178

while line1 and line2:
    tags = line1.split('\t')[1]
    tag_list = tags.split('|')
    if target_tag in tag_list:
        line1_t = line1.split('\t')[0]     # remove the tag
        line2_t = line2.split('\t')[0]
        f3.write(line1_t)
        f3.write('\n')
        f4.write(line2_t)
        f4.write('\n')
        write_count += 1
    line1 = f1.readline()
    line2 = f2.readline()
    a += 1
    if a % 10000 == 0:  # progress report
        print(':::INFO::: %d lines checked' % a)
        print(':::INFO::: current progress %.2f%%' % (a / total_titles * 100))
    # if write_count > 10:
    #     break

f1.close()
f2.close()
f3.close()
f4.close()

# make test query #####################################################
f1 = open("D://ANU_project//question_retrieval_tool//link_pair_en", "r", encoding='utf-8')
f2 = open("D://ANU_project//question_retrieval_tool//link_pair_ru", "r", encoding='utf-8')
f3 = open("D://ANU_project//question_retrieval_tool//test_dataset//%s_test_query_utf8" % target_tag, "a+", encoding='utf-8')

ru_lines = f2.readlines()
en_line = f1.readline()
write_count = 0
a = 0


while en_line:
    en_line = en_line.replace('\n', '')
    tags = en_line.split('\t')[2]
    tag_list = tags.split('|')

    if target_tag in tag_list:

        anwser_title = en_line.split('\t')[1]
        anwser_id = int(en_line.split('\t')[0])

        for ru_line in ru_lines:
            ru_line.replace('\n', '')
            query_id = int(ru_line.split('\t')[2])

            if query_id == anwser_id:
                query_title = ru_line.split('\t')[0]
                f3.write(query_title + '\t' + anwser_title)
                f3.write('\n')
                write_count += 1

    en_line = f1.readline()
    a += 1

print(a)
print(write_count)





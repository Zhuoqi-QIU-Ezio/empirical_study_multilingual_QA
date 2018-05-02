#!/usr/bin/python
# -*- coding: UTF-8 -*-

#ru_letters_b = [b'\xd0\x90', b'\xd0\xb0', b'\xd0\x91', b'\xd0\xb1', b'\xd0\x92', b'\xd0\xb2', b'\xd0\x93', b'\xd0\xb3', b'\xd0\x94', b'\xd0\xb4', b'\xd0\x95', b'\xd0\xb5', b'\xd0\x81', b'\xd1\x91', b'\xd0\x96', b'\xd0\xb6', b'\xd0\x97', b'\xd0\xb7', b'\xd0\x98', b'\xd0\xb8', b'\xd0\x99', b'\xd0\xb9', b'\xd0\x9a', b'\xd0\xba', b'\xd0\x9b', b'\xd0\xbb', b'\xd0\x9c', b'\xd0\xbc', b'\xd0\x9d', b'\xd0\xbd', b'\xd0\x9e', b'\xd0\xbe', b'\xd0\x9f', b'\xd0\xbf', b'\xd0\xa0', b'\xd1\x80', b'\xd0\xa1', b'\xd1\x81', b'\xd0\xa2', b'\xd1\x82', b'\xd0\xa3', b'\xd1\x83', b'\xd0\xa4', b'\xd1\x84', b'\xd0\xa5', b'\xd1\x85', b'\xd0\xa6', b'\xd1\x86', b'\xd0\xa7', b'\xd1\x87', b'\xd0\xa8', b'\xd1\x88', b'\xd0\xa9', b'\xd1\x89', b'\xd0\xaa', b'\xd1\x8a', b'\xd0\xab', b'\xd1\x8b', b'\xd0\xac', b'\xd1\x8c', b'\xd0\xad', b'\xd1\x8d', b'\xd0\xae', b'\xd1\x8e', b'\xd0\xaf', b'\xd1\x8f']
#ru_letters_s = ['А', 'а', 'Б', 'б', 'В', 'в', 'Г', 'г', 'Д', 'д', 'Е', 'е', 'Ё', 'ё', 'Ж', 'ж', 'З', 'з', 'И', 'и', 'Й', 'й', 'К', 'к', 'Л', 'л', 'М', 'м', 'Н', 'н', 'О', 'о', 'П', 'п', 'Р', 'р', 'С', 'с', 'Т', 'т', 'У', 'у', 'Ф', 'ф', 'Х', 'х', 'Ц', 'ц', 'Ч', 'ч', 'Ш', 'ш', 'Щ', 'щ', 'Ъ', 'ъ', 'Ы', 'ы', 'Ь', 'ь', 'Э', 'э', 'Ю', 'ю', 'Я', 'я']

target_tag = 'python'
bad_count = 0
write_count = 0
f0 = open("D://ANU_project//data_ru//Posts.xml", "rb")
print("文件名为: ", f0.name)
line = f0.readline()
print("读取第1行 %s" % (line))
line = f0.readline()
print("读取第2行 %s" % (line))
a = 0
f1 = open('D://ANU_project//question_retrieval_tool//ru_python_scorehigh_query_2', 'a+', encoding='utf-8')

while line:
    line = f0.readline()
    line_str = line.decode('utf-8', 'ignore')

    # a += 1
    # if a > 50:
    #     break

    try:
        c_title = line_str.split('Title="')[1]
        c_title = c_title.split('"')[0]
        c_title = c_title.replace('\n', '')
        c_title = c_title.replace('\t', '')

        c_body = line_str.split('Body="')[1]
        c_body = c_body.split('"')[0]
        c_body = c_body.replace('\n', '')
        c_body = c_body.replace('\t', '')
        c_body = c_body.replace('&lt;p&gt;', '')
        c_body = c_body.replace('&lt;/p&gt;', '')

        c_tag = line_str.split('Tags="')[1]
        c_tag = c_tag.split('"')[0]
        c_tag = c_tag.replace('\n', '')
        c_tag = c_tag.replace('\t', '')
        c_tag = c_tag.replace('&gt;&lt;', '|')
        c_tag = c_tag.replace('&lt;', '')
        c_tag = c_tag.replace('&gt;', '')

        c_score = line_str.split('Score="')[1]
        c_score = c_score.split('"')[0]
        c_score = c_score.replace('\n', '')

        c_tag_list = c_tag.split('|')
        c_score_int = int(c_score)

        if target_tag in c_tag_list and c_score_int > 4 and c_score_int < 8:
            f1.write('\t'.join([c_title, c_body, c_tag, c_score]))
            f1.write('\n')
            write_count += 1
    except:
        bad_count += 1

f0.close()
f1.close()
print("DONE:")
print(write_count)
print("BAD_COUNT:")
print(bad_count)

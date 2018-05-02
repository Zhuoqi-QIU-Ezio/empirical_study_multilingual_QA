import re

# ru_part ################################
# bad_count = 0
# write_count = 0
# f0 = open("D://ANU_project//data_ru//Posts.xml", "rb")
# print("文件名为: ", f0.name)
# line = f0.readline()
# print("读取第1行 %s" % (line))
# line = f0.readline()
# print("读取第2行 %s" % (line))
# a = 0
# f1 = open('D://ANU_project//question_retrieval_tool//link_pair_ru', 'a+', encoding='utf-8')
# line = f0.readline()
#
# while line:
#
#     line_str = line.decode('utf-8', 'ignore')
#     a += 1
#     line = f0.readline()
#
#     # if a > 1000:
#     #     break
#
#     if 'https://stackoverflow.com/questions/' in line_str:
#
#         c_link_id = line_str.split('https://stackoverflow.com/questions/')[1]
#         c_link_id = c_link_id.split('/')[0]
#         if not c_link_id.isdigit():
#             continue
#     #print(line_str.split('Title="'))
#         try:
#             c_title = line_str.split('Title="')[1]
#             #c_body = line_str.split('Body="')[1]
#             c_tag = line_str.split('Tags="')[1]
#             c_title = c_title.split('"')[0]
#             c_title = c_title.replace('\n', '')
#         #c_body = c_body.split('"')[0]
#         #c_body = c_body.replace('\n', '')
#         #c_body = c_body.replace('&lt;p&gt;', '')
#         #c_body = c_body.replace('&lt;/p&gt;', '')
#             c_tag = c_tag.split('"')[0]
#             c_tag = c_tag.replace('\n', '')
#             c_tag = c_tag.replace('&gt;&lt;', '|')
#             c_tag = c_tag.replace('&lt;', '')
#             c_tag = c_tag.replace('&gt;', '')
#
#             f1.write('\t'.join([c_title, c_tag, c_link_id]))
#             f1.write('\n')
#             write_count += 1
#         #f1.close()
#
#         except:
#             bad_count += 1
#     else:
#         continue
#
# print('RU::: %d' % a)
# f0.close()
# f1.close()
# print("DONE:")
# print(write_count)
# print("BAD_COUNT:")
# print(bad_count)

# en_part ############################################

bad_count = 0
write_count = 0
f0 = open("D://ANU_project//data_main//Posts.xml", "rb")
print("文件名为: ", f0.name)
line = f0.readline()
print("读取第1行 %s" % (line))
line = f0.readline()
print("读取第2行 %s" % (line))
line = f0.readline()

a = 0
f1 = open('D://ANU_project//question_retrieval_tool//link_pair_en', 'a+', encoding='utf-8')

f2 = open('D://ANU_project//question_retrieval_tool//link_pair_ru', 'r', encoding='utf-8')
id_list = []
f2_lines = f2.readlines()
for f2_line in f2_lines:
    id1 = f2_line.split('\t')[2]
    id1 = id1.replace('\n', '')
    id_list.append(int(id1))
id_list = sorted(id_list)
print('total_id_num:%d' % len(id_list))
print(id_list)
f2.close()

while line:

    line_str = line.decode('utf-8', 'ignore')
    a += 1
    line = f0.readline()

    # if a > 10:
    #     break

    try:
        id2 = line_str.split('Id="')[1]
        id2 = id2.split('"')[0]
        c_id = int(id2)
        if c_id not in id_list:
            continue
    except:
        continue

    try:

        c_title = line_str.split('Title="')[1]
            #c_body = line_str.split('Body="')[1]
        c_tag = line_str.split('Tags="')[1]
        c_title = c_title.split('"')[0]
        c_title = c_title.replace('\n', '')
        #c_body = c_body.split('"')[0]
        #c_body = c_body.replace('\n', '')
        #c_body = c_body.replace('&lt;p&gt;', '')
        #c_body = c_body.replace('&lt;/p&gt;', '')
        c_tag = c_tag.split('"')[0]
        c_tag = c_tag.replace('\n', '')
        c_tag = c_tag.replace('&gt;&lt;', '|')
        c_tag = c_tag.replace('&lt;', '')
        c_tag = c_tag.replace('&gt;', '')

        f1.write('\t'.join([id2, c_title, c_tag]))
        f1.write('\n')
        write_count += 1
        print(id2)

    except:
        bad_count += 1




print('RU::: %d' % a)
f0.close()
f1.close()
print("DONE:")
print(write_count)
print("BAD_COUNT:")
print(bad_count)
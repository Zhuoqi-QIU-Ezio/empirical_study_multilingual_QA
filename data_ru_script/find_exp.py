# bad_count = 0
# write_count = 0
# detect_count = 0
# f0 = open("D://ANU_project//data_ru//Posts.xml", "rb")
# print("文件名为: ", f0.name)
# line = f0.readline()
# print("读取第1行 %s" % (line))
# line = f0.readline()
# print("读取第2行 %s" % (line))
# a = 0
# f1 = open('D://ANU_project//data_ru//post_accept_ru', 'a+', encoding='utf-8')
# line = f0.readline()
#
# while line:
#
#     line_str = line.decode('utf-8', 'ignore')
#     a += 1
#     line = f0.readline()
#
#     try:
#         accept_id = line_str.split('AcceptedAnswerId="')[1]
#         user_id = line_str.split('OwnerUserId="')[1]
#         c_title = line_str.split('Title="')[1]
#         #c_body = line_str.split('Body="')[1]
#         #c_tag = line_str.split('Tags="')[1]
#
#         accept_id = accept_id.split('"')[0]
#         accept_id = accept_id
#
#         user_id = user_id.split('"')[0]
#         user_id = user_id
#
#         c_title = c_title.split('"')[0]
#         c_title = c_title.replace('\n', '')
#         #c_body = c_body.split('"')[0]
#         #c_body = c_body.replace('\n', '')
#         #c_body = c_body.replace('&lt;p&gt;', '')
#         #c_body = c_body.replace('&lt;/p&gt;', '')
#             # c_tag = c_tag.split('"')[0]
#             # c_tag = c_tag.replace('\n', '')
#             # c_tag = c_tag.replace('&gt;&lt;', '|')
#             # c_tag = c_tag.replace('&lt;', '')
#             # c_tag = c_tag.replace('&gt;', '')
#
#         f1.write('\t'.join([c_title, user_id, accept_id]))
#         f1.write('\n')
#         write_count += 1
#         #f1.close()
#
#     except:
#         bad_count += 1
#
# print('RU::: %d' % a)
# f0.close()
# f1.close()
# print("DONE:")
# print(write_count)
# print("BAD_COUNT:")
# print(bad_count)
# print(detect_count)
######################################################################################################
bad_count = 0
write_count_1 = 0
write_count_2 = 0
detect_count = 0

# check_pair = []
# parent_check = []
# f2 = open('D://ANU_project//data_ru//post_accept_ru', 'r', encoding='utf-8')
# acc_posts = f2.readlines()
#
# for post in acc_posts:
#     c_user_id = post.split('\t')[1].replace('\n', '')
#     c_acc_id = post.split('\t')[2].replace('\n', '')
#     #c_title = post.split('\t')[0]
#     check_pair.append((c_acc_id,c_user_id))
#     parent_check.append(c_acc_id)
#
# print(len(check_pair))
# print(len(parent_check))
# # print(check_pair[0])
# # print(check_pair[1])
# # print(check_pair[2])


f0 = open("D://ANU_project//data_ru//Posts.xml", "rb")
line = f0.readline()
line = f0.readline()

#f1 = open('D://ANU_project//data_ru//example_final', 'a+', encoding='utf-8')
f3 = open('D://ANU_project//data_ru//link_answer_ru', 'a+', encoding='utf-8')
#line = f0.readline()

while line:

        line_str = line.decode('utf-8', 'ignore')
        line = f0.readline()

        try:
            parent_id = line_str.split('ParentId="')[1]
            user_id = line_str.split('OwnerUserId="')[1]
            body = line_str.split('Body="')[1]
            body = body.split('"')[0]

            parent_id = parent_id.split('"')[0]
            parent_id_int = int(parent_id)

            user_id = user_id.split('"')[0]
            user_id_int = int(user_id)
            detect_count += 1

            # if (parent_id, user_id) in check_pair:
            #
            #     f1.write('\t'.join([parent_id, user_id]))
            #     f1.write('\n')
            #     write_count_1 += 1
            # if parent_id in parent_check:
            #     f3.write('\t'.join([user_id, parent_id]))
            #     f3.write('\n')
            #     write_count_2 += 1
            if 'https://stackoverflow.com/questions/' in body:
                f3.write('\t'.join([user_id,parent_id]))
                f3.write('\n')
                write_count_1 += 1
        except:
            bad_count += 1

f3.close()
print("DONE:")
print(write_count_1)
print(write_count_2)
print("BAD_COUNT:")
print(bad_count)
print(detect_count)
#########################################################################################################
# bad_count = 0
# write_count = 0
# detect_count = 0
# f2 = open('D://ANU_project//data_ru//post_accept_ru', 'r', encoding='utf-8')
# f1 = open('D://ANU_project//data_ru//user_acc', 'a+', encoding='utf-8')
# acc_posts = f2.readlines()
#
# for post in acc_posts:
#     c_user_id = post.split('\t')[1].replace('\n', '')
#     c_acc_id = post.split('\t')[2].replace('\n', '')
#     c_title = post.split('\t')[0].replace('\n', '')
#     f1.write('\t'.join([c_user_id,c_acc_id]))
#     f1.write('\n')
#     write_count += 1
#
# print(write_count)
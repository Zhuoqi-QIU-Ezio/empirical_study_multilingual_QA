#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 打开文件
# user_post_count = {}
# bad_count = 0
# fo = open("D://ANU_project//data_ru//Posts.xml", "rb")
# print("文件名为: ", fo.name)
# line = fo.readline()
# print("读取第一行 %s" % (line))
# a = 0
# while line:
#     line = fo.readline()
#     line = bytes.decode(line)
#
#     #reputation_caculation
#     # if 'Reputation="' in line:
#     #     line1 = line.split('Reputation="')
#     #     line2 = line1[1]
#     #     line3 = line2.split('"')
#     #     rep_score = int(line3[0])
#     #     #print(rep_score)
#     #     if rep_score >= 200:
#     #         a = a +1
#
#     try:
#         line1 = line.split('OwnerUserId="')
#         line2 = line1[1]
#         line3 = line2.split('"')
#         user_id = line3[0]
#         if user_id in user_post_count:
#             user_post_count[user_id] += 1
#         else:
#             user_post_count[user_id] = 1
#     except:
#         bad_count += 1
# # sum = 0
# # for key,value in user_post_count.items():
# #     sum += value
# # print("sum")
# # print(sum)
#
# # print(user_post_count)
# print("bad_count:")
# print(bad_count)
#
# filtered_users = []
# post_sum = 0
# for key,value in user_post_count.items():
#     if value >= 100:
#         filtered_users.append(key)
#         post_sum += value
#
# print(len(filtered_users))
# print(post_sum)

bad_count = 0
fo = open("D://ANU_project//data_main//Users_m.xml", "rb")
print("文件名为: ", fo.name)
line = fo.readline()
print("读取第一行 %s" % (line))
a = 0


while line:
    line = fo.readline()
    line_str = line.decode('utf-8')
    try :
        #print('')
        id = line_str.split('AccountId="')[1]
        id = id.split('"')[0]
        with open('D://ANU_project//main_user_id.txt', 'a+') as f1:
            f1.write(id)
            f1.write('\n')
            f1.close()
            a += 1
    except:
        bad_count += 1

print(a)
print(bad_count)




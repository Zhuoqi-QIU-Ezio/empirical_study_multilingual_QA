#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 打开文件
ru_letters_b = [b'\xd0\x90', b'\xd0\xb0', b'\xd0\x91', b'\xd0\xb1', b'\xd0\x92', b'\xd0\xb2', b'\xd0\x93', b'\xd0\xb3', b'\xd0\x94', b'\xd0\xb4', b'\xd0\x95', b'\xd0\xb5', b'\xd0\x81', b'\xd1\x91', b'\xd0\x96', b'\xd0\xb6', b'\xd0\x97', b'\xd0\xb7', b'\xd0\x98', b'\xd0\xb8', b'\xd0\x99', b'\xd0\xb9', b'\xd0\x9a', b'\xd0\xba', b'\xd0\x9b', b'\xd0\xbb', b'\xd0\x9c', b'\xd0\xbc', b'\xd0\x9d', b'\xd0\xbd', b'\xd0\x9e', b'\xd0\xbe', b'\xd0\x9f', b'\xd0\xbf', b'\xd0\xa0', b'\xd1\x80', b'\xd0\xa1', b'\xd1\x81', b'\xd0\xa2', b'\xd1\x82', b'\xd0\xa3', b'\xd1\x83', b'\xd0\xa4', b'\xd1\x84', b'\xd0\xa5', b'\xd1\x85', b'\xd0\xa6', b'\xd1\x86', b'\xd0\xa7', b'\xd1\x87', b'\xd0\xa8', b'\xd1\x88', b'\xd0\xa9', b'\xd1\x89', b'\xd0\xaa', b'\xd1\x8a', b'\xd0\xab', b'\xd1\x8b', b'\xd0\xac', b'\xd1\x8c', b'\xd0\xad', b'\xd1\x8d', b'\xd0\xae', b'\xd1\x8e', b'\xd0\xaf', b'\xd1\x8f']
ru_letters_s = ['А', 'а', 'Б', 'б', 'В', 'в', 'Г', 'г', 'Д', 'д', 'Е', 'е', 'Ё', 'ё', 'Ж', 'ж', 'З', 'з', 'И', 'и', 'Й', 'й', 'К', 'к', 'Л', 'л', 'М', 'м', 'Н', 'н', 'О', 'о', 'П', 'п', 'Р', 'р', 'С', 'с', 'Т', 'т', 'У', 'у', 'Ф', 'ф', 'Х', 'х', 'Ц', 'ц', 'Ч', 'ч', 'Ш', 'ш', 'Щ', 'щ', 'Ъ', 'ъ', 'Ы', 'ы', 'Ь', 'ь', 'Э', 'э', 'Ю', 'ю', 'Я', 'я']
bad_count = 0
fo = open("D://ANU_project//data_ru//Posts.xml", "rb")
print("文件名为: ", fo.name)
line = fo.readline()
print("读取第一行 %s" % (line))
a = 0
b = 0
ru = 0
ru_loc = 0
ru_let = 0


while line:
    line = fo.readline()
    line_str = line.decode('utf-8')
    try :
        #print('')
        tag_str = line_str.split('AboutMe="')[1]
        id = line_str.split('AccountId="')[1]
        id = id.split('"')[0]
        #tag_str = line_str.split('Location="')[1]
        tag_str = tag_str.split('"')[0]
        #print(tag_str)
        #print('with@@@@')
        tag = tag_str.encode('utf-8')
        #print(len(tag))
        #print(len(tag_str))
        #print(tag)
    #line = bytes.decode(line)
        # if 'Russia' in tag_str or 'RU' in tag_str or 'russia' in tag_str:
        # #if 'Ru' in tag_str:
        #     #print(tag_str)
        #     with open('D://ANU_project//data_main//location_hit_user.txt','a+') as f1 :
        #         f1.write(id)
        #         f1.write('\n')
        #         f1.close()
        #     ru_loc += 1
        #     ru += 1

        if len(tag) > len(tag_str) and len(tag) <= 2 * len(tag_str):
            for let in tag_str:
                if let in ru_letters_s :
                    ru_let += 1
                    ru += 1
                    with open('D://ANU_project//data_main//about_hit_user.txt', 'a+') as f1:
                        f1.write(id)
                        f1.write('\n')
                        f1.close()
                    break


            b = b + 1
            #print(tag)
    except:
        bad_count += 1
    a += 1
    #if a >= 50:
        #break
print('ALL USERS:')
print(a)
print('NON-EN:')
print(b)
print('BAD_C:')
print(bad_count)
print('RU-LOC:')
print(ru_loc)
print('RU-LET')
print(ru_let)
print('RU_ALL:')
print(ru)

    #reputation_caculation
    # if 'Reputation="' in line:
    #     line1 = line.split('Reputation="')
    #     line2 = line1[1]
    #     line3 = line2.split('"')
    #     rep_score = int(line3[0])
    #     #print(rep_score)
    #     if rep_score >= 200:
    #         a = a +1
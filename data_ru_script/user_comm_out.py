f0 = open("D://ANU_project//data_ru//main_ru_result", "r")
ids = f0.readlines()
tar_ids = []
for id in ids:
    id = id.replace('\n','')
    try:
        id = int(id)
    except:
        continue
    tar_ids.append(id)

#print(tar_ids)
#fuck

bad_count = 0
break_flag = False

for item in tar_ids:

    target_Aid = item

    f1 = open("D://ANU_project//data_main//Users_m.xml", "rb")
    f2 = open("D://ANU_project//data_ru//Users.xml", "rb")
    #print("文件名为: ", f1.name)
    line1 = f1.readline()
    line1 = f1.readline()
    #print("读取第2行 %s" % (line1))
    #print("文件名为: ", f2.name)
    line2 = f2.readline()
    line2 = f2.readline()
    #print("读取第2行 %s" % (line2))

    while line1:
        line1 = f1.readline()
        line_str = line1.decode('utf-8', 'ignore')

        try:
            c_Aid = line_str.split('AccountId="')[1]
            c_Aid = c_Aid.split('"')[0]
            c_Aid = c_Aid.replace('\n', '')
            c_Aid = c_Aid.replace('\t', '')

            if  int(c_Aid) == target_Aid:
                main_user = line1
                break
        except:
            bad_count += 1

    while line2:
        line2 = f2.readline()
        line_str = line2.decode('utf-8', 'ignore')

        try:
            c_Aid = line_str.split('AccountId="')[1]
            c_Aid = c_Aid.split('"')[0]
            c_Aid = c_Aid.replace('\n', '')
            c_Aid = c_Aid.replace('\t', '')

            c_rps = line_str.split('Reputation="')[1]
            c_rps = c_rps.split('"')[0]
            c_rps = c_rps.replace('\n', '')
            c_rps = c_rps.replace('\t', '')

            if int(c_Aid) == target_Aid:
                ru_user = line2
                ru_user_rp = int(c_rps)
                break

        except:
            bad_count += 1

    while ru_user_rp > 1000:
        print("MAIN:::::::::::")
        print(main_user)
        print('RUUUUU:::::::::')
        print(ru_user)
        print(ru_user_rp)
        break

    f1.close()
    f2.close()

print("BAD_COUNT:")
print(bad_count)

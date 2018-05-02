f0 = open("D://ANU_project//data_main//target_eg_user", "r")
ids = f0.readlines()
tar_ids = []
for id in ids:
    id = id.replace('\n','')
    try:
        id = int(id)
    except:
        continue
    tar_ids.append(id)

# print(tar_ids)
# fuck

bad_count = 0
break_flag = False

for item in tar_ids:

    target_Aid = item

    f1 = open("D://ANU_project//data_main//Users_m.xml", "rb")

    line1 = f1.readline()
    line1 = f1.readline()



    while line1:
        line1 = f1.readline()
        line_str = line1.decode('utf-8', 'ignore')

        try:
            c_Aid = line_str.split('AccountId="')[1]
            c_Aid = c_Aid.split('"')[0]
            c_Aid = c_Aid.replace('\n', '')
            c_Aid = c_Aid.replace('\t', '')

            c_rps = line_str.split('Reputation="')[1]
            c_rps = c_rps.split('"')[0]
            c_rps = c_rps.replace('\n', '')
            c_rps = c_rps.replace('\t', '')

            if  int(c_Aid) == target_Aid and int(c_rps) > 100:
                print(line_str)
                break
        except:
            bad_count += 1

    f1.close()


print("BAD_COUNT:")
print(bad_count)
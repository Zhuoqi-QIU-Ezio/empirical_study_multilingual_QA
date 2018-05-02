
f2 = open("D://ANU_project//data_ru//Users.xml", "rb")

line2 = f2.readline()
line2 = f2.readline()

user_num_1 = 0
user_num_2 = 0
user_num_3 = 0
user_num_4 = 0
user_num_5 = 0
bad_count = 0

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
            rps = int(c_rps)

            if rps >= 10 and rps < 100:
                user_num_1 += 1
            if rps >= 100 and rps < 200:
                user_num_2 += 1
            if rps >= 200 and rps < 500:
                user_num_3 += 1
            if rps >= 500 and rps < 1000:
                user_num_4 += 1
            if rps >= 1000:
                user_num_5 += 1

    except:
            bad_count += 1

print(user_num_1)
print(user_num_2)
print(user_num_3)
print(user_num_4)
print(user_num_5)
print(bad_count)
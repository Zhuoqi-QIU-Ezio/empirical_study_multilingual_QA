f0 = open("D://ANU_project//data_ru//comm_tags", "r")

line0 = f0.readlines()

comm_tags = []
bad_count = 0
comm_count_1 = 0
comm_count_2 = 0
ru_to_en_fre = {}
total_post_en = 44534041
total_post_ru = 428587

for tag in line0:
    tag = tag.replace('\n', '')
    comm_tags.append(tag)

f0.close()
#print(comm_tags)
for comm_tag in comm_tags:

    try:

        f1 = open("D://ANU_project//data_ru//Tags.xml", "rb")
        f2 = open("D://ANU_project//data_main//Tags_m.xml", "rb")

        line1 = f1.readline()
        line1 = f1.readline()
        line2 = f2.readline()
        line2 = f2.readline()

        while line1:
            line1 = f1.readline()
            line_str = line1.decode('utf-8', 'ignore')

            c_tag = line_str.split('TagName="')[1]
            c_tag = c_tag.split('"')[0]
            c_tag = c_tag.replace('\n', '')
            c_tag = c_tag.replace('\t', '')

            c_count = line_str.split('Count="')[1]
            c_count = c_count.split('"')[0]
            c_count = c_count.replace('\n', '')
            c_count = c_count.replace('\t', '')
            c_count = int(c_count)

            if c_tag == comm_tag:
                comm_count_1 += 1
                tag_ru_count = c_count
                break


        while line2:
            line2 = f2.readline()
            line_str = line2.decode('utf-8', 'ignore')

            c_tag = line_str.split('TagName="')[1]
            c_tag = c_tag.split('"')[0]
            c_tag = c_tag.replace('\n', '')
            c_tag = c_tag.replace('\t', '')

            c_count = line_str.split('Count="')[1]
            c_count = c_count.split('"')[0]
            c_count = c_count.replace('\n', '')
            c_count = c_count.replace('\t', '')
            c_count = int(c_count)

            if c_tag == comm_tag:
                comm_count_2 += 1
                tag_en_count = c_count
                break

        rel_fre = (tag_ru_count/total_post_ru)/(tag_en_count/total_post_en)
        ru_to_en_fre[comm_tag] = rel_fre

    except:
        bad_count += 1

    f1.close()
    f2.close()

print(comm_count_1)
print(comm_count_2)
print(ru_to_en_fre)
print(bad_count)
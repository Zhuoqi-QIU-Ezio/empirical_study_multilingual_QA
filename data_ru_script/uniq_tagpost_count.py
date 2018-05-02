f0 = open("D://ANU_project//data_ru//Posts.xml", "rb")
print("文件名为: ", f0.name)
line = f0.readline()
print("读取第1行 %s" % (line))
line = f0.readline()
print("读取第2行 %s" % (line))

f1 = open("D://ANU_project//data_ru//comm_tags", "r")
comm_tags = f1.readlines()
comm_tag_list = []
uniq_count = 0
other_count = 0
bad_count = 0
for item in comm_tags:
    item = item.replace('\n', '')
    comm_tag_list.append(item)

#print(comm_tag_list)

while line:
    line = f0.readline()
    line_str = line.decode('utf-8', 'ignore')
    try:
        c_tag = line_str.split('Tags="')[1]
        c_tag = c_tag.split('"')[0]
        c_tag = c_tag.replace('\n', '')
        c_tag = c_tag.replace('\t', '')
        c_tag = c_tag.replace('&gt;&lt;', '|')
        c_tag = c_tag.replace('&lt;', '')
        c_tag = c_tag.replace('&gt;', '')

        c_tag_list = c_tag.split('|')
        for tag in c_tag_list:
            if tag not in comm_tag_list:
                uniq_count += 1
                break
            else:
                other_count += 1

    except:
        bad_count += 1

print(uniq_count)
print(other_count)
print(bad_count)
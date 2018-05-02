f0 = open('D://ANU_project//question_retrieval_tool//link_pair_en','r',encoding='utf-8')
line = f0.readline()
tag_pool = []
a = 1
while line:
    tags = line.split('\t')[2]
    tag_list = tags.split('|')
    for item in tag_list:
        tag_pool.append(item)

    line = f0.readline()
    a += 1

print(tag_pool)
print(a)
tag_count = {}

for i in tag_pool:

    if tag_pool.count(i):
        tag_count[i] = tag_pool.count(i)
print(tag_count)

dict= sorted(tag_count.items(), key=lambda d:d[1], reverse = True)
print(dict)
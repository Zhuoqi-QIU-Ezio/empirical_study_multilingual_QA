import pandas as pd
import numpy
import scipy.stats as stats

f0 = open("D://ANU_project//data_ru//comm_tags", "r")
f1 = open("D://ANU_project//data_ru//tags_sort_en", "r")
f2 = open("D://ANU_project//data_ru//tags_sort_ru", "r")

line0 = f0.readlines()
line1 = f1.readlines()
line2 = f2.readlines()

comm_tags = []
en_tag_rank = []
ru_tag_rank = []
comm_rank_en = []
comm_rank_ru = []
bad_count = 0

for tag in line0:
    tag = tag.replace('\n', '')
    comm_tags.append(tag)

#print(comm_tags)

for tag in line1:
    tag = tag.replace('\n', '')
    tag = tag.split('\t')[0]
    en_tag_rank.append(tag)

for tag in line2:
    tag = tag.replace('\n', '')
    tag = tag.split('\t')[0]
    ru_tag_rank.append(tag)

print(en_tag_rank)
print(ru_tag_rank)

for item in comm_tags:
    if item in en_tag_rank and item in ru_tag_rank:
        comm_rank_en.append(en_tag_rank.index(item))
        comm_rank_ru.append(ru_tag_rank.index(item))
    else:
        bad_count += 1

print(comm_rank_en)
print(len(comm_rank_en))
print(comm_rank_ru)
print(len(comm_rank_ru))
print(bad_count)

# X = pd.DataFrame({"A":[34,12,78,84,26], "B":[54,87,35,25,82], "C":[56,78,0,14,13], "D":[0,23,72,56,14], "E":[78,12,31,0,34]})
# Y = pd.DataFrame({"A1":[45,24,65,65,65], "B1":[45,87,65,52,12], "C1":[98,52,32,32,12], "D1":[0,23,1,365,53], "E1":[24,12,65,3,65]})
#
# a = pd.concat([X,Y], axis=1).corr(method="spearman").iloc[5:,:5]
# print(a)

cor, pval = stats.spearmanr(comm_rank_en, comm_rank_ru)
print(cor)
print(pval)


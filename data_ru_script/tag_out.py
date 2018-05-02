import requests
import time
import hashlib
import json

ru_letters_b = [b'\xd0\x90', b'\xd0\xb0', b'\xd0\x91', b'\xd0\xb1', b'\xd0\x92', b'\xd0\xb2', b'\xd0\x93', b'\xd0\xb3', b'\xd0\x94', b'\xd0\xb4', b'\xd0\x95', b'\xd0\xb5', b'\xd0\x81', b'\xd1\x91', b'\xd0\x96', b'\xd0\xb6', b'\xd0\x97', b'\xd0\xb7', b'\xd0\x98', b'\xd0\xb8', b'\xd0\x99', b'\xd0\xb9', b'\xd0\x9a', b'\xd0\xba', b'\xd0\x9b', b'\xd0\xbb', b'\xd0\x9c', b'\xd0\xbc', b'\xd0\x9d', b'\xd0\xbd', b'\xd0\x9e', b'\xd0\xbe', b'\xd0\x9f', b'\xd0\xbf', b'\xd0\xa0', b'\xd1\x80', b'\xd0\xa1', b'\xd1\x81', b'\xd0\xa2', b'\xd1\x82', b'\xd0\xa3', b'\xd1\x83', b'\xd0\xa4', b'\xd1\x84', b'\xd0\xa5', b'\xd1\x85', b'\xd0\xa6', b'\xd1\x86', b'\xd0\xa7', b'\xd1\x87', b'\xd0\xa8', b'\xd1\x88', b'\xd0\xa9', b'\xd1\x89', b'\xd0\xaa', b'\xd1\x8a', b'\xd0\xab', b'\xd1\x8b', b'\xd0\xac', b'\xd1\x8c', b'\xd0\xad', b'\xd1\x8d', b'\xd0\xae', b'\xd1\x8e', b'\xd0\xaf', b'\xd1\x8f']
ru_letters_s = ['А', 'а', 'Б', 'б', 'В', 'в', 'Г', 'г', 'Д', 'д', 'Е', 'е', 'Ё', 'ё', 'Ж', 'ж', 'З', 'з', 'И', 'и', 'Й', 'й', 'К', 'к', 'Л', 'л', 'М', 'м', 'Н', 'н', 'О', 'о', 'П', 'п', 'Р', 'р', 'С', 'с', 'Т', 'т', 'У', 'у', 'Ф', 'ф', 'Х', 'х', 'Ц', 'ц', 'Ч', 'ч', 'Ш', 'ш', 'Щ', 'щ', 'Ъ', 'ъ', 'Ы', 'ы', 'Ь', 'ь', 'Э', 'э', 'Ю', 'ю', 'Я', 'я']


api_url = "http://api.fanyi.baidu.com/api/trans/vip/translate"   # baidu developer account
my_appid = '20180311000134261'
cyber = 'Yp3vRSB_0_HjSuikUA3n'

def requests_for_dst(word):
    # init salt and final_sign
    salt = str(time.time())[:10]
    final_sign = str(my_appid) + word + salt + cyber
    final_sign = hashlib.md5(final_sign.encode("utf-8")).hexdigest()
    paramas = {                                             # baidu translate parameters
                 'q': word,
                 'from': 'ru',
                 'to': 'en',
                 'appid': '%s' % my_appid,
                 'salt': '%s' % salt,
                 'sign': '%s' % final_sign
             }

    response = requests.get(api_url, params=paramas).content
    content = str(response, encoding="utf-8")
    json_reads = json.loads(content)
    #print(':::INFO:::translated_query --- %s' % json_reads['trans_result'][0]['dst'])
    return json_reads['trans_result'][0]['dst']   # return translated query in english

f1 = open('D://ANU_project//data_ru//tags_name_ru', 'a+')
f2 = open("D://ANU_project//data_ru//Tags.xml", "rb")

line2 = f2.readline()
line2 = f2.readline()

while line2:
    line2 = f2.readline()
    line_str = line2.decode('utf-8', 'ignore')
    c_name = line_str.split('TagName="')[1]
    c_name = c_name.split('"')[0]
    c_name = c_name.replace('\n', '')
    c_name = c_name.replace('\t', '')

    for item in ru_letters_s:
        if item in c_name:
            c_name = c_name = requests_for_dst(c_name)
            break
    #c_name = requests_for_dst(c_name)
    c_name = c_name.replace('the ','')

    c_count = line_str.split('Count="')[1]
    c_count = c_count.split('"')[0]
    c_count = c_count.replace('\n', '')
    c_count = c_count.replace('\t', '')
    #c_count = int(c_count)

    #f1.write('\t'.join([c_name, c_count]))
    f1.write(c_name)
    f1.write('\n')

f1.close()
f2.close()

import requests
import json
import re
import time
import random
import emoji

if __name__ == '__main__':

    headerlist = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991",
           "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.94",
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36 OPR/47.0.2631.39",
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
           "Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
           "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
           "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
           "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
           "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0",
           "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"]
    #隨機選擇headers
    user_agent = random.choice(headerlist)
    headers = {'User-Agent': user_agent}
    URL = 'https://www.dcard.tw/_api/forums/relationship/posts?popular=true&limit=100'
    #URL = 'https://www.dcard.tw/_api/posts?popular=true&limit=100'
    API1 = 'http://dcard.tw/_api/posts/'
    
    API2 = '/comments'
    
    a = requests.get(URL,headers= headers).text
    b = json.loads(a)

    '''with open("posts.json",'r',encoding = 'utf-8') as load_f:
        b = json.load(load_f)
    '''
    output = open('relationship1129.txt', 'w', encoding='utf-8')
    #print(b)
    for jason in b:
        
        APIcomment = API1 + str(jason['id']) + API2

        print(APIcomment)

        c = requests.get(APIcomment).text
        d = json.loads(c)
        for dick in d:  
            try:
                #print(re.findall('[A-z][0-9]+', dick['content']))
                '''for n in re.findall('([\u4e00-\u9fff]+[0-9]*[A-z]*)+', dick['content']):
                    output.write(n + '\n')
                    #print(n)'''

                dick['content'] = dick['content'].translate(str.maketrans('','','B,b')) #去掉B
                dick['content'] = re.sub("\d+", "", dick['content']) #去掉數字
                
                dick['content'] = emoji.demojize(dick['content'])# 去掉表情
                dick['content'] = re.sub(r':(.*):','',dick['content']).strip() #去掉表情處裡過後的 :(英文):
                dick['content'] = dick['content'].lstrip() #去除左邊空格
                dick['content'] = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', dick['content'], flags=re.MULTILINE) #去除網址

                output.write(dick['content']+ '\n')
            except:
                print('我邊緣人沒有人回我喇幹')
    output.close()
    
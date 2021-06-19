#!/usr/bin/env python3
#-*- coding:utf-8 -*-
from bs4.builder import HTML
import requests,time,random
from bs4 import BeautifulSoup as bs



def down(url):#获取代理ip
    urll = requests.get(url)
    with open('ip.txt','wb') as fr:
        fr.write(urll.content)
    print('获取ip成功')
def ip():#读取代理ip
    path = 'ip.txt'
    ip_use_list =[]
    with open(path,"r",encoding='UTF-8') as fr:
        ip_use_lines = fr.readlines()
        for ip_use_line in ip_use_lines:
            ip_use_new = ip_use_line.replace('\n','')
            ip_use_list.append(ip_use_new)
    return ip_use_list
def over(ip,xieyi_1):#显示活的代理ip
    num = 1
    num_1 = 1
    ip_num = len(ip)
    print(f'协议为{xieyi_1},一共获取{ip_num}个代理ip')
    
    url = 'http://ip-api.com/json/?fields=61439'
    #url = 'http://ip.cn/'
    #url = 'http://www.cip.cc/'
    #url = 'https://www.baidu.com/'
    open(f"{xieyi_1}.txt", 'w').close()#清空文本
    for i in range(ip_num):        
        try:                
            proxy_data={'http':f'{xieyi_1}://'+ip[i],
                        'https':f'{xieyi_1}://'+ip[i]}
            head_data = {'User-Agent':'Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; BAC-AL00 Build/HUAWEIBAC-AL00) AppleWebKit/537.36 (KHTML, like Gecko) '\
                         'Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.9.4.974 UWS/2.13.1.48 Mobile Safari/537.36 AliApp(DingTalk/4.5.11) '\
                         'com.alibaba.android.rimet/10487439 Channel/227200 language/zh-CN'}
            html = requests.get(url,headers=head_data,proxies=proxy_data,timeout=(15)) #timeout超时时间
            #yield html.text
            top = html.json()
            yield num,top['city'],top['query'],ip[i],num_1#,city            
            with open(f'{xieyi_1}.txt',"a+") as f:
                f.writelines(f'{ip[i]}\n')
                yield f'已写入.......{ip[i]}'

            num+=1            
            num_1+=1
        except:
            yield num,'错误'
            num+=1
            pass
    return f'总共有{num_1}个有效ip'
if __name__ == '__main__':
    xieyi = ['http','https','socks4','socks5']
    xieyi_1 = random.choice(xieyi)#随机协议
    #xieyi_1 = 'socks4'
    url = f'https://www.proxy-list.download/api/v1/get?type={xieyi_1}'
    #print(url)
    path = down(url)
    ip = ip()
    for i in over(ip,xieyi_1):
        print(i)

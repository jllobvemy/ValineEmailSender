import requests
import json
import time
import re
import datetime
from emailsender import email_sender

if __name__ == '__main__':
    h = { # Header
        'x-avoscloud-application-id': 'xxxxxxxxxxxxxxxxxxx', # AppID
         'x-avoscloud-application-key': 'xxxxxxxxxxxxxxxxxxxxxx', # AppKey
         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    }
    p = { # params
        'limit': '1',
        'order': '-updatedAt'
    }
    r = requests.get('https://leancloud.cn:443/1.1/classes/Comment', params=p, headers=h)
    comment = json.loads(r.text) # 加载Json
    t = comment['results'][0]['insertedAt']['iso'] # 获取时间，此时间为ISO时间，需要转换
    text = comment['results'][0]['comment'] # 评论内容
    url = 'www.jllobvemy.com' + comment['results'][0]['url'] # 地址
    regex = re.compile(r'\..*') # 格式化时间
    t = re.sub(regex, '', t)
    delta = datetime.timedelta(hours=8) # 本地时间与国际标准时间差8小时
    ctime = time.strptime(t, '%Y-%m-%dT%H:%M:%S') # 格式化时间
    timestamp = time.mktime(ctime) # 转为时间戳使得time转为datetime
    dtime = datetime.datetime.fromtimestamp(timestamp) # 转为datetime
    dtime += delta # 时间转化
    print('last_message:', dtime)
    with open('time.txt', 'r+') as f:
        old_time = f.read()
        print('file_message:', old_time)
        if old_time == str(dtime): # 与文件中记载的时间进行比较，相同则不处理，不同则发送邮件告知
            print('same')
        else:
            print('diff')
            email_sender('有人给你新评论啦', '评论时间: ' + str(dtime) + '\n' + '内容: ' + text + '\n' + '地址: ' + url + '\n')
            # print('评论时间: ' + str(dtime) + '\n' + '内容: ' + text + '\n' + '地址: ' + url + '\n')
            f.seek(0)
            f.truncate()
            f.write(str(dtime))

#!/usr/bin/env python3
# encoding: utf-8

from urllib import request, parse
username = '学号'
password = '密码' #加密后的密码，查询post内容部分可获取
data = parse.urlencode([
    ('username', username),
    ('password', password),
    ('domain', ''),
    ('enablemacauth', '0')
])


req = request.Request('http://a.suda.edu.cn/index.php/index/login')
req.add_header('Origin', 'http://a.suda.edu.cn')
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/60.0.3112.113 Chrome/60.0.3112.113 Safari/537.36')
req.add_header('Referer', 'http://a.suda.edu.cn/index.php?url=aHR0cDovL3dnLnN1ZGEuZWR1LmNuLw==')
req.add_header('Cookie', 'PHPSESSID=argivmkto5c9qf1chf6b8ghvr3; think_language=zh-CN; sunriseUsername=1408404043; sunriseDomain=campus')
req.add_header('X-Requested-With', 'XMLHttpRequest')

with request.urlopen(req, data=data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k,v in f.getheaders():
        print('%s: %s' % (k,v))
    print('Data:', f.read().decode('utf-8'))

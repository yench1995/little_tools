#!/usr/bin/env python3
# encoding: utf-8

from urllib import request, parse

login_data = parse.urlencode([])

url = 'http://a.suda.edu.cn/index.php/index/logout'
referer = 'http://a.suda.edu.cn/index.php?url=aHR0cDovL3dnLnN1ZGEuZWR1LmNuLw=='
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/60.0.3112.113 Chrome/60.0.3112.113 Safari/537.36'
origin = 'http://a.suda.edu.cn'

req = request.Request(url)
req.add_header('Origin', origin)
req.add_header('User-Agent', user_agent)
req.add_header('Referer', referer)

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k,v))
    print('Data:', f.read().decode('utf-8'))

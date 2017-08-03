import re
import requests

usrl = 'https://isc.sans.edu/tools/reversehash.html'
s = requests.session()
s.headers['User-Agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0'
q = s.get(usrl)
# TODO token和Cookies是绑定的　记得先从ｇｅｔ中得到ｔｏｋｅｎ再去发送请求
print(s.cookies['dshield'])
html = q.text
string = '<input type="submit" value="Search" /><input type="hidden" name="token" value="(.*)" />'
pattern = re.compile(string)
m = pattern.findall(html)
post = {'text': '202cb962ac59075b964b07152d234b70'}
post['token'] = m[0].strip()
print(post['token'])

p = s.post(url=usrl, data=post)

with open('log.html', 'w') as f:
    f.write(p.text)
import re
import requests

s = requests.session()
s.headers['User-Agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0'
p = s.get('http://www.cmd5.org')
p.encoding = p.apparent_encoding
post = {'__EVENTTARGET': 'Button1',
            '__EVENTARGUMENT': '',
            '__VIEWSTATEGENERATOR': 'CA0B0334',
            'ctl00$ContentPlaceHolder1$TextBoxInput': '202cb962ac59075b964b07152d234b70',
            'ctl00$ContentPlaceHolder1$InputHashType': 'md5(md5($pass))',
            'ctl00$ContentPlaceHolder1$Button1': '查询',
            'ctl00$ContentPlaceHolder1$HiddenField1': ''}
html = p.text
string = 'name="__VIEWSTATE" id="__VIEWSTATE" value="(.*)" />'
m = re.compile(string).findall(html)
post['__VIEWSTATE'] = m[0]
hearders = {
            'Host': 'www.cmd5.com',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '1942',
            'Referer': 'http://www.cmd5.com/',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache'}
string = 'id="ctl00_ContentPlaceHolder1_HiddenField2" value="(.*)" />'
m = re.compile(string).findall(html)
post['ctl00$ContentPlaceHolder1$HiddenField'] = m[0]
# 若没有headers 则没有返回的数据
s.headers['Content-Type'] =  'application/x-www-form-urlencoded'
s.headers['Referer'] = 'http://www.cmd5.com/'
response = s.post('http://www.cmd5.com/', data=post)
response.encoding = response.apparent_encoding
strings = '''<span id="ctl00_ContentPlaceHolder1_LabelAnswer">(.*)<br /><br /><a target'''
pattern = re.compile(strings)
m = pattern.findall(response.text)
print(s.headers)
with open('log.html', 'w') as f:
    f.write(response.text)
print(m[0])

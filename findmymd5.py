#!/usr/bin/env python3

try:
    import requests
    from bs4 import BeautifulSoup
    import re
    import hashlib
    from random import randint
except ImportError as e:
    print("缺少必要库")


MD5 = None


class HASHCRACK():
    '''
    crack md5 in http://hashcrack.com

    Attributes:
        hashValue: needed to be cracked md5
    '''
    name = "hashcrack"
    url = "http://hashcrack.com"

    def __init__(self, hashValue):
        self.hashValue = hashValue

    def crack(self):
        '''
        crack md5 in website
        Returns:
            ths answer of md5
        '''
        post = {'auth': '8272hgt',
                'hash': self.hashValue,
                'string': None,
                'Submit': 'Submit'}
        url = 'http://hashcrack.com/index.php'
        resonse = requests.post(url, data=post, timeout=3)
        html = resonse.text
        soup = BeautifulSoup(html, 'lxml')
        # <span class=hervorheb2>123</span></div></TD>
        t = soup.find('span', attrs={'class': 'hervorheb2'})
        return t.string


class HASHTOOLKIT():
    '''
    http://hashtoolkit.com/reverse-hash/?hash=824d8ee415a6efd2fa97b4092105d955

    '''

    name = "hashtoolkit"
    url = "http://hashtoolkit.com"

    def __init__(self, hashValue):
        self.hashValue = hashValue

    def crack(self):
        get_url = self.url + r'/reverse-hash/?hash=' + self.hashValue
        response = requests.get(get_url, timeout=3)
        html = response.text
        s = BeautifulSoup(html, 'lxml')
        t = s.find('span', attrs={'title': "decrypted md5 hash"})
        return t.string


class CMD5():
    ''' http://www.cmd5.org '''
    name = 'cmd5'
    url = 'http://www.cmd5.org/'

    def __init__(self, hashValue):
        self.hashValue = hashValue

    def crack(self):
        s = requests.session()
        s.get('http://www.cmd5.org')

        post = {'__EVENTTARGET': 'Button1',
                '__EVENTARGUMENT': '',
                '__VIEWSTATE': 'gtjewOj+HEbwv5moj1QqiVmsF6kTb1pmOq/RSrv1vTl19rURTV55y5XwTdZ+MgOwtqdtgi1RGS1rjt70jPb9Cic+VviEInnPYqFLm2e2JEPJr9KEgrLte9RdOVz6P8W38sHw7R/OfM5aHxzkMvpci4iNi3va+ctO8BB8W03lm/iIJmXZxcwQmWVZb2ERjo7MnDm07kUHMpj9ts6HReYBapsPpxsLSdNIsdpg9xbNUduPIGUyKSD0LKlO/yRysW51k6D8a3ZuZj47AUL13wfu9a1HdcEMOfWe4u9XA6c5ymuk5IuthQ0LaHQnHOiiwLe6v+zk6BZS/nvZo6V/vVX72QkfyYh1bUAnwYNknlBUVfLNx68WpdH6t/KRLZuDLctUcanHy15JYFWpC4z5634E5f9tSTgB57RV833w+A7T2xNTT3u9DcCO6uIQh4Y5mwYf1v6qqlliitD+wY0ldjXB4FMVWskMEz1iqE0BaEKLxPcSJT5VcDExzeVzw/2NRXMaKJ3gBt+R18Ma3LTXAQor9JSQTKm2HluOEUeG+pRF+W4FqUTV4KAcbP3R+ZPbMBd7hBmGYgav7YXBq36HKdWqI2kFhg08lkKCdWBUtM3ERdqIolp0g1y1x30guUuxNRr9ddlTXx6YjBTy8fa1vMcwCN4kAGz0dnp3lIQz2J8NOmpGUFX6Hiy3REB0Nm6XLbuhinXHJK4mkZVREKOZB8cg2NDo52DVrbnhvh/pGi6zxgzL28GE/ApjQFc+9Zyz+6AS0hTpVkF873TyLpjwGXV2NY0PW2kGLl5BDs44pMhrB7GspaKWOMRd3R8WpenYjnKMVog7oTR4lbkK2FJ1lafCKN0JpcUzjhaIE4UiGLBqY5Au8bRT7O/dSxO4UiOConsJk2cxxfoZaC/IW2AYdpGxPaNIjtyuONePMsuwA8PHoelZZ/LNPWJIXPPFh123HsH7vmzEBnQbPr4E7qCaOnhtLUpBNI4PoJ7UtazEvfIP+88oB5MCmM7O/1ZaAOT1rXARwU4ifIT9I6DHSkcnXmLaM2oxW1KrmBzvaZfw6vZ3TdSO4C7zRgV1LyiGtKQxLCfDNALvBMgNai8aRAu4UvFVsnD0seEVOQ7hCCFvKJoSzKUFgz2yi2dKNsqWklPxwq3dFy+qvLjL1yr60PaTBRqRJ4Xd9/tLSfM4qFTcY9YBix+tYRndGAiq0WPp8n1VSHgBNeW6xY7i1wap0Fx6skAaaP52CNGEdKgh3FDoKQpIAegf9FO7lhF57WQYWigrfgI6Ph5hY3dAAQ6kxJ1aphZLbuRJSZ/FYdWbwHdZa9+Yv62eNlNV8DCGOz4EAZSAxFMCUqQiCs9RO530d21qUitSxcYxocVSN95uplwlPi1tvEgDmlONCId0FdqZb1oDTt2UDVtGqYWLltRvYhszwf418DzJ5e8=',
                '__VIEWSTATEGENERATOR': 'CA0B0334',
                'ctl00$ContentPlaceHolder1$TextBoxInput': '202cb962ac59075b964b07152d234b70',
                'ctl00$ContentPlaceHolder1$InputHashType': 'md5(md5($pass))',
                'ctl00$ContentPlaceHolder1$Button1': '查询',
                'ctl00$ContentPlaceHolder1$HiddenField1': '',
                'ctl00$ContentPlaceHolder1$HiddenField': 'xAo8jpr6Q7/lr81tr3uNyRcQqKX3xoyvWLbBPPK16nGyfGp7bn6977O3e1EuEoDo'}
        # 若没有headers 则没有返回的数据
        hearders = {
            'Host': 'www.cmd5.com',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '1942',
            'Referer': 'http://www.cmd5.com/',
            'Cookie': 'ASP.NET_SessionId=eur50sa5zfbom53gff4i4ed1; comefrom=https://www.baidu.com/link?url=6sjybewmhlwquvfs2iqzvkrsuvw2dp-xgekrasr1luq&wd=&eqid=910a0fef00004180000000035980769b; FirstVisit=2017/8/1 14:41:08; Hm_lvt_0b7ba6c81309fff7ce4498ec7b107c0b=1501591271,1501592417; Hm_lpvt_0b7ba6c81309fff7ce4498ec7b107c0b=1501592417',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache'}

        response = s.post('http://www.cmd5.com/', data=post, headers=hearders)
        response.encoding = response.apparent_encoding
        strings = '''<span id="ctl00_ContentPlaceHolder1_LabelAnswer">(.*)<br /><br /><a target'''
        pattern = re.compile(strings)
        m = pattern.findall(response.text)
        return m[0]


class DMD5():
    ''' http://www.dmd5.com/md5-decrypter.jsp'''

    name = "dmd5"
    url = "http://www.dmd5.com"

    def __init__(self, hashValue):
        self.hashValue = hashValue

    def crack(self):
        post = {'_VIEWRESOURSE' : 'c4c92e61011684fc23405bfd5ebc2b31',
                'result' : 'c1fa08ee052e00e5b8e7527f9211d9c0453bc6f335a6181f2f58c7816f79278e75b690137e34374df3cfcf7dadfe7828dcd0c37a5bc4b493a94730b376b54c80ad8db7d2b168fff553584bff499fd06bd9dd0dbef033481c98020ec237c8c5ed54490cd46b03610d2ea2d1428e0f715ea4a79c07f40416c2de6d657f2eb6ee562d7743db5311a04aa4fa1cb0d034b6868d9abf6ec279'}
        post['md5'] = self.hashValue
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0'}
        response = requests.post(
            'http://www.dmd5.com/md5-decrypter.jsp', data=post, headers=headers)
        response.encoding = response.apparent_encoding
        html = response.text
        with open('log.html','w') as f:
            f.write(html)
        string = '''解密结果：([0-9a-f]*)</p><p>密文类型：md5</p>'''
        pattern = re.compile(string)
        matcher = pattern.findall(html)
        return matcher[0]


def is_success(answer):
    '''
    TO test whether the answer is rigth
    Args:
        answer: a answer that is searched
    Returns:
        if the answer is wrong, raise a Exception

    '''
    global MD5
    m = hashlib.md5()
    m.update(answer.encode())
    m = m.hexdigest()
    if(m != MD5):
        raise Exception


def main():
    # TODO 最后一旦找到直接退出　md5为用户命令行输入的值，并将其全部转换为小写  加上随机数　每次从随机的一个位置开始查询防止被网站ban ip
    ALLCRACK = [HASHCRACK, HASHTOOLKIT, CMD5, DMD5]
    global MD5
    MD5 = '202cb962ac59075b964b07152d234b70'
    random_int = randint(0, len(ALLCRACK))
    for i in range(len(ALLCRACK)):
        cracker = ALLCRACK[(i + random_int) % len(ALLCRACK)](MD5)
        print('%s is cracking.' % cracker.url, end='')
        try:
            answer = cracker.crack()
            is_success(answer)
            print('done!')
            print('the answer is %s' % answer)
            # exit(0)
        except Exception as e:
            print(e)
            continue

    print('No Found This Md5!')

if __name__ == '__main__':
    main()

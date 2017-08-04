#!/usr/bin/env python3

try:
    import requests
    from bs4 import BeautifulSoup
    import re
    import hashlib
    from random import randint
    import sys
except ImportError as e:
    print(" requests , BeautifulSoup are needed.try to 'pip3 install requests beautifulsoup4'")


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
        resonse = requests.post(url, data=post, timeout=2)
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
        response = requests.get(get_url, timeout=2)
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
        s.headers[
            'User-Agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0'
        p = s.get('http://www.cmd5.org', timeout=2)
        p.encoding = p.apparent_encoding
        post = {'__EVENTTARGET': 'Button1',
                '__EVENTARGUMENT': '',
                '__VIEWSTATEGENERATOR': 'CA0B0334',
                'ctl00$ContentPlaceHolder1$InputHashType': 'md5(md5($pass))',
                'ctl00$ContentPlaceHolder1$Button1': '查询',
                'ctl00$ContentPlaceHolder1$HiddenField1': ''}
        post['ctl00$ContentPlaceHolder1$TextBoxInput'] = self.hashValue
        html = p.text
        string = 'name="__VIEWSTATE" id="__VIEWSTATE" value="(.*)" />'
        m = re.compile(string).findall(html)
        post['__VIEWSTATE'] = m[0]
        '''
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
                    '''
        string = 'id="ctl00_ContentPlaceHolder1_HiddenField2" value="(.*)" />'
        m = re.compile(string).findall(html)
        post['ctl00$ContentPlaceHolder1$HiddenField'] = m[0]
        # 若没有headers 则没有返回的数据
        s.headers['Content-Type'] = 'application/x-www-form-urlencoded'
        s.headers['Referer'] = 'http://www.cmd5.com/'
        response = s.post('http://www.cmd5.com/', data=post, timeout=2)
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
        post = {'_VIEWRESOURSE': 'c4c92e61011684fc23405bfd5ebc2b31',
                'result': 'c1fa08ee052e00e5b8e7527f9211d9c0453bc6f335a6181f2f58c7816f79278e75b690137e34374df3cfcf7dadfe7828dcd0c37a5bc4b493a94730b376b54c80ad8db7d2b168fff553584bff499fd06bd9dd0dbef033481c98020ec237c8c5ed54490cd46b03610d2ea2d1428e0f715ea4a79c07f40416c2de6d657f2eb6ee562d7743db5311a04aa4fa1cb0d034b6868d9abf6ec279'}
        post['md5'] = self.hashValue
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0'}
        response = requests.post(
            'http://www.dmd5.com/md5-decrypter.jsp', data=post, headers=headers, timeout=2)
        response.encoding = response.apparent_encoding
        html = response.text
        string = '''解密结果：([0-9a-f]*)</p><p>密文类型：md5</p>'''
        pattern = re.compile(string)
        matcher = pattern.findall(html)
        return matcher[0]


class PMD5():
    ''' http://pmd5.com/#'''
    name = 'pmd5'
    url = 'http://pmd5.com/#'

    def __init__(self, hashValue):
        self.hashValue = hashValue

    def crack(self):
        post = {'__VIEWSTATE': '/wEPDwUKMTM4NTE3OTkzOQ9kFgJmD2QWAgIFDxYEHgVjbGFzcwULdGlwIHN1Y2Nlc3MeCWlubmVyaHRtbAWhATxpIGNsYXNzPSJpY29uZm9udCI+JiN4ZTY5MTs8L2k+PHAgY2xhc3M9ImluZm8iPuaCqOafpeivoueahOWtl+espuS4suaYr+KAnDxlbT4yMDJjYjk2MmFjNTkwNzViOTY0YjA3MTUyZDIzNGI3MDwvZW0+4oCdLOino+WvhueahOe7k+aenOS4uuKAnDxlbT4xMjM8L2VtPuKAnSE8L3A+ZGQtO6cvbeoJkiaoshSqYE2S5f5PtA==',
                '__VIEWSTATEGENERATOR': 'CA0B0334',
                '__EVENTVALIDATION': '/wEWAwK+nKzTAwLigPTXCQKU9f3vAmsrjwD8v1twmEnA1Nr7h4Jic4/O',
                'jiemi': 'MD5解密'}
        post['key'] = self.hashValue
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0'}
        response = requests.post(
            self.url, data=post, headers=headers, timeout=2)
        response.encoding = response.apparent_encoding
        html = response.text
        string = '''</em>”,解密的结果为“<em>(.*)</em>”!</p></div>'''
        pattern = re.compile(string)
        m = pattern.findall(html)
        return m[0]


class CRACKHASH():
    ''' http://crackhash.com/ '''
    name = 'crackhash'
    url = "http://crackhash.com/"

    def __init__(self, hashValue):
        self.hashValue = hashValue

    def crack(self):
        post = {'crack': 'crack'}
        post['hash'] = self.hashValue
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0'}
        response = requests.post(
            self.url, data=post, headers=headers, timeout=2)
        response.encoding = response.apparent_encoding
        html = response.text
        string = '''==> ([0-9a-f]*)</center><'''
        pattern = re.compile(string)
        m = pattern.findall(html)
        return m[0]


class ISCSANS():
    ''' https://isc.sans.edu/tools/reversehash.html
    该网站容易超时
    '''
    name = 'isc_sans_edu'
    url = 'https://isc.sans.edu/tools/reversehash.html'

    def __init__(self, hashValue):
        self.hashValue = hashValue

    def crack(self):
        '''
        Cookie 与　token 照应
        '''
        s = requests.session()
        s.headers[
            'User-Agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0'
        # 给seesion设置Cookie和得到与之对应的token
        q = s.get(self.url, timeout=3)
        html = q.text
        string = '<input type="submit" value="Search" /><input type="hidden" name="token" value="(.*)" />'
        pattern = re.compile(string)
        m = pattern.findall(html)
        post = {'text': '202cb962ac59075b964b07152d234b70'}
        post['token'] = m[0].strip()
        p = s.post(url=self.url, data=post, timeout=3)
        html = p.text
        string = 'md5 hash ' + self.hashValue + ' =(.*)</p><br />'
        pattern = re.compile(string)
        m = pattern.findall(html)
        return m[0].strip()


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
    if(len(sys.argv) != 2):
        print('''\tUsage:python findmymd5.py md5Hash''')
        exit(0)
    ALLCRACK = [HASHCRACK, HASHTOOLKIT, CMD5, DMD5, PMD5, CRACKHASH, ISCSANS]
    global MD5
    MD5 = sys.argv[1].lower()
    random_int = randint(0, len(ALLCRACK))
    for i in range(len(ALLCRACK)):
        cracker = ALLCRACK[(i + random_int) % len(ALLCRACK)](MD5)
        print('%s is cracking.' % cracker.url, end='')
        try:
            answer = cracker.crack()
            is_success(answer)
            print('done!')
            print('the answer is %s' % answer)
            exit(0)
        except Exception as e:
            # print(e)
            print('fail!')
            continue

    print('No Found This Md5!')

if __name__ == '__main__':
    main()

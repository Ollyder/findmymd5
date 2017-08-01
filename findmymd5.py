#!/usr/bin/env python3

try:
    import requests
    from bs4 import BeautifulSoup
    import re
    import hashlib
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
        response = requests.get(get_url)
        html = response.text
        s = BeautifulSoup(html, 'lxml')
        t = s.find('span',attrs={'title':"decrypted md5 hash"})
        return t.string


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
    # TODO 最后一旦找到直接退出
    ALLCRACK = [HASHCRACK, HASHTOOLKIT]
    global MD5
    MD5 = '202cb962ac59075b964b07152d234b70'
    for i in range(len(ALLCRACK)):
        cracker = ALLCRACK[i](MD5)
        print('%s is cracking.' % cracker.url, end='')
        try:
            answer = cracker.crack()
            is_success(answer)
            print('done!')
            print('the answer is %s' % answer)
            exit(0)
        except Exception as e:
            print('fail!')
            continue

    print('No Found This Md5!')

if __name__ == '__main__':
    main()

import re

f = open('log.html','r')
s = f.read()
f.close()

strings = '''<span id="ctl00_ContentPlaceHolder1_LabelAnswer">(.*)<br /><br /><a target'''
pattern = re.compile(strings)
m = pattern.findall(s)
print(m)
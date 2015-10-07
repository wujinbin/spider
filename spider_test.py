# -*-coding:utf8-*-

import requests

html = requests.get('http://www.jikexueyuan.com/course/pythonbase//2-0-0/')
print html.text

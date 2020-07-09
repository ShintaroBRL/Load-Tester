from lxml import html
import requests
import logging
import threading
import time

def loginpan(n):
    print 'login n', n, 'iniciado!'

    logintoken = ""

    url = ''

    x = requests.post(url)
    tree = html.fromstring(x.content)
    logintoken = tree.xpath('//input[@name="logintoken"]/@value')
    
    login_form = {'username': n, 'password': n, 'logintoken': logintoken[0]}
    login = requests.post(url, data = login_form)
    response = html.fromstring(login.content)
    error = response.xpath('//div[@class="alert alert-danger"]/text()')
    
    print 'status: ', logintoken, login_form, error

x = range(10,310)
for i in x:
    x = threading.Thread(target=loginpan, args=(i,))
    x.start()
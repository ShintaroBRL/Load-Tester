#/usr/bin/python
# -*- coding: utf-8 -*-
# coding: utf-8

from lxml import html 
import sys
import requests 
import logging 
import threading 
import time
import os, shutil

if (len(sys.argv) < 3):
    print ("\nComo usar: login-flood.py <url> <quantidade> <ssl: true/false>\n")
    sys.exit()

url = str(sys.argv[1])
qtd = int(sys.argv[2])+11
ssl = bool(sys.argv[3])

sucesso = 0
fail = 0

def loginpan(n):
    print('login nº '+str(n)+' iniciado!\n')

    with requests.Session() as session:

        logintoken = ""

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36'
        }

        fisrt = session.get(url, verify=ssl, headers=headers)
        tree = html.fromstring(fisrt.content)
        logintoken = tree.xpath('//input[@name="logintoken"]/@value')
        
        login_form = {'username': str(n), 'password': str(n), 'logintoken': logintoken[0]}
        login = session.post(url, data = login_form, verify=ssl, headers=headers)
        response = html.fromstring(login.content)
        status = response.xpath('//div[@class="alert alert-danger"]/text()')

        if status == "":
            sucesso = sucesso + 1
            status = "Logado"

        with open("logs/test"+str(n)+".html", mode='wb') as localfile:
            localfile.write(login.content)
        
        print("\n")
        print('header: ', login.headers, '\n')
        print('Login Token: ', logintoken, '\n') 
        print('User: ', login_form, '\n')
        print('Status: ', status, '\n')
        print("\n")

folder = 'logs/'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

x = range(10,qtd)
for i in x:
    x = threading.Thread(target=loginpan, args=(i,))
    x.start()
    time.sleep(0.1)
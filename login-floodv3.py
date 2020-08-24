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
from progress.bar import ShadyBar
import logging

if (len(sys.argv) < 4):
    print ("\nComo usar: login-flood.py <url> <quantidade> <ssl: true/false> <sleep>\n")
    sys.exit()

url  = str(sys.argv[1])
qtd  = int(sys.argv[2])+1
ssl  = bool(sys.argv[3])
tm  = float(sys.argv[4])

bars = Collection()
starting = ShadyBar('Iniciando', max=qtd-1, suffix = '%(percent)d%% [%(index)d/%(max)d] (%(elapsed)ds)')
response = ShadyBar('Respostas', max=qtd-1, suffix = '%(percent)d%% [%(index)d/%(max)d] (%(elapsed)ds)')
bars.extend(download_bar, install_bar)

def start():
    clear_logs()
    setup_logging()
    logging.warning('Programa iniciado')
    x = range(1,qtd)
    for i in x:
        x = threading.Thread(target=fire, args=(i,))
        x.start()
        starting.next()
        time.sleep(tm)  

    starting.finish()

def setup_logging():
    logging.basicConfig(format='%(asctime)s [%(levelname)s]: %(message)s', filename='logs/logs.log', level=logging.DEBUG)

def fire(id):
    logging.info('login nº '+str(id)+' iniciado!')

    with requests.Session() as session:

        logintoken = ""

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36'
        }

        fisrt = session.get(url, verify=ssl, headers=headers)
        tree = html.fromstring(fisrt.content)
        logintoken = tree.xpath('//input[@name="logintoken"]/@value')
        login_form = ""

        try:
            if id <= 9:
                login_form = {'username': '0'+str(id), 'password': '0'+str(id), 'logintoken': str(logintoken[0])}
            elif id >= 10:
                login_form = {'username': str(id), 'password': str(id), 'logintoken': str(logintoken[0])}
        except:
            logging.warning("Erro de token no login: "+ str(id))
            logging.warning("Erro de token: "+ logintoken)

        login = session.post(url, data = login_form, verify=ssl, headers=headers)
        resposta = html.fromstring(login.content)
        status = resposta.xpath('//div[@class="alert alert-danger"]/text()')

        with open("logs/test"+str(id)+".html", mode='wb') as localfile:
            localfile.write(login.content)
        
        try:
            logging.debug('######################################')
            logging.debug('Resposta de: '+str(id))
            #logging.debug('header: '+ str(login.headers))
            logging.debug('Login Token: '+ logintoken[0]) 
            logging.debug('User: '+ str(login_form))
            logging.debug('Status: '+ str(status))
            logging.debug('######################################')
        except:
            logging.warning('Login token error')

        response.next()

def clear_logs():
    folder = 'logs/'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            logging.warning('Failed to delete %s. Reason: %s' % (file_path, e))

start()
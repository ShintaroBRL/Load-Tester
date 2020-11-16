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

class Dispatch:
    def __init__(self,url,ssl,id,progressbar):

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
                debug = "\n\n"+"######################################"+"\n"
                debug += "Resposta de: "+str(id)+"\n"
                debug += "Login Token: "+ logintoken[0]+"\n"
                debug += "User: "+ str(login_form)+"\n"
                debug += "Status: "+ str(status)+"\n"
                debug += "######################################"+"\n"
                logging.debug(debug)
            except:
                logging.warning('Login token error')
            
            progressbar.update(id)
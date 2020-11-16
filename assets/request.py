#/usr/bin/python
# -*- coding: utf-8 -*-
# coding: utf-8

import os, shutil
import logging
from clint.textui import colored
import threading
from dispatch import Dispatch

class Request:
    def onStart(init):
        print colored.red("Limpando Logs!")
        for filename in os.listdir('logs/'):
            file_path = os.path.join('logs/', filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                logging.warning('Failed to delete %s. Reason: %s' % (file_path, e))
        logging.basicConfig(format='%(asctime)s [%(levelname)s]: %(message)s', filename='logs/logs.log', level=logging.DEBUG)
        print colored.yellow("Sistema iniciado!\n")
    
    def Run(init,index,progress,count,url,ssl):
        threading.Thread(target=Dispatch, args=(url,ssl,index,progress,)).start()
    
    def OnFinish(init):
        print "\nLoadTest finalizado!\nResultados: \n"
        exit(0)

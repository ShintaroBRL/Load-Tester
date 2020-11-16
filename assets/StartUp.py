#installed modules
from pyfiglet import Figlet
from clint.textui import colored
import argparse

#system modules
import time
import sys
import os

#Metas
__author__ = "Juliano Lira Florentino"
__description__ = "Programa desenvolvido para teste de carga em sistemas de login"
__version__ = "V2.0.0"

#Configs
os.system('cls' if os.name == 'nt' else 'clear')    #Clear screen on start
parser = argparse.ArgumentParser()                  # Initialize parser
 
#Args configs
parser.add_argument("-u","--url", help = "Link para os testes", required=True)
parser.add_argument("-s","--ssl", help = "Use ssl", type=bool, required=True)
parser.add_argument("-l","--logs", help = "Generate Logs", type=bool, required=True)
parser.add_argument("--users", help = "quantidade de usuarios", type=int, required=True)
parser.add_argument("--sleep", help = "tempo de espera", type=float, required=True)
args = parser.parse_args()

#Print welcome
class StartUp:

    def keyboardInterruptHandler(init, signal, frame):
        exit(0)

    def __init__(init):
        print colored.yellow(Figlet(font='slant').renderText('Load Tester'))
        print colored.yellow("author: ")+colored.red(__author__)
        print colored.yellow("Description: ")+colored.red(__description__)
        print colored.yellow("Version: ")+colored.red(__version__)
        print "\n"
    
    def getArgs(init):
        return args
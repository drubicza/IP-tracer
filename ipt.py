#!/usr/bin/env python
# -*- coding: utf-8 -*-

#WARNA
R = '\033[31m'
w = '\033[37m'
Y = '\033[33m'
W = '\033[00m'
i='\033[31m[\033[37m+\033[31m] \033[37m '
#BAHAN
import os
import sys
import time
from urllib import *
from time import sleep
import marshal
def Banner():
    print """\033[31m
    ________        __
   /  _/ __ \      / /__________ _________  _____
   / // /_/ /_____/ __/ ___/ __ `/ ___/ _ \/ ___/
 _/ // ____/_____/ /_/ /  / /_/ / /__/  __/ /
/___/_/          \__/_/   \__,_/\___/\___/_/ \033[37mv1.0
"""
def clear():
    os.system("clear")
def clear1():
    if 'linux' or 'unix' in sys.platform:
            clear()
    elif 'win' in sys.platform:
            os.system("cls")
    elif 'darwin' in sys.platform:
            os.system("cls")
    else:
            clear()


def connection():
    if 'status' == 'success':
        pass
    else:
        print ""
        print "%s[%s!%s] %sERROR%s: %s[Errno 7] No address associated with hostname" % (R,Y,R,W,R,W)
        print ""
        exit()
def trackipaddress():
    clear()
    Banner()
    try:
        ip = raw_input(" \033[00mEnter IP \033[31m>>>\033[00m ")
    except:
        keluar()
    ip1 = "https://ipapi.co/"+ip+"/yaml/"
    pp1 = urlopen(ip1).read()
    clear()
    print (pp1)
    sys.exit
def trackyouripaddress():
    clear()
    Banner()
    key = raw_input("Press Enter To Continue ")
    ip2 = "https://ipapi.co/yaml/"
    pp2 = urlopen(ip2).read()
    clear()
    print (pp2)
    sys.exit
def keluar():
    clear()
    Banner()
    print " "
    print i+"Thanks For Using This Tool ..."
    print i+"Have Bad Day ..."
    print i+"Good By ..."
    print ""
    exit()
def msg():
    print '%s[%s#%s] %sAuthor  %s: %sYou & You' % (R, Y, R, W, R, W)
    print '%s[%s#%s] %sDate    %s: %s01-01-1001 (01:01:01)' % (R, Y, R, W, R, W)
    print '%s[%s#%s] %sGithub  %s: %sgithub.com/afelfgie' % (R, Y, R, W, R, W)
    print '%s[%s#%s] %sPlatform%s: %spython' % (R, Y, R, W, R, W)
    print ''

def info():
    print "%s[%s#%s] %sAuthor  %s: %sGunadiCBR" % (R,Y,R,W,R,W)
    print "%s[%s#%s] %sDate    %s: %s01-01-1001 (01:01:01)" % (R,Y,R,W,R,W)
    print "%s[%s#%s] %sGithub  %s: %sgithub.com/afelfgie" % (R,Y,R,W,R,W)
    print "%s[%s#%s] %sPlatform%s: %spython" % (R,Y,R,W,R,W)
    print ""
def tya():
    print "%s[%s1%s] %sTrack IP Address" % (R,Y,R,W)
    print "%s[%s2%s] %sTrack Your Ip Address" % (R,Y,R,W)
    print "%s[%s0%s] %sExit" % (R,Y,R,W)
    print " \033[00m"
def runner():
    tya()
    try:
        choice = raw_input(" IP-tracer \033[31m>>>\033[00m ")
    except:
        keluar()
    if choice == '1':
        trackipaddress()
    elif choice == '2':
        trackyouripaddress()
    elif choice == '0':
        keluar()
    else:
        _main()
def _main():
    clear1()
    Banner()
    msg()
    runner()

##################################
if __name__ == "__main__":
        try:
        _main()
    except KeyboardInterrupt:
        keluar()
##################################

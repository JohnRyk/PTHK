#!/usr/bin/env python3
# coding: utf-8

import sys
import argparse

def cmdArgParser():
    parser = argparse.ArgumentParser(description='PTHK -> Mobie Pentest Hook Kit.\t(Author: JRZ)')
    
    parser.add_argument('-v','--version',action='version',version='%(prog)s v1.0 Happy hacking <3')
    parser.add_argument('-U',dest='usb',action='store_true',help="Connect to device via USB")
    parser.add_argument('-H','--host',help="Connect to remote host (ip:port)")
    parser.add_argument('-n','--name',help="Process name to attach")
    parser.add_argument('-f','--spawn',help="Spawn package: (Accept package name)")
    parser.add_argument('-p','--pid',help="Target process id")
    parser.add_argument('-c','--classname',help="Target classname")
    parser.add_argument('-l','--load',help="Specify script path to load")
    parser.add_argument('--echo',dest='echo',action='store_true',help="Simple hook test, if it works will print \"Hello Frida\"")
    parser.add_argument('--enum',dest='enum',action='store_true',help="Enumerate switch. Uses to enumerate classes or methods")
    parser.add_argument('--hook-exit', dest='hook_exit', action='store_true', help="Hooking android System.exit")
    parser.add_argument('--hook-llib', dest='hook_llib', action='store_true', help="Hooking app load Libs")
    parser.add_argument('--hook-lurl', dest='hook_lurl', action='store_true', help="Hooking app load Urls")
    parser.add_argument('--hook-sms', dest='hook_sms', action='store_true', help="Hooking android send SMS")

    #if len(sys.argv) == 1:
    #    sys.argv.append("-h")
    
    args = parser.parse_args()
    return args
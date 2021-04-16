#!/usr/bin/env python3

def banner():
    banner = """
           _    _                     _          _     _             _     _   _ _   
 _ __  ___| |__(_)___   _ __  ___ _ _| |_ ___ __| |_  | |_  ___  ___| |__ | |_(_) |_ 
| '  \/ _ \ '_ \ / -_) | '_ \/ -_) ' \  _/ -_|_-<  _| | ' \/ _ \/ _ \ / / | / / |  _|
|_|_|_\___/_.__/_\___| | .__/\___|_||_\__\___/__/\__| |_||_\___/\___/_\_\ |_\_\_|\__|
                       |_|                                                                       
""" + " " * 80 + "v1.0" + "\n" + " " * 73 + "Author: JRZ\n"  + "-" * 85

    example = "\n\
Example:\n\
    \tConnect over USB: \n\
    \t\t./pthk.py -U -n <process> --echo\n\
    \t\t./pthk.py -U -f <package> --echo\n\
    \t\t./pthk.py -U -n <process> --enum\n\
    \t\t./pthk.py -U -n <process> -c <class> --enum\n\
    \tConnect over TCP (For example: adb forward tcp:8888 tcp:8888): \n\
    \t\t./pthk.py -H 127.0.0.1:8888 -n <process> --echo\n\
    \t\t./pthk.py -H 127.0.0.1:8888 -f <package> --echo"
    print(banner)
    print(example)
    print()



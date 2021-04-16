#!/usr/bin/env python3
# coding: utf-8

import frida

def device(TYPE_USB,HOST):
    device = ""
    if TYPE_USB:
        #print("[*] Getting device over USB")
        try:
            device = frida.get_usb_device(1000)
        except Exception as e:
            print("[-] Error get device over USB failed !")
            print(e)
    elif HOST != None:
       #print("[*] Getting device over TCP")
        try:
            port = HOST.split(':')[1]
            if int(port) == 27042:
                device = frida.get_remote_device()
            else:
                device = frida.get_device_manager().add_remote_device(HOST)
        except Exception as e:
            print("[-] Error get device over TCP failed !")
            print(e)
    return device



    

#!/usr/bin/env python3
# coding: utf-8

import frida
import time
import sys
import os


def launch_hook(device, script_to_load, load_type, func_type, args):
    hang = True     # Default hang up after loading.
    if load_type == "process" or load_type == "pid":
        PROCESS = args.name
        PID = args.pid
        if func_type == "enum":
            hang = False
        attach_hook(device, script_to_load, hang, process_name=PROCESS, pid=PID)
    elif load_type == "package":
        PACKAGE = args.spawn
        if func_type == "enum":
            hang = False
        spawn_hook(device, script_to_load, hang, package_name=PACKAGE)
        pass


def attach_hook(device, script_to_load, hang, process_name=None, pid=None):
    try:
        if pid == None:
            pid = device.get_process(process_name).pid
        session = device.attach(int(pid))
        script = session.create_script(script_to_load)
        script.load()
        if hang:
            sys.stdin.read()
    except Exception as e:
        print("[-] Error attach hook failed !")
        print(e)


def spawn_hook(device, script_to_load, hang, package_name=None):
    try:
        if package_name != None:
            pid = device.spawn([package_name])
        session = device.attach(int(pid))
        script = session.create_script(script_to_load)
        script.load()
        time.sleep(1)
        device.resume(pid)
        if hang:
            sys.stdin.read()
    except Exception as e:
        print("[-] Error spawn hook failed !")
        print(e)

#!/usr/bin/env python3
# coding: utf-8

from lib.load import loader

def manager(device, load_type, func_type, args):
    if func_type == "":
        print("[-] Missing action parameter")
        return
    if func_type == "load":
        # load script
        loader.load(device, load_type, func_type, args)
    elif func_type != "":
        # build-in function
        loader.load_build_in(device, load_type, func_type, args)



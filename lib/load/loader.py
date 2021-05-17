#!/usr/bin/env python3
# coding: utf-8

import os
import sys
from lib.load import hooker

enum_classes_js = '''
'use strict'
if(Java.available){
    Java.perform(function(){
        try{
            var allClassName = new Array();
            Java.enumerateLoadedClasses({
                onMatch: function(className){
                    allClassName.push(className);
                },
                onComplete: function(){
                    allClassName.sort();
                    function output(value){
                        console.log(value);
                    }
                    allClassName.forEach(output);
                }
            });
        }catch(error){
            console.error("[-] An error occured !");
            console.log(String(error.stack));
        }
    });
}else{
    console.error("[-] Java is not available !");
}
'''

enum_class_methods_js = \
"'use strict'\n\
if(Java.available){\n\
    Java.perform(function(){\n\
        try{\n\
            var target_class_name = '%s';\n\
            var allMethodName = new Array();\
            var target_class_obj = Java.use(target_class_name);\n\
            allMethodName = Object.getOwnPropertyNames(target_class_obj).join('%s').split('%s');\
            allMethodName.sort();\
            function output(value){\
                console.log(value);\
            }\
            allMethodName.forEach(output);\
            //console.error('[*] Enumerate methods all Done !');\n\
        }catch(error){\n\
            console.error('[-] An error occured !');\n\
            console.log(String(error.stack));\n\
        }\n\
    });\n\
}else{\n\
    console.error('[-] Java is not available !');\n\
}"


def load(device, load_type,func_type, args):
    path = args.load
    script = get_script(classname="",path=path)
    if script == "":
        print("[-] Get script error !")
        return
    hooker.launch_hook(device, script, load_type, func_type, args)
    

def load_build_in(device, load_type, func_type, args):
    # [ echo | enum | hook_exit | hook_llib | hook_lurl | hook_sms | load ]
    HOOK_CLASS = args.classname
    script_path = get_script_path(func_type)
    script = get_script(classname=HOOK_CLASS, path=script_path)
    if script == "":
        print("[-] Get script error !")
        return
    hooker.launch_hook(device, script, load_type, func_type, args)


def get_script_path(func_type):
    script_name = ""
    script_path = ""
    script_perfix = sys.path[0] + "/lib/script/"
    if func_type == "load" or func_type == "enum":
        return ""
    if func_type == "echo":
        script_name = "hello.js"
    elif func_type == "hook_exit":
        script_name = "hook_java_exit.js"
    elif func_type == "hook_llib":
        script_name = "hook_java_llib.js"
    elif func_type == "hook_lurl":
        script_name = "hook_java_lurl.js"
    elif func_type == "hook_sms":
        script_name = "hook_java_sms.js"
    script_path = script_perfix + script_name
    return script_path


def get_script(classname="", path=""):
    script = ""
    if path != "":
        if not os.path.exists(path):
            print("[-] Error: Cannot locate that script: %s" % os.path.realpath(path))
            return
        with open(path,'r') as f:
            script = f.read()
            return script
    if classname:
        return enum_class_methods_js % (classname,r"\n",r"\n")
    else:
        return enum_classes_js


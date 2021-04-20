import lib.core.getBanner as getBanner 
import lib.core.parseArg as parseArg
import lib.core.getDevice as getDevice
import lib.load.control as control


def handler():
    args = parseArg.cmdArgParser()

    PROCESS = args.name
    PACKAGE = args.spawn
    PID = args.pid
    TYPE_USB = args.usb
    HOST = args.host
    HOOK_CLASS = args.classname

    if PACKAGE == None and PROCESS == None and PID == None:
        getBanner.banner()
        print("[-] Parameter error !")
        return

    # USB | TCP
    #conn_type = ""
    #if TYPE_USB:
    #    conn_type = "usb"
    #elif HOST:
    #    conn_type = "tcp"

    # Get device
    device = getDevice.device(TYPE_USB,HOST)
    if device == "":
        getBanner.banner()
        print("[-] Error: No device was specified.")
        return

    # package | process | pid
    load_type = ""
    if PROCESS:
        load_type = "process"   # attach
    elif PACKAGE:
        load_type = "package"   # spawn
    elif PID:
        load_type = "pid"  # attach

    # echo | enum | hook_exit | hook_llib | hook_lurl | hook_sms | load
    func_type = ""
    if args.load != None:
        func_type = "load"  # !
    elif args.echo:
        func_type = "echo"
    elif args.enum:
        func_type = "enum"
    elif args.hook_exit:
        func_type = "hook_exit"
    elif args.hook_llib:
        func_type = "hook_llib"
    elif args.hook_lurl:
        func_type = "hook_lurl"
    elif args.hook_sms:
        func_type = "hook_sms"

    # debug info
    def info(PROCESS, PACKAGE, PID, TYPE_USB, HOST, HOOK_CLASS, device):
        print("PROCESS: %s\nPACKAGE: %s\nPID: %s\nTYPE_USB: %s\nHOST: %s\nHOOK_CLASS: %s" % (PROCESS,PACKAGE,PID,TYPE_USB,HOST,HOOK_CLASS) )
        print("-"*30)
        print("device: %s" % device)
        print("Function type %s" % func_type)
        print("-"*30)

    # info()
    control.manager(device, load_type, func_type, args)
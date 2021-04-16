'use strict'
setImmediate(function(){
    console.error("[*] Starting script");
    Java.perform(function(){
        try{
            console.warn("[*] Hooking calls to System.exit");
            const System = Java.use("java.lang.System");
            const Log = Java.use("android.util.Log");
            const Exception = Java.use("java.lang.Exception");

            System.exit.implementation = function(){
                console.log("[*] System.exit called");
                console.log(Log.getStackTraceString(Exception.$new()));
            }
        }catch(error){
            console.error("[-] An error occured !");
            console.log(String(error.stack));
        }
    });
});
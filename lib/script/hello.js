'use strict'
if(Java.available){
        Java.perform(function(){
                console.log("");
                console.log("[+] Hello Frida!");
        });
}else{
        console.error("[-] Java is not available");
}
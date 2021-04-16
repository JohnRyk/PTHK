Java.perform(function(){
    try{
        console.log("[*] Start hooking load url... ");
        const webView = Java.use('android.webkit.WebView');
        webView.loadUrl.overloads[0].implementation = function(){
            console.log('android.webkit.WebView("' + Object.values(arguments) + '")');
            return this.loadUrl.overloads[0].apply(this,arguments);
        }
    }catch(error){
        console.error("[-] An error occured !");
        console.log(String(error.stack));
    }
});
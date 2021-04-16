Java.perform(function() {
    var smsManager = Java.use("android.telephony.SmsManager");
    var Base64 = Java.use("android.util.Base64");
    console.log("[*] Start hooking sms... ");
    if (smsManager) {
        smsManager.sendTextMessage.overloads[0].implementation = function(dest) {
            send("call " + smsManager + "->sendTextMessage for " + dest);
            return this.sendTextMessage.overloads[0].apply(this, arguments);
        };
        smsManager.sendDataMessage.overloads[0].implementation = function(dest, source, destPort, data) {
            send("call " + smsManager + "->sendDataMessage for " + dest);
            send("source: " + source);
            send("destPort: " + destPort);
            send("data: " + data);
            var data_string = Object.values(data);
            console.log(data_string);
            console.log(Base64.encodeToString(data,0));
            return this.sendDataMessage.overloads[0].apply(this, arguments);
        };
        smsManager.sendMultipartTextMessage.overloads[0].implementation = function(dest) {
            send("call " + smsManager + "->sendMultipartTextMessage for " + dest);
            return this.sendMultipartTextMessage.overloads[0].apply(this, arguments);
        };
    }
});
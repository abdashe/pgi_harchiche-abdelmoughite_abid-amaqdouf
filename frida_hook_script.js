
// Script Frida pour com.example.app
Java.perform(function() {
    var Cipher = Java.use("javax.crypto.Cipher");
    var HttpURLConnection = Java.use("java.net.HttpURLConnection");
    
    // Hook Cipher.getInstance
    Cipher.getInstance.overload('java.lang.String').implementation = function(algorithm) {
        console.log("[CRYPTO] Cipher algoritme: " + algorithm);
        return this.getInstance(algorithm);
    };
    
    // Hook HttpURLConnection.setRequestProperty
    HttpURLConnection.setRequestProperty.implementation = function(key, value) {
        console.log("[NETWORK] Header: " + key + " = " + value);
        return this.setRequestProperty(key, value);
    };
});

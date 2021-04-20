
# PTHK - Mobie Pentest Hook Kit


```
           _    _                     _          _     _             _     _   _ _   
 _ __  ___| |__(_)___   _ __  ___ _ _| |_ ___ __| |_  | |_  ___  ___| |__ | |_(_) |_ 
| '  \/ _ \ '_ \ / -_) | '_ \/ -_) ' \  _/ -_|_-<  _| | ' \/ _ \/ _ \ / / | / / |  _|
|_|_|_\___/_.__/_\___| | .__/\___|_||_\__\___/__/\__| |_||_\___/\___/_\_\ |_\_\_|\__|
                       |_|                                                                       
                                                                                v1.0
                                                                         Author: JRZ
-------------------------------------------------------------------------------------

Example:
    	Connect over USB: 
    		./pthk.py -U -n <process> --echo
    		./pthk.py -U -f <package> --echo
    		./pthk.py -U -n <process> --enum
    		./pthk.py -U -n <process> -c <class> --enum
    	Connect over TCP (For example: adb forward tcp:8888 tcp:8888): 
    		./pthk.py -H 127.0.0.1:8888 -n <process> --echo
    		./pthk.py -H 127.0.0.1:8888 -f <package> --echo
```

## Tips

`sudo ln -s /home/xyz/.../PTHK/pthk.py /usr/bin/pthk` create a soft link </br>
`./fRid4-sEv3r -l 0.0.0.0:8888` change default listen port </br>
`Ctrl + d` to detach


### Locate class by package name 

```
jrz:~/myTools/PTHK$ ./pthk.py -U -n jakhar.aseem.diva --enum | grep diva
jakhar.aseem.diva.MainActivity
jakhar.aseem.diva.NotesProvider
jakhar.aseem.diva.NotesProvider$DBHelper
```

### Locate method by method name

```
jrz:~/myTools/PTHK$ ./pthk.py -U -n jakhar.aseem.diva --enum -c jakhar.aseem.diva.MainActivity | grep Create
dispatchFragmentsOnCreateView
mCreated
onCreate
onCreateContextMenu
onCreateDescription
onCreateDialog
onCreateNavigateUpTaskStack
onCreateOptionsMenu
onCreatePanelMenu
...
```



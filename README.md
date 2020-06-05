# Live_cc_checker
This script will check live cc and Grab proxy and check proxy if its working or not
```
>>>  _      _                             _               _             
>>> | |    (_)                           | |             | |            
>>> | |     ___   _____    ___ ___    ___| |__   ___  ___| | _____ _ __ 
>>> | |    | \ \ / / _ \  / __/ __|  / __| '_ \ / _ \/ __| |/ / _ \ '__|
>>> | |____| |\ V /  __/ | (_| (__  | (__| | | |  __/ (__|   <  __/ |   
>>> |______|_| \_/ \___|  \___\___|  \___|_| |_|\___|\___|_|\_\___|_|   
>>>                                                                                  
>>>                                               Coded by script1337
>>>                            Github : https://github.com/ScRiPt1337
>>>         
>>>     Examples{
>>>                     ./chxd checkproxy /path/to/proxylist 100 >>> {Check if proxy is working or not}
>>>                     ./chxd grabproxy 100 1000 >>> {Grab https proxys}
>>>                     ./chxd creditC proxy.txt cc.txt >>> {To check credit card is valid or not}
>>>                     ./chxd creditC proxy.txt cc.txt config.txt >>> {check credit cards using coustm api with common success response}
>>>                     ./chxd creditC proxy.txt cc.txt config.txt success.txt >>> {check credit cards using coustm api}
```

> how to use your own api with live cc checker

```
# grab the request with burp suite which contain your credit card number and replace them with FUZZ_CC 
# replace month with FUZZ_MN
# replace year with FUZZ_YR
# replace cvv with FUZZ_CVV
# DNT: 1 add this in the end of your header
# and your can run this command 
# ./chxd creditC proxy.txt cc.txt config.txt

# you also can specify the success response using this command {if any string from success.txt found in response thats  be mean card is valid }
# ./chxd creditC proxy.txt cc.txt config.txt success.txt
```
> it's only for Education Purposes
> I am not going to be responsible for anything

> if your using linux can run chxd
> if your using windows run winchxd.exe in cmd ( Dont just double click it run it using cmd )

> how to use video : https://www.youtube.com/watch?v=g_Hc2kmtatg

> join us here: https://discord.gg/gkGA44z

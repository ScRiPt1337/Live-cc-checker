import os
import sys
from time import sleep
import subprocess


def run(hell,ninja,script,debug):
    if str(os.name).startswith("n"):
        os.system("wsl chmod +x chxd")
        os.system("wsl ./chxd " + hell + " " + ninja + " " + script + " " + debug)
    else:
        os.system("chmod +x chxd")
        os.system("./chxd " + hell + " " + ninja + " " + script + " " + debug)


def checkwsl():
    result = subprocess.check_output("wsl -e uname", shell=True)
    if result == "Linux":
        return True
    else:
        return False
    
banner = """
                          _             
                         (_)            
__      ____ _ _ __ _ __  _ _ __   __ _ 
\ \ /\ / / _` | '__| '_ \| | '_ \ / _` |
 \ V  V / (_| | |  | | | | | | | | (_| |
  \_/\_/ \__,_|_|  |_| |_|_|_| |_|\__, |
                                   __/ |
                                  |___/ 
"""        
banner += "Make sure wsl is installed\n"
banner += "If its not install\n"
banner += "you can watch this vidoe and installed it!\n"
banner += "https://www.youtube.com/watch?v=wM-wBciLeDw"

#print(banner)
checkxz = checkwsl()
if checkxz:
    pass
else:
    print(banner)
    sys.exit()
try:
    try:
        hell = sys.argv[1]
        ninja = sys.argv[2]
        script = sys.argv[3]
    except:
        if str(os.name).startswith("n"):
            os.system("wsl ./chxd")
        else:
            os.system("./chxd")
        sys.exit()
    try:
        debug = sys.argv[4]
    except:
        debug = "False"
    run(hell,ninja,script,debug)
except Exception as e:
    print(e)
    

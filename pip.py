import os , os.path , sys , readline

def modcmd(arg):
    os.system(sys.executable+" "+sys.prefix+"/bin/"+arg)

if not (os.path.exists(sys.prefix+"/bin/pip")):
    print("Debes instalar pip primero")

while 1:
     cmd = input('--->')
     if (cmd==""): break;
     modcmd(cmd)        
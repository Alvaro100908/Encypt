#-*- coding: utf-8 -*-
#marshal py3
import os,sys,time,marshal
from rich.panel import Panel as nel
from rich import print as cetak

if sys.version[0] in '2':
        exit("[sorry] use python version 3")

sys.stdout.write('\x1b]2; Encrypt Alvaro\x07')
###------------------[ Colorv1 ]---------------------###
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
white = '\33[0;37m' #PUTIH
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +

os.system('clear')
print(' • Subscribe Dulu Channel Aink •')
os.system('xdg-open https://youtube.com/@AlvaroGaming390 ')
time.sleep(2)



bannerpy = """
\x1b[1;91m     ╔╦╗┌─┐┬─┐┌─┐┬ ┬┌─┐┬ 
\x1b[1;97m     ║║║├─┤├┬┘└─┐├─┤├─┤│
\x1b[1;97m     ╩ ╩┴ ┴┴└─└─┘┴ ┴┴ ┴┴─┘ Update V3
\x1b[1;97m     Creator\x1b[1;91m :\x1b[1;97m Alvaro
\x1b[1;97m     Tiktok\x1b[1;91m :\x1b[1;97m  alvarotiktok1786
\x1b[1;97m     Youtube\x1b[1;91m :\x1b[1;97m Alvaro gaming\n
"""

def bannerpy3():
          try:
              os.system('clear')
              print(bannerpy)
              cetak(nel ('[-] Contoh > /sdcard/file.py'))
              file = input ('  [-] File Kamu : ')
              o = file.replace('.py', '')
          except KeyboardInterrupt:
              sys.exit()
          else:
              try:
                  strng = open(file, 'r').read()
              except IOError:
                  print ('\n Error No such file or directory\n')
                  sys.exit()
              try:
                  code = compile(strng,'','exec')
                  data = marshal.dumps(code)
              except TypeError:
                  print ('File already to compiled\n') 
                  sys.exit()

          fileout = open(o + '_enc.py', 'w')
          fileout.write('#Compiled By Alvaro\n')
          fileout.write('#https://github.com/Dra-ID\n#Youtube: Vindra ID\n')
          fileout.write('import marshal\n')
          fileout.write('exec(marshal.loads(' + repr(data) + '))')
          fileout.close()
          time.sleep(3) 
          print ('\n  [-]File Succes Di Compiled : ' + u + o + '_enc.py\n')
          time.sleep(3)
          vindra = input ('  [-] Ingin encrypt lagi? [Y/N] ')
          if vindra =="":
                      cetak(nel('Command not found !'))
                      sys.exit()
          elif vindra =="y" or vindra =="Y":
                      bannerpy3()
          else:
                      if vindra =="n" or vindra =="N":
                                  cetak(nel('   > Terimakasih bos ;v'))
                      else:
                                  cetak(nel('   Command not found !'))
                                  sys.exit()


if __name__=='__main__':
        try:os.system('git pull')
        except:pass
        bannerpy3()

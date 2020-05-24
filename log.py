from getpass import getpass
import os
import time

def menu():
      while True:
           print("")
           os.system("clear")
           print('\033[1;36;40m<─────────────── v.1.2 ───────────────>')
           print('')
           os.system('date | lolcat')
           print("\033[1;93m")
           print(" \033[1;92m      TEACH THE LEARNED THINGS)")
           print(" \033[1;92m  STAY CONNECT WITH MATHEESH-TECH)")
           print("\033[1;93m")
           print("  <───────[ MATHEESH TECH ]───────>")
           print("")
           try:
                x = str(input('\033[1;92mUsername \033[1;93m: '))
                print("")
                e = getpass('\033[1;92mPassword \033[1;93m: ')
                print ("")
                if x=="matheesh" and e=="matheesh":
                   print('wait...')
                   time.sleep(1)
                   os.system('clear')
                   print('')
                   os.system('figlet ' + x + ' | lolcat')
                   print('\033[1;92m ────────────────────────────────────── ')
                   print("")
                   break
                else:
                      print("")
                      print("")
                      print("\033[1;91m     Wrong Password")
                      print("")
           except Exception:
                      
                      print("")
                      print("")
                      print("\033[1;91m     Wrong Password")
           except KeyboardInterrupt:
                      print("")
                      os.system('killall -9 com.termux')
                      print("")
                      print("")
                      print("\033[1;91m     Wrong Password")
menu()

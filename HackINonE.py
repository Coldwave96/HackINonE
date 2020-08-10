#!/usr/bin/env python3
# coding: UTF-8

import os
import sys
import socket
from time import sleep
from platform import system

def logo():
    banner = '''
______  __            ______      ____________   __               __________
___  / / /_____ _________  /__    ____  _/__  | / /  ________________  ____/
__  /_/ /_  __ `/  ___/_  //_/     __  / __   |/ /   _  __ \_  __ \_  __/   
_  __  / / /_/ // /__ _  ,<       __/ /  _  /|  /    / /_/ /  / / /  /___   
/_/ /_/  \__,_/ \___/ /_/|_|      /___/  /_/ |_/     \____//_/ /_//_____/   {}
                                                            
                                                            Produced by Coldsnap
                                                            
               [*] Personal Blog: https://coldwave96.github.io [*]
               [*]   https://github.com/Coldwave96/HackINonE   [*]
               [*]    Please Don't Use It As An Illegal Way    [*]
    '''.format(version)
    print(banner)

class Main:
    def __init__(self):
        logo()

    def clear(self):
        if system() == 'Linux':
            os.system('clear')
        if system() == 'Windows':
            os.system('cls')

    def check_num(self, num, func, keys):
        if num == '':
            self.clear()
            func()

        if not num in keys:
            print('Out Of The Function List =.=')
            sleep(1)
            self.clear()
            func()

    def menu(self):
        self.clear()
        logo()
        print('''
        [01] Hide Yourself
        [02] Gather Information
        [99] Update or Uninstall
        [00] Exit
        ''')

        func_menu = {
            '01':self.hide,
            '02':self.info,
            '00':self.exit,
            '99':self.update
        }

        num = input('HackINonE $$ ')

        if len(num) == 1:
            num = '0' + num

        self.check_num(num, self.menu, func_menu.keys())

        func_menu[num]()

    def exit(self):
        print('Thank You For Supporting ^.^')
        sleep(1)
        self.clear()
        sys.exit()

    ###### Module[01] ######
    def hide(self):
        self.clear()
        os.system('figlet -f standard -c Hacker Hiding Tools | lolcat | boxes -d dog -a hcvc')

        print('''
            [01] Anonmously Surf
            [02] Multitor
            [00] Back
        ''')

        func_hide = {
            '01':self.anonsurf,
            '02':self.multitor,
            '00':self.menu
        }

        num = input('HackINonE $$ ')

        if len(num) == 1:
            num = '0' + num

        self.check_num(num, self.hide, func_hide.keys())

        func_hide[num]()

    def anonsurf(self):
        self.clear()
        os.system('echo \"Anonsurf will anonymize the entire system under TOR using IPTables. It will also allow you to start and stop i2p as well.\" | lolcat | boxes -d peek -a hcvc')
        num = input('[1]Install [2]Run [3]Stop [0]Main Menu $$ ')

        self.check_num(num, self.anonsurf, ['1', '2', '3', '0'])

        if num == '1':
            os.system("cd /usr/share/doc/HackINonE && sudo git clone https://github.com/Und3rf10w/kali-anonsurf.git")
            os.system("cd kali-anonsurf && sudo ./installer.sh && cd .. && sudo rm -r kali-anonsurf")
            self.anonsurf()

        if num == '2':
            os.system("sudo anonsurf start")
            self.anonsurf()

        if num == '3':
            os.system("sudo anonsurf stop")
            self.anonsurf()

        if num == '0':
            self.menu()

    def multitor(self):
        self.clear()
        os.system('echo \"Multitor provides one single endpoint for clients. Supports HAProxy, socks protocol and http-proxy servers: polipo, privoxy and hpts.\" | lolcat | boxes -d peek -a hcvc')
        num = input('[1]Install [0]Back $$ ')

        self.check_num(num, self.multitor, ['1', '0'])

        if num == '1':
            os.system("cd /usr/share/doc/HackINonE && sudo git clone https://github.com/trimstray/multitor")
            os.system("cd multitor;sudo bash setup.sh install")
            self.multitor()

        if num == '0':
            self.hide()

    ###### Module[02] ######
    def info(self):
        self.clear()
        os.system("figlet -f standard -c Information Gathering Tools | lolcat | boxes -d dog -a hcvc")

        print('''
            [01] Nmap
            [00] Back
        ''')

        func_info = {
            '01':self.nmap,
            '00':self.menu
        }

        num = input('HackINonE $$ ')

        if len(num) == 1:
            num = '0' + num

        self.check_num(num, self.info, func_info.keys())

        func_info[num]()

    def nmap(self):
        self.clear()
        os.system('echo \"Nmap - the Network Mapper\" | lolcat | boxes -d peek -a hcvc')
        num = input('[1]Install [2]Start [0]Back $$ ')

        self.check_num(num, self.nmap, ['1', '2', '0'])

        if num == '1':
            os.system("cd /usr/share/doc/HackINonE && sudo git clone https://github.com/nmap/nmap.git")
            os.system("sudo chmod -R 755 nmap && cd nmap && sudo ./configure && make && sudo make install")
            self.nmap()

        if num == '2':
            self.ports()

        if num == '0':
            self.info()

    def ports(self):
        self.clear()
        target = input('Select a Target IP: ')
        os.system(f"sudo nmap -A -T4 -v -Pn {target}")
        input('\nPress Enter to back...')
        self.info()

    ###### Module[99] ######
    def update(self):
        self.clear()
        logo()
        print("""
            [01] Update Tool or System 
            [02] Uninstall HackingTool
            [00] Back
        """)

        func_update = {
            '01':self.updatesys,
            '02':self.uninstall,
            '00':self.menu
        }

        num = input('HackINonE $$ ')

        if len(num) == 1:
            num = '0' + num

        self.check_num(num, self.update, func_update.keys())

        func_update[num]()

    def updatesys(self):
        self.clear()
        num = input("[1]Update System [2]Update HackINonE [0]Back $$ ")

        self.check_num(num, self.updatesys, ['1', '2', '0'])

        if num == "1":
            os.system("sudo apt update && sudo apt full-upgrade -y")
            os.system("sudo apt-get install tor openssl curl && sudo apt-get update tor openssl curl ")
            os.system("sudo apt-get install python3-pip")
            self.updatesys()

        if num == "2":
            os.system("sudo chmod +x /etc/;sudo chmod +x /usr/share/doc;sudo rm -rf /usr/share/doc/HackINonE/;cd /etc/;sudo rm -rf /etc/HackINonE/;mkdir HackINonE;cd HackINonE;git clone https://github.com/Coldwave96/HackINonE.git;cd HackINonE;sudo chmod +x install.sh;./install.sh")
            self.updatesys()

        if num == "0":
            self.menu()

    def uninstall(self):
        self.clear()
        num = input("[1]Uninstall [0]Back $$ ")

        self.check_num(num, self.uninstall, ['1', '0'])

        if num == "1":
            print("HackINonE started to uninstall..\n")
            sleep(1)
            os.system("sudo chmod +x /etc/;sudo chmod +x /usr/share/doc;sudo rm -rf /usr/share/doc/HackINonE/;cd /etc/;sudo rm -rf /etc/HackINonE/;")
            print("\nHackINonE Successfully Uninstall..")
            self.exit()

        if num == "0":
            self.update()

if __name__ == '__main__':
    version = 'v0.11'
    run = Main()
    try:
        if system() == 'Linux':
            os.system('clear')
            run.menu()

        # If not Linux and probably Windows
        elif system() == "Windows":
            print("Please Run This Tool In Debian System For Best Result.")
            sleep(2)

        else:
            print("Please Check Your Sytem or Open new issue ...")

    except KeyboardInterrupt:
        print("\nExiting ..!!!")
        sleep(2)

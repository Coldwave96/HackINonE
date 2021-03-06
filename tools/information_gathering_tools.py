# coding=utf-8
import os
import socket
import subprocess
import webbrowser

from core import HackINonE
from core import HackINonECollection
from core import clear_screen


class NMAP(HackINonE):
    TITLE = "Network Map (nmap)"
    DESCRIPTION = "Free and open source utility for network discovery and security auditing"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/nmap/nmap.git",
        "sudo chmod -R 755 nmap && cd nmap && sudo ./configure && make && sudo make install"
    ]
    PROJECT_URL = "https://github.com/nmap/nmap"

    def __init__(self):
        super(NMAP, self).__init__(runnable=False)


class Dracnmap(HackINonE):
    TITLE = "Dracnmap"
    DESCRIPTION = "Dracnmap is an open source program which is using to \n" \
                  "exploit the network and gathering information with nmap help."
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/Screetsec/Dracnmap.git",
        "cd Dracnmap && chmod +x Dracnmap.sh"
    ]
    PROJECT_URL = "https://github.com/Screetsec/Dracnmap"

    def __init__(self):
        super(Dracnmap, self).__init__(runnable=False)


class PortScan(HackINonE):
    TITLE = "Port scanning"

    def __init__(self):
        super(PortScan, self).__init__(installable=False)

    def run(self):
        clear_screen()
        target = input('Select a Target IP: ')
        subprocess.run(["sudo", "nmap", "-O", "-Pn", target])


class Host2IP(HackINonE):
    TITLE = "Host to IP "

    def __init__(self):
        super(Host2IP, self).__init__(installable=False)

    def run(self):
        clear_screen()
        host = input("Enter host name (e.g. www.google.com):-  ")
        ips = socket.gethostbyname(host)
        print(ips)


class XeroSploit(HackINonE):
    TITLE = "Xerosploit"
    DESCRIPTION = "Xerosploit is a penetration testing toolkit whose goal is to perform\n" \
                  "man-in-the-middle attacks for testing purposes"
    INSTALL_COMMANDS = [
        "git clone https://github.com/LionSec/xerosploit.git",
        "cd xerosploit && sudo python install.py"
    ]
    RUN_COMMANDS = ["sudo xerosploit"]
    PROJECT_URL = "https://github.com/LionSec/xerosploit"


class RedHawk(HackINonE):
    TITLE = "RED HAWK (All In One Scanning)"
    DESCRIPTION = "All in one tool for Information Gathering and Vulnerability Scanning."
    INSTALL_COMMANDS = ["git clone https://github.com/Tuhinshubhra/RED_HAWK.git"]
    RUN_COMMANDS = ["cd RED_HAWK;php rhawk.php"]
    PROJECT_URL = "https://github.com/Tuhinshubhra/RED_HAWK"


class ReconSpider(HackINonE):
    TITLE = "ReconSpider(For All Scaning)"
    DESCRIPTION = "ReconSpider is most Advanced Open Source Intelligence (OSINT)" \
                  " Framework for scanning IP Address, Emails, \n" \
                  "Websites, Organizations and find out information from" \
                  " different sources.\n"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/bhavsec/reconspider.git",
        "sudo apt install python3 python3-pip && cd reconspider && sudo python3 setup.py install"
    ]
    PROJECT_URL = "https://github.com/bhavsec/reconspider"

    def __init__(self):
        super(ReconSpider, self).__init__(runnable=False)


class IsItDown(HackINonE):
    TITLE = "IsItDown (Check Website Down/Up)"
    DESCRIPTION = "Check Website Is Online or Not"

    def __init__(self):
        super(IsItDown, self).__init__(
            [('Open', self.open)], installable=False, runnable=False)

    def open(self):
        webbrowser.open_new_tab("https://www.isitdownrightnow.com/")


class Infoga(HackINonE):
    TITLE = "Infoga - Email OSINT"
    DESCRIPTION = "Infoga is a tool gathering email accounts informations\n" \
                  "(ip, hostname, country,...) from different public source"
    INSTALL_COMMANDS = [
        "git clone https://github.com/m4ll0k/Infoga.git",
        "cd infoga;sudo python setup.py install"
    ]
    RUN_COMMANDS = ["cd infoga;python infoga.py"]
    PROJECT_URL = "https://github.com/m4ll0k/Infoga"


class ReconDog(HackINonE):
    TITLE = "ReconDog"
    DESCRIPTION = "ReconDog Information Gathering Suite"
    INSTALL_COMMANDS = ["git clone https://github.com/s0md3v/ReconDog.git"]
    RUN_COMMANDS = ["cd ReconDog;sudo python dog"]
    PROJECT_URL = "https://github.com/s0md3v/ReconDog"


class Striker(HackINonE):
    TITLE = "Striker"
    DESCRIPTION = "Recon & Vulnerability Scanning Suite"
    INSTALL_COMMANDS = [
        "git clone https://github.com/s0md3v/Striker.git",
        "cd Striker && pip3 install -r requirements.txt"
    ]
    PROJECT_URL = "https://github.com/s0md3v/Striker"

    def run(self):
        site = input("Enter Site Name (example.com) >> ")
        os.system("cd Striker;")
        subprocess.run(["sudo", "python3", "striker.py", site])


class SecretFinder(HackINonE):
    TITLE = "SecretFinder (like API & etc)"
    DESCRIPTION = "SecretFinder - A python script for find sensitive data \n" \
                  "like apikeys, accesstoken, authorizations, jwt,..etc \n " \
                  "and search anything on javascript files.\n\n " \
                  "Usage: python SecretFinder.py -h"
    INSTALL_COMMANDS = [
        "git clone https://github.com/m4ll0k/SecretFinder.git secretfinder",
        "cd secretfinder; sudo pip3 install -r requirements.txt"
    ]
    PROJECT_URL = "https://github.com/m4ll0k/SecretFinder"

    def __init__(self):
        super(SecretFinder, self).__init__(runnable=False)


class Shodan(HackINonE):
    TITLE = "Find Info Using Shodan"
    DESCRIPTION = "Get ports, vulnerabilities, informations, banners,..etc \n " \
                  "for any IP with Shodan (no apikey! no rate limit!)\n" \
                  "[X] Don't use this tool because your ip will be blocked by Shodan!"
    INSTALL_COMMANDS = ["git clone https://github.com/m4ll0k/Shodanfy.py.git"]
    PROJECT_URL = "https://github.com/m4ll0k/Shodanfy.py"

    def __init__(self):
        super(Shodan, self).__init__(runnable=False)


class PortScannerRanger(HackINonE):
    TITLE = "Port Scanner - rang3r"
    DESCRIPTION = "rang3r is a python script which scans in multi thread\n " \
                  "all alive hosts within your range that you specify."
    INSTALL_COMMANDS = [
        "git clone https://github.com/floriankunushevci/rang3r.git;"
        "sudo pip install termcolor"
    ]
    PROJECT_URL = "https://github.com/floriankunushevci/rang3r"

    def run(self):
        ip = input("Enter Ip >> ")
        os.system("cd rang3r;")
        subprocess.run(["sudo", "python", "rang3r.py", "--ip", ip])


class Breacher(HackINonE):
    TITLE = "Breacher"
    DESCRIPTION = "An advanced multithreaded admin panel finder written in python."
    INSTALL_COMMANDS = ["git clone https://github.com/s0md3v/Breacher.git"]
    PROJECT_URL = "https://github.com/s0md3v/Breacher"

    def __init__(self):
        super(Breacher, self).__init__(runnable=False)


class XCDN(HackINonE):
    TITLE = "XCDN"
    DESCRIPTION = "Try to find out the real ip behind cdn."
    INSTALL_COMMANDS = ["git clone https://github.com/3xp10it/xcdn.git"]
    PROJECT_URL = "https://github.com/3xp10it/xcdn"

    def run(self):
        url = input("Enter Url >> ")
        os.system('cd xcdn')
        subprocess.run(['sudo', 'python3', 'xdn.py', url])


class TideFinger(HackINonE):
    TITLE = "TideFinger"
    DESCRIPTION = "A tool which is used for analysing web finger."
    INSTALL_COMMANDS = [
        "git clone https://github.com/TideSec/TideFinger.git;"
        "sudo pip install lxml requests bs4"
    ]
    PROJECT_URL = "https://github.com/TideSec/TideFinger"

    def run(self):
        url = input("Enter Url >> ")
        os.system("cd TideFinger")
        subprocess.run(['sudo', 'python', 'TiderFinger.py', '-u', url])


class GooHak(HackINonE):
    TITLE = "GooHak"
    DESCRIPTION = "Automatically Launch Google Hacking Queries Against A Target Domain."
    INSTALL_COMMANDS = [
        "git clone https://github.com/1N3/Goohak.git",
        "cd Goohak; sudo chmod +x goohak"
    ]
    PROJECT_URL = "https://github.com/1N3/Goohak"

    def run(self):
        target = input("Enter Domain >> ")
        os.system('cd Goohak')
        subprocess.run(['sudo', './goohak', target])


class GitMiner(HackINonE):
    TITLE = "GitMiner"
    DESCRIPTION = "Tool for advanced mining for content on Github."
    INSTALL_COMMANDS = [
        "git clone http://github.com/UnkL4b/GitMiner",
        "cd GitMiner; sudo pip3 install -r requirements.txt"
    ]
    PROJECT_URL = "https://github.com/UnkL4b/GitMiner"

    def __init__(self):
        super(GitMiner, self).__init__(runnable=False)


class R3con1z3r(HackINonE):
    TITLE = "R3con1z3r"
    DESCRIPTION = "R3con1z3r is a lightweight Web information gathering tool \n" \
                  "with an intuitive features written in python.\n" \
                  "it provides a powerful environment in which open source intelligence (OSINT) " \
                  "\nweb-based footprinting can be conducted quickly and thoroughly."
    INSTALL_COMMANDS = ["pip install r3con1z3r"]
    RUN_COMMANDS = ['r3con1z3r']
    PROJECT_URL = "https://github.com/abdulgaphy/r3con1z3r"


class Dumpall(HackINonE):
    TITLE = "Dump all"
    DESCRIPTION = "/.git /.svn /.DS_Store folder disclosure exploit tool."
    INSTALL_COMMANDS = ["pip install dumpall"]
    PROJECT_URL = "https://github.com/0xHJK/dumpall"

    def run(self):
        target = input("Enter Url >> ")
        subprocess.run(['sudo', 'dumpall', '-u', target])


class InformationGatheringTools(HackINonECollection):
    TITLE = "Information gathering tools"
    TOOLS = [
        NMAP(),
        Dracnmap(),
        PortScan(),
        Host2IP(),
        XeroSploit(),
        RedHawk(),
        ReconSpider(),
        IsItDown(),
        Infoga(),
        ReconDog(),
        Striker(),
        SecretFinder(),
        Shodan(),
        PortScannerRanger(),
        Breacher(),
        XCDN(),
        TideFinger(),
        GooHak(),
        GitMiner(),
        R3con1z3r(),
        Dumpall()
    ]

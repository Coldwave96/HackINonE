# coding=utf-8
import os
import subprocess

from core import HackINonE
from core import HackINonECollection


class Web2Attack(HackINonE):
    TITLE = "Web2Attack"
    DESCRIPTION = "Web hacking framework with tools, exploits by python"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/santatic/web2attack.git"]
    RUN_COMMANDS = ["cd web2attack && sudo bash w2aconsole"]
    PROJECT_URL = "https://github.com/santatic/web2attack"


class Skipfish(HackINonE):
    TITLE = "Skipfish"
    DESCRIPTION = "Skipfish – Fully automated, active web application " \
                  "security reconnaissance tool \n " \
                  "Usage: skipfish -o [FolderName] targetip/site"
    RUN_COMMANDS = [
        "sudo skipfish -h",
        'echo "skipfish -o [FolderName] targetip/site"|boxes -d headline | lolcat'
    ]

    def __init__(self):
        super(Skipfish, self).__init__(installable=False)


class SubDomainFinder(HackINonE):
    TITLE = "SubDomain Finder"
    DESCRIPTION = "Sublist3r is a python tool designed to enumerate " \
                  "subdomains of websites using OSINT \n " \
                  "Usage:\n\t" \
                  "[1] python sublist3r.py -d example.com \n" \
                  "[2] python sublist3r.py -d example.com -p 80,443"
    INSTALL_COMMANDS = [
        "sudo pip install requests argparse dnspython",
        "sudo git clone https://github.com/aboul3la/Sublist3r.git",
        "cd Sublist3r && sudo pip install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd Sublist3r && python sublist3r.py -h"]
    PROJECT_URL = "https://github.com/aboul3la/Sublist3r"


class CheckURL(HackINonE):
    TITLE = "CheckURL"
    DESCRIPTION = "Detect evil urls that uses IDN Homograph Attack.\n\t" \
                  "[!] python3 checkURL.py --url google.com"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/UndeadSec/checkURL.git"]
    RUN_COMMANDS = ["cd checkURL && python3 checkURL.py --help"]
    PROJECT_URL = "https://github.com/UndeadSec/checkURL"


class Blazy(HackINonE):
    TITLE = "Blazy(Also Find ClickJacking)"
    DESCRIPTION = "Blazy is a modern login page bruteforcer"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/UltimateHackers/Blazy.git",
        "cd Blazy && sudo pip install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd Blazy && sudo python blazy.py"]
    PROJECT_URL = "https://github.com/UltimateHackers/Blazy"


class SubDomainTakeOver(HackINonE):
    TITLE = "Sub-Domain TakeOver"
    DESCRIPTION = "Sub-domain takeover vulnerability occur when a sub-domain " \
                  "\n (subdomain.example.com) is pointing to a service " \
                  "(e.g: GitHub, AWS/S3,..)\n" \
                  "that has been removed or deleted.\n" \
                  "Usage:python3 takeover.py -d www.domain.com -v"
    INSTALL_COMMANDS = [
        "git clone https://github.com/m4ll0k/takeover.git",
        "cd takeover;sudo python3 setup.py install"
    ]
    PROJECT_URL = "https://github.com/m4ll0k/takeover"

    def __init__(self):
        super(SubDomainTakeOver, self).__init__(runnable=False)


class Dirb(HackINonE):
    TITLE = "Dirb"
    DESCRIPTION = "DIRB is a Web Content Scanner. It looks for existing " \
                  "(and/or hidden) Web Objects.\n" \
                  "It basically works by launching a dictionary based " \
                  "attack against \n a web server and analizing the response."
    INSTALL_COMMANDS = [
        "sudo git clone https://gitlab.com/kalilinux/packages/dirb.git",
        "cd dirb;sudo ./configure;make"
    ]
    PROJECT_URL = "https://gitlab.com/kalilinux/packages/dirb"

    def run(self):
        url = input("Enter Url >> ")
        subprocess.run(["sudo", "dirb", url])


class Subdomain3(HackINonE):
    TITLE = "Subdomain3"
    DESCRIPTION = "Subdomain3 is a new generation of tool , It helps penetration testers " \
                  "\n to discover more information in a shorter time than other tools." \
                  "\n The information includes subdomains, IP, CDN, and so on."
    INSTALL_COMMANDS = [
        'git clone https://github.com/yanxiu0614/subdomain3.git',
        'cd subdomain3;sudo pip install -r requirement.txt'
    ]
    PROJECT_URL = "https://github.com/yanxiu0614/subdomain3"

    def run(self):
        target = input("Enter Domain >> ")
        os.system('cd subdomain3')
        subprocess.run(["sudo", "python3", "brutedns.py", '-d', target, '-s', 'high', "-l", "5"])


class WAFW00F(HackINonE):
    TITLE = "WAFW00F"
    DESCRIPTION = "The Web Application Firewall Fingerprinting Tool. "
    INSTALL_COMMANDS = [
        "git clone https://github.com/EnableSecurity/wafw00f.git",
        "cd wafw00f;sudo python setup.py install"
    ]
    PROJECT_URL = "https://github.com/EnableSecurity/wafw00f"

    def run(self):
        url = input("Enter Url >> ")
        subprocess.run(['wafw00f', url])


class Xwaf(HackINonE):
    TITLE = "XWAF"
    DESCRIPTION = "Automatic bypass waf by brute force."
    INSTALL_COMMANDS = ["git clone https://github.com/3xp10it/xwaf.git"]
    PROJECT_URL = "https://github.com/3xp10it/xwaf"

    def __init__(self):
        super(Xwaf, self).__init__(runnable=False)


class WhatWaf(HackINonE):
    TITLE = "WhatWaf"
    DESCRIPTION = "Detect and bypass web application firewalls and protection systems."
    INSTALL_COMMANDS = [
        "git clone https://github.com/ekultek/whatwaf.git",
        "cd whatwaf && sudo chmod +x setup.sh && sudo ./setup.sh install"
    ]
    RUN_COMMANDS = ["whatwaf"]
    PROJECT_URL = "https://github.com/ekultek/whatwaf"

class ScanT3r(HackINonE):
    TITLE = "ScanT3r"
    DESCRIPTION = "Scant3r - web application vulnerability scanner"
    INSTALL_COMMANDS = [
        "git clone https://github.com/knassar702/scant3r",
        "cd scant3r && pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["python3 scant3r.py -h"]
    PROJECT_URL = "https://github.com/knassar702/scant3r"


class WebAttackTools(HackINonECollection):
    TITLE = "Web Attack tools"
    DESCRIPTION = ""
    TOOLS = [
        Web2Attack(),
        Skipfish(),
        SubDomainFinder(),
        CheckURL(),
        Blazy(),
        SubDomainTakeOver(),
        Dirb(),
        Subdomain3(),
        WAFW00F(),
        Xwaf(),
        WhatWaf(),
        ScanT3r()
    ]

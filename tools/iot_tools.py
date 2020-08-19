# coding=utf-8
from core import HackINonE
from core import HackINonECollection


class RouterSploit(HackINonE):
    TITLE = "RouterSploit"
    DESCRIPTION = "Exploitation Framework for Embedded Devices"
    INSTALL_COMMANDS = [
        "git clone https://www.github.com/threat9/routersploit",
        'cd routersploit; sudo python3 -m pip install -r requirements.txt'
    ]
    RUN_COMMANDS = ['cd routersploit && sudo python3 rsf.py']
    PROJECT_URL = "https://github.com/threat9/routersploit"


class PRET(HackINonE):
    TITLE = "PRET"
    DESCRIPTION = "Printer Exploitation Toolkit - The tool that made dumpster diving obsolete.\n" \
                  "Usage: pret.py [-h] [-s] [-q] [-d] [-i file] [-o file] target {ps,pjl,pcl}"
    INSTALL_COMMANDS = [
        "git clone https://github.com/RUB-NDS/PRET.git",
        "sudo pip install colorama pysnmp",
        "sudo apt-get install imagemagick ghostscript"
    ]
    PROJECT_URL = "https://github.com/RUB-NDS/PRET"

    def __init__(self):
        super(PRET, self).__init__(runnable=False)


class IOTTools(HackINonECollection):
    TITLE = "IOT Tools"
    TOOLS = [
        RouterSploit(),
        PRET()
    ]

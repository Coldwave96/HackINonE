# coding=utf-8
from core import HackINonE
from core import HackINonECollection


class BBScan(HackINonE):
    TITLE = "BBScan"
    DESCRIPTION = "A fast vulnerability scanner."
    INSTALL_COMMANDS = [
        "git clone https://github.com/lijiejie/BBScan.git",
        "cd BBScan; pip install -r requirements.txt"
    ]
    PROJECT_URL = "https://github.com/lijiejie/BBScan"

    def __init__(self):
        super(BBScan, self).__init__(runnable=False)


class W9scan(HackINonE):
    TITLE = "w9scan"
    DESCRIPTION = "Plug-in type web vulnerability scanner "
    INSTALL_COMMANDS = ["git clone https://github.com/w-digital-scanner/w9scan.git"]
    RUN_COMMANDS = ["cd w9scan && sudo python w9scan.py"]
    PROJECT_URL = "https://github.com/w-digital-scanner/w9scan"


class VulnScanTools(HackINonECollection):
    TITLE = "Vulnerablities Scanner"
    TOOLS = [
        BBScan(),
        W9scan()
    ]

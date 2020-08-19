# coding=utf-8
import os
from time import sleep

from core import HackINonE
from core import HackINonECollection


class UpdateTool(HackINonE):
    TITLE = "Update Tool or System"
    DESCRIPTION = "Update Tool or System"

    def __init__(self):
        super(UpdateTool, self).__init__([
            ("Update System", self.update_sys),
            ("Update HackINonE", self.update_ht)
        ], installable=False, runnable=False)

    def update_sys(self):
        os.system("sudo apt update && sudo apt full-upgrade -y")
        os.system("sudo apt-get install tor openssl curl && sudo apt-get update tor openssl curl")
        os.system("sudo apt-get install python3-pip")

    def update_ht(self):
        os.system("sudo chmod +x /etc/;"
                  "sudo chmod +x /usr/share/doc;"
                  "sudo rm -rf /usr/share/doc/HackINonE/;"
                  "cd /etc/;"
                  "sudo rm -rf /etc/hackINone/;"
                  "mkdir HackINonE;"
                  "cd HackINonE;"
                  "git clone https://github.com/Coldwave96/HackINonE.git;"
                  "cd HackINonE;"
                  "sudo chmod +x install.sh;"
                  "./install.sh")


class UninstallTool(HackINonE):
    TITLE = "Uninstall HackINonE"
    DESCRIPTION = "Uninstall HackINonE"

    def __init__(self):
        super(UninstallTool, self).__init__([
            ('Uninstall', self.uninstall)
        ], installable=False, runnable=False)

    def uninstall(self):
        print("HackINonE started to uninstall..\n")
        sleep(1)
        os.system("sudo chmod +x /etc/;"
                  "sudo chmod +x /usr/share/doc;"
                  "sudo rm -rf /usr/share/doc/HackINonE/;"
                  "cd /etc/;"
                  "sudo rm -rf /etc/hackINone/;")
        print("\nHackINonE Successfully Uninstalled..")
        print("Happy Hacking..!!")
        sleep(1)


class ToolManager(HackINonECollection):
    TITLE = "Update or Uninstall | HackINonE"
    TOOLS = [
        UpdateTool(),
        UninstallTool()
    ]

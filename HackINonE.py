#!/usr/bin python3
# coding: UTF-8

import os
import webbrowser
from time import sleep
from platform import system

from core import HackINonECollection
from tools.anonsurf import AnonSurfTools
from tools.ddos import DDOSTools
from tools.exploit_frameworks import ExploitFrameworkTools
from tools.forensic_tools import ForensicTools
from tools.information_gathering_tools import InformationGatheringTools
from tools.other_tools import OtherTools
from tools.payload_creator import PayloadCreatorTools
from tools.phising_attack import PhishingAttackTools
from tools.post_exploitation import PostExploitationTools
from tools.remote_administration import RemoteAdministrationTools
from tools.reverse_engineering import ReverseEngineeringTools
from tools.sql_tools import SqlInjectionTools
from tools.steganography import SteganographyTools
from tools.tool_manager import ToolManager
from tools.webattack import WebAttackTools
from tools.wireless_attack_tools import WirelessAttackTools
from tools.wordlist_generator import WordlistGeneratorTools
from tools.xss_attack import XSSAttackTools
from tools.vulnerablitiy_scanner import VulnScanTools
from tools.iot_tools import IOTTools
from tools.weak_pass_brute import WeakPwdBruteTools


def logo():
    banner = '''\033[33m
______  __            ______      ____________   __               __________
___  / / /_____ _________  /__    ____  _/__  | / /  ________________  ____/
__  /_/ /_  __ `/  ___/_  //_/     __  / __   |/ /   _  __ \_  __ \_  __/   
_  __  / / /_/ // /__ _  ,<       __/ /  _  /|  /    / /_/ /  / / /  /___   
/_/ /_/  \__,_/ \___/ /_/|_|      /___/  /_/ |_/     \____//_/ /_//_____/   {}
                                                            
                                                            Produced by Coldsnap
                                                            
       \033[34m[*] Personal Blog: https://coldwave96.github.io [*]
       \033[34m[*]   https://github.com/Coldwave96/HackINonE   [*]
       \033[91m[*]    Please Don't Use It As An Illegal Way    [*]
       \033[97m '''.format(version)

    print(banner + '\033[0m \033[97m')


all_tools = [
    AnonSurfTools(),
    InformationGatheringTools(),
    WordlistGeneratorTools(),
    WeakPwdBruteTools(),
    WirelessAttackTools(),
    SqlInjectionTools(),
    PhishingAttackTools(),
    WebAttackTools(),
    PostExploitationTools(),
    ForensicTools(),
    PayloadCreatorTools(),
    ExploitFrameworkTools(),
    ReverseEngineeringTools(),
    DDOSTools(),
    RemoteAdministrationTools(),
    XSSAttackTools(),
    SteganographyTools(),
    VulnScanTools(),
    IOTTools(),
    OtherTools(),
    ToolManager()
]


class AllTools(HackINonECollection):
    TITLE = "All tools"
    TOOLS = all_tools

    def show_info(self):
        logo()


if __name__ == "__main__":
    version = "v1.0"
    try:
        if system() == 'Linux':
            fpath = "/home/HackINonE.txt"
            if not os.path.exists(fpath):
                os.system('clear')
                print("""
                        [@] Set Path (All your tools will be install in that directory)
                        [1] Manual 
                        [2] Default
                """)
                choice = input("HackINonE $$ ")

                if choice == "1":
                    inpath = input("Enter Path (with Directory Name) >> ")
                    with open(fpath, "w") as f:
                        f.write(inpath)
                    print("Successfully Path Set...!!")
                elif choice == "2":
                    autopath = "/home/HackINonE/"
                    with open(fpath, "w") as f:
                        f.write(autopath)
                    print(f"Your Default Path Is:- {autopath}")
                    sleep(3)
                else:
                    print("Try Again..!!")
                    exit(0)

            with open(fpath) as f:
                archive = f.readline()
                if not os.path.exists(archive):
                    os.mkdir(archive)
                os.chdir(archive)
                all_tools = AllTools()
                all_tools.show_options()

        # If not Linux and probably Windows
        elif system() == "Windows":
            print("\033[91m Please Run This Tool In Debian System For Best Result " "\e[00m")
            sleep(2)
            webbrowser.open_new_tab("https://tinyurl.com/y522modc")

        else:
            print("Please Check Your Sytem or Open new issue ...")

    except KeyboardInterrupt:
        print("\nExiting ...!!!")
        sleep(2)

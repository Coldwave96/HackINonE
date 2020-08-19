# coding=utf-8
import os

from core import HackINonE
from core import HackINonECollection


class WebPwdCommonCrack(HackINonE):
    TITLE = "web_pwd_common_crack"
    DESCRIPTION = "Weak Password Crack Tool(Websites Without CAPTCHA)"
    INSTALL_COMMANDS = [
        "git clone https://github.com/TideSec/web_pwd_common_crack",
        "cd web_pwd_common_crack && pip install -r requirements.txt"
    ]
    RUN_COMMANDS = ['sudo python web_pwd_crack.py url.txt 50']
    PROJECT_URL = "https://github.com/TideSec/web_pwd_common_crack"

    def before_run(self):
        print("[*] Please Add Your Target Urls Into url.txt First !!! [*]")
        os.system('cd web_pwd_common_crack && gedit url.txt')


class Blazy(HackINonE):
    TITLE = "Blazy"
    DESCRIPTION = "Blazy is a modern login bruteforcer which also tests for CSRF, Clickjacking, Cloudflare and WAF."
    INSTALL_COMMANDS = [
        "git clone https://github.com/UltimateHackers/Blazy",
        "cd Blazy && pip install -r requirements.txt"
    ]
    RUN_COMMANDS = ["sudo python blazy.py"]
    PROJECT_URL = "https://github.com/s0md3v/Blazy"


class WeakPwdBruteTools(HackINonECollection):
    TITLE = "Weak Password Brute Tools"
    TOOLS = [
        WebPwdCommonCrack(),
        Blazy()
    ]

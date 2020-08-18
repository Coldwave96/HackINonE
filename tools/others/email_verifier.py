# coding=utf-8
from core import HackINonE
from core import HackINonECollection


class KnockMail(HackINonE):
    TITLE = "Knockmail"
    DESCRIPTION = "KnockMail Tool Verify If Email Exists"
    INSTALL_COMMANDS = [
        "git clone https://github.com/4w4k3/KnockMail.git",
        "cd KnockMail;sudo pip install -r requeriments.txt"
    ]
    RUN_COMMANDS = ["cd KnockMail;python knock.py"]
    PROJECT_URL = "https://github.com/4w4k3/KnockMail"


class EmailVerifyTools(HackINonECollection):
    TITLE = "Email Verify tools"
    TOOLS = [KnockMail()]

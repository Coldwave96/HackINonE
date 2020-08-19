# coding=utf-8
import subprocess

from core import HackINonE
from core import HackINonECollection
from core import validate_input


class SteganoHide(HackINonE):
    TITLE = "SteganoHide"
    INSTALL_COMMANDS = ["sudo apt-get install steghide -y"]

    def run(self):
        choice_run = input(
            "[1] Hide\n"
            "[2] Extract\n"
            "[0]Cancel\n"
            ">> ")
        choice_run = validate_input(choice_run, [1, 2, 0])
        if choice_run is None:
            print("Please choose a valid input")
            return self.run()

        if choice_run == 0:
            return

        if choice_run == 1:
            file_hide = input("Enter Filename you want to Embed (1.txt) >> ")
            file_to_be_hide = input("Enter Cover Filename(test.jpeg) >> ")
            subprocess.run(
                ["steghide", "embed", "-cf", file_to_be_hide, "-ef", file_hide])

        elif choice_run == "2":
            from_file = input("Enter Filename From Extract Data >> ")
            subprocess.run(["steghide", "extract", "-sf", from_file])


class StegnoCracker(HackINonE):
    TITLE = "StegnoCracker"
    DESCRIPTION = "SteganoCracker is a tool that uncover hidden data inside " \
                  "files\n using brute-force utility"
    INSTALL_COMMANDS = [
        "pip3 install stegcracker && pip3 install stegcracker -U --force-reinstall"]

    def run(self):
        filename = input("Enter Filename:- ")
        passfile = input("Enter Wordlist Filename:- ")
        subprocess.run(["stegcracker", filename, passfile])


class Whitespace(HackINonE):
    TITLE = "Whitespace"
    DESCRIPTION = "Use whitespace and unicode chars for steganography"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/beardog108/snow10.git",
        "sudo chmod -R 755 snow10"
    ]
    RUN_COMMANDS = ["cd snow10 && firefox index.html"]
    PROJECT_URL = "https://github.com/beardog108/snow10"


class SteganographyTools(HackINonECollection):
    TITLE = "Steganograhy tools"
    TOOLS = [
        SteganoHide(),
        StegnoCracker(),
        Whitespace()
    ]

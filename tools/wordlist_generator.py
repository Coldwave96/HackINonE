# coding=utf-8
from core import HackINonE
from core import HackINonECollection


class Cupp(HackINonE):
    TITLE = "Cupp"
    DESCRIPTION = "WlCreator is a C program that can create all possibilities of passwords,\n " \
                  "and you can choose Length, Lowercase, Capital, Numbers and Special Chars"
    INSTALL_COMMANDS = ["git clone https://github.com/Mebus/cupp.git"]
    PROJECT_URL = "https://github.com/Mebus/cupp.git"

    def __init__(self):
        super(Cupp, self).__init__(runnable=False)


class WlCreator(HackINonE):
    TITLE = "WordlistCreator"
    DESCRIPTION = "WlCreator is a C program that can create all possibilities" \
                  " of passwords,\n and you can choose Lenght, Lowercase, " \
                  "Capital, Numbers and Special Chars"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/Z4nzu/wlcreator.git"]
    RUN_COMMANDS = ["cd wlcreator && sudo gcc -o wlcreator wlcreator.c && ./wlcreator 5"]
    PROJECT_URL = "https://github.com/Z4nzu/wlcreator"


class GoblinWordGenerator(HackINonE):
    TITLE = "Goblin WordGenerator"
    DESCRIPTION = "Goblin WordGenerator"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/UndeadSec/GoblinWordGenerator.git"]
    RUN_COMMANDS = ["cd GoblinWordGenerator && python3 goblin.py"]
    PROJECT_URL = "https://github.com/UndeadSec/GoblinWordGenerator.git"


class Showme(HackINonE):
    TITLE = "Password list (1.4 Billion Clear Text Password)"
    DESCRIPTION = "This tool allows you to perform OSINT and reconnaissance on " \
                  "an organisation or an individual. It allows one to search " \
                  "1.4 Billion clear text credentials which was dumped as " \
                  "part of BreachCompilation leak. This database makes " \
                  "finding passwords faster and easier than ever before."
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/Viralmaniar/SMWYG-Show-Me-What-You-Got.git",
        "cd SMWYG-Show-Me-What-You-Got && pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd SMWYG-Show-Me-What-You-Got && python SMWYG.py"]
    PROJECT_URL = "https://github.com/Viralmaniar/SMWYG-Show-Me-What-You-Got"


class WordlistGeneratorTools(HackINonECollection):
    TITLE = "Wordlist Generator"
    TOOLS = [
        Cupp(),
        WlCreator(),
        GoblinWordGenerator(),
        Showme()
    ]

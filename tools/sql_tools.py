# coding=utf-8
from core import HackINonE
from core import HackINonECollection


class Sqlmap(HackINonE):
    TITLE = "Sqlmap tool"
    DESCRIPTION = "sqlmap is an open source penetration testing tool that " \
                  "automates the process of \n" \
                  "detecting and exploiting SQL injection flaws and taking " \
                  "over of database servers \n " \
                  "[!] python sqlmap.py -u [<http://example.com>] --batch --banner \n " \
                  "More Usage [!] https://github.com/sqlmapproject/sqlmap/wiki/Usage"
    INSTALL_COMMANDS = [
        "sudo git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev"]
    PROJECT_URL = "https://github.com/sqlmapproject/sqlmap"

    def __init__(self):
        super(Sqlmap, self).__init__(runnable=False)


class NoSqlMap(HackINonE):
    TITLE = "NoSqlMap"
    DESCRIPTION = "NoSQLMap is an open source Python tool designed to \n " \
                  "audit for as well as automate injection attacks and exploit.\n " \
                  "\033[91m " \
                  "[*] Please Install MongoDB \n "
    INSTALL_COMMANDS = [
        "git clone https://github.com/codingo/NoSQLMap.git",
        "sudo chmod -R 755 NoSQLMap;cd NoSQLMap;python setup.py install"
    ]
    RUN_COMMANDS = ["python NoSQLMap"]
    PROJECT_URL = "https://github.com/codingo/NoSQLMap"


class SQLiScanner(HackINonE):
    TITLE = "Damn Small SQLi Scanner"
    DESCRIPTION = "Damn Small SQLi Scanner (DSSS) is a fully functional SQL " \
                  "injection\nvulnerability scanner also supporting GET and " \
                  "POST parameters.\n" \
                  "[*]python3 dsss.py -h[help] | -u[URL]"
    INSTALL_COMMANDS = ["git clone https://github.com/stamparm/DSSS.git"]
    PROJECT_URL = "https://github.com/stamparm/DSSS"

    def __init__(self):
        super(SQLiScanner, self).__init__(runnable=False)


class Explo(HackINonE):
    TITLE = "Explo"
    DESCRIPTION = "Explo is a simple tool to describe web security issues " \
                  "in a human and machine readable format.\n " \
                  "Usage:- \n " \
                  "[1] explo [--verbose|-v] testcase.yaml \n " \
                  "[2] explo [--verbose|-v] examples/*.yaml"
    INSTALL_COMMANDS = [
        "git clone https://github.com/dtag-dev-sec/explo.git",
        "cd explo;sudo python setup.py install"
    ]
    PROJECT_URL = "https://github.com/dtag-dev-sec/explo"

    def __init__(self):
        super(Explo, self).__init__(runnable=False)


class Blisqy(HackINonE):
    TITLE = "Blisqy - Exploit Time-based blind-SQL injection"
    DESCRIPTION = "Blisqy is a tool to aid Web Security researchers to find " \
                  "Time-based Blind SQL injection \n on HTTP Headers and also " \
                  "exploitation of the same vulnerability.\n " \
                  "For Usage >> \n"
    INSTALL_COMMANDS = ["git clone https://github.com/JohnTroony/Blisqy.git"]
    PROJECT_URL = "https://github.com/JohnTroony/Blisqy"

    def __init__(self):
        super(Blisqy, self).__init__(runnable=False)


class Leviathan(HackINonE):
    TITLE = "Leviathan - Wide Range Mass Audit Toolkit"
    DESCRIPTION = "Leviathan is a mass audit toolkit which has wide range " \
                  "service discovery,\nbrute force, SQL injection detection " \
                  "and running custom exploit capabilities. \n " \
                  "[*] It Requires API Keys \n " \
                  "More Usage [!] https://github.com/utkusen/leviathan/wiki"
    INSTALL_COMMANDS = [
        "git clone https://github.com/leviathan-framework/leviathan.git",
        "cd leviathan;sudo pip install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd leviathan;python leviathan.py"]
    PROJECT_URL = "https://github.com/leviathan-framework/leviathan"


class SQLScan(HackINonE):
    TITLE = "SQLScan"
    DESCRIPTION = "sqlscan is quick web scanner for find an sql inject point." \
                  " not for educational, this is for hacking."
    INSTALL_COMMANDS = [
        "sudo apt install php php-bz2 php-curl php-mbstring curl",
        "sudo curl https://raw.githubusercontent.com/Cvar1984/sqlscan/dev/build/main.phar --output /usr/local/bin/sqlscan",
        "chmod +x /usr/local/bin/sqlscan"
    ]
    RUN_COMMANDS = ["sudo sqlscan"]
    PROJECT_URL = "https://github.com/Cvar1984/sqlscan"


class NoSQLAttack(HackINonE):
    TITLE = "NoSQLAttack"
    DESCRIPTION = "NoSQLAttack is an open source Python tool \n" \
                  "to automate exploit MongoDB server IP on Internet \n" \
                  "and disclose the database data by MongoDB \n" \
                  "default configuration weaknesses and injection attacks."
    INSTALL_COMMANDS = [
        "git clone https://github.com/youngyangyang04/NoSQLAttack.git",
        'cd NoSQLAttack; sudo python setup.py install'
    ]
    RUN_COMMANDS = ['NoSQLAttack']
    PROJECT_URL = "https://github.com/youngyangyang04/NoSQLAttack"


class Enumdb(HackINonE):
    TITLE = "enumdb"
    DESCRIPTION = "Relational database brute force and post exploitation tool for MySQL and MSSQL."
    INSTALL_COMMANDS = ["pip3 install enumdb"]
    RUN_COMMANDS = ['enumdb']
    PROJECT_URL = "https://github.com/m8r0wn/enumdb"


class SqlInjectionTools(HackINonECollection):
    TITLE = "SQL Injection Tools"
    TOOLS = [
        Sqlmap(),
        NoSqlMap(),
        SQLiScanner(),
        Explo(),
        Blisqy(),
        Leviathan(),
        SQLScan(),
        NoSQLAttack(),
        Enumdb()
    ]

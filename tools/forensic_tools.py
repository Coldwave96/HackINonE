# coding=utf-8
import os

from core import HackINonE
from core import HackINonECollection


class Autopsy(HackINonE):
    TITLE = "Autopsy"
    DESCRIPTION = "Autopsy is a platform that is used by Cyber Investigators.\n" \
                  "[!] Works in any Os\n" \
                  "[!] Recover Deleted Files from any OS & MEdia \n" \
                  "[!] Extract Image Metadata"
    RUN_COMMANDS = "sudo autopsy"

    def __init__(self):
        super(Autopsy, self).__init__(installable=False)


class Wireshark(HackINonE):
    TITLE = "Wireshark"
    DESCRIPTION = "Wireshark is a network capture and analyzer \n" \
                  "tool to see what’s happening in your network.\n " \
                  "And also investigate Network related incident"
    RUN_COMMANDS = ["sudo wireshark"]

    def __init__(self):
        super(Wireshark, self).__init__(installable=False)


class BulkExtractor(HackINonE):
    TITLE = "Bulk extractor"
    DESCRIPTION = "An Investigating Tool"
    PROJECT_URL = "https://github.com/simsong/bulk_extractor"

    def __init__(self):
        super(BulkExtractor, self).__init__([
            ('GUI Mode (Download required)', self.gui_mode),
            ('CLI Mode', self.cli_mode)
        ], installable=False, runnable=False)

    def gui_mode(self):
        os.system("sudo git clone https://github.com/simsong/bulk_extractor.git")
        os.system("ls src/ && cd .. && cd java_gui && ./BEViewer")
        print("If you getting error after clone go to /java_gui/src/ And Compile .Jar file && run ./BEViewer")
        print("Please Visit For More Details About Installation >> https://github.com/simsong/bulk_extractor")

    def cli_mode(self):
        os.system("sudo apt-get install bulk_extractor")
        print("bulk_extractor and options")
        os.system("bulk_extractor")
        os.system('echo "bulk_extractor [options] imagefile" | boxes -d headline | lolcat')


class Guymager(HackINonE):
    TITLE = "Disk Clone and ISO Image Aquire"
    DESCRIPTION = "Guymager is a free forensic imager for media acquisition."
    INSTALL_COMMANDS = ["sudo apt install guymager"]
    RUN_COMMANDS = ["sudo guymager"]
    PROJECT_URL = "https://guymager.sourceforge.io/"


class Toolsley(HackINonE):
    TITLE = "Toolsley"
    DESCRIPTION = "Toolsley got more than ten useful tools for investigation.\n" \
                  "[+]File signature verifier\n" \
                  "[+]File identifier \n" \
                  "[+]Hash & Validate \n" \
                  "[+]Binary inspector \n " \
                  "[+]Encode text \n" \
                  "[+]Data URI generator \n" \
                  "[+]Password generator"
    PROJECT_URL = "https://www.toolsley.com/"

    def __init__(self):
        super(Toolsley, self).__init__(installable=False, runnable=False)


class ForensicTools(HackINonECollection):
    TITLE = "Forensic tools"
    TOOLS = [
        Autopsy(),
        Wireshark(),
        BulkExtractor(),
        Guymager(),
        Toolsley()
    ]

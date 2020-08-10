#!/bin/bash
clear

BLACK='\e[30m'
RED='\e[31m'
GREEN='\e[92m'
YELLOW='\e[33m'
ORANGE='\e[93m'
BLUE='\e[34m'
PURPLE='\e[35m'
CYAN='\e[36m'
WHITE='\e[37m'
NC='\e[0m'
purpal='\033[35m'

echo -e "${ORANGE} "
echo ""
echo "______  __            ______ ________                   __________";
echo "___  / / /_____ _________  /_____  _/______________________  ____/";
echo "__  /_/ /_  __ \`/  ___/_  //_/__  / __  __ \  __ \_  __ \_  __/   ";
echo "_  __  / / /_/ // /__ _  ,<  __/ /  _  / / / /_/ /  / / /  /___   ";
echo "/_/ /_/  \__,_/ \___/ /_/|_| /___/  /_/ /_/\____//_/ /_//_____/   ";
echo "                                                                  ";

echo "${BLUE}                                 Produced By Coldsnap ${NC}";
echo ""
echo "${RED}      [!] Attention Please!!! This Tool MUst Run As Root [!]       ${NC}"
echo ""
echo "${CYAN} Select Your System: ${NC}"
echo ""
echo "${WHITE} [1] Kali Linux ${NC}"
echo "${WHITE} [0] Exit ${NC}"
echo -n -e "HackINonE >> "
read num
INSTALL_DIR="/usr/share/doc/HackINonE"
BIN_DIR="/usr/bin/"
if [ $num == 1 ]; then
	echo "${GREEN} [*] Checking Internet Connection ... ${NC}"
	wget -q --tries=10 --timeout=20 --spider https://github.com
	if [[ $? -eq 0 ]]; then
	   echo -e ${BLUE}"[✔] Loading ... "
	    sudo apt-get update && apt-get upgrade
	    sudo apt-get install python-pip
	    echo "${GREEN} [✔] Checking directories... ${NC}"
	    if [ -d "$INSTALL_DIR" ]; then
	        echo "${YELLOW} [!] A Directory HackINonE Was Found.. Do You Want To Replace It ? [y/n]: ${NC}";
	        read input
	        if [ "$input" = "y" ]; then
	            rm -R "$INSTALL_DIR"
	        else
	            exit
	        fi
	    fi
    		echo "${PURPLE} [✔] Installing ... ${NC}";
		echo "";
		git clone https://github.com/Coldwave96/HackINonE.git "$INSTALL_DIR";
		echo "#!/bin/bash
		python3 $INSTALL_DIR/HackINonE.py" '${1+"$@"}' > hackINone;
		sudo chmod +x hackINone;
		sudo cp hackINone $BIN_DIR;
		rm hackINone;
		echo "";
		echo "${purpal}[✔] Trying to installing Requirements ... ${NC}"
		sudo apt-get install -y figlet
		sudo apt-get install boxes
		sudo pip3 install lolcat
		sudo pip3 install boxes
		sudo pip3 install flask
		sudo pip3 install requests
	else
		echo -e $RED "Please Check Your Internet Connection ..!! "
	fi

    if [ -d "$INSTALL_DIR" ]; then
        echo "";
        echo "[✔] Successfuly Installed !!! ";
        echo "";
        echo "";
        echo -e "		[+]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[+]"
        echo 		"		[+]						      		[+]"
        echo -e "		[+]     ✔✔✔ Now Just Type In Terminal (hackINone) ✔✔✔ 	[+]"
        echo 		"		[+]						      		[+]"
        echo -e "		[+]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[+]"
    else
        echo "${BLACK}[✘] Installation Failed !!! [✘]${NC}";
        exit
    fi
elif [ $num -eq 0 ];
then
    echo -e $RED "[✘] Thank You !! [✘]"
    exit
else
    echo -e $RED "[!] Select Valid Option [!]"
fi

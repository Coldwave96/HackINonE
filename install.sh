#!/bin/bash
clear

RED='\e[31m'
ORANGE='\e[93m'
BLUE='\e[34m'

echo -e "${ORANGE} "
echo ""
echo "______  __            ______ ________                   __________";
echo "___  / / /_____ _________  /_____  _/______________________  ____/";
echo "__  /_/ /_  __ \`/  ___/_  //_/__  / __  __ \  __ \_  __ \_  __/   ";
echo "_  __  / / /_/ // /__ _  ,<  __/ /  _  / / / /_/ /  / / /  /___   ";
echo "/_/ /_/  \__,_/ \___/ /_/|_| /___/  /_/ /_/\____//_/ /_//_____/   ";
echo "                                                                  ";

echo "                                              Produced By Coldsnap";
echo ""
echo "      [!] Attention Please!!! This Tool MUst Run As Root [!]      ";
echo ""
echo "Select Your System: "
echo ""
echo "$[1] Kali Linux "
echo "$[0] Exit "
echo -n -e "HackINonE >> "
read num
INSTALL_DIR="/usr/share/doc/HackINonE"
BIN_DIR="/usr/bin/"
if [ $num == 1 ]; then
	echo "[*] Checking Internet Connection ... "
	wget -q --tries=10 --timeout=20 --spider https://github.com
	if [[ $? -eq 0 ]]; then
	    echo -e $BLUE "[✔] Loading ... "
	    sudo apt-get update && apt-get upgrade
	    sudo apt-get install python-pip
	    echo "[*] Checking directories... "
	    if [ -d "$INSTALL_DIR" ]; then
	        echo " [!] A Directory HackINonE Was Found.. Do You Want To Replace It ? [y/n]: ";
	        read input
	        if [ "$input" = "y" ]; then
	            rm -R "$INSTALL_DIR"
	        else
	            exit
	        fi
	    fi
    		echo "[✔] Installing ... ";
		echo "";
		git clone https://github.com/Coldwave96/HackINonE.git "$INSTALL_DIR";
		echo "#!/bin/bash
		python3 $INSTALL_DIR/HackINonE.py" '${1+"$@"}' > hackINone;
		sudo chmod +x hackINone;
		sudo cp hackINone $BIN_DIR;
		rm hackINone;
		echo "";
		echo "[✔] Trying to installing Requirements ... "
		sudo apt-get install -y figlet
		sudo apt-get install boxes
		sudo apt-get install gedit
		sudo pip3 install lolcat
		sudo pip3 install boxes
		sudo pip3 install flask
		sudo pip3 install requests
	else
		echo -e $RED "Please Check Your Internet Connection ..!! "
	fi

    if [ -d "$INSTALL_DIR" ]; then
        echo "";
        echo "[✔] Successfully Installed !!! ";
        echo "";
        echo "";
        echo -e "		[+]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[+]"
        echo -e "		[+]          Now Just Type In Terminal (hackINone)     	        [+]"
        echo -e "		[+]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[+]"
    else
        echo "[✘] Installation Failed !!! [✘]";
        exit
    fi
elif [ $num -eq 0 ];
then
    echo -e $RED "[✘] Thank You !! [✘]"
    exit
else
    echo -e $RED "[!] Select Valid Option [!]"
fi

#!/bin/bash
clear

echo "______  __            ______ ________                   __________";
echo "___  / / /_____ _________  /_____  _/______________________  ____/";
echo "__  /_/ /_  __ \`/  ___/_  //_/__  / __  __ \  __ \_  __ \_  __/   ";
echo "_  __  / / /_/ // /__ _  ,<  __/ /  _  / / / /_/ /  / / /  /___   ";
echo "/_/ /_/  \__,_/ \___/ /_/|_| /___/  /_/ /_/\____//_/ /_//_____/   ";
echo "                                                                  ";

echo "                                              Produced By Coldsnap";
echo ""
echo "      [!] Attention Please!!! This Tool MUst Run As Root [!]       "
echo ""
echo "Select Your System: "
echo ""
echo "[1] Kali Linux "
echo "[0] Exit "
echo -n -e "HackINonE >> "
read num
INSTALL_DIR="/usr/share/doc/HackINonE"
BIN_DIR="/usr/bin/"
if [ $num == 1 ]; then
	echo "\033[1;34m [*] Checking Internet Connection .. \033[1;34m"
	wget -q --tries=10 --timeout=20 --spider https://github.com
	if [[ $? -eq 0 ]]; then
	   echo -e "\033[1;34m [✔] Loading ... \033[1;34m"
	    sudo apt-get update && apt-get upgrade
	    sudo apt-get install python-pip
	    echo "\033[1;34m [✔] Checking directories... \033[1;34m"
	    if [ -d "$INSTALL_DIR" ]; then
	        echo "\033[1;31m [!] A Directory HackINonE Was Found.. Do You Want To Replace It ? [y/n]:  \033[0m" ;
	        read input
	        if [ "$input" = "y" ]; then
	            rm -R "$INSTALL_DIR"
	        else
	            exit
	        fi
	    fi
    		echo "\033[1;34m [✔] Installing ... \033[1;34m";
		echo "";
		git clone https://github.com/Coldwave96/HackINonE.git "$INSTALL_DIR";
		echo "#!/bin/bash
		python3 $INSTALL_DIR/HackINonE.py" '${1+"$@"}' > hackINone;
		sudo chmod +x hackINone;
		sudo cp hackINone $BIN_DIR;
		rm hackINone;
		echo "";
		echo "\033[1;34m [✔] Trying to installing Requirements ... \033[1;34m"
		sudo apt-get install -y figlet
		sudo apt-get install boxes
		sudo pip3 install lolcat
		sudo pip3 install boxes
		sudo pip3 install flask
		sudo pip3 install requests
	else
		echo -e "\033[1;31m Please Check Your Internet Connection ..!! \033[0m"
	fi

    if [ -d "$INSTALL_DIR" ]; then
        echo "";
        echo "\033[1;34m [✔] Successfuly Installed !!! \033[1;34m";
        echo "";
        echo "";
        echo -e "		[+]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[+]"
        echo 		"		[+]						      		[+]"
        echo -e "		[+]     ✔✔✔ Now Just Type In Terminal (hackINone) ✔✔✔ 	[+]"
        echo 		"		[+]						      		[+]"
        echo -e "		[+]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[+]"
    else
        echo "\033[1;31m [✘] Installation Failed !!! [✘] \033[0m";
        exit
    fi
elif [ $num -eq 0 ];
then
    echo -e "\033[1;34m [✘] Thank You !! [✘] \033[1;34m"
    exit
else
    echo -e "\033[1;31m [!] Select Valid Option [!] \033[0m"
fi

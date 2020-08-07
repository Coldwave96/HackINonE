#!/bin/bash
echo "_________     ______________                             ";
echo "__  ____/________  /_____  /___________________ ________ ";
echo "_  /    _  __ \_  /_  __  /__  ___/_  __ \  __ \`/__  __ \\";
echo "/ /___  / /_/ /  / / /_/ / _(__  )_  / / / /_/ /__  /_/ /";
echo "\____/  \____//_/  \__,_/  /____/ /_/ /_/\__,_/ _  .___/ ";
echo "                                                /_/      ";

clear

sudo chmod +x /etc/

clear

sudo chmod +x /usr/share/doc

clear

sudo rm -rf /usr/share/doc/HackINonE/

clear

cd /etc/

clear

sudo rm -rf /etc/HackINonE

clear

mkdir HackINonE

clear

cd HackINonE

clear

git clone https://github.com/Coldwave96/HackINonE.git

clear

cd HackINonE

clear

sudo chmod +x install.sh

clear

./install.sh

clear
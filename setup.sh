#!/bin/sh

mkdir $HOME/.sshm
cp sshm.py $HOME/.sshm/sshm.py
touch $HOME/.sshm/sshm-info
if [ -e "$HOME/.bashrc" ]
then
    echo
    echo alias sshm = "python ~/.sshm/sshm.py" >> $HOME/.bashrc
    echo An alias for sshm has been written to your .bashrc.
    echo If you use a different shell, add the following line
    echo to the shell\'s rc file: alias sshm = "python ~/.sshm/sshm.py"
else    
    echo It seems your .bashrc is not in your home directory
    echo Add the following lineto your .bashrc and you will be
    echo good to go: alias sshm = "python ~/.sshm/sshm.py"
fi
echo
echo SSH Manager is now installed. See README.txt for usage help,
echo or visit the github page. Thank you for using SSHM!
echo
exit

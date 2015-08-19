Purpose
-------
SSH Manager (SSHM for short) is a program designed to make using SSH from the command line an easier experience. 

Installation
------------
1) Navigate to the downloaded folder and run: chmod +x setup.sh

2) Run setup.sh

Use
---
Conncting:
    
To SSH into a server, run the command, "sshm -connect [Default Name]", replacing [Default Name] with the name of a default you have already created 

Creating Defaults:

SSH Manager stores your commonly used SSH information to make connecting to a server with a given set of parameters easier. This information is stored in what are known as "defaults". To create a new default, simply type the command, "sshm -create_default", and follow the instructions.

Deleting Defaults:

To delete a default, run the command, "sshm -delete_default [Default Name]", replacing [Default Name] with the name of the default you want to delete

Note
----
SSH Manager is still under developement! This is the very first version and still lacks a large amount of functionality. See TODO to find out what will be in future updates! Be sure to add any comments on bugs and functionality recommendations/requests.

Thank you for using SSH Manager. Enjoy!

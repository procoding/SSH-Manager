from os.path import expanduser
import subprocess
import sys

def createDefault(filename):
        dataFile = open(filename, 'a')
        data = []
        print('Please enter in the following data for your default...')
        data.append(raw_input('Default Name: '))
        data.append(raw_input('Username: '))
        data.append(raw_input('Hostname: '))
        data.append(raw_input('Port (Write "none" if your session does not require you to specify): '))
        data.append(raw_input('Will you only use this default while on the same network as the host (y/n)? '))

        info = "{}:{}:{}:{}:{}:".format(data[0], data[1], data[2], data[3], data[4])

        dataFile.write(info + "\n")
        dataFile.close()

def deleteDefault(filename, defaultName):
        dataFile = open(filename, 'r')
        lines = dataFile.readlines()
        dataFile.close()
        dataFile = open(filename, 'w')
        for line in lines:
                if(line[:len(defaultName)] != defaultName):
                        dataFile.write(line)



def parse(filename, defaultName):
        dataFile = open(filename, 'r')
        info = ''
        for line in enumerate(dataFile):
            info = line[1]
            if(info[:len(defaultName)] == defaultName):
                    break
        dataFile.close()

        data = info.split(':')

        if(data[3] != 'none' and data[4] == 'y'):
                cmd = "ssh -p {} {}@{}.local".format(data[3], data[1], data[2])
        elif(data[3] != 'none' and data[4] == 'n'):
                cmd = "ssh -p {} {}@{}".format(data[3], data[1], data[2])
        elif(data[3] == 'none' and data[4] == 'y'):
                cmd = "ssh {} {}@{}".format(data[1], data[2])
        elif(data[3] == 'none' and data[4] == 'n'):
                cmd = "ssh {}@{}".format(data[1], data[2]) 
        return cmd

def connect(cmd):
        subprocess.call(cmd, shell=True)
        return 0

#Main script body

if('-connect' in sys.argv):
        cmd = parse(expanduser('~') + '/.sshm/sshm-info', sys.argv[sys.argv.index('-connect') + 1])
        connect(cmd)
if('-create_default' in sys.argv):
        createDefault(expanduser('~' + '/.sshm/sshm-info'))
if('-delete_default' in sys.argv):
        deleteDefault(expanduser('~') + '/.sshm/sshm-info', sys.argv[sys.argv.index('-delete_default') + 1])

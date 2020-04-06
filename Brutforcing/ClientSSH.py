import logging
import sys
import paramiko
import paramiko.transport
cmd1 = 'ifconfig'
cmd2 = 'cat /etc/passwd'
cmd3 = 'netstat -an'
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
try:
    ssh.connect('localhost', username='root', password='password')
except paramiko.SSHException:
    print 'erreur de connection'
stdin, stdout, stderr = ssh.exec_command(cmd1)

for line in stdout.readlines():
    print line.strip()
ssh.close()


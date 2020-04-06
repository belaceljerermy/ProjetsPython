# coding=utf-8
import socket
import threading

# on importe les libraire
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# on crée le serveur avec les librairie
bind_ip = "0.0.0.0"
bind_port = 8096
# on crée les variavle  ip et port
server.bind((bind_ip, bind_port))
server.listen(2)
# on initiallise le serveur en écoute ip plus port
print "[+] ecoute sur l'address %s et port %d" % (bind_ip, bind_port)
(client, (ip, port)) = server.accept()
# on affiche le serveur est a l'écoute
print "Ip client est : %s " % ip
print "Port client est : %d " % port
# une fois connecter on affiche l'ip et port du client

data = 'noob'
reponse = 'merci de me contacter'
# on crée la variable data contenant noob
while len(data):
    # on bloucle sur data
    data = client.recv(2048)
    # on limite la valeur de reception a 2048
    print "Client envoyer: ", data
    # on affiche envoye de donné
    client.send(reponse)
# on envoie les donné eton répond

print "fermeture des connection"
client.close()
# on ferme la connection avec le client
server.close()
#on eteint le serveur
print "fermeture du serveur"

# coding=utf-8
import socket
# on importe les lib
server_ip = "10.0.2.4"
server_port = 8096
#on spécifie le serveur distant
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# on crée le client
client.connect((server_ip, server_port))
# on connect le client au serveur
requete = raw_input("salut tout le monde")
# on crée une requete que l'on parametre
client.send(requete)
# on envoie la requete
reponse = client.recv(4096)
# on limite la taille des information envoyer
print reponse
# on affiche la réponce


import urllib
from time import sleep

print("[+]--------------------------------------------------[+]")
print("[+]-----               BY Z3r0Dy                -----[+]")
print("[+]-----                 Firts                  -----[+]")
print("[+]-----                 Urllib                 -----[+]")
print("[+]-----               Isuiteexpet              -----[+]")
print("[+]-----                                        -----[+]")
print("[+]--------------------------------------------------[+]")
sleep(3)


def GetData(url, data):
    return url + '?' + urllib.urlencode(data)


Site = raw_input("Veuillez saisir l'url : \r\n")
print ("l'url est : ") + str(Site)
requete = raw_input("Veuillez saisir le parametre: \r\n")
print "le parametre : " + str(requete)
Donnee = raw_input("Veuillez saisir la donnee : \r\n")
print "la donnee : " + str(Donnee)

url = GetData(Site, [(requete, Donnee)])
print "Exploitation de l'adresse", url




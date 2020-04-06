from time import sleep
from bs4 import BeautifulSoup
from pip._vendor import requests

print("[+]--------------------------------------------------[+]")
print("[+]-----               BY Z3r0Dy                -----[+]")
print("[+]-----                 Firts                  -----[+]")
print("[+]-----                 Urllib                 -----[+]")
print("[+]-----               Isuiteexpet              -----[+]")
print("[+]-----                                        -----[+]")
print("[+]--------------------------------------------------[+]")
sleep(3)

Site = raw_input("Veuillez saisir l'url : \r\n")
req = requests.get("https://" + Site)
soup = BeautifulSoup(req.text, "lxml")
for link in soup.find_all('a'):
    current_link = link.get('href')
    if current_link.endswith('pdf'):
        print 'lien vers un PDF : ', current_link

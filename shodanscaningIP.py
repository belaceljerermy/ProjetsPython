import shodan
import requests

SHODAN_API_KEY = "K1ZxnGKvrJ3q73zFJJ06ai50IoW5TIXU"
api = shodan.Shodan(SHODAN_API_KEY)
try:
    #host = api.host('159.180.238.52')
    target = "www.suiteexpert.fr"
    dnsResolve = 'https://api.shodan.io/dns/resolve?hostnames='+ target + '&key=' + SHODAN_API_KEY
    resolved = requests.get(dnsResolve)
    HostIP = resolved.json()[target]
    host = api.host(HostIP)
    print 'IP : %s' % host['ip_str']
    print host['os']
    print host['data']
    for item in host['data']:
        print 'Port : %s ' % item['port']
        print 'Bannier : %s  ' % item['data']
except shodan.APIError, e:
    print 'ERREUR : %s' % e



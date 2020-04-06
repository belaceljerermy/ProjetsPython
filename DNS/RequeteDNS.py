# coding=utf-8
import dns.version
import dns.resolver
print 'Version DnsPython: ',dns.version.version

reponse = dns.resolver.query('kondah.com', 'MX')
for data in reponse:
    print "Serveur MX : " , data.exchange,'preferance', data.preference

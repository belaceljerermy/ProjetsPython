import shodan
SHODAN_API_KEY = "K1ZxnGKvrJ3q73zFJJ06ai50IoW5TIXU"
api = shodan.Shodan(SHODAN_API_KEY)
try:
    results = api.search('SCADA')
    print 'Resultat %s'%results['total']
    for result in results['matches']:
        print 'IP : %s'%result['ip_str']
        print result['data']

except shodan.APIError, e:
    print 'ERREUR : %s'%e




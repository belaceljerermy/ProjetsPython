import urllib
httpReponse = urllib.urlopen("http://10.0.2.6")
print httpReponse.read()
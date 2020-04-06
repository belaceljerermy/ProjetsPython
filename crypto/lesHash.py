import hashlib

messagemd5 = raw_input("Veuiller entrer la chaine a Hasher  md5 : \r\n")
md5 = hashlib.md5(messagemd5.encode())

print "Voici le message Md5 : %s \r" % messagemd5
print "Voici le hash Md5 : %s \r\n" % md5.hexdigest()

messagesha1 = raw_input("Veuiller entrer la chaine a Hasher SHA-1 : \r\n")
sha1 = hashlib.sha1(messagesha1.encode())
print "Voici le message SHA-1 : %s \r" % messagesha1
print "Voici le hash SHA-1  : %s \r\n" % sha1.hexdigest()

messagesha224 = raw_input("Veuiller entrer la chaine a Hasher sha224 : \r\n")
sha24 = hashlib.sha224(messagesha224.encode())
print "Voici le message sha224: %s \r" % messagesha224
print "Voici le hash sha224  : %s \r\n" % sha24.hexdigest()

messagesha256 = raw_input("Veuiller entrer la chaine a Hasher sha256  : \r\n")
sha256 = hashlib.sha256(messagesha256.encode())
print "Voici le message sha256: %s \r" % messagesha256
print "Voici le hash sha256  : %s \r\n" % sha256.hexdigest()

messagesha384 = raw_input("Veuiller entrer la chaine a Hasher sha384 : \r\n")
sha384 = hashlib.sha384(messagesha384.encode())
print "Voici le message sha384: %s \r" % messagesha384
print "Voici le hash sha384  : %s \r\n" % sha384.hexdigest()

messagesha512 = raw_input("Veuiller entrer la chaine a Hasher sha512 : \r\n")
sha512 = hashlib.sha512(messagesha512.encode())
print "Voici le message sha512: %s \r" % messagesha512
print "Voici le hash sha512  : %s \r\n" % sha512.hexdigest()

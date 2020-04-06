from string import maketrans, lowercase, uppercase


def rot13(messagerot13):
    lower = maketrans(lowercase, lowercase[13:] + lowercase[:13])
    upper = maketrans(uppercase, uppercase[13:] + uppercase[:13])
    return messagerot13.translate(lower).translate(upper)


messagerot13 = raw_input("Veuiller entrer la chaine a Coder en Rot13 : \r\n")

print rot13(messagerot13)

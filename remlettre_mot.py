list1 = ["toto", "papa", "tata"]
lettre = ["a", "e", "x"]
def rempalce_letrre (list1,lettre):
    i = 0
    x = 0
    print len(list1)
    print len(lettre)
    while i < len(list1):
        while x < len(lettre):
            word = list1[i].remplace(list1[i], lettre[x])
            motdeliste = list1[i] + word
            print motdeliste
            x = x + x
        i = i + i
    print motdeliste
rempalce_letrre(list1,lettre)

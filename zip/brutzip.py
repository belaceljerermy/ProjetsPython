import zipfile

fichier = "/root/Bureau/zipfile.zip"
dico = "/root/Bureau/dico.txt"

password = None
fichier_ouverture = zipfile.ZipFile(fichier)
with open(dico, 'r') as f:
    for line in f.readlines():
        password = line.strip('\n')
        try:
            fichier_ouverture.extractall(pwd=password)
            password = 'mot de passe trouver : %s ' % password
            print password
        except:
            pass

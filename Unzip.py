#Martin Couture
#Décembre 2020
#Il suffit d'indiquer le répertoire et les fichiers ZIP sont extraient dans un répertoire ayant le même nom.
#Fait avec Python 3.X

import os, zipfile

#Liste des fichiers ZIP
repertoire = input("Entrer le chemin du répertoire: ")
chemin = repertoire.replace("\\", "/") + "/"
dicoZip = {}

listeFichiers = os.listdir(chemin)
for fichier in listeFichiers:
    if os.path.isfile(chemin + fichier):
        nomFichier, nomExtension = os.path.splitext(fichier)
        if nomExtension == ".zip":
            dicoZip[nomFichier] = fichier

cles = dicoZip.keys()

for cle in cles:
    print("Création du répertoire ->", cle)
    if not os.path.exists(chemin + cle):
       os.mkdir(chemin + cle )
    else:
        print("Répertoire déjà existant...")
    with zipfile.ZipFile(chemin + dicoZip[cle], 'r') as zipObj:
        print("Extraction des fichiers...")
        zipObj.extractall(chemin  + cle )











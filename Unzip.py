#Martin Couture
#Décembre 2022
#Il suffit d'indiquer le répertoire dans "chemin d'accès". 
#Les fichier sont dézippés dans avec le même nom du fichier zip comme nom de répertoire. 
#Fait avec Python 3.X

import os
from zipfile import ZipFile

chemin = r"chemin d'accès"
os.chdir(chemin)
dir_list = os.listdir(chemin)

for elem in dir_list:
    if elem[len(elem)-4:] == ".zip":
        with ZipFile(elem, 'r') as zip:
            zip.extractall(elem[:len(elem)-4])
            print("Dézippé : ",elem[:len(elem)-4])












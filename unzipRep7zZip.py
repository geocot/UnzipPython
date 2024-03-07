import os, py7zr, zipfile

repertoire = r"Votre répertoire"
os.chdir(repertoire)


def creationRepertoire(nomFichier):
    print("Traitement du fichier: ", nomFichier)
    os.makedirs(os.path.splitext(nomFichier)[0])


def extraction7z(nomFichier):
    creationRepertoire(nomFichier)
    with py7zr.SevenZipFile(nomFichier, 'r') as archive:
        archive.extractall(path=os.getcwd() + "/" + os.path.splitext(nomFichier)[0])


def extractionZip(nomFichier):
    creationRepertoire(nomFichier)
    with zipfile.ZipFile(nomFichier, 'r') as zip:
        zip.extractall(path=os.getcwd() + "/" + os.path.splitext(nomFichier)[0])

fichiersRAR = []
fichiers = os.listdir(repertoire)
for fichier in fichiers:
    if os.path.isfile(fichier):
        if os.path.splitext(fichier)[1] == ".7z":
            extraction7z(fichier)
        elif os.path.splitext(fichier)[1] == ".zip":
            extractionZip(fichier)
        elif os.path.splitext(fichier)[1] == ".rar":
            fichiersRAR.append(fichier)

if len(fichiersRAR):
    print("Les fichiers suivants n'ont pas été faits:")
    for fichierRAR in fichiersRAR:
        print(fichierRAR)



import requests
import numpy as np
#liste erstellen
allhtml = []
#zahlenwert für die Seitenzahl pro internetseite, Abstand von 28
pages = np.arange(3332, 6608, 28)
# für den definierten Zahlenbereich die jeweilige Internetseite aufrufen und in die Liste allhtml einfügen
# erstere beide Zahlen müssen verändert werden, falls Bilder 1-3332
for page in pages:
    page = requests.get("http://www.marquesdecollections.fr/result.cfm?sparam=2&search=&artcoll=&artname=&textveld=0&textveld2=tout&textIni=&textveld3=0&textveld4=tout&textIni2=&image=0&image2=tout&image3=0&image4=tout&technique=marque+estamp%C3%A9e&technique2=0&color=0&tekst=&begin=" + str(page) + "&limnum=6633&lang=3")
    allhtml.append(page.content.decode("utf-8"))
#Parser erstellen
from html.parser import HTMLParser
class FritsLugt(HTMLParser):
    def __init__(self): # Konstruktor der Klasse FritsLugt wird aufgerufen und die Liste results wird erstellt
        super().__init__() # Aufruf des Konstruktors der Basisklasse HTMLParser wird aufgerufen
                            # super bezieht sich auf die Basisklasse HTMLParser und ruft den Konstruktor auf und übergibt die Parameter self
        self.results=[] # Liste wird erstellt und mit dem Namen results bezeichnet
    def handle_starttag(self, tag, attrs): # Methode handle_starttag wird aufgerufen und die Parameter tag und attrs werden übergeben
        if tag == "img": # wenn der Parameter tag den Wert "img" hat wird die folgende Bedingung ausgeführt
            for name, link in attrs: # für den Parameter name und link wird die Bedingung ausgeführt
                if name == "src" and link.endswith(".jpg"): # wenn der Parameter name den Wert "src" hat und der Parameter link mit ".jpg" endet wird die folgende Bedingung ausgeführt
                    self.results.append(link)  #
parser = FritsLugt() # Objekt der Klasse FritsLugt wird erstellt und mit dem Namen parser bezeichnet
parser.feed(str(allhtml)) # Methode feed wird aufgerufen und der Parameter allhtml wird übergeben
import os
imgData = "/Pfad/für/Speicherort/der/Bilder/eingeben"
try:
    os.path.exists(imgData)
except:
    pass
for url in parser.results:
        f = open((imgData + '{}.jpg'.format(os.path.basename(url).split(".")[0])),'wb')
        f.write(requests.get(url).content)
        f.close()

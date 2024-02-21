<!-- https://github.com/skills/communicate-using-markdown -->


# Grading Criteria Programmieren T3INF1004
In jedem Unterbereich werden die Punkte (gerne auch Links ins GIT) erklärt, wie das LO erreicht worden ist.
Alle Kriterien betreffen nur die Projektarbeit. Beweismaterial kommt aus dem Gruppenprojekt.

## FACHKOMPETENZ (40 Punkte)

# Die Studierenden kennen die Grundelemente der prozeduralen Programmierung. (10)
Das Projekt wurde in unterschiedliche Dateien/Klassen aufgeteilt. Diese wiederum haben verschiedene Methoden, welche
unterschiedliche Zwecke erfüllen. Damit wurde ein Gesamtproblem in viele kleine Teilprobleme unterteilt und die
prozedurale Programmierung wurde umgesetzt.

# Sie können die Syntax und Semantik von Python (10)
Hier haben wir einige Verbesserungsvorschläge anzumelden.

Zunächst wurde eine objektorientierte Programmierung angestrebt, was positiv hervorzuheben ist. Hierbei sollte jedoch
auch auf einen konsequenten Stil geachtet werden.
```python
class Forumseite:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Forumseite")

        # Button erstellen
        self.hinzufuegen_button = tk.Button(self.root, text="Hinzufügen", command=self.hinzufuegen)
        self.hinzufuegen_button.pack()
```
Hier wurde Beispielsweise ein schöner Konstruktor für eine Klasse erstellt während hier ...
```python
#Fenster "Titelseite" erstellen
forumseite =  Tk()
(forumseite.title('Wilkommen im Karteikartensystem'))

# Ikon hinzufügen (auskommentiert)
forumseite.iconbitmap("hand-page01.ico")
```
leider die Klasse (Forumseite.py) im Nichts beginnt.

Des Weiteren sollte man auf ungenutzte Import-Statements achten und auf diese verzichten. Diese werden grau von der IDE
unterlegt und "fressen" lediglich Leistung beim Programmablauf.
```python
import tkinter as tk # unused
from tkinter import messagebox # unused
import sys # unused
import time
import subprocess
```

Positiv hervorzuheben gilt der, trotz dessen, lesbare Code. Die Variablen sind sprechend formuliert und der Code wurde
schön kommentiert. Dies hilft beim Verständnis der Gedankengänge ungemein.
```python
#Button Einführung
EinfuehrungButton = Button(forumseite, text='Einführung', bg='darkgrey', fg='white', height=10, width=35,font = myFont, command = ClickEinfuehrung).grid(row=1, column=1)

#Button Lernen
LernenButton = Button(forumseite, text='Lernen', bg='darkgrey', fg='white', height=10, width=35,font = myFont, command = ClickLernen ).grid(row=2, column=1)

#Button Hinzufügen
HinzufuegenButton = Button(forumseite, text='Hinzufügen', bg='darkgrey', fg='white', height=10, width=35,font = myFont, command= ClickHinzufuegen ).grid(row=1, column=2)

#Button Beenden
BeendenButton = Button(forumseite, text='Beenden', bg='darkgrey', fg='white', height=10, width=35,font = myFont, command= Beenden).grid(row=2, column=2)
```

# Sie können ein größeres Programm selbständig entwerfen, programmieren und auf Funktionsfähigkeit testen (Das Projekt im Team) (10)
Die Zusammenarbeit ist als unbeteiligte Person schwer einzuschätzen, anhand der Commits würde man darauf schließen,
dass es ein Ein-Mann-Projekt ist, was jedoch nicht unbedingt repräsentativ sein muss.

Ansonsten ist die Funktionsfähigkeit generell gegeben, die Fehlermeldung bei Programmstart könnte jedoch noch behoben
werden.

# Sie kennen verschiedene Datenstrukturen und können diese exemplarisch anwenden. (10)
Das Projekt sieht verschiedene Datenstrukturen vor. Zunächst gilt hier das Modul Tkinter hervorzuheben. Dieses wurde
ausgiebig genutzt, um die gesamte GUI aufzubauen.
```python
self.root = tk.Tk()
self.root.title("Forumseite")

# Button erstellen
self.hinzufuegen_button = tk.Button(self.root, text="Hinzufügen", command=self.hinzufuegen)
self.hinzufuegen_button.pack()
```

Des Weiteren wurde auch eine externe Datei eingebunden was auch positiv zu erwähnen ist.
```python
with open("Datenbank.txt", "w") as file:
    for key in text_dict.keys():
        if key and text_dict[key]:
            file.write(f"{key}{text_dict[key]}")
```

Auch ein Errorhandler ist zu erwähnen.
```python
try:
    # Start Titelseite.py
    titelseite_process = subprocess.Popen(["python", "Titelseite.py"])

    # Wait for 3 seconds
    time.sleep(3)

    # Close Titelseite.py
    titelseite_process.terminate()

    # Open Forumseite.py
    subprocess.Popen(["python", "Forumseite.py"])

except FileNotFoundError:
    print("Error: Make sure Titelseite.py and Forumseite.py exist in the same directory.")
```

Hinzu kommen dann noch For-Schleifen und If-Verzweigungen.
```python
for key in text_dict.keys():
    if key and text_dict[key]:
        file.write(f"{key}{text_dict[key]}")
```


## METHODENKOMPETENZ (10 Punkte)

# Die Studierenden können eine Entwicklungsumgebung verwenden um Programme zu erstellen (10)
Zu den verwendeten Tools gibt es für uns offensichtlich nur 
[GitHub](https://github.com/ArthurFleck35x/Karteikartensystem). Weitere Tools können nicht identifiziert werden.

## PERSONALE UND SOZIALE KOMPETENZ (20 Punkte)

# Die Studierenden können ihre Software erläutern und begründen. (5)
Wir können dies nur anhand der Kommentare im Code beurteilen. Diese sind vorhanden und größtenteils verständlich.

An manchen Stellen im Code dürften es jedoch auch noch ein paar mehr, bzw. ausführlichere Kommentare sein.
```python
# Hintergrundfarbe von "Hinzufügen" auf oliv setzen
titelseite.configure(bg='olive')
```
Dieses Statement wirkt zum Beispiel nur, wenn das Fenster in der Größe verändert wird und das Label nicht mehr den
kompletten Bildschirm belegt. Dies ist auf den ersten Blick nicht ersichtlich.

# Sie können existierenden Code analysieren und beurteilen. (5)
Diese "grading criteria" ist für die Gruppe des Karteikartensystems entstanden. 

Link zum Projekt [hier](https://github.com/ArthurFleck35x/Karteikartensystem).

# Sie können sich selbstständig in Entwicklungsumgebungen und Technologien einarbeiten und diese zur Programmierung und Fehlerbehebung einsetzen. (10)
Anhand des Codes ist ersichtlich, dass mit dem Modul Tkinter gearbeitet wurde. Dieses wurde in den Vorlesungen 
nicht behandelt und lässt folglich darauf schließen, dass die Inhalte eigenständig erarbeitet wurden.
```python
import tkinter as tk
```

Des Weiteren wurden auch externe Dateien eingebunden und zur Zwischenspeicherung verwendet.
```python
def lade_fragen_antworten():
    try:
        with open("datenbank.txt", "r", encoding="utf-8") as file:
            fragen_antworten = [line.strip() for line in file.readlines()]
        return fragen_antworten
    except FileNotFoundError:
        print("Datei 'datenbank.txt' nicht gefunden.")
        return []
```

## ÜBERGREIFENDE HANDLUNGSKOMPETENZ (30 Punkte)

# Die Studierenden können eigenständig Problemstellungen der Praxis analysieren und zu deren Lösung Programme entwerfen (30)
Die Aufgabe ein Karteikartensystem von Grund auf zu erstellen ist durchaus eine komplexe Problemstellung.
In diesem Projekt sieht man, dass sich im Vorfeld Gedanken gemacht wurden wie das Problem unterteilt werden kann, damit
es "bearbeitbar" wird und man einen Anfang findet. Die Struktur des Projektes lässt auf eine schrittweise Bearbeitung
schließen, was der prozeduralen Programmierung entspricht und sicherlich sinnvoll für solch ein Projekt ist. Dadurch
wird das Gesamtproblem greifbar gemacht und auch die Teamarbeit wird ermöglicht.


## Kenntnisse in prozeduraler Programmierung:

# - Algorithmenbeschreibung
Hier zu sehen ist eine kurze Beschreibung was diese Methode / dieser Algorithmus erledigt.
```python
def execute_titelseite():
    """
    Führt Titelseite.py für 3 Sekunden aus und öffnet Forumseite.py.
    """
```

# - Datentypen
Das Projekt beinhaltet verschiedene Datentypen. Es wurde mit Objekten von Tkinter gearbeitet, ...
```python
self.master.iconbitmap("hand-page01.ico")

self.frage_text = tk.Label(master, text=self.frage_antwort_liste[self.aktuelle_frage_index], height=5, width=30, bg='darkgrey', fg='white', borderwidth=2, relief="sunken")

self.antwort_button = tk.Button(master, text="Antwort", bg='darkgrey', fg='white', height=2, width=25,font = self.myFont, command=self.zeige_antwort)
```

es wurde mit Schriftarten gearbeitet, ...
```python
myFont = font.Font(size=50, weight="bold", family="Helvetica")
```

es wurde mit Strings gearbeitet, ...
```python
text = "Im Forum findest du alles was du zum Lernen brauchst."
```

und auch mit Indexen, sprich Integers, ...
```python
antwort_index = self.aktuelle_frage_index + 1
```

und vielem mehr.

# - E/A-Operationen und Dateiverarbeitung
E/A-Operationen werden verwendet, um Daten zwischenzuspeichern.
```python
def speichern():
    with open("Datenbank.txt", "w") as file:
        for key in text_dict.keys():
            if key and text_dict[key]:
                file.write(f"{key}{text_dict[key]}")
```

# - Operatoren
Das Projekt beinhaltet Vergleichsoperatoren, ...
```python
if antwort_index < len(self.frage_antwort_liste):
```

sowie Rechenoperatoren.
```python
self.aktuelle_frage_index += 2
```

# - Kontrollstrukturen
Als Kontrollstrukturen wurden sowohl If-Verzweigungen, ...
```python
if antwort_index < len(self.frage_antwort_liste):
```

als auch Schleifen verwendet.
```python
fragen_antworten = [line.strip() for line in file.readlines()]
```

# - Funktionen
Das Projekt sieht viele Methoden und Funktionen vor. Hier ein Beispiel:
```python
def ClickForum():
    # Hier öffnen wir die "einführung.py" Datei mit subprocess
    subprocess.Popen(["python", "Forumseite.py"])
    speichern()
    master.destroy()
```

# - String-Verarbeitung
Im Projekt werden zum Beispiel die Fragen als Strings verarbeitet und dann zwischengespeichert.
```python
def speichereDieKarte():
    text_key = entry_frage .get("1.0", tkinter.END)
    text_value = entry_antwort.get("1.0", tkinter.END)
    text_dict[text_key] = text_value
    entry_antwort.delete(1.0, tkinter.END)
    entry_frage.delete(1.0, tkinter.END)
```

# - Strukturierte Datentypen
Strukturierte Datentypen werden hier auch zur Speicherung von Fragen verwendet.
```python
text_dict = {}
```

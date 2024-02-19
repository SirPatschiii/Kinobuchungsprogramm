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
<!-- Jeder in der Gruppe: You have helped someone else and taught something to a fellow student (get a support message from one person) -->

# Sie können existierenden Code analysieren und beurteilen. (5)
<!-- Pro Gruppe:You have critiqued another group project. Link to your critique here (another wiki page on your git) and link the project in the critique, use these evaluation criteria to critique the other project. Make sure they get a top grade after making the suggested changes -->

# Sie können sich selbstständig in Entwicklungsumgebungen und Technologien einarbeiten und diese zur Programmierung und Fehlerbehebung einsetzen. (10)
<!-- Which technology did you learn outside of the teacher given input -->
<!-- Did you or your group get help from someone in the classroom (get a support message here from the person who helped you) -->



## ÜBERGREIFENDE HANDLUNGSKOMPETENZ (30 Punkte)

# Die Studierenden können eigenständig Problemstellungen der Praxis analysieren und zu deren Lösung Programme entwerfen (30)
<!-- Which parts of your project are you proud of and why (describe, analyse, link) -->
<!-- Where were the problems with your implementation, timeline, functionality, team management (describe, analyse, reflect from past to future, link if relevant) -->



## Kenntnisse in prozeduraler Programmierung:

# - Algorithmenbeschreibung

# - Datentypen

# - E/A-Operationen und Dateiverarbeitung

# - Operatoren

# - Kontrollstrukturen

# - Funktionen

# - Stringverarbeitung

# - Strukturierte Datentypen



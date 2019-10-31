# 4 Gewinnt Bot Turnier

Willkommen beim wichtigsten Kampf des Jahrhunderts.
 Das «4 Gewinnt» Turnier ist ein Turnier wobei nur
  Bots gegeneinander spielen. Und woher kommen die Bots?
   Da kommt ihr ins Spiel. Jeder der Interessiert ist und 
   etwas lernen will darf beim Turnier mitmachen indem sie 
   Ihren eigenen (oder mehrere) Bots schreiben.

## Wie funktioniert denn ein Bot?

Es gibt viele verschieden Möglichkeiten
 wie man ein Bot schreiben kann.
  Man kann ein Deeplearning Bot schreiben,
   der selber trainiert werden muss damit er funktioniert.
    Man kann aber auch ein Bot schreiben der Wahrscheinlichkeiten
     berechnet, und falls man sich ganz glücklich
      fühlt kann man sogar ein Bot schreiben der alles 
      auf gut Glück ratet.
      
## Wie Kann ich mein Projekt richtig Einstellen

Um beim Turnier mitzumachen solltet ihr zuerst das GitHub Projekt Clonen. 
Ich erkläre euch hier wie man das mit PyCharm machen kann,
 aber es sollte ähnlich funktionieren für andere IDEs.
 
Zuerst solltet ihr PyCharm von Jetbrains installieren falls ihr noch keine anderen Tools habt. 
Dann schliesst alle Projekte falls ihr schon eins offen hattet 
und ihr solltet dann die Möglichkeit haben, ein Projekt von Version Control zu holen..

![Projekt Clonen](https://raw.githubusercontent.com/jorgeparavicini/FourWins/master/images/Jetbrains%20Clone.png)

Klickt auf diese Option und setzt bei der URL den volgenden Link ein:

> https://github.com/jorgeparavicini/FourWins.git

Nun könnt ihr das Grundprojekt Clonen und sobald es Fertig ist, könnt ihr es aufmachen.

## Wie kann ich denn endlich den Bot schreiben?

Wenn Ihr das Projekt Korrekt Geclont habt sollte eure Ordnerstruktur ungefähr so aussehen:

![Ordner Struktur](https://raw.githubusercontent.com/jorgeparavicini/FourWins/master/images/Folder%20Structure.png)

Um einen neuen Bot zu schreiben müsst ihr eine neue Python Datei unter dem Ordner "bots" erstellen.
Dies Könnt ihr tun indem ihr auf den Ordenr rechtsklicken und "Neu > Python Datei" wählen. 
Gebt einen Namen ein der euren Bot passt und öffnet die Datei. Nun können wir anfangen den bot zu schreiben.

Damit der Turnier Manager euren Bot finden kann, **muss** er eine Unterklass des `BaseBot` sein.
Ihr tut das indem ihr eine neue Klasse definiert:

```python
class BotName(BaseBot):
    ...
```
Der Name `BaseBot` könnt ihr beliebig ändern auf was ihr wollt.  

Um euren Bot einen Namen zu geben setzt unterhalb der oben genannter Zeile die folgende Zeile ein:

```python
name = "<Euer Bot Name>"
```
wobei `<Euer Bot Name>` der name euer Botes ist.

Nun habt ihr gesagt, dass wir ein neuer Bot haben wollen, der alles übernimmt was im `BaseBot` schon existiert.
Dies müsst ihr übernehmen sonst kann der Turnier Manager nicht mit eurem Bot kommunizieren, plus hat es viele nützliche funktionen die euch helfen können.

Damit eurer Bot überhaupt versteht müsst ihr die Datei wo der BaseBot geschrieben ist importieren.
Dies tut ihr indem ihr die volgende zeile am Anfang eurer Bot Datei hinschreibt:

```python
from . import BaseBot, CellState
```

Damit Importiert ihr die Klasse `BaseBot` und `CellState` welche euch helfen kann zu identfizieren,
wem eine Zelle gehört.

### Wie gehts weiter?

Nun habt ihr das basische erledigt und könnt anfangen euren eigenen Code zu schreiben.
Es gibt eine funktion die ihr implementieren müsst, dies heist `get_guess` und muss eine ganze Nummer zurückgeben.
Damit wird der TurnierManager euch fragen in welcher Zeile ihr euren Chip hintun werdet.

Doch passt auf, falls eure Antwort invalid ist, wird er ignoriert und der gegnerische Bot ist wieder daran.
Es gibt 2 Möglichkeiten wie ihr ein Invaliden Entscheid treffen könnt.
- Der Entscheid ist ausserhalb des Spielfeldes, das Spielfeld geht von 0 - `grid.width - 1`
das "-1" ist wichtig da das Feld bei 0 anfängt.
- Der Entscheid ist in einer voller Spalte. Man kann natürlich nicht ein Chip reintun wo die Spalte schon voll ist.

Wenn ihr das beachtet könnt ihr in eurer Bot class die volgende Funktion implementieren:

```python
def get_guess(self) -> int:
    ...
```

Sobald diese Funktion eingerichtet ist könntet ihr eurer Bot einsetzen

Bis jetzt sollte euer Bot so aussehen

```python
from . import BaseBot, CellState

class BotName(BaseBot):
    name = "Test Bot"
    def get_guess(self) -> int:
        return 0
```

das `return 0` solltet ihr nun so abändern dass es immer eine korrekte Zahl zurückgibt.

## Spiel Testen

Es gibt zwei Arten wie ihr das Spiel starten könnt in der Konsole oder Graphisch.
Um das Spiel in der Konsole abzuspielen müsst Ihr Rechts Click auf die Datei `four_wins.py`
machen und die Option `Run four_wins.py` auswählen.


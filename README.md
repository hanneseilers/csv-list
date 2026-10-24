# CSV-Tabellenansicht

Einzelne HTML-Seite zum interaktiven Durchsuchen beliebiger CSV-Dateien (läuft komplett im Browser, keine Daten verlassen den Rechner).

- `index.html` im Browser öffnen, dann **Datei wählen…** oder CSV per Drag & Drop auf die Seite ziehen
- Volltextsuche, Filter pro Spalte, Sortierung, Spalten ein-/ausblenden
- Klick auf eine Zeile zeigt alle Details rechts
- Gefilterte Liste als CSV exportieren

Trennzeichen und Zeichensatz werden automatisch erkannt.

## Build

`src/template.html` ist die Quelle, `index.html` wird daraus erzeugt:

```
python3 src/build.py index.html                 # leere Seite
python3 src/build.py index.local.html daten.csv # mit eingebetteten Daten (Semikolon-CSV)
```

CSV-Dateien und `index.local.html` sind per `.gitignore` ausgeschlossen.

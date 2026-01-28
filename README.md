# Python-Übungsset (100 Funktionen)

Dieses Repository enthält 100 Basis-Übungsfunktionen in `aufgaben.py`. Jede
Funktion hat einen deutschen Docstring, `pass` als Platzhalter und soll von den
Studierenden implementiert werden. Fokus: Strings, Listen, Dicts/Sets,
Schleifen, einfache Mathematik und saubere Funktionalität.

## Aufteilung nach GitHub-Benutzernamen (10 Personen, je 10 Aufgaben)
- **84edu**: Funktionen 001–010 (`aufgabe_001` bis `aufgabe_010`)
- **crazyhome77**: Funktionen 011–020 (`aufgabe_011` bis `aufgabe_020`)
- **hallochupi-sketch**: Funktionen 021–030 (`aufgabe_021` bis `aufgabe_030`)
- **jess-compliance-dev**: Funktionen 031–040 (`aufgabe_031` bis `aufgabe_040`)
- **Kenan999**: Funktionen 041–050 (`aufgabe_041` bis `aufgabe_050`)
- **lgoik90-progfrog**: Funktionen 051–060 (`aufgabe_051` bis `aufgabe_060`)
- **NorbertFabian65**: Funktionen 061–070 (`aufgabe_061` bis `aufgabe_070`)
- **sabrinabudiono-art**: Funktionen 071–080 (`aufgabe_071` bis `aufgabe_080`)
- **ThiasRS**: Funktionen 081–090 (`aufgabe_081` bis `aufgabe_090`)
- **vmichele80**: Funktionen 091–100 (`aufgabe_091` bis `aufgabe_100`)

Hinweis: Die Nummer ist im Funktionsnamen enthalten. Bitte bearbeitet nur den
euch zugewiesenen Bereich, damit Merge-Konflikte minimiert werden. Eure
Zuweisung steht auch direkt als Kommentar über jeder Aufgabe in `aufgaben.py`.

## Vorgehensweise für Studierende
1. Repository klonen: `git clone <repo-url>`
2. In das Repo wechseln: `cd Project-x`
3. Eigenen Branch anlegen (Beispiel für 84edu):
   - `git checkout -b 84edu/aufgaben-001-010`
4. Nur eure Funktionen in `aufgaben.py` implementieren (Docstring lesen).
5. Lokale Checks (Beispiele):
   - Optional: einfache Selbsttests schreiben/ausführen
   - Falls Tests bereitgestellt werden: `python -m pytest`
6. Änderungen prüfen: `git status`
7. Änderungen vormerken und committen:
   - `git add aufgaben.py`
   - `git commit -m "Implementiere Aufgaben 001-010"`
8. Branch pushen: `git push origin 84edu/aufgaben-001-010`
9. Pull Request (PR) im Git-Host erstellen. Reviewer: Dozent oder Teamlead.
10. Feedback einarbeiten, PR aktualisieren (`git add` + `git commit --amend` oder
    neuer Commit, dann `git push --force-with-lease` bei amend).

## Qualitätsleitplanken
- Halte dich an PEP 8 (Lesbarkeit vor Cleverness).
- Sinnvolle Variablennamen, kurze Funktionen, keine unnötigen globalen Zustände.
- Docstrings nicht löschen; ergänze Beispiele, falls hilfreich.
- Prüfe Randfälle (leere Listen, None, negative Zahlen, Sonderzeichen).
- Schreibe kleine, wiederverwendbare Hilfsfunktionen nur, wenn nötig.

## Konflikte vermeiden
- Arbeite ausschließlich im zugewiesenen Funktionsbereich.
- Ziehe vor neuem Work `git pull origin main` (oder `git fetch` + `git rebase`).
- Bei Konflikten: ruhig bleiben, Konflikt markieren, lokal testen, erst dann
  committen.

## Abgabeformat
- Ein PR pro Person/Branch.
- Commit-Messages: kurz und beschreibend (z.B. `Implementiere Aufgaben 035-040`).
- Keine Änderungen an fremden Bereichen oder an der Aufteilung.

Viel Erfolg und fragt bei Unklarheiten früh nach!

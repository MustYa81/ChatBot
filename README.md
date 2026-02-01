# ChatBot Projekt 23 
**Ostfalia / TU Clausthal – Wintersemester 2025/26**

Ein modularer, regelbasierter deutschsprachiger Chatbot mit erweiterten Funktionen:  
Fragen-Antwort-System, Wetterabfragen, Trivia-Spiel, Temperaturvergleich (Sense HAT vs. OpenWeather) und Service-Provider-Tools.

Projekt im Rahmen des Moduls [Interdisziplinäres Digitalisierungsprojekt 1] – Team ChatBot-23.


## Inhaltsverzeichnis
- [Überblick](#überblick)
- [Features](#features)
- [Voraussetzungen](#voraussetzungen)
- [Installation](#installation)
- [Konfiguration (OpenWeather API-Key)](#konfiguration-openweather-api-key)
- [Projektstruktur](#projektstruktur)
- [CLI Nutzung](#cli-nutzung)
- [Datenformate](#datenformate)
- [Raspberry Pi vs. Laptop Setup](#raspberry-pi-vs-laptop-setup)
- [Logging](#logging)
- [Tests](#tests)
- [Troubleshooting](#troubleshooting)
- [Lizenz](#lizenz)


## Überblick
Der ChatBot beantwortet vordefinierte Fragen aus einer Wissensbasis. Unbekannte Fragen führen zu Vorschlägen (Keyword‑Treffer) oder einer Standardantwort.
Zusätzlich erkennt er Wetter-Intents (z.B. „Wetter in Berlin 2026-02-05“) und kann ein Trivia-Spiel starten.

Für das Service‑Provider‑Szenario gibt es eine Temperaturgenauigkeits‑Auswertung: tägliche Temperaturänderung **Δ = max(T) − min(T)** aus Sensor‑CSV (Sense HAT) vs. Wetter‑CSV (OpenWeather Logger).


## Features
- Interaktiver Chat (Standardmodus) mit:
  - Exit-Kommandos: `exit`, `quit`, `bye`, `q`, `ende`, `tschüss`
  - Trivia-Start im Chat: `trivia`
  - Trivia beenden: `exit trivia`
- Direkte Frage per CLI: `--question "..."`
- Alle Fragen aus der Wissensbasis auflisten: `--list-questions`
- CSV-Import einer neuen Wissensbasis: `--import-csv Data/new_questions.csv`
- Wetter per CLI: `--weather CITY` optional mit `--date YYYY-MM-DD`
- Temperaturvergleich (letzte 3 überlappende Tage): `--temp-accuracy`
- Logging in `app.log`: `--log` und Level via `--level INFO|WARNING`
- Debug: `--debug` (führt Unit‑Tests aus)


## Voraussetzungen
- Python **3.8+**
- Internetzugang (nur für Wetter/Logger)
- **OpenWeather API Key** als Umgebungsvariable `OPENWEATHER_API_KEY`

### Python Packages
Minimal (Runtime):
- `requests` (Wetter-API)  
- `pandas` (CSV‑Import in `main.py`)

Empfohlen (Dev/Test):
- `pytest` (für `questions_tests2.py`)


## Installation
```bash
# Optional: venv
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
```

**Vorschlag für requirements.txt**
```txt
pandas 3.0.0
requests 2.32.5
pytest 9.0.2
```


## Konfiguration (OpenWeather API-Key)
Setze den API‑Key als Environment Variable:

**Linux/macOS**
```bash
export OPENWEATHER_API_KEY="DEIN_KEY"
```

**Windows PowerShell**
```powershell
$env:OPENWEATHER_API_KEY="DEIN_KEY"
```

Optional (Komfort): `.env` + `python-dotenv`
- Nur nötig, wenn du Keys bequem aus `.env` laden willst.
- In deinem Code ist `python-dotenv` aktuell **nicht erforderlich** (es wird nicht importiert).


## Projektstruktur
Empfohlene Struktur (wie vom Code erwartet):

```
.
├── Data/
│   ├── questions_and_answers.json
│   ├── trivia_questions.json
│   ├── sense_hat_temperature_data.csv
│   └── weather_temperature_data.csv
│
├── docs/
│   ├── architecture_technical_specs.md
│   └── Meeting_Log_and_Progress.md
│
├── src/
│   ├── __init__.py
│   ├── weather.py
│   ├── forecast_logger.py
│   ├── compare_temperatures.py
│   ├── user_interaction.py
│   ├── validator.py
│   └── trivia_game.py
│
├── tests/
│   ├── __init__.py
│   ├── questions_tests.py
│   └── questions_tests2.py
│
├── main.py
├── README.md
└── requirements.txt
```

**Wichtig:** Auf Linux (Raspberry Pi) ist `Data/` case‑sensitive. Ordner muss exakt `Data` heißen.


## CLI Nutzung

### Hilfe
```bash
python main.py --help
```

### Interaktiver Chat (Default)
```bash
python main.py
```

### Eine Frage direkt stellen
```bash
python main.py --question "Wer bist du?"
```

### Alle bekannten Fragen anzeigen
```bash
python main.py --list-questions
```

### Wissensbasis aus CSV importieren
```bash
python main.py --import-csv Data/new_questions.csv
```

### Trivia starten
```bash
python main.py --trivia
```

**Trivia beenden (im Spiel):**
- `exit trivia` / `quit trivia` / `stop trivia`

### Wetter per CLI
Aktuelles Wetter:
```bash
python main.py --weather Berlin
```

Optionaler Termin (wenn im 5‑Tage Forecast verfügbar):
```bash
python main.py --weather Berlin --date 2026-02-05
```

### Temperaturvergleich (Sensor vs. OpenWeather Log)
```bash
python main.py --temp-accuracy
```

Verwendete Dateien (Default):
- `Data/sense_hat_temperature_data.csv`
- `Data/weather_temperature_data.csv`


## Datenformate

### 1) Wissensbasis JSON
Pfad: `Data/questions_and_answers.json`

Format: Dictionary `{question: {answers: [...], variants: [...], keywords: [...]}}`  
Beispiel: siehe Datei in `Data/`.

### 2) Trivia JSON
Pfad: `Data/trivia_questions.json`

Format: Liste von Fragen:
```json
[
  {
    "question": "…",
    "options": ["A", "B", "C", "D"],
    "correct_index": 1
  }
]
```

### 3) Sensor CSV (Sense HAT)
Pfad: `Data/sense_hat_temperature_data.csv`  
Header muss Spalten enthalten, die mit **Timestamp** und **Temperature** beginnen.  
Timestamps werden akzeptiert als:
- `YYYY-mm-dd HH:MM:SS`
- `dd/mm/YYYY HH:MM`

### 4) Wetter CSV (OpenWeather Logger)
Default Output: `Data/weather_temperature_data.csv`  
Header wird vom Logger gesetzt:
- `Timestamp`, `Temperature (°C)`, `Location`


## Raspberry Pi vs. Laptop Setup

### Raspberry Pi (Sense HAT)
- Ziel: `Data/sense_hat_temperature_data.csv` erzeugen (mit deinem Sense‑HAT‑Logger)
- Datei anschließend im Projekt unter `Data/` verfügbar machen (kopieren/syncen)

### Laptop/PC
1) OpenWeather Logger laufen lassen (schreibt Wetter‑CSV):
```bash
python forecast_logger.py --city Berlin
```
2) Danach Accuracy‑Report:
```bash
python main.py --temp-accuracy
```


## Logging
Logging ist standardmäßig aus.

Aktivieren:
```bash
python main.py --log
```

Log-Level setzen:
```bash
python main.py --log --level INFO
```

Ergebnis: `app.log` im Projektverzeichnis.


## Tests
Unittest (Standardlib):
```bash
python -m unittest
```

Pytest (wenn installiert):
```bash
pytest
```


## Troubleshooting

### Wetter-Fehler 404 / City wird „komisch“
Wenn du Datum an den City‑String hängst (z.B. „Berlin 2026-01-10“), interpretiert OpenWeather das als Stadtnamen.
Nutze stattdessen:
```bash
python main.py --weather Berlin --date 2026-01-10
```

### `Data/` nicht gefunden (Pi)
Ordnername muss exakt `Data` heißen (Groß-/Kleinschreibung!).

### Import schlägt fehl
- Pfad prüfen
- Datei muss `.csv` sein
- CSV muss erwartete Spalten/Indexstruktur haben (siehe `main.py` Importlogik)


## Lizenz
Füge hier eure Lizenz/Abgabehinweise ein (z.B. MIT) oder nenne die Kursvorgaben.

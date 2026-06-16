# Pflegeplanet – Website-Nachbau

Statischer Nachbau von **pflege-planet.de** inkl. aller Landingpages, erstellt als
reines HTML/CSS/JS (ohne Build-Abhängigkeiten, ohne Framework).

## Seiten

| Seite | Pfad |
|-------|------|
| Startseite | `/index.html` |
| Pflegebox | `/pflegebox/` |
| Pflegebox anpassen | `/pflegebox/pflegebox-anpassen/` |
| Pflegehilfsmittel-Katalog | `/pflegehilfsmittel-katalog/` |
| Fragen & Antworten | `/fragen/` |
| Über uns | `/ueber-uns/` |
| Impressum | `/impressum/` |
| Datenschutz | `/datenschutz/` |

## Lokal ansehen

Da die Seiten root-relative Links (`/pflegebox/` …) verwenden – wie die Originalseite –
am besten über einen lokalen Server öffnen:

```bash
python3 -m http.server 8000
# danach http://localhost:8000 im Browser öffnen
```

## Design

Farben und Typografie wurden aus den Original-Screenshots übernommen:

- **Dunkles Teal-Grün** `#305850` – Sektionen, Footer, Headlines, Kontaktbereich
- **Lime-Akzent** `#aac63e` – Buttons, Links, Highlights, Icons
- **Sekundär-Grün** `#7baea7` – gedämpfte Sub-Headlines
- Schriften: **Quicksand** (Headlines/Navigation/Buttons) + **Mukta** (Fließtext)

Alle Texte (Hero, Voraussetzungen, Produkte, 3-Schritte-Ablauf, Testimonial,
FAQ, Impressum mit echten Firmendaten) entsprechen den Original-Inhalten.

## Aufbau / Wartung

- `assets/css/styles.css` – komplettes Design-System
- `assets/js/main.js` – Mobile-Navigation, FAQ-Accordion, aktive Nav-Markierung
- `assets/img/logo.svg` – Logo
- `index.html` – handgepflegte Startseite
- `build.py` + `pages_content.py` – erzeugen die Unterseiten aus gemeinsamen
  Bausteinen (Header, Kontaktsektion, Footer), damit Navigation/Layout überall
  identisch sind. Neu erzeugen mit: `python3 build.py`

## Hinweise

- **Bilder:** Die Originalfotos (Hero, Team, Tim Bodung, Produktbilder) konnten
  nicht aus der Live-Seite gezogen werden (Bot-Schutz + Netzwerk-Allowlist der
  Build-Umgebung). Als Platzhalter dienen passende Inline-SVG-Illustrationen.
  Echte Fotos einfach in `assets/img/` ablegen und die entsprechenden
  `<svg>`-Platzhalter durch `<img>` ersetzen.
- Das Kontaktformular ist Frontend-only (kein Versand-Backend hinterlegt).
- Die Datenschutzerklärung ist inhaltlich an Standard-DSGVO-Texte angelehnt und
  sollte vor Live-Betrieb rechtlich geprüft werden.

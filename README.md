# Pflegeplanet – Website (Next.js)

Nachbau von **pflege-planet.de** inkl. aller Landingpages – umgesetzt mit
[**Next.js**](https://nextjs.org) (App Router, React 19). Gleiches Design/HTML,
vorbereitet für schrittweise neue Funktionen (React-Komponenten & API-Routen).

## Schnellstart

```bash
npm install
npm run dev      # Entwicklungsserver: http://localhost:3000
npm run build    # Produktions-Build
npm run start    # Build lokal starten
```

## Projektstruktur

```
app/
  layout.jsx          # Root-Layout (Header, Footer, Interactions, globales CSS)
  globals.css         # komplettes Design-System
  content.js          # gemeinsame Bausteine (Header/Footer/Kontakt) + Seiteninhalte
  page.jsx                                  # /
  pflegebox/page.jsx                        # /pflegebox/
  pflegebox/pflegebox-anpassen/page.jsx     # /pflegebox/pflegebox-anpassen/
  pflegehilfsmittel-katalog/page.jsx        # /pflegehilfsmittel-katalog/
  fragen/page.jsx                           # /fragen/
  ueber-uns/page.jsx                        # /ueber-uns/
  impressum/page.jsx                        # /impressum/
  datenschutz/page.jsx                      # /datenschutz/
components/
  Contact.jsx         # Kontaktsektion (Formular + Ansprechpartner)
  Interactions.jsx    # 'use client' – Mobile-Nav, FAQ-Accordion, Formular, aktive Nav
public/
  assets/img/logo.svg
```

Die Seiteninhalte und die wiederkehrenden Bausteine (Header/Footer/Kontakt)
liegen als HTML-Partials in `app/content.js` und werden gerendert, damit der
Aufbau pixelgenau zum Original passt. Die Interaktivität läuft über die
React-Client-Komponente `Interactions.jsx`.

## Neue Funktionen ergänzen

- **React-Komponente / Seite:** neue Datei unter `app/.../page.jsx` (Route) oder
  `components/`. Neue interaktive Bausteine am besten direkt als React-Komponente
  (statt HTML-Partial) bauen.
- **Formular-Backend / API:** Route Handler unter `app/api/<name>/route.js`
  anlegen. Das Kontaktformular postet bereits auf `/api/kontakt`; aktuell wird
  der Submit clientseitig abgefangen (`Interactions.jsx`). Sobald
  `app/api/kontakt/route.js` existiert, kann dort echt verarbeitet/versendet
  werden.

## Design

Farben aus den Original-Screenshots gesampelt:

- **Dunkles Teal-Grün** `#305850` – Sektionen, Footer, Headlines, Kontaktbereich
- **Lime-Akzent** `#aac63e` – Buttons, Links, Highlights, Icons
- **Sekundär-Grün** `#7baea7` – gedämpfte Sub-Headlines
- Schriften: **Quicksand** (Headlines/Navigation/Buttons) + **Mukta** (Fließtext)

## Hinweise

- **Bilder:** Originalfotos (Hero, Team, Tim Bodung, Produkte) konnten nicht aus
  der Live-Seite gezogen werden (Bot-Schutz + Netzwerk-Allowlist). Als Platzhalter
  dienen Inline-SVGs – echte Bilder in `public/assets/img/` ablegen und einsetzen.
- Die Datenschutzerklärung ist an Standard-DSGVO-Texte angelehnt und sollte vor
  Live-Betrieb rechtlich geprüft werden.

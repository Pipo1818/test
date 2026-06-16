# Pflegeplanet – Website (Astro)

Nachbau von **pflege-planet.de** inkl. aller Landingpages – umgesetzt mit
[**Astro**](https://astro.build). Statisch-schnell, komponentenbasiert und
vorbereitet für schrittweise neue Funktionen.

## Schnellstart

```bash
npm install
npm run dev      # Entwicklungsserver: http://localhost:4321
npm run build    # Produktions-Build nach dist/
npm run preview  # Build lokal ansehen
```

## Projektstruktur

```
src/
  layouts/
    Base.astro          # HTML-Grundgerüst (Head, Header, Footer, Kontakt, Skripte)
  components/
    Header.astro        # Topbar + Navigation
    Footer.astro        # Footer + WhatsApp-Button
    Contact.astro       # Kontaktsektion mit Formular + Ansprechpartner
  pages/                # je Datei = eine Route
    index.astro                         # /
    pflegebox/index.astro               # /pflegebox/
    pflegebox/pflegebox-anpassen.astro  # /pflegebox/pflegebox-anpassen/
    pflegehilfsmittel-katalog.astro     # /pflegehilfsmittel-katalog/
    fragen.astro                        # /fragen/
    ueber-uns.astro                     # /ueber-uns/
    impressum.astro                     # /impressum/
    datenschutz.astro                   # /datenschutz/
  styles/
    styles.css          # komplettes Design-System
public/
  assets/img/logo.svg
  assets/js/main.js     # Mobile-Nav, FAQ-Accordion, Formular-Handling
```

## Neue Funktionen ergänzen

- **Statische Komponente/Seite:** neue `.astro`-Datei in `src/pages/` oder
  `src/components/` anlegen.
- **Interaktivität (Islands):** UI-Framework-Komponente (z. B. React/Svelte/Vue)
  via `npx astro add react` einbinden und mit `client:load` aktivieren.
- **Formular-Backend / API:** Server-Endpunkte unter `src/pages/api/*.ts` –
  dafür einen Adapter aktivieren (`npx astro add node` o. Ä.) und in
  `astro.config.mjs` `output: 'server'` setzen. Das Kontaktformular postet
  bereits auf `/api/kontakt`; aktuell wird der Submit clientseitig abgefangen.

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

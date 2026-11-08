# Stadtklima-Labor
**Fiktives, nichtkommerzielles wissenschaftliches Lehrprojekt** zu städtischen Wärmeinseln und klimaangepasster Stadtplanung. Die Inhalte beruhen auf DWD und Umweltbundesamt; es werden keine Messdaten oder institutionelle Zugehörigkeiten vorgetäuscht.

**Website:** https://dsongtn.github.io/stadtklima-labor/

## SEO-Fallstudie für F174V (HAW Kiel, November 2026)
- **Baseline:** `seo-baseline-v0.1` / Commit `d99816f454a2fe03068955e9ffa7f72f095738fa` – eine einzelne kurze Startseite mit allgemeinem Title, ohne Meta Description und ohne vertiefende interne Navigation.
- **Intervention:** aussagekräftige Seitentitel und Beschreibungen, nutzerorientierte H1/H2-Struktur, zusätzliche fachliche Seiten, nachvollziehbare Quellennachweise, interne Links und mobilfähige semantische Gestaltung.
- **Evidenz:** `git diff seo-baseline-v0.1..main`, `python3 tests/check_site.py`, veröffentlichte HTTP-Statuscodes und wiederholbare Checks. Eine frische Testseite besitzt noch keine nachweisbare organische Reichweitenverbesserung.
- **Geschützte Privatsphäre:** keine Tracker, Cookies, Werbeanzeigen, Nutzerkonten oder externen Fonts.

## Projektstruktur
```
index.html               Haupteinstieg: Was ist eine städtische Wärmeinsel?
massnahmen.html          Suchintention: Maßnahmen gegen Stadthitze
quellen.html             Literatur, Grenzen, Arbeitsweise
assets/site.css          gemeinsame responsive Gestaltung
sitemap.xml              kanonische öffentliche URLs
.nojekyll                GitHub Pages ohne Jekyll-Verarbeitung
tests/check_site.py      statische Qualitäts- und SEO-Prüfungen
evidence/                interne Mess- und Methodennotizen
```

## Reproduktion
```sh
python3 tests/check_site.py
git show seo-baseline-v0.1:index.html | head -n 10
git diff --stat seo-baseline-v0.1..main
```
GitHub Pages: Settings -> Pages -> Deploy from branch -> main / (root). GitHub übernimmt das Hosting unter der github.io-Domain; keine eigene Domain.

## Quellen
DWD: Klimadienste für Kommunen; UBA: Klimafolgen Handlungsfeld Bauwesen, Regenwasserverdunstung und Kühlung, naturbasierte Klimaanpassung, nachhaltige Gebäudeklimatisierung. Direkte Links und methodische Grenzen stehen unter [Quellen & Methode](https://dsongtn.github.io/stadtklima-labor/quellen.html).

# SEO-Fallstudie: Prüfprotokoll (08.11.2026)

## Website und Versionskontrolle
- Öffentliche Adresse: https://dsongtn.github.io/stadtklima-labor/
- GitHub Pages: main /(root), HTTPS aktiviert, keine eigene Domain.
- **Baseline:** Git-Tag `seo-baseline-v0.1`, Commit `d99816f454a2fe03068955e9ffa7f72f095738fa` (erste echte Projektversion, keine historische Bestandswebsite).
- **Optimierte Fassung:** Commit `715de0463da071e1f5764d1d995c1252e601a8d8`.
- Änderungen: `git diff seo-baseline-v0.1 715de04`.

## Ursprünglicher Zustand
- Eine öffentliche HTML-Startseite mit allgemeinen Informationen zum Stadtklima.
- Title: `Stadtklima – Wissensprojekt`.
- Keine Meta Description, keine eigenständigen vertiefenden Seiten, kein XML-Sitemap-Verzeichnis.
- HTTP GET im veröffentlichten Zustand: **200**, HTML-Antwort **2.167 Byte** (curl). Kein historischer organischer Traffic vorhanden.

## Änderungen der optimierten Fassung
- Eindeutiger Titel und Meta Description für jede wichtige Seite.
- Suchintent-getrennte Inhalte: Startseite „städtische Wärmeinsel“, zweite Seite „Maßnahmen gegen Hitze in Städten“, dritte Seite „Quellen und Methode“.
- Semantische Überschriften, interne Navigationslinks, Skip-Link, mobile CSS-Breakpoints und dokumentierte Kanonicals.
- Evidenzbasierte Inhalte mit DWD- und UBA-Quellen; bewusste Abgrenzung der fiktiven Projektidentität von realen Institutionen.
- Eine XML-Sitemap mit drei kanonischen URLs.

## Beobachtete technische Ergebnisse nach Veröffentlichung
| URL | HTTP | MIME | Übertragene Bytes |
|---|---:|---|---:|
| `/` | 200 | text/html | 10.378 |
| `/massnahmen.html` | 200 | text/html | 8.704 |
| `/quellen.html` | 200 | text/html | 7.405 |
| `/assets/site.css` | 200 | text/css | 6.959 |
| `/sitemap.xml` | 200 | application/xml | 428 |

Die Angaben beziehen sich auf den Projektpfad `/stadtklima-labor/` und wurden per `curl -L` vom MacBook gegen die öffentlichen URL-Adressen überprüft. GitHub Pages meldete den Build-Status **built**. Alle 3 HTML-Seiten haben individuelle Titles und Meta Descriptions (151/155/153 Zeichen), jeweils ein H1, korrekte kanonische URLs und funktionierende interne Linkziele. `python3 tests/check_site.py` meldete `ok: true` und keine gefundenen Fehler.

**Wichtig zur Interpretation:** Die optimierte Homepage ist größer, weil sie mehr Fachinhalt bietet. Dies ist keine gemessene Ladezeitverbesserung. HTTP-Downloadzeiten sind Momentaufnahmen und kein LCP/INP/CLS-Referenzwert.

## Externe SEO-Tools und fehlende Evidenz
- **Google PageSpeed Insights API** wurde für die mobile Webseite angefragt; die öffentliche API gab HTTP **429 (daily quota exceeded)** zurück. **Kein Lighthouse Score wurde erhoben**, und es werden keine Werte erfunden.
- Der Dozent nennt u.a. WebPageTest, Google Search Console und SEORCH. Ein Search-Console-Nachweis erfordert verifizierte Eigentümerschaft und eine neue Domain hat keine historische Datenreihe. Eine manuelle PageSpeed- oder SEORCH-Analyse im Browser kann zusätzlich nachgereicht werden.
- Es gibt noch keinen Nachweis, dass Google eine der drei Seiten indexiert, ein Ranking verbessert oder organische Klicks generiert hat. Solche Wirkungen sind keine legitime Vorher/Nachher-Kennzahl am Publikationstag.

## Grenzen und nächste Schritte
1. Bei Zugang zu PageSpeed Insights: mobile und Desktop-Tests mitsamt Datum/URL/Screenshots durchführen; Labordaten nicht als Feldmessung darstellen.
2. Optional Search Console für die URL-Prefix-Property nutzen und Sitemap einreichen, falls der Eigentümer die Verifizierung autorisiert.
3. Search-Intent-Passung später anhand realer Suchanfragen bewerten, nicht aus Meta-Tag-Längen ableiten.
4. Den 3–4-seitigen ECTS-PDF-Bericht mit Website, Baseline-Commit, Veränderungen, Testbefunden, Grenzen und Quellen erstellen.

Dieses Prüfprotokoll ist die Nachweisdokumentation zum Kurs. Es ist keine offizielle wissenschaftliche Studie.

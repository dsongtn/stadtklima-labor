#!/usr/bin/env python3
"""Reproducible static SEO checks; no simulated Google rankings."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit, unquote
from collections import Counter
import json
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://dsongtn.github.io"
PREFIX = "/stadtklima-labor/"
PAGES = ("index.html", "massnahmen.html", "quellen.html")

class Audit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.in_title = False
        self.in_head = False
        self.h1_count = 0
        self.headings = []
        self.description = ""
        self.canonical = ""
        self.lang = ""
        self.viewport = False
        self.links = []
        self.ids = set()
        self.images_missing_alt = 0
        self.nav_count = 0
        self.skip_link = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html": self.lang = a.get("lang", "")
        if tag == "head": self.in_head = True
        if tag == "title" and self.in_head: self.in_title = True
        if tag == "h1": self.h1_count += 1
        if tag in ("h1", "h2", "h3"): self.headings.append(tag)
        if tag == "nav": self.nav_count += 1
        if tag == "meta" and a.get("name", "").lower() == "description": self.description = a.get("content", "")
        if tag == "meta" and a.get("name", "").lower() == "viewport": self.viewport = True
        if tag == "link" and a.get("rel") == "canonical": self.canonical = a.get("href", "")
        if tag == "a":
            self.links.append(a.get("href", ""))
            if a.get("href") == "#inhalt": self.skip_link = True
        if tag == "img" and not a.get("alt") and a.get("alt") != "": self.images_missing_alt += 1
        if "id" in a: self.ids.add(a["id"])

    def handle_endtag(self, tag):
        if tag == "title": self.in_title = False
        if tag == "head": self.in_head = False

    def handle_data(self, data):
        if self.in_title: self.title += data

errors = []
audits = {}
parsed = {}
for file in PAGES:
    f = ROOT / file
    if not f.is_file():
        errors.append(f"Missing page: {file}")
        continue
    text = f.read_text(encoding="utf-8")
    doc = Audit()
    doc.feed(text)
    parsed[file] = doc
    url = ORIGIN + PREFIX + ("" if file == "index.html" else file)
    if doc.lang != "de": errors.append(f"{file}: expected lang=de")
    if not doc.viewport: errors.append(f"{file}: missing viewport")
    if len(doc.title.strip()) < 20: errors.append(f"{file}: weak/empty title")
    if not 70 <= len(doc.description) <= 200: errors.append(f"{file}: description length outside practical review range")
    if doc.h1_count != 1: errors.append(f"{file}: expected exactly one h1, found {doc.h1_count}")
    if doc.canonical != url: errors.append(f"{file}: incorrect canonical {doc.canonical!r}")
    if not doc.skip_link or "inhalt" not in doc.ids: errors.append(f"{file}: skip link not usable")
    if doc.images_missing_alt: errors.append(f"{file}: images missing alt")
    if doc.nav_count < 1: errors.append(f"{file}: missing navigation")
    if '<link rel="stylesheet" href="assets/site.css">' not in text: errors.append(f"{file}: missing shared stylesheet")
    audits[file] = {"title": doc.title.strip(), "description_length": len(doc.description), "h1_count": doc.h1_count, "internal_links": 0, "bytes_utf8": len(text.encode("utf-8")), "heading_count": len(doc.headings)}
for file, doc in parsed.items():
    base = ORIGIN + PREFIX + ("" if file == "index.html" else file)
    for href in doc.links:
        if not href or href.startswith(("mailto:", "javascript:")):
            continue
        target = urlsplit(urljoin(base, href))
        if target.netloc != urlsplit(ORIGIN).netloc or not target.path.startswith(PREFIX):
            continue
        audits[file]["internal_links"] += 1
        rel = unquote(target.path[len(PREFIX):])
        if not rel: rel = "index.html"
        target_file = ROOT / rel
        if not target_file.is_file(): errors.append(f"{file}: broken internal link to {href!r}")
        elif target.fragment and rel in parsed and target.fragment not in parsed[rel].ids:
            errors.append(f"{file}: broken fragment {href!r}")
if len({parsed[k].title for k in parsed}) != len(parsed): errors.append("Titles are not unique")
if len({parsed[k].description for k in parsed}) != len(parsed): errors.append("Descriptions are not unique")
try:
    ns = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    tree = ET.parse(ROOT / "sitemap.xml")
    urls = {x.text for x in tree.iter(ns + "loc")}
    expected = {ORIGIN + PREFIX + ("" if f == "index.html" else f) for f in PAGES}
    if urls != expected: errors.append(f"Sitemap URLs mismatch: {urls ^ expected}")
except Exception as e: errors.append(f"Invalid sitemap: {e}")
if not (ROOT / ".nojekyll").exists(): errors.append("Missing .nojekyll")
if not (ROOT / "assets/site.css").exists(): errors.append("Missing CSS")
print(json.dumps({"ok": not errors, "pages": audits, "sitemap_urls": len(PAGES), "errors": errors}, ensure_ascii=False, indent=2))
sys.exit(0 if not errors else 1)

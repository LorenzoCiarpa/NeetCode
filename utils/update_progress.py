#!/usr/bin/env python3
"""Rigenera la dashboard di progresso NeetCode dentro il README.

Scansiona la struttura prodotta dal GitHub Sync di NeetCode:

    <topic-folder>/<problem-slug>/submission-N.<ext>

Ogni slug viene risolto tramite utils/neetcode_catalog.json (piu' eventuali
override in utils/extra_problems.json) in (nome, difficolta, pattern). Il
risultato viene iniettato nel README tra i marker <!-- PROGRESS:START --> e
<!-- PROGRESS:END -->.

Uso:
    python utils/update_progress.py              # rigenera il README
    python utils/update_progress.py --report     # stampa gli slug sconosciuti
                                                 # gia' pronti da incollare in
                                                 # utils/extra_problems.json
"""

from __future__ import annotations

import argparse
import json
import subprocess
from collections import defaultdict
from pathlib import Path
from typing import NamedTuple

# --------------------------------------------------------------------------
# Configurazione
# --------------------------------------------------------------------------

# Quale lista tracciare nelle tabelle: "neetcode250" oppure "all".
# Cambia solo questa riga quando finisci i 250 e vuoi passare al catalogo pieno.
TRACK_LIST = "neetcode250"

# Se True, mostra la checklist espandibile di tutti i problemi della lista.
SHOW_CHECKLIST = True

# --------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "utils" / "neetcode_catalog.json"
OVERRIDES = ROOT / "utils" / "extra_problems.json"
README = ROOT / "README.md"

MARKERS = ("<!-- PROGRESS:START -->", "<!-- PROGRESS:END -->")

SKIP_DIRS = {".git", ".github", "utils", "scripts", "docs", "site", ".venv"}

DIFFICULTIES = ("Easy", "Medium", "Hard")
DIFF_EMOJI = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}

EXT_LANG = {
    ".py": "Python",
    ".ts": "TypeScript",
    ".js": "JavaScript",
    ".java": "Java",
    ".cpp": "C++",
    ".cs": "C#",
    ".go": "Go",
    ".rs": "Rust",
    ".kt": "Kotlin",
    ".swift": "Swift",
    ".sql": "SQL",
}


class Solved(NamedTuple):
    slug: str
    topic: str
    attempts: int
    languages: tuple[str, ...]


# --------------------------------------------------------------------------
# Caricamento catalogo
# --------------------------------------------------------------------------


def load_catalog() -> dict:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    if OVERRIDES.exists():
        extra = json.loads(OVERRIDES.read_text(encoding="utf-8"))
        for slug, meta in extra.get("problems", {}).items():
            meta.setdefault("lists", ["all"])
            meta.setdefault("difficulty", "Medium")
            meta.setdefault("pattern", "Altro")
            catalog["problems"][slug] = meta
        catalog["aliases"].update(extra.get("aliases", {}))
        recount(catalog)
    return catalog


def recount(catalog: dict) -> None:
    """Ricalcola i totali per lista dopo aver applicato gli override."""
    for key, entry in catalog["lists"].items():
        patterns: dict[str, int] = defaultdict(int)
        for meta in catalog["problems"].values():
            if key in meta.get("lists", []):
                patterns[meta["pattern"]] += 1
        entry["patterns"] = dict(sorted(patterns.items()))
        entry["count"] = sum(patterns.values())


def resolve(slug: str, catalog: dict) -> dict | None:
    problems = catalog["problems"]
    if slug in problems:
        return problems[slug]
    alias = catalog["aliases"].get(slug)
    return problems.get(alias) if alias else None


def canonical(slug: str, catalog: dict) -> str:
    return slug if slug in catalog["problems"] else catalog["aliases"].get(slug, slug)


def ordered_patterns(catalog: dict, present: set[str]) -> list[str]:
    preferred = [p for p in catalog.get("pattern_order", []) if p in present]
    rest = sorted(present - set(preferred))
    return preferred + rest


# --------------------------------------------------------------------------
# Scansione
# --------------------------------------------------------------------------


def scan() -> list[Solved]:
    found: list[Solved] = []
    for topic_dir in sorted(p for p in ROOT.iterdir() if p.is_dir()):
        if topic_dir.name.startswith(".") or topic_dir.name in SKIP_DIRS:
            continue
        for problem_dir in sorted(p for p in topic_dir.iterdir() if p.is_dir()):
            files = [
                f
                for f in problem_dir.iterdir()
                if f.is_file() and not f.name.startswith(".")
            ]
            if not files:
                continue
            langs = sorted({EXT_LANG.get(f.suffix, f.suffix.lstrip(".")) for f in files})
            found.append(
                Solved(problem_dir.name, topic_dir.name, len(files), tuple(langs))
            )
    return found


def bar(solved: int, total: int, width: int = 12) -> str:
    filled = round(solved / total * width) if total else 0
    return "█" * filled + "░" * (width - filled)


def last_activity() -> str:
    try:
        out = subprocess.check_output(
            ["git", "-C", str(ROOT), "log", "-1", "--format=%ad", "--date=short"],
            stderr=subprocess.DEVNULL,
        )
        return out.decode().strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""


# --------------------------------------------------------------------------
# Rendering
# --------------------------------------------------------------------------


def render(solved: list[Solved], catalog: dict) -> str:
    problems = catalog["problems"]
    tracked_list = catalog["lists"][TRACK_LIST]
    totals = tracked_list["patterns"]
    label = tracked_list["label"]

    by_pattern: dict[str, set[str]] = defaultdict(set)
    languages: set[str] = set()
    unknown: list[Solved] = []
    off_list: dict[str, dict] = {}
    hit_slugs: set[str] = set()

    for item in solved:
        languages.update(item.languages)
        meta = resolve(item.slug, catalog)
        if meta is None:
            unknown.append(item)
            continue
        slug = canonical(item.slug, catalog)
        if TRACK_LIST not in meta.get("lists", []):
            off_list[slug] = meta
            continue
        by_pattern[meta["pattern"]].add(slug)
        hit_slugs.add(slug)

    # Contatori sugli slug deduplicati: la stessa cartella puo' comparire due
    # volte se NeetCode ha sincronizzato sia lo slug proprio sia quello LeetCode.
    counts = {
        d: sum(1 for s in hit_slugs if problems[s]["difficulty"] == d)
        for d in DIFFICULTIES
    }

    done = sum(len(v) for v in by_pattern.values())
    total = tracked_list["count"]
    pct = round(done / total * 100) if total else 0

    lines = [
        f"### {label} &nbsp;·&nbsp; {done} / {total} &nbsp;·&nbsp; {pct}%",
        "",
        f"`{bar(done, total, 24)}`",
        "",
        "| | " + " | ".join(f"{DIFF_EMOJI[d]} {d}" for d in DIFFICULTIES) + " |",
        "|:--|:--:|:--:|:--:|",
        "| **Risolti** | "
        + " | ".join(f"**{counts[d]}**" for d in DIFFICULTIES)
        + " |",
        "| **Totale lista** | "
        + " | ".join(
            str(
                sum(
                    1
                    for m in problems.values()
                    if m["difficulty"] == d and TRACK_LIST in m.get("lists", [])
                )
            )
            for d in DIFFICULTIES
        )
        + " |",
        "",
        "| Pattern | Risolti | Totale | Progresso |",
        "|---------|--------:|-------:|:----------|",
    ]

    for pattern in ordered_patterns(catalog, set(totals)):
        s = len(by_pattern.get(pattern, ()))
        t = totals.get(pattern, 0)
        p = round(s / t * 100) if t else 0
        lines.append(f"| {pattern} | {s} | {t} | `{bar(s, t)}` {p}% |")

    if SHOW_CHECKLIST:
        catalog_by_pattern: dict[str, list[tuple[str, dict]]] = defaultdict(list)
        for slug, meta in problems.items():
            if TRACK_LIST in meta.get("lists", []):
                catalog_by_pattern[meta["pattern"]].append((slug, meta))

        lines += ["", "### Dettaglio per pattern", ""]
        for pattern in ordered_patterns(catalog, set(catalog_by_pattern)):
            hit = by_pattern.get(pattern, set())
            entries = sorted(catalog_by_pattern[pattern], key=lambda e: e[1]["name"])
            t = len(entries)
            p = round(len(hit) / t * 100) if t else 0
            lines += [
                "<details>",
                f"<summary><b>{pattern}</b> &nbsp;·&nbsp; {len(hit)}/{t} ({p}%)</summary>",
                "",
            ]
            for slug, meta in entries:
                mark = "x" if slug in hit else " "
                url = f"https://neetcode.io/problems/{slug}"
                lines.append(
                    f"- [{mark}] {DIFF_EMOJI[meta['difficulty']]} [{meta['name']}]({url})"
                )
            lines += ["", "</details>", ""]

    if off_list:
        lines += [
            "",
            f"### Fuori lista &nbsp;·&nbsp; {len(off_list)}",
            "",
            "<details>",
            f"<summary>Risolti ma non presenti in {label}</summary>",
            "",
            "| Problema | Difficoltà | Pattern |",
            "|----------|:----------:|---------|",
            *(
                f"| {m['name']} | {DIFF_EMOJI[m['difficulty']]} {m['difficulty']} | {m['pattern']} |"
                for m in sorted(off_list.values(), key=lambda m: m["name"])
            ),
            "",
            "</details>",
            "",
        ]

    if unknown:
        lines += [
            "",
            f"### Altro &nbsp;·&nbsp; {len(unknown)}",
            "",
            "<details>",
            f"<summary>{len(unknown)} soluzioni non ancora mappate nel catalogo</summary>",
            "",
            "| Slug | Topic | Submission |",
            "|------|-------|-----------:|",
            *(
                f"| [`{u.slug}`](https://neetcode.io/problems/{u.slug}) | {u.topic} | {u.attempts} |"
                for u in sorted(unknown, key=lambda u: u.slug)
            ),
            "",
            "</details>",
            "",
        ]

    footer = f"_Linguaggi: {', '.join(sorted(languages)) or '—'}_"
    date = last_activity()
    if date:
        footer += f" &nbsp;·&nbsp; _Ultimo aggiornamento: {date}_"
    lines += ["", footer]

    return "\n".join(lines)


def report(solved: list[Solved], catalog: dict) -> int:
    """Stampa gli slug sconosciuti come JSON pronto per extra_problems.json."""
    unknown = [s for s in solved if resolve(s.slug, catalog) is None]
    if not unknown:
        print("Nessuno slug sconosciuto: il catalogo copre tutte le soluzioni.")
        return 0
    stub = {
        "problems": {
            u.slug: {
                "name": u.slug.replace("-", " ").title(),
                "difficulty": "Medium",
                "pattern": "Altro",
                "lists": ["all"],
            }
            for u in sorted(unknown, key=lambda u: u.slug)
        }
    }
    print(f"{len(unknown)} slug non mappati. Incolla in utils/extra_problems.json\n")
    print(json.dumps(stub, indent=2, ensure_ascii=False))
    return 0


def inject(text: str, block: str) -> str:
    start, end = MARKERS
    i, j = text.find(start), text.find(end)
    if i == -1 or j == -1:
        raise SystemExit(f"Marker non trovati nel README: {start} / {end}")
    return text[: i + len(start)] + "\n" + block + "\n" + text[j:]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--report",
        action="store_true",
        help="stampa gli slug sconosciuti invece di riscrivere il README",
    )
    args = parser.parse_args()

    catalog = load_catalog()
    solved = scan()

    if args.report:
        raise SystemExit(report(solved, catalog))

    block = render(solved, catalog)
    README.write_text(
        inject(README.read_text(encoding="utf-8"), block), encoding="utf-8"
    )
    unknown = sum(1 for s in solved if resolve(s.slug, catalog) is None)
    print(
        f"Dashboard aggiornata — lista '{TRACK_LIST}', "
        f"{len(solved)} problemi trovati, {unknown} non mappati."
    )


if __name__ == "__main__":
    main()

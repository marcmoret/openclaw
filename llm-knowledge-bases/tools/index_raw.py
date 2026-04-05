from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw"
OUT_DIR = RAW / "_index"
OUT_FILE = OUT_DIR / "sources.json"

SKIP_DIRS = {"_index"}


@dataclass
class SourceRecord:
    relpath: str
    kind: str
    suffix: str
    size: int
    mtime_utc: str


def infer_kind(path: Path) -> str:
    parts = set(path.parts)
    if "x" in parts:
        return "social-post"
    if "articles" in parts:
        return "article"
    if "papers" in parts:
        return "paper"
    if "repos" in parts:
        return "repo"
    if "datasets" in parts:
        return "dataset"
    if "images" in parts:
        return "image"
    if "inbox" in parts:
        return "inbox"
    return "other"


def iter_files(root: Path) -> Iterable[Path]:
    if not root.exists():
        return []
    results = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        results.append(path)
    return sorted(results)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    records = []
    for path in iter_files(RAW):
        stat = path.stat()
        records.append(
            SourceRecord(
                relpath=str(path.relative_to(ROOT)).replace("\\", "/"),
                kind=infer_kind(path.relative_to(RAW)),
                suffix=path.suffix.lower(),
                size=stat.st_size,
                mtime_utc=datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(),
            )
        )

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "root": str(ROOT).replace("\\", "/"),
        "count": len(records),
        "sources": [asdict(r) for r in records],
    }
    OUT_FILE.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Wrote {OUT_FILE} with {len(records)} sources")


if __name__ == "__main__":
    main()

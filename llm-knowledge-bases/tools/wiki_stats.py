from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"


def count_words(text: str) -> int:
    return len(text.split())


def main() -> None:
    files = sorted(WIKI.rglob("*.md")) if WIKI.exists() else []
    total_words = 0
    for path in files:
        total_words += count_words(path.read_text(encoding="utf-8", errors="ignore"))

    print(f"wiki_files={len(files)}")
    print(f"wiki_words={total_words}")


if __name__ == "__main__":
    main()

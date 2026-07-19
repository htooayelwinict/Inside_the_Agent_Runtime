from __future__ import annotations

import re
import sys
from pathlib import Path

PLACEHOLDER_WORDS = ("TO" + "DO", "T" + "BD", "FIX" + "ME")
PLACEHOLDERS = re.compile(
    r"\b(" + "|".join(PLACEHOLDER_WORDS) + r")\b",
    re.IGNORECASE,
)
LINKS = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
FENCED_CODE = re.compile(
    r"^[ \t]*(`{3,}|~{3,})[^\n]*\n.*?^[ \t]*\1[ \t]*$",
    re.MULTILINE | re.DOTALL,
)
MAIN_CHAPTER_FILE = re.compile(r"^(?P<number>\d{2})-.+\.md$")
MAIN_CHAPTER_H1 = re.compile(r"^# Chapter (?P<number>\d{2})\b", re.MULTILINE)
EXPECTED_MAIN_CHAPTERS = tuple(range(17))


def check_main_chapters(root: Path) -> list[str]:
    chapters_dir = root / "book" / "chapters"
    if not chapters_dir.exists():
        return []

    errors: list[str] = []
    by_number: dict[int, list[Path]] = {}
    for path in sorted(chapters_dir.glob("[0-9][0-9]-*.md")):
        file_match = MAIN_CHAPTER_FILE.match(path.name)
        if file_match is None:
            continue
        file_number = int(file_match.group("number"))
        by_number.setdefault(file_number, []).append(path)

        text = path.read_text(encoding="utf-8")
        h1_match = MAIN_CHAPTER_H1.search(text)
        if h1_match is None:
            errors.append(f"{path}: missing numbered Chapter H1")
            continue
        h1_number = int(h1_match.group("number"))
        if h1_number != file_number:
            errors.append(
                f"{path}: filename/H1 chapter number mismatch: "
                f"filename {file_number:02d}, H1 {h1_number:02d}"
            )

    if not by_number:
        return errors

    for number, paths in sorted(by_number.items()):
        if len(paths) > 1:
            rendered = ", ".join(str(path) for path in paths)
            errors.append(f"duplicate main chapter number {number:02d}: {rendered}")

    actual = set(by_number)
    expected = set(EXPECTED_MAIN_CHAPTERS)
    missing = sorted(expected - actual)
    unexpected = sorted(actual - expected)
    if missing:
        errors.append(
            "missing main chapter numbers: "
            + ", ".join(f"{number:02d}" for number in missing)
        )
    if unexpected:
        errors.append(
            "unexpected main chapter numbers: "
            + ", ".join(f"{number:02d}" for number in unexpected)
        )
    return errors


def check_book(root: Path) -> list[str]:
    errors: list[str] = []
    for path in sorted(root.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        prose = FENCED_CODE.sub("", text)
        if PLACEHOLDERS.search(prose):
            errors.append(f"{path}: unresolved placeholder")
        for target in LINKS.findall(prose):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            local_target = target.split("#", 1)[0]
            if local_target and not (path.parent / local_target).resolve().exists():
                errors.append(f"{path}: broken local link: {target}")
    errors.extend(check_main_chapters(root))
    return errors


if __name__ == "__main__":
    failures = check_book(Path(__file__).resolve().parents[1])
    if failures:
        print("\n".join(failures))
        sys.exit(1)
    print("book checks passed")

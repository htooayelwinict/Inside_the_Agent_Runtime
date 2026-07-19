from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from scripts.check_book import check_book


def write_main_chapters(root: Path) -> None:
    chapters = root / "book" / "chapters"
    chapters.mkdir(parents=True, exist_ok=True)
    for number in range(17):
        (chapters / f"{number:02d}-chapter-{number:02d}.md").write_text(
            f"# Chapter {number:02d} — Sample\n",
            encoding="utf-8",
        )


class CheckBookTests(unittest.TestCase):
    def test_reports_unresolved_placeholders(self) -> None:
        with TemporaryDirectory() as temp:
            root = Path(temp)
            chapter = root / "book" / "chapters" / "sample.md"
            chapter.parent.mkdir(parents=True)
            marker = "TO" + "DO"
            chapter.write_text(
                f"# Sample\n\n{marker}: explain this\n",
                encoding="utf-8",
            )
            self.assertIn("unresolved placeholder", "\n".join(check_book(root)))

    def test_reports_broken_local_link(self) -> None:
        with TemporaryDirectory() as temp:
            root = Path(temp)
            chapter = root / "book" / "chapters" / "sample.md"
            chapter.parent.mkdir(parents=True)
            chapter.write_text("[missing](../missing.md)\n", encoding="utf-8")
            self.assertIn("broken local link", "\n".join(check_book(root)))

    def test_ignores_links_inside_fenced_code_blocks(self) -> None:
        with TemporaryDirectory() as temp:
            root = Path(temp)
            chapter = root / "book" / "chapters" / "sample.md"
            chapter.parent.mkdir(parents=True)
            chapter.write_text(
                "```markdown\n[missing](../missing.md)\n```\n",
                encoding="utf-8",
            )
            self.assertEqual([], check_book(root))

    def test_accepts_contiguous_00_through_16_sequence(self) -> None:
        with TemporaryDirectory() as temp:
            root = Path(temp)
            write_main_chapters(root)
            self.assertEqual([], check_book(root))

    def test_reports_filename_h1_number_mismatch(self) -> None:
        with TemporaryDirectory() as temp:
            root = Path(temp)
            write_main_chapters(root)
            chapter = root / "book" / "chapters" / "03-chapter-03.md"
            chapter.write_text("# Chapter 04 — Wrong\n", encoding="utf-8")
            self.assertIn(
                "filename/H1 chapter number mismatch",
                "\n".join(check_book(root)),
            )

    def test_reports_duplicate_main_chapter_number(self) -> None:
        with TemporaryDirectory() as temp:
            root = Path(temp)
            write_main_chapters(root)
            duplicate = root / "book" / "chapters" / "03-duplicate.md"
            duplicate.write_text("# Chapter 03 — Duplicate\n", encoding="utf-8")
            self.assertIn(
                "duplicate main chapter number 03",
                "\n".join(check_book(root)),
            )

    def test_reports_missing_main_chapter_number(self) -> None:
        with TemporaryDirectory() as temp:
            root = Path(temp)
            write_main_chapters(root)
            (root / "book" / "chapters" / "03-chapter-03.md").unlink()
            self.assertIn(
                "missing main chapter numbers: 03",
                "\n".join(check_book(root)),
            )


if __name__ == "__main__":
    unittest.main()

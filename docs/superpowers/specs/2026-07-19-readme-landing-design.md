# README Landing Page Design

Date: 2026-07-19
Status: Approved direction, pending implementation review

## Goal

Turn the repository README into a reader-first landing page for **Inside the Agent Runtime**. A first-time visitor should understand what the book promises, who it serves, and where to begin without losing the repository's source-backed technical credibility.

## Audience and Positioning

The primary audience is a reader who knows basic Python and wants to understand how an AI Agent Runtime works internally. Contributors and reviewers are a secondary audience.

The landing page will present the project as a practical Burmese-first technical book with an executable companion. Travis234, Pi, and Hermes remain the evidence and implementation context rather than the title-level identity.

## Information Hierarchy

The README will use this order:

1. Book title and one consolidated subtitle
2. Short reader promise
3. Immediate navigation links
4. What the reader will learn
5. Who the book is for
6. Six-part learning journey
7. Executable companion and verified commands
8. Scope boundary
9. Source evidence and attribution
10. Current status and review report

The first screen should answer three questions: what is this, why should I read it, and where do I start?

## Hero and Navigation

The main heading remains `Inside the Agent Runtime`.

The Burmese title and technical scope will be consolidated into one readable subtitle instead of three consecutive level-three headings. Duplicate horizontal rules will be removed.

Immediately after the opening promise, the README will provide ordinary Markdown links for:

- starting with Chapter 00;
- opening the full table of contents;
- viewing the offline examples;
- reading the technical review report.

The links will remain useful in GitHub and other standard Markdown renderers without requiring HTML buttons or external assets.

## Core Content

The opening copy will explain that the book follows a prompt through the Agent Loop, Tool execution, Context Window pressure, Compaction, persistence, and debugging. It will emphasize behavioral understanding over line-by-line source translation.

The existing long feature list will become a compact learning journey organized around the six book parts. It will describe outcomes rather than repeat every chapter title.

The audience section will retain the current beginner-friendly prerequisites and state explicitly that prior Pi, Hermes, or Travis234 source knowledge is not required.

## Executable Companion

The README will identify the five offline examples and state the locally verified boundary precisely:

- no API key or network is required for the examples;
- Python 3.13 is the documented interpreter;
- the local suite contains 24 tests;
- passing these tests validates the teaching artifacts, not the full Travis234 runtime or live providers.

The two primary verification commands will remain visible and copyable.

## Evidence, Scope, and Attribution

The README will keep the project boundary explicit: this is not a complete Travis234 product manual or provider catalog.

Pinned source mapping, the Claim Ledger, and the Review Report will be linked as credibility paths below the reader-facing material. Attribution and licensing will remain intact. Claims will not be expanded beyond the existing verified evidence.

## Related Files

`book/README.md` will be updated from the old “Travis234 Book Manuscript” identity to the new book title and will serve as a concise manuscript-directory guide rather than duplicate the root landing page.

The user's uncommitted `book/chapters/00-thankyou_note.md` will not be edited or added to navigation as part of this landing-page change. Its placement requires a separate editorial decision.

## Non-Goals

- No cover image, badges, screenshots, or generated artwork
- No chapter renaming or reordering
- No changes to runtime examples or tests
- No expansion of provider, TUI, or extension documentation
- No changes to the thank-you note or its navigation
- No alteration of licensing terms or pinned source revisions

## Verification

Implementation will be checked with:

```bash
python3.13 scripts/check_book.py
python3.13 -m unittest discover -s tests -v
git diff --check
```

A final editorial pass will also confirm that:

- the title appears consistently in the root and book READMEs;
- all landing-page links resolve;
- the opening contains only one subtitle hierarchy and no duplicate divider;
- the 24-test statement retains its local teaching-artifact boundary;
- the user's thank-you-note work remains unchanged.

# Agent Runtime Loop Companion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a source-backed Chapter 03 that teaches one Agent Runtime run chronologically, renumber the existing Chapter 03–15 sequence to Chapter 04–16 without rewriting its prose, and release a verified 17-chapter local edition.

**Architecture:** Draft the new chapter at a temporary non-numbered manuscript path so it can receive an independent prose/source review while the current book remains valid. Then perform one atomic Git-aware renumbering migration for chapter files, navigation, SUMMARY and claim links; strengthen the book checker with TDD; update current-edition metadata; and finish with fresh local/upstream evidence plus a commit-specific archive.

**Tech Stack:** Markdown, Python 3 standard library, `unittest`, Git, Ripgrep, Mermaid, pinned Pi/Travis234 source clones.

## Global Constraints

- The approved design is `docs/superpowers/specs/2026-07-19-agent-runtime-loop-companion-design.md`.
- Keep current Chapter 00–02 prose unchanged; Chapter 02 may change only its `Next` navigation line.
- Keep current Chapter 03–15 prose unchanged except H1/H2 numbering, Previous/Next navigation, chapter-number cross-references and renamed Markdown link targets.
- Do not reorder or interleave the existing Lewis chapters; after renumbering they remain together as Chapter 11–16.
- New Chapter 03 title: `Agent Runtime Loop ကို အစအဆုံးဖတ်ခြင်း`.
- New Chapter 03 target: 1,800–2,300 words; story/dialogue 15–20%; source-backed teaching 80–85%.
- In Chapter 03 story prose, prefer `Agent`, `Runtime`, `Loop`, `Tool Call` and `Tool Result`; use Pi/Travis234 proper names only for source comparison and Source Notes.
- Use pinned revisions exactly: Pi `1f0dbc008c9b3e88017d42e8a1b46d416ad2b6b6`; Travis234 `68b1831691b8ec93f9550ce63b80cdcb7a591b2e`.
- Do not add a new executable example; teach with compact pseudocode, event order, state snapshots, a comparison table and existing forward links.
- Do not copy sentences, dialogue, examples or code from Agentic AI Book or the style-reference site; use only their high-level teaching rhythm.
- Preserve natural Burmese-first prose and the canonical terms in `STYLE_GUIDE.md`.
- Do not create a GitHub remote, push a branch or open a pull request.
- Use `apply_patch` for file-content edits; `git mv` is required for chapter renames.
- Every task must finish with a clean diff check, focused verification, one commit and an independent review gate.

---

## File Responsibility Map

### New chapter

- `book/chapters/x03-agent-runtime-loop-walkthrough.md` — temporary reviewable draft path used only in Task 1.
- `book/chapters/03-agent-runtime-loop-walkthrough.md` — final Chapter 03 path after Task 2.

### Renumbered chapters

- `book/chapters/04-typescript-to-python-semantic-port.md` through `book/chapters/16-building-a-trustworthy-port.md` — Git-renamed current Chapter 03–15 files with mechanical number/link edits only.

### Navigation and evidence

- `book/SUMMARY.md` — final 00–16 table of contents.
- `book/references/CLAIM_LEDGER.md` — current-edition `Used in` labels and paths.
- `book/chapters/appendices/a-installation.md` — Previous link to Chapter 16.

### Durable checks

- `scripts/check_book.py` — existing link/placeholder checks plus exact 00–16 filename/H1 sequence rules.
- `tests/test_check_book.py` — mismatch, duplicate, missing and valid-sequence regression tests.

### Edition metadata and release evidence

- `README.md` — 17-chapter status and corrected recommended entry numbers.
- `book/README.md` — companion-chapter authoring status and story/source boundary.
- `book/REVIEW_REPORT.md` — final companion audit, renumbering audit, actual checks and explicit non-rerun boundaries.
- `/workspace/scratch/b03ff60760ed/Travis234-Book-<short-commit>.zip` — commit-specific release archive outside Git.

---

### Task 1: Draft and review the Agent Runtime Loop companion chapter

**Files:**

- Create: `book/chapters/x03-agent-runtime-loop-walkthrough.md`
- Read: `book/chapters/02-pi-agent-loop-anatomy.md`
- Read: `book/chapters/10-one-night-unfinished-bug.md`
- Read: `STYLE_GUIDE.md`
- Read: `book/references/SOURCE_MAP.md`
- Read: `book/references/CLAIM_LEDGER.md`
- Inspect: `/workspace/scratch/b03ff60760ed/pi-reference/packages/agent/src/agent-loop.ts`
- Inspect: `/workspace/scratch/b03ff60760ed/pi-reference/packages/agent/src/agent.ts`
- Inspect: `/workspace/scratch/b03ff60760ed/travis234/travis/agent/agent_loop.py`
- Inspect: `/workspace/scratch/b03ff60760ed/travis234/travis/agent/agent.py`

**Interfaces:**

- Consumes: `C-LOOP-ORDER`, `C-MESSAGE-DRAIN`, `C-ABORT-OWNERSHIP`, `P-LOOP`, `P-AGENT`, `P-TYPES`, `T-LOOP`, `T-AGENT`, `T-TYPES`, `T-EVENT-STREAM`, `T-RUN-LEASE`.
- Produces: complete Chapter 03 prose at the temporary `x03-...` path; Task 2 renames it without rewriting the approved prose.

- [ ] **Step 1: Reconfirm the exact common and Travis-specific run order**

Inspect the pinned sources and record these boundaries in the task report before drafting:

```text
run entry
  → copy prompts into new_messages/current_context
  → agent_start
  → initial turn_start
  → prompt message_start/message_end
  → shared outer/inner loop
  → stream assistant partial/final message
  → prepare/execute/finalize requested Tool Calls
  → append Tool Result messages
  → turn_end
  → prepare-next-turn / stop / steering boundaries
  → follow-up boundary
  → agent_end
```

Also record the bounded source difference: Travis234 performs an explicit `signal.aborted` check after `turn_end` and before `prepare_next_turn`; the chapter must not present that one line as an identical upstream Pi statement.

- [ ] **Step 2: Write the exact opening incident and fictional boundary**

Open with Lewis asking the Agent to locate where one focused test begins to fail. Use one successful `read_file` Tool Call only. The opening must establish this tension:

```text
Lewis expects one request and one answer.
The trace reveals two model requests separated by one Tool Result.
```

Keep dialogue to 1–3 short exchanges. Before the first source-backed claim, state that Lewis and the incident are fictional and are not a production incident or contributor history.

Start the temporary file with this exact H1:

```markdown
# Chapter 03 — Agent Runtime Loop ကို အစအဆုံးဖတ်ခြင်း
```

- [ ] **Step 3: Use the exact H2 structure**

```markdown
## ၃.၁ Request တစ်ခုက Run တစ်ခုဖြစ်လာတဲ့အချိန်
## ၃.၂ Agent Owner က ဘာကိုပိုင်သလဲ
## ၃.၃ Initial Messages နဲ့ Run စတင်ခြင်း
## ၃.၄ ပထမ Model Boundary
## ၃.၅ Assistant Stream ကို Message တစ်ခုဖြစ်အောင်တည်ဆောက်ခြင်း
## ၃.၆ Tool Call ကို Prepare → Execute → Finalize လုပ်ခြင်း
## ၃.၇ Tool Result က Context ထဲပြန်ဝင်လာခြင်း
## ၃.၈ Updated Context နဲ့ ဒုတိယ Model Call
## ၃.၉ Steering နဲ့ Follow-up ဝင်တဲ့နေရာ
## ၃.၁၀ Loop ကို ရပ်စေတဲ့လမ်းကြောင်းများ
## ၃.၁၁ Run တစ်ခုလုံးကို State Snapshots နဲ့ဖတ်ခြင်း
## ၃.၁၂ Pi ကနေ Travis234 ဆီ Source Flow လိုက်ဖတ်ခြင်း
## ၃.၁၃ Lewis ရဲ့မှတ်စု
## ၃.၁၄ အနှစ်ချုပ်
## ၃.၁၅ Source Notes
```

No additional H2 headings are allowed. H3 headings may be used only when a long comparison would otherwise obscure one teaching question.

- [ ] **Step 4: Teach owner, Run, Turn and message state before showing the loop**

Section ၃.၂ must distinguish:

| Term | Required explanation |
|---|---|
| Agent owner | Owns queues, configuration, current run coordination and the public prompt/control surface |
| Run | One active processing lifetime from `agent_start` to `agent_end`, possibly containing multiple turns |
| Turn | One assistant response boundary, including its requested Tool Calls and Tool Results |
| Message | Durable/context input item observed by the next model request |
| Tool invocation | External work requested by an assistant Tool Call; completion is not the same as context insertion |

Explain each English term in natural Burmese on first use. Do not turn the section into a file inventory.

- [ ] **Step 5: Add the call-flow and event timeline teaching artifacts**

Include a compact generic call flow:

```text
Lewis
  → Agent owner
  → loop config
  → shared Runtime Loop
  → first model request
  → read_file Tool Call
  → Tool Result message
  → second model request
  → final assistant message
```

Include an event timeline that respects the pinned source order:

```text
agent_start
turn_start
message_start(user)
message_end(user)
message_start(assistant)
message_update(...)
message_end(assistant with Tool Call)
tool_execution_start(read_file)
tool_execution_end(read_file)
message_start(Tool Result)
message_end(Tool Result)
turn_end
turn_start
message_start(assistant)
message_end(final assistant)
turn_end
agent_end
```

Label this as a simplified successful teaching trace. State that providers may omit an explicit partial `start`, in which case the Runtime still emits a message start/end boundary around the final assistant message.

- [ ] **Step 6: Add three context snapshots and explain the second model request**

Use these conceptual snapshots:

```text
Before model request 1:
  [user request]

Before model request 2:
  [user request, assistant Tool Call, Tool Result]

After completion:
  [user request, assistant Tool Call, Tool Result, final assistant message]
```

Explain that a completed Tool body does not mutate the already-finished model request. The Runtime must create a Tool Result message and issue a new model request with updated context.

- [ ] **Step 7: Bound Tool lifecycle and control-message coverage**

Section ၃.၆ introduces Prepare → Execute → Finalize only at the control-flow level. It must link forward to final Chapter 05 for Tool Execution and final Chapter 13 for failure/hook details rather than repeating them.

Section ၃.၉ must state:

```text
Steering: drained before the next model request inside the active run.
Follow-up: drained after the inner work would otherwise finish.
Abort: cooperative signal; not an automatic force-stop guarantee.
```

Link forward to final Chapter 12 for the dedicated story. Do not claim that the simple scenario tests live provider cancellation, threads or RunLease behavior.

- [ ] **Step 8: Add the stop-path comparison and source-reading map**

The stop table must cover exactly these outcomes:

| Outcome | Required boundary |
|---|---|
| Normal completion | No Tool Calls, no steering, no follow-up |
| Assistant error/aborted | Turn ends and Agent ends without new work |
| Cooperative signal observed | No new model/tool work starts after the observation boundary |
| Stop hook | Ends after the completed-turn context is available |
| Terminating Tool batch | Does not continue merely because Tool Calls existed |
| Steering queued | Enters the next model request inside the active inner loop |
| Follow-up queued | Re-enters the inner loop rather than ending the Run |

Section ၃.၁၂ maps these exact source names:

```text
Pi: runAgentLoop → runLoop → streamAssistantResponse → executeToolCalls
Travis234: run_agent_loop_async → _run_loop → _stream_assistant_response → _execute_tool_calls
Agent owners: Agent queue/control surface in agent.ts and agent.py
```

- [ ] **Step 9: Add exact Source Notes and navigation**

Source Notes must cite all consumed claim/source IDs and both pinned revisions. It must say that the chapter explains control-flow boundaries but does not prove the full provider, hook, Tool, Compaction or persistence integrations.

Temporary navigation for the staging draft:

```markdown
Previous: [Chapter 02 — Pi Agent Loop Anatomy](02-pi-agent-loop-anatomy.md)

Next: [Chapter 03 — TypeScript ကနေ Python သို့ Semantic Port](03-typescript-to-python-semantic-port.md)
```

Task 2 changes the second label/target to final Chapter 04.

- [ ] **Step 10: Run focused editorial and source checks**

Run:

```bash
wc -w book/chapters/x03-agent-runtime-loop-walkthrough.md
rg -n '^## ' book/chapters/x03-agent-runtime-loop-walkthrough.md
rg -n 'C-LOOP-ORDER|C-MESSAGE-DRAIN|C-ABORT-OWNERSHIP|P-LOOP|P-AGENT|P-TYPES|T-LOOP|T-AGENT|T-TYPES|T-EVENT-STREAM|T-RUN-LEASE' book/chapters/x03-agent-runtime-loop-walkthrough.md
rg -n 'လက်နဲ့|ဒီ chapter မှာ|မှတ်ထားရမယ့်အချက်|architecture review|အောက်ပါအတိုင်းဖြစ်သည်' book/chapters/x03-agent-runtime-loop-walkthrough.md
python3 scripts/check_book.py
git diff --check
```

Expected:

- Word count is 1,800–2,300.
- Exactly 15 H2 headings appear in the prescribed order.
- Required IDs and both revisions appear in Source Notes.
- The editorial phrase scan has no output.
- Book checker and diff check pass.

- [ ] **Step 11: Commit the independently reviewable draft**

```bash
git add book/chapters/x03-agent-runtime-loop-walkthrough.md
git diff --cached --check
git commit -m "docs: draft Agent Runtime Loop walkthrough"
```

Review gate: natural Burmese, story/teaching balance, event accuracy, source boundaries, no overlap with later deep dives and no copied reference phrasing.

---

### Task 2: Atomically renumber the manuscript and integrate navigation

**Files:**

- Rename: `book/chapters/x03-agent-runtime-loop-walkthrough.md` → `book/chapters/03-agent-runtime-loop-walkthrough.md`
- Rename: current `book/chapters/03-*.md` through `book/chapters/15-*.md` according to the approved migration map
- Modify: `book/chapters/02-pi-agent-loop-anatomy.md`
- Modify: all renamed Chapter 04–16 files mechanically
- Modify: `book/SUMMARY.md`
- Modify: `book/references/CLAIM_LEDGER.md`
- Modify: `book/chapters/appendices/a-installation.md`

**Interfaces:**

- Consumes: approved staged Chapter 03 from Task 1.
- Produces: valid main manuscript paths `00-...` through `16-...`; Task 3 can enforce this sequence in the checker.

- [ ] **Step 1: Record the pre-migration baseline**

Run and save the output in the task report:

```bash
git status --short
git rev-parse HEAD
wc -w book/chapters/{03-typescript-to-python-semantic-port,04-tool-execution-bounded-concurrency,05-context-window-pressure,06-hermes-style-compaction,07-pi-meets-hermes,08-minimal-runtime-lab,09-parity-divergence-lessons,10-one-night-unfinished-bug,11-steering-followup-cancellation,12-when-tools-fail,13-session-resume-after-restart,14-debugging-agent-trajectory,15-building-a-trustworthy-port}.md
```

Expected baseline counts, in current Chapter 03–15 order:

```text
1100 1131 1275 1556 1410 1261 1026 1453 1337 1355 1605 1525 1793
```

If the counts differ before any edit, stop and report the discrepancy rather than forcing these values.

- [ ] **Step 2: Rename existing files in descending order**

Run from `book/chapters` so no destination collides:

```bash
git mv 15-building-a-trustworthy-port.md 16-building-a-trustworthy-port.md
git mv 14-debugging-agent-trajectory.md 15-debugging-agent-trajectory.md
git mv 13-session-resume-after-restart.md 14-session-resume-after-restart.md
git mv 12-when-tools-fail.md 13-when-tools-fail.md
git mv 11-steering-followup-cancellation.md 12-steering-followup-cancellation.md
git mv 10-one-night-unfinished-bug.md 11-one-night-unfinished-bug.md
git mv 09-parity-divergence-lessons.md 10-parity-divergence-lessons.md
git mv 08-minimal-runtime-lab.md 09-minimal-runtime-lab.md
git mv 07-pi-meets-hermes.md 08-pi-meets-hermes.md
git mv 06-hermes-style-compaction.md 07-hermes-style-compaction.md
git mv 05-context-window-pressure.md 06-context-window-pressure.md
git mv 04-tool-execution-bounded-concurrency.md 05-tool-execution-bounded-concurrency.md
git mv 03-typescript-to-python-semantic-port.md 04-typescript-to-python-semantic-port.md
git mv x03-agent-runtime-loop-walkthrough.md 03-agent-runtime-loop-walkthrough.md
```

- [ ] **Step 3: Update H1 and H2 numbering mechanically**

Use `apply_patch` on every renamed file. Apply this exact prefix map:

| Old | New | Burmese H2 prefix |
|---:|---:|---|
| 03 | 04 | `၃.` → `၄.` |
| 04 | 05 | `၄.` → `၅.` |
| 05 | 06 | `၅.` → `၆.` |
| 06 | 07 | `၆.` → `၇.` |
| 07 | 08 | `၇.` → `၈.` |
| 08 | 09 | `၈.` → `၉.` |
| 09 | 10 | `၉.` → `၁၀.` |
| 10 | 11 | `၁၀.` → `၁၁.` |
| 11 | 12 | `၁၁.` → `၁၂.` |
| 12 | 13 | `၁၂.` → `၁၃.` |
| 13 | 14 | `၁၃.` → `၁၄.` |
| 14 | 15 | `၁၄.` → `၁၅.` |
| 15 | 16 | `၁၅.` → `၁၆.` |

Do not change words after the numeric H1/H2 prefixes.

- [ ] **Step 4: Rebuild the exact Previous/Next chain**

Required chain:

```text
00 → 01 → 02 → 03 → 04 → 05 → 06 → 07 → 08
   → 09 → 10 → 11 → 12 → 13 → 14 → 15 → 16 → Appendix A
```

Specific boundary edits:

- Chapter 02 Next → `03-agent-runtime-loop-walkthrough.md`.
- Chapter 03 Previous → Chapter 02; Next → `04-typescript-to-python-semantic-port.md`.
- Every renamed chapter label and filename uses its new number.
- Appendix A Previous → `../16-building-a-trustworthy-port.md`.

- [ ] **Step 5: Update the known prose cross-references mechanically**

Apply these exact semantic replacements; do not run a blind global number replacement:

- Final Chapter 06: old `Chapter 06` Compaction forward reference → `Chapter 07`.
- Final Chapter 09: old Chapter 02/04 overview → Chapter 02/05; old Chapter 07 lifecycle → Chapter 08.
- Final Chapter 10: old Chapter 04/08 behavior links → Chapter 05/09; old Chapter 03 semantic-port link → Chapter 04.
- Final Chapter 11: both old Chapter 08 Minimal Runtime references → Chapter 09.
- New Chapter 03 forward links → Chapter 05, 09, 12, 13, 15 and 16 exactly as the design specifies.

Preserve the rest of every paragraph byte-for-byte where practical.

- [ ] **Step 6: Update SUMMARY and Claim Ledger paths**

`book/SUMMARY.md` must add this entry immediately after Chapter 02:

```markdown
- [Agent Runtime Loop ကို အစအဆုံးဖတ်ခြင်း](chapters/03-agent-runtime-loop-walkthrough.md)
```

Shift all subsequent main-chapter paths/labels through Chapter 16. Parts remain Part I–VI in their current order.

In `book/references/CLAIM_LEDGER.md`:

- Add Chapter 03 to `C-LOOP-ORDER`, `C-MESSAGE-DRAIN` and `C-ABORT-OWNERSHIP`.
- Shift every current Chapter 03–15 link label/path to Chapter 04–16.
- Preserve evidence and verification columns exactly.

- [ ] **Step 7: Run link, stale-path and prose-lock audits**

Run:

```bash
python3 scripts/check_book.py
rg -n '^Previous:|^Next:' book/chapters
rg -n '\((03-typescript-to-python-semantic-port|04-tool-execution-bounded-concurrency|05-context-window-pressure|06-hermes-style-compaction|07-pi-meets-hermes|08-minimal-runtime-lab|09-parity-divergence-lessons|10-one-night-unfinished-bug|11-steering-followup-cancellation|12-when-tools-fail|13-session-resume-after-restart|14-debugging-agent-trajectory|15-building-a-trustworthy-port)\.md\)' book README.md
wc -w book/chapters/{04-typescript-to-python-semantic-port,05-tool-execution-bounded-concurrency,06-context-window-pressure,07-hermes-style-compaction,08-pi-meets-hermes,09-minimal-runtime-lab,10-parity-divergence-lessons,11-one-night-unfinished-bug,12-steering-followup-cancellation,13-when-tools-fail,14-session-resume-after-restart,15-debugging-agent-trajectory,16-building-a-trustworthy-port}.md
git diff --check
```

Expected:

- Checker passes.
- The old-target scan has no output.
- Existing-chapter word counts remain exactly `1100 1131 1275 1556 1410 1261 1026 1453 1337 1355 1605 1525 1793` in final Chapter 04–16 order.
- `git diff --find-renames=80%` recognizes each current Chapter 03–15 file as a rename.
- Manual diff inspection finds only allowed H1/H2/navigation/cross-reference changes in existing prose.

- [ ] **Step 8: Commit the atomic migration**

```bash
git add book/chapters book/SUMMARY.md book/references/CLAIM_LEDGER.md
git diff --cached --check
git commit -m "docs: renumber chapters for Runtime Loop companion"
```

Review gate: correct rename detection, exact 00–16 navigation, no stale links, no unintended prose changes and current claim evidence preserved.

---

### Task 3: Add durable chapter-number validation with TDD

**Files:**

- Modify: `scripts/check_book.py`
- Modify: `tests/test_check_book.py`

**Interfaces:**

- Consumes: final main chapter files `00-...` through `16-...` from Task 2.
- Produces: `check_main_chapters(root: Path) -> list[str]`; `check_book(root)` includes its errors.

- [ ] **Step 1: Add a fixture helper and four failing tests**

Add to `tests/test_check_book.py`:

```python
def write_main_chapters(root: Path) -> None:
    chapters = root / "book" / "chapters"
    chapters.mkdir(parents=True, exist_ok=True)
    for number in range(17):
        (chapters / f"{number:02d}-chapter-{number:02d}.md").write_text(
            f"# Chapter {number:02d} — Sample\n",
            encoding="utf-8",
        )
```

Add these tests:

```python
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
        self.assertIn("filename/H1 chapter number mismatch", "\n".join(check_book(root)))

def test_reports_duplicate_main_chapter_number(self) -> None:
    with TemporaryDirectory() as temp:
        root = Path(temp)
        write_main_chapters(root)
        duplicate = root / "book" / "chapters" / "03-duplicate.md"
        duplicate.write_text("# Chapter 03 — Duplicate\n", encoding="utf-8")
        self.assertIn("duplicate main chapter number 03", "\n".join(check_book(root)))

def test_reports_missing_main_chapter_number(self) -> None:
    with TemporaryDirectory() as temp:
        root = Path(temp)
        write_main_chapters(root)
        (root / "book" / "chapters" / "03-chapter-03.md").unlink()
        self.assertIn("missing main chapter numbers: 03", "\n".join(check_book(root)))
```

- [ ] **Step 2: Run the focused tests and observe RED**

Run:

```bash
python3 -m unittest tests.test_check_book -v
```

Expected: the four new tests fail because chapter-number validation does not exist; the three existing placeholder/link tests still pass.

- [ ] **Step 3: Implement the minimal checker**

Add to `scripts/check_book.py`:

```python
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
```

At the end of `check_book(root)`, before returning, add:

```python
    errors.extend(check_main_chapters(root))
```

- [ ] **Step 4: Run focused and full tests to observe GREEN**

Run:

```bash
python3 -m unittest tests.test_check_book -v
python3 -m unittest discover -s tests -v
python3 scripts/check_book.py
```

Expected:

- Seven `CheckBookTests` pass.
- Full local suite reports 21 tests passed.
- CLI prints `book checks passed`.

- [ ] **Step 5: Commit the checker and tests**

```bash
git add scripts/check_book.py tests/test_check_book.py
git diff --cached --check
git commit -m "test: validate main chapter numbering"
```

Review gate: exact 00–16 rule, no false failures for temporary roots without numbered chapters, clear diagnostics and preserved existing checks.

---

### Task 4: Update current-edition metadata and perform the prose-lock audit

**Files:**

- Modify: `README.md`
- Modify: `book/README.md`
- Read/audit: all final Chapter 00–16 files
- Read/audit: `book/SUMMARY.md`
- Read/audit: `book/references/CLAIM_LEDGER.md`

**Interfaces:**

- Consumes: final paths/navigation from Task 2 and durable checker from Task 3.
- Produces: public-facing 17-chapter status and a verified existing-prose lock for Task 5's Review Report.

- [ ] **Step 1: Update root README status and entry points**

Required content changes:

- Replace `Chapter 00–15` / `main sequence ၁၆ ခန်း` with `Chapter 00–16` / `main sequence ၁၇ ခန်း`.
- Add one bullet stating that Chapter 03 walks through one Agent Runtime run from prompt to completion.
- Change the recommended semantic-port entry from old Chapter 03 to Chapter 04.
- Change the Context Window entry from old Chapter 05 to Chapter 06.
- Keep the source/pinned-revision and no-full-feature-catalog boundaries unchanged.

- [ ] **Step 2: Update book README without changing the Part structure**

State that Part II now contains the Chapter 03 Runtime walkthrough between anatomy and semantic porting. Preserve Part I–VI status and the fictional-scenario versus pinned-source evidence boundary.

- [ ] **Step 3: Audit current manuscript links and exact visible titles**

Run:

```bash
python3 scripts/check_book.py
rg -n '^# Chapter|^Previous:|^Next:' book/chapters
rg -n '^# Chapter|^## [၀-၉]+\.' book/chapters/[0-9][0-9]-*.md
rg -n 'Chapter (0[3-9]|1[0-6])' README.md book --glob '*.md'
```

Inspect every match. Do not change the external Software Engineering reference links in Appendix D merely because their displayed source chapter number differs from this book.

- [ ] **Step 4: Perform the existing-prose lock audit**

Run:

```bash
git diff --find-renames=80% --word-diff=porcelain 0d554e1..HEAD -- book/chapters
wc -w book/chapters/{04-typescript-to-python-semantic-port,05-tool-execution-bounded-concurrency,06-context-window-pressure,07-hermes-style-compaction,08-pi-meets-hermes,09-minimal-runtime-lab,10-parity-divergence-lessons,11-one-night-unfinished-bug,12-steering-followup-cancellation,13-when-tools-fail,14-session-resume-after-restart,15-debugging-agent-trajectory,16-building-a-trustworthy-port}.md
```

Expected:

- Renamed existing chapters contain only allowed numbering, navigation, link-target and chapter-reference changes.
- Counts remain exactly `1100 1131 1275 1556 1410 1261 1026 1453 1337 1355 1605 1525 1793`.
- New Chapter 03 is the only new main prose.

If a moved chapter count or non-mechanical paragraph differs, fix that drift before committing metadata.

- [ ] **Step 5: Run current-edition checks and commit**

```bash
python3 -m unittest discover -s tests -v
python3 scripts/check_book.py
git diff --check
git add README.md book/README.md
git diff --cached --check
git commit -m "docs: integrate Runtime Loop companion edition"
```

Expected: 21 tests pass, checker passes and worktree is clean after commit.

Review gate: 17-chapter public status, unchanged Parts, accurate entry numbers and demonstrated prose lock.

---

### Task 5: Run final evidence checks, update the review report and archive the edition

**Files:**

- Modify: `book/REVIEW_REPORT.md`
- Generate outside Git: `/workspace/scratch/b03ff60760ed/Travis234-Book-<short-commit>.zip`

**Interfaces:**

- Consumes: complete 17-chapter manuscript and 21-test suite.
- Produces: current final review record, clean `main` commit and validated commit-specific archive.

- [ ] **Step 1: Run complete local verification**

Run from the book repository:

```bash
python3 -m py_compile scripts/check_book.py examples/minimal_runtime.py examples/lewis_message_control.py examples/lewis_tool_outcomes.py examples/lewis_session_restore.py examples/lewis_trace_reader.py tests/test_check_book.py tests/test_minimal_runtime.py tests/test_lewis_workshop.py
python3 examples/minimal_runtime.py
python3 examples/lewis_message_control.py
python3 examples/lewis_tool_outcomes.py
python3 examples/lewis_session_restore.py
python3 examples/lewis_trace_reader.py
python3 -m unittest discover -s tests -v
python3 scripts/check_book.py
git diff --check
```

Expected: compile succeeds; five demos exit 0; 21 tests pass; book checker and diff check pass.

- [ ] **Step 2: Run final manuscript scans**

Run:

```bash
wc -w book/chapters/03-agent-runtime-loop-walkthrough.md
rg -n '^## ' book/chapters/03-agent-runtime-loop-walkthrough.md
rg -n '^# Chapter|^Previous:|^Next:' book/chapters
rg -n '^# Chapter|^## [၀-၉]+\.' book/chapters/[0-9][0-9]-*.md
rg -n 'လက်နဲ့|ဒီ chapter မှာ|မှတ်ထားရမယ့်အချက်|architecture review|အောက်ပါအတိုင်းဖြစ်သည်' book/chapters/03-agent-runtime-loop-walkthrough.md book/chapters/{11-one-night-unfinished-bug,12-steering-followup-cancellation,13-when-tools-fail,14-session-resume-after-restart,15-debugging-agent-trajectory,16-building-a-trustworthy-port}.md
rg -n 'Planned Chapter|TO''DO|T''BD' book README.md GLOSSARY.md
git diff --find-renames=80% 0d554e1..HEAD --stat
```

Expected: Chapter 03 has 1,800–2,300 words and 15 exact H2s; the phrase and planned-label scans have no output; existing story chapters remain clean.

- [ ] **Step 3: Re-run the targeted pinned-source verifier**

From `/workspace/scratch/b03ff60760ed/travis234` at revision `68b1831691b8ec93f9550ce63b80cdcb7a591b2e`, run:

```bash
python3 scripts/verify_acceptance.py --parity-json
```

Expected: exit 0; Pi 74 parity / 4 divergence and Hermes 11 parity / 0 divergence. Record this as a targeted manifest/schema/evidence verifier, not a full Travis234 suite run.

- [ ] **Step 4: Update Review Report with current actual results**

Add an `Agent Runtime Loop Companion` section that records:

- Chapter 03 title, word count, story/teaching audit and exact pinned source boundaries.
- Final Chapter 00–16 sequence and reciprocal navigation audit.
- Checker numbering rules and actual 21-test result.
- Existing current Chapter 03–15 → final Chapter 04–16 migration map.
- Confirmation that existing prose changed only for allowed numbering/navigation/cross-reference edits.
- Updated Lewis audit labels from old Chapter 10–15 to final Chapter 11–16.
- Targeted parity-verifier result.
- Explicit statement that the full Travis234 suite, live providers, PyPI install and Docker pull were not rerun.

Update stale current-edition statements elsewhere in the report so the same file does not claim both a 16- and 17-chapter current sequence.

- [ ] **Step 5: Commit Review Report and verify committed HEAD**

```bash
git add book/REVIEW_REPORT.md
git diff --cached --check
git commit -m "docs: complete Runtime Loop companion review"
python3 -m unittest discover -s tests -v
python3 scripts/check_book.py
git diff --check
git status --short
git log -1 --oneline
```

Expected: 21 tests pass; checker/diff pass; status is clean; final commit is the review commit.

- [ ] **Step 6: Create and validate the commit-specific archive**

Use the actual final short commit in the filename:

```bash
git archive --format=zip --output="/workspace/scratch/b03ff60760ed/Travis234-Book-$(git rev-parse --short HEAD).zip" --prefix=Travis234-Book/ HEAD
unzip -t "/workspace/scratch/b03ff60760ed/Travis234-Book-$(git rev-parse --short HEAD).zip"
sha256sum "/workspace/scratch/b03ff60760ed/Travis234-Book-$(git rev-parse --short HEAD).zip"
```

Expected: every archived file reports `OK`; unzip reports no compressed-data errors; SHA-256 is recorded in the task report. Do not delete older local archives.

- [ ] **Step 7: Request final whole-branch review**

Review from base `0d554e1` to final HEAD for:

- Approved Chapter 03 content and source accuracy.
- Natural Burmese and story/teaching balance.
- Exact existing-prose lock.
- Correct Git renames and 00–16 links.
- Checker behavior/tests.
- Current Review Report evidence boundaries.
- Archive/HEAD identity and hash.

Critical and Important findings must be fixed and re-reviewed. Record Minor findings explicitly before release handoff.

---

## Completion Definition

The plan is complete only when all five task commits and review gates are finished, the final whole-branch reviewer returns no Critical/Important findings, `main` is clean, the local test suite and book checker pass, and the newest commit-specific ZIP is validated and linked for the user.

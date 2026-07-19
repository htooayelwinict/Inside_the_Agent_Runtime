# Reader-First README Landing Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the root README into a reader-first landing page for *Inside the Agent Runtime* and align the manuscript-directory README with the new title.

**Architecture:** Keep the root README as the public entry point and `book/README.md` as a concise directory guide. Use ordinary Markdown links and existing repository artifacts; no images, badges, HTML controls, dependencies, chapter changes, or runtime changes are needed.

**Tech Stack:** GitHub-flavored Markdown, Python 3.13 book checker, Python `unittest`, Git

## Global Constraints

- Preserve the user's current uncommitted title work in `README.md` as the starting point.
- Do not edit or stage `book/chapters/00-preface-attribution.md`.
- Do not edit, stage, or add `book/chapters/00-thankyou_note.md` to navigation.
- Keep `Inside the Agent Runtime` as the root H1.
- Use one consolidated subtitle; remove duplicate horizontal rules.
- Use plain Markdown links that work on GitHub without external assets.
- State Python 3.13 and 24 local tests without implying full Travis234 or live-provider validation.
- Preserve licensing, attribution, pinned-source boundaries, and the existing six-part chapter order.

---

## File Structure

- Modify `README.md`: public reader-first landing page, navigation, learning journey, executable-companion boundary, evidence, attribution, and status.
- Modify `book/README.md`: concise manuscript-directory guide using the new title and links to navigation/evidence.
- Do not modify any other source, chapter, example, test, or metadata file.

### Task 1: Rewrite the Root Landing Page

**Files:**
- Modify: `README.md`
- Verify: `scripts/check_book.py`

**Interfaces:**
- Consumes: existing `book/SUMMARY.md`, `book/chapters/00-preface-attribution.md`, `examples/`, `book/references/SOURCE_MAP.md`, `book/references/CLAIM_LEDGER.md`, and `book/REVIEW_REPORT.md` paths.
- Produces: a public Markdown entry point whose local links are validated by `scripts/check_book.py`.

- [ ] **Step 1: Record the user-owned files that must remain outside this task**

Run:

```bash
git status --short
git diff -- README.md book/chapters/00-preface-attribution.md
```

Expected: `README.md` and `book/chapters/00-preface-attribution.md` may be modified, and `book/chapters/00-thankyou_note.md` may be untracked. Treat the current README content as input; do not reset any file.

- [ ] **Step 2: Replace the fragmented hero with one title hierarchy**

Use this opening structure in `README.md`:

```markdown
# Inside the Agent Runtime

## AI Agent တစ်ခု ဘယ်လိုစဉ်းစားသလဲ — Pi Loop မှ Hermes Compaction အထိ Python ဖြင့် Runtime တစ်ခုတည်ဆောက်ခြင်း

AI Agent တစ်ခုက prompt ကိုလက်ခံပြီး Tool ကိုဘယ်လိုရွေးသလဲ၊ result ကို context ထဲဘယ်လိုပြန်ထည့်သလဲ၊ Context Window ပြည့်လာတဲ့အခါ အရေးကြီးတဲ့ state ကိုဘယ်လိုဆက်ထိန်းသလဲ။ ဒီစာအုပ်က Pi-style Agent Loop မှ Hermes-style Compaction အထိ Runtime တစ်ခုရဲ့အတွင်းပိုင်းကို Python code၊ offline labs နဲ့ pinned source evidence တို့ဖြင့် အဆင့်လိုက်ရှင်းပြထားပါတယ်။

**[စာအုပ်စဖတ်ရန်](book/chapters/00-preface-attribution.md)** · **[မာတိကာ](book/SUMMARY.md)** · **[Offline Examples](examples/)** · **[Technical Review](book/REVIEW_REPORT.md)**
```

Remove both consecutive `---` dividers. Keep the existing Agentic AI Book and Travis234 links for the attribution section rather than repeating them above the primary navigation.

- [ ] **Step 3: Add outcome-focused learning and audience sections**

Replace the existing topic inventory with these sections and ideas, preserving natural Burmese sentence flow:

```markdown
## ဒီစာအုပ်ပြီးရင် ဘာမြင်လာမလဲ

- Prompt တစ်ခုက model → Tool Calls → ordered Tool Results → model အစီအစဉ်နဲ့ ဘယ်လိုဖြတ်သန်းသလဲ
- Parallel Tool execution မှာ completion order နဲ့ model မြင်တဲ့ result order ဘာကြောင့်ကွာနိုင်သလဲ
- Context Window pressure ကို truncation တစ်ခုတည်းမဟုတ်ဘဲ Compaction pipeline နဲ့ ဘယ်လိုကိုင်တွယ်သလဲ
- TypeScript implementation ကို Python သို့ syntax မဟုတ်ဘဲ observable behavior ထိန်းပြီး ဘယ်လို port လုပ်သလဲ
- Steering၊ Follow-up၊ failure၊ restart နဲ့ trace တွေကို Runtime boundary အလိုက် ဘယ်လိုစစ်သလဲ

## ဘယ်သူတွေဖတ်သင့်လဲ
```

Retain the four existing audience bullets and the sentence explaining that prior Pi, Hermes, or Travis234 source knowledge is unnecessary.

- [ ] **Step 4: Present the six-part learning journey**

Add a compact section linking each part to its first relevant chapter:

```markdown
## စာအုပ်ရဲ့ Learning Journey

1. **Runtime ဘာကြောင့်လိုသလဲ** — Pi နဲ့ Hermes ကို mental model တစ်ခုထဲချိတ်ကြည့်မယ်။
2. **Agent Loop ကို port လုပ်ခြင်း** — prompt ကနေ completion အထိ loop၊ messages နဲ့ bounded Tool execution ကိုလိုက်ဖတ်မယ်။
3. **Compaction ကို port လုပ်ခြင်း** — Context Window pressure၊ deterministic cleanup နဲ့ structured summary ကိုခွဲမယ်။
4. **Runtime တစ်ခုအဖြစ်ပေါင်းခြင်း** — loop lifecycle ထဲ Compaction ဝင်တဲ့နေရာနဲ့ parity boundary ကိုစစ်မယ်။
5. **Lewis ရဲ့ Runtime incidents** — ordering၊ steering၊ Tool failure၊ restart နဲ့ trace debugging ကို case studies နဲ့လေ့လာမယ်။
6. **Trustworthy port workshop** — observable contracts၊ focused tests နဲ့ intentional divergence ကို evidence အဖြစ်ချိတ်မယ်။
```

Link each bold label to the corresponding first chapter: `01`, `02`, `06`, `08`, `11`, and `16`. Follow with a single link to `book/SUMMARY.md` for the complete chapter list.

- [ ] **Step 5: Add the executable-companion boundary**

Use this content, retaining the existing commands:

````markdown
## Offline Runtime Companion

Repository ထဲမှာ API key နဲ့ network မလိုတဲ့ Python examples ငါးခုပါပါတယ်။ သူတို့က Agent Loop၊ message control၊ Tool outcomes၊ session restore နဲ့ trace reading contracts ကို concept တစ်ခုချင်းစမ်းနိုင်အောင် ခွဲထားတာပါ။

```bash
python3.13 -m unittest discover -s tests -v
python3.13 scripts/check_book.py
```

Local suite မှာ tests ၂၄ ခုရှိပါတယ်။ ဒီ result က စာအုပ်ရဲ့ teaching artifacts နဲ့ manuscript checks ကိုသာ validate လုပ်ပြီး Travis234 full suite၊ live provider သို့မဟုတ် network integration ကို အစားမထိုးပါဘူး။
````

- [ ] **Step 6: Finish with scope, evidence, attribution, and status**

Keep the existing product-manual boundary under `## ဒီစာအုပ်ရဲ့ Scope`. Add direct links to:

```markdown
- [Pinned Source Map](book/references/SOURCE_MAP.md)
- [Technical Claim Ledger](book/references/CLAIM_LEDGER.md)
- [Review Report](book/REVIEW_REPORT.md)
```

Retain the CC BY-NC-SA 4.0 manuscript statement and Pi/Hermes/Travis234 MIT-notice statement. Keep the current status concise: 17 main chapters, four appendices, offline labs, and a reminder to re-check upstream documentation when pinned revisions change.

- [ ] **Step 7: Run the manuscript link checker**

Run:

```bash
python3.13 scripts/check_book.py
```

Expected: `book checks passed`.

- [ ] **Step 8: Review the root README diff without staging unrelated files**

Run:

```bash
git diff -- README.md
git diff --check -- README.md
```

Expected: one H1, one consolidated H2 subtitle, no duplicate divider, four primary navigation links, six learning-journey items, explicit Python 3.13/24-test boundary, and no whitespace errors.

### Task 2: Align the Manuscript Directory README

**Files:**
- Modify: `book/README.md`
- Verify: `scripts/check_book.py`

**Interfaces:**
- Consumes: the title and positioning established in Task 1.
- Produces: a concise directory guide that links to `SUMMARY.md`, `references/SOURCE_MAP.md`, `references/CLAIM_LEDGER.md`, and `REVIEW_REPORT.md`.

- [ ] **Step 1: Replace the old manuscript identity**

Use this heading and opening:

```markdown
# Inside the Agent Runtime — စာအုပ်ဖိုင်များ

ဒီ directory ထဲမှာ *Inside the Agent Runtime* ရဲ့ Chapter 00–16၊ appendices၊ source mapping နဲ့ technical review artifacts တွေရှိပါတယ်။ Root [README](../README.md) က စာအုပ်မိတ်ဆက်ဖြစ်ပြီး ဒီစာမျက်နှာက manuscript area ကိုလမ်းညွှန်ပေးပါတယ်။
```

- [ ] **Step 2: Replace drafted-status language with navigation and evidence links**

Remove the six `drafted` bullets. Use:

```markdown
## ဖတ်ရန်

- [မာတိကာ](SUMMARY.md)
- [Chapter 00 မှ စဖတ်ရန်](chapters/00-preface-attribution.md)
- [Glossary](../GLOSSARY.md)

## Technical Evidence

- [Pinned Source Map](references/SOURCE_MAP.md)
- [Technical Claim Ledger](references/CLAIM_LEDGER.md)
- [Review Report](REVIEW_REPORT.md)
```

Keep one short paragraph explaining the problem-first, Burmese-first teaching approach and the fictional status of Lewis. Do not duplicate the full root README or introduce new claims.

- [ ] **Step 3: Verify both README files together**

Run:

```bash
python3.13 scripts/check_book.py
git diff --check -- README.md book/README.md
```

Expected: `book checks passed` and no diff-check output.

- [ ] **Step 4: Commit only the landing-page files**

Run:

```bash
git add README.md book/README.md
git diff --cached --name-only
```

Expected staged paths:

```text
README.md
book/README.md
```

Then run:

```bash
git commit -m "docs: polish reader-first book landing"
```

Do not stage `book/chapters/00-preface-attribution.md` or `book/chapters/00-thankyou_note.md`.

### Task 3: Final Verification and Ownership Check

**Files:**
- Verify: `README.md`
- Verify: `book/README.md`
- Preserve: `book/chapters/00-preface-attribution.md`
- Preserve: `book/chapters/00-thankyou_note.md`

**Interfaces:**
- Consumes: the committed landing-page changes from Tasks 1–2.
- Produces: fresh evidence that the documentation-only change did not break the repository and did not absorb unrelated user work.

- [ ] **Step 1: Run the full repository checks**

Run:

```bash
python3.13 -m unittest discover -s tests -v
python3.13 scripts/check_book.py
git diff --check
```

Expected: 24 tests pass, `book checks passed`, and no diff-check output.

- [ ] **Step 2: Confirm commit and working-tree ownership**

Run:

```bash
git show --stat --oneline HEAD
git status --short
```

Expected: the landing commit contains only `README.md` and `book/README.md`. The user's pre-existing preface modification and untracked thank-you note remain visible in working-tree status and are not part of the landing commit.

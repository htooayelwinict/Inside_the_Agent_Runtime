# Agent Runtime Loop Companion Chapter Design

**Date:** 2026-07-19
**Status:** Approved design pending implementation plan
**Repository:** Travis234 Book

## 1. Goal

Chapter 02 ရဲ့ Pi Agent Loop anatomy ကိုဖတ်ပြီးနောက် စာဖတ်သူက prompt တစ်ခု Runtime ထဲဝင်လာချိန်ကနေ Agent run အဆုံးသတ်ချိန်အထိ control flow၊ messages၊ events နဲ့ state transitions ကို chronological order နဲ့ရှင်းရှင်းလင်းလင်းဖတ်နိုင်စေရမယ်။

ဒီရည်ရွယ်ချက်အတွက် Chapter 02 နောက်မှာ source-backed teaching နဲ့ Lewis scenario ကိုဟန်ချက်ညီညီပေါင်းထားတဲ့ companion chapter အသစ်တစ်ခန်းထည့်မယ်။ လက်ရှိ chapter အစီအစဉ်၊ prose နဲ့ story voice ကိုမရောဘဲ လက်ရှိ Chapter 03–15 ကို နံပါတ်တစ်ခုစီသာရွှေ့မယ်။

Main sequence က Chapter 00–16၊ စုစုပေါင်း ၁၇ ခန်းဖြစ်လာမယ်။

## 2. Approved Editorial Decision

### 2.1 What stays unchanged

- လက်ရှိ Chapter 00–02 ရဲ့ prose ကိုမပြန်ရေးဘူး။ Chapter 02 မှာ companion chapter ဆီသွားတဲ့ `Next` navigation ကိုသာပြောင်းမယ်။
- လက်ရှိ Chapter 03–15 ရဲ့ section order၊ examples၊ dialogue၊ teaching explanations နဲ့ Source Notes claims ကိုမပေါင်း၊ မဖြတ်၊ မပြန်ရေးဘူး။
- လက်ရှိ Lewis chapters တွေကို Part V/VI ထဲမှာအခုရှိနေတဲ့အစီအစဉ်အတိုင်းပဲထားမယ်။ Technical chapters ကြားပြန်မညှပ်ဘူး။
- Pi၊ Travis234၊ Hermes နဲ့ Agentic AI Book pinned revisions မပြောင်းဘူး။
- ယခင် design specs နဲ့ implementation plans တွေဟာ သမိုင်းမှတ်တမ်းဖြစ်လို့ နံပါတ်အသစ်နဲ့ပြန်မရေးဘူး။ ဒီ spec က current-edition migration ကို သီးခြားမှတ်တမ်းတင်မယ်။

### 2.2 What changes

- `book/chapters/03-agent-runtime-loop-walkthrough.md` ကို Chapter 03 အသစ်အဖြစ်ထည့်မယ်။
- လက်ရှိ Chapter 03–15 files ကို Chapter 04–16 အဖြစ် `git mv` နဲ့ရွှေ့မယ်။
- ရွှေ့ထားတဲ့ chapters တွေမှာ filename၊ H1/H2 chapter number၊ Previous/Next navigation နဲ့ chapter-number cross-references ကိုသာ current sequence နဲ့ညှိမယ်။
- `book/SUMMARY.md`, `README.md`, `book/README.md`, `book/references/CLAIM_LEDGER.md`, `book/REVIEW_REPORT.md` နဲ့ Appendix A navigation ကို current sequence နဲ့ညှိမယ်။
- Book checker ကို main-chapter numbering နဲ့ filename/H1 consistency စစ်နိုင်အောင်ချဲ့မယ်။

## 3. Final Chapter Sequence

Parts အစီအစဉ်ကိုမပြောင်းဘဲ Part II ထဲ Chapter 03 အသစ်ထည့်မယ်။

| New chapter | Title | Source |
|---:|---|---|
| 00 | Preface နှင့် Attribution | current Chapter 00 |
| 01 | Pi နဲ့ Hermes ကို ဘာကြောင့်တွဲကြည့်ရတာလဲ | current Chapter 01 |
| 02 | Pi Agent Loop Anatomy | current Chapter 02 |
| 03 | Agent Runtime Loop ကို အစအဆုံးဖတ်ခြင်း | new companion chapter |
| 04 | TypeScript ကနေ Python သို့ Semantic Port | current Chapter 03 |
| 05 | Tool Execution နှင့် Bounded Concurrency | current Chapter 04 |
| 06 | Context Window ပြည့်လာတဲ့ပြဿနာ | current Chapter 05 |
| 07 | Hermes-style Compaction | current Chapter 06 |
| 08 | Pi နဲ့ Hermes တွေ့ဆုံရာ | current Chapter 07 |
| 09 | Minimal Runtime Lab | current Chapter 08 |
| 10 | Parity, Divergence နှင့် သင်ခန်းစာများ | current Chapter 09 |
| 11 | တစ်ညနဲ့မပြီးတဲ့ Bug | current Chapter 10 |
| 12 | Agent ကို လမ်းပြန်ညွှန်ရတဲ့အချိန် | current Chapter 11 |
| 13 | Tool က အမှားပြန်လာတဲ့အခါ | current Chapter 12 |
| 14 | ပြန်ဖွင့်လိုက်တော့ အလုပ်ဘယ်ကဆက်မလဲ | current Chapter 13 |
| 15 | Agent ရဲ့လမ်းကြောင်းကို Trace နဲ့ Debug လုပ်ခြင်း | current Chapter 14 |
| 16 | ယုံကြည်ရတဲ့ Python Port တစ်ခုဖြစ်လာဖို့ | current Chapter 15 |

### 3.1 File migration map

| Current file | New file |
|---|---|
| `03-typescript-to-python-semantic-port.md` | `04-typescript-to-python-semantic-port.md` |
| `04-tool-execution-bounded-concurrency.md` | `05-tool-execution-bounded-concurrency.md` |
| `05-context-window-pressure.md` | `06-context-window-pressure.md` |
| `06-hermes-style-compaction.md` | `07-hermes-style-compaction.md` |
| `07-pi-meets-hermes.md` | `08-pi-meets-hermes.md` |
| `08-minimal-runtime-lab.md` | `09-minimal-runtime-lab.md` |
| `09-parity-divergence-lessons.md` | `10-parity-divergence-lessons.md` |
| `10-one-night-unfinished-bug.md` | `11-one-night-unfinished-bug.md` |
| `11-steering-followup-cancellation.md` | `12-steering-followup-cancellation.md` |
| `12-when-tools-fail.md` | `13-when-tools-fail.md` |
| `13-session-resume-after-restart.md` | `14-session-resume-after-restart.md` |
| `14-debugging-agent-trajectory.md` | `15-debugging-agent-trajectory.md` |
| `15-building-a-trustworthy-port.md` | `16-building-a-trustworthy-port.md` |

## 4. Chapter 03 Content Design

### 4.1 Chapter promise

Chapter 02 က Agent Loop ရဲ့ components နဲ့ boundaries ကို anatomy အဖြစ်ပြထားတယ်။ Chapter 03 အသစ်က အဲဒီအစိတ်အပိုင်းတွေကို run တစ်ခုရဲ့ အချိန်အစီအစဉ်အတိုင်းပြန်စုပေးမယ်။ စာဖတ်သူက chapter အဆုံးမှာ အောက်ကမေးခွန်းတွေကိုဖြေနိုင်ရမယ်။

- User request က ဘယ် owner ဆီအရင်ဝင်သလဲ။
- Run တစ်ခုနဲ့ Turn တစ်ခု ဘာကွာသလဲ။
- Assistant response တစ်ခုက partial state ကနေ completed message ဘယ်လိုဖြစ်လာသလဲ။
- Tool body ပြီးတာနဲ့ model က result ကို ဘာကြောင့်မသိသေးသလဲ။
- Tool Result ကို context ထဲထည့်ပြီးနောက် model request အသစ် ဘာကြောင့်လိုသလဲ။
- Steering၊ Follow-up နဲ့ abort signal တို့ ဘယ် boundary တွေမှာသက်ရောက်သလဲ။
- Agent run တစ်ခု ဘယ်အခြေအနေတွေမှာရပ်သလဲ။

### 4.2 Story scenario

Lewis က failing test တစ်ခုရဲ့ အစကိုရှာပေးဖို့ Agent ကို request တစ်ကြောင်းပို့မယ်။ ပထမ assistant response က `read_file` Tool Call တစ်ခုထုတ်မယ်။ Tool Result ပြန်ဝင်လာပြီးမှ ဒုတိယ model request က failure ရဲ့အစကိုရှင်းပြမယ်။

ဒီ scenario မှာ Tool တစ်ခုတည်းနဲ့ success path ကိုသာသုံးမယ်။ Parallel ordering၊ unknown Tool၊ invoked failure၊ session restart နဲ့ trace debugging ကို နောက်ပိုင်းသက်ဆိုင်ရာ chapters တွေအတွက်ချန်ထားမယ်။ ဒါကြောင့် Chapter 03 က control flow ကိုအာရုံစိုက်ပြီး existing Lewis stories နဲ့မထပ်ဘူး။

Lewis နဲ့ဖြစ်ရပ်ဟာ fictional ဖြစ်ကြောင်း source-backed explanation မစခင်ပြောမယ်။ Story body မှာ `Agent`, `Runtime`, `Loop`, `Tool Call`, `Tool Result` ကိုအဓိကသုံးပြီး Pi/Travis234 proper names ကို source comparison နဲ့ Source Notes မှာပဲသုံးမယ်။

### 4.3 Exact section structure

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

### 4.4 Teaching artifacts inside the chapter

Chapter အသစ်မှာ executable example အသစ်မဖန်တီးဘူး။ အောက်က teaching artifacts ကို prose ထဲသုံးမယ်။

- Agent owner → loop config → shared loop ကိုပြတဲ့ compact call-flow diagram
- First model call နဲ့ second model call ကိုခွဲပြတဲ့ event timeline
- Model request မတိုင်ခင် context snapshots သုံးခု
- Tool Call ရဲ့ Prepare → Execute → Finalize overview
- Normal completion၊ steering continuation၊ follow-up continuation၊ abort/error/terminate stop paths comparison table
- Pi function names ကနေ Travis234 function names ဆီ source-reading map
- နောက်ပိုင်း Minimal Runtime Lab ဆီ forward link

Chapter 03 ဟာ production source ကို line-by-line ဘာသာပြန်မှာမဟုတ်ဘူး။ State ဘယ်မှာပြောင်းတယ်၊ owner ဘယ်သူလဲ၊ boundary ပျက်ရင်ဘာဖြစ်နိုင်တယ်ဆိုတာကိုရှင်းမယ်။

### 4.5 Depth and balance

- Target length: 1,800–2,300 words
- Story and dialogue: 15–20%
- Source-backed teaching: 80–85%
- Dialogue: incident ကိုစဖို့လိုတဲ့ 1–3 short exchanges သာ
- Code: compact pseudocode နဲ့ state snapshots; production file dump မထည့်
- Each section rhythm: question/incident → source boundary → plain-language explanation → state change → failure consequence → next-section bridge

## 5. Source and Claim Boundaries

Chapter 03 က pinned revisions အသစ်မထည့်ဘဲ current source map ကိုသုံးမယ်။

| Topic | Source IDs / claim IDs |
|---|---|
| Outer/inner control flow | `C-LOOP-ORDER`, `P-LOOP`, `T-LOOP` |
| Agent owner and queue surface | `P-AGENT`, `T-AGENT` |
| Messages and events | `P-TYPES`, `T-TYPES`, `T-EVENT-STREAM` |
| Steering/follow-up overview | `C-MESSAGE-DRAIN` |
| Cooperative abort and ownership overview | `C-ABORT-OWNERSHIP`, `T-RUN-LEASE` |
| Tool lifecycle overview | `T-LOOP`; Chapter 05/13 deep-dive links |

Chapter 03 က full cancellation၊ Tool hooks၊ bounded concurrency၊ session persistence၊ Compaction သို့မဟုတ် provider-specific streaming အားလုံးအလုပ်မှန်ကြောင်း မသက်သေပြဘူး။ သက်ဆိုင်ရာ chapters နဲ့ Source Notes ဆီ scope ကိုရှင်းရှင်းလွှဲမယ်။

## 6. Editorial Contract

- Burmese-first prose သုံးပြီး stable technical terms ကိုသာ English အတိုင်းထားမယ်။
- English term ပထမဆုံးပေါ်ချိန်မှာ မြန်မာလိုအဓိပ္ပာယ်ရှင်းမယ်။
- Source comparison မဟုတ်တဲ့ story paragraphs ထဲ Pi/Travis234 proper names မထပ်သုံးဘူး။
- Feature inventory လိုမရေးဘဲ behavior၊ design reason၊ state transition နဲ့ failure consequence ကိုဆက်ရှင်းမယ်။
- Report-tone transitions၊ တိုက်ရိုက်ဘာသာပြန်သလိုဖြစ်တဲ့အသုံးအနှုန်းနဲ့ prohibited phrase list ကိုရှောင်မယ်။
- Agentic AI Book ရဲ့ problem-first teaching rhythm ကိုသာလေ့လာပြီး စာကြောင်း၊ dialogue၊ code sample နဲ့ဇာတ်လမ်းကိုမကူးဘူး။
- Canonical terms (`Agent Loop`, `Runtime`, `Tool Call`, `Tool Result`, `Steering`, `Follow-up`, `Abort`, `Turn`, `Run`) ကိုစာအုပ်တစ်လျှောက်တစ်သမတ်တည်းသုံးမယ်။
- Fictional scenario နဲ့ pinned source claims ကို chapter အစမှာတစ်ကြိမ်၊ Source Notes မှာတစ်ကြိမ် ခွဲပြမယ်။

## 7. Renumbering and Cross-reference Rules

### 7.1 Content lock for existing chapters

ရွှေ့ထားတဲ့ current Chapter 03–15 files တွေမှာ အောက်က changes သာခွင့်ပြုမယ်။

- H1 chapter number
- H2 Burmese section prefix
- Previous/Next labels and targets
- Prose ထဲက current-edition chapter-number references
- Markdown links whose target filenames changed

Story wording၊ technical explanation၊ code/output blocks၊ claims နဲ့ examples ကိုမပြင်ဘူး။ Renames ကို `git diff --find-renames` နဲ့ review လုပ်ပြီး non-mechanical prose drift မရှိကြောင်းစစ်မယ်။

### 7.2 Files that must be synchronized

- `book/SUMMARY.md`: Chapter 03 အသစ်နဲ့ Chapter 04–16 paths
- `README.md`: main sequence ၁၇ ခန်း၊ recommended entry chapter numbers
- `book/README.md`: current Part status နဲ့ companion-chapter description
- `book/references/CLAIM_LEDGER.md`: every `Used in` label/path
- `book/REVIEW_REPORT.md`: current chapter numbers၊ new Chapter 03 audit၊ actual word/test counts
- `book/chapters/appendices/a-installation.md`: Previous → Chapter 16
- All main-chapter Previous/Next links and prose cross-references

`GLOSSARY.md`, source implementation files၊ examples နဲ့ Lewis workshop tests ကို behavior change မရှိသရွေ့မပြင်ဘူး။

## 8. Checker and Tests

### 8.1 Durable book checks

`scripts/check_book.py` ကို အောက်က rules နဲ့ချဲ့မယ်။

- Main chapter filename numeric prefix နဲ့ H1 `Chapter NN` ကိုက်ရမယ်။
- Main chapter numbers ထပ်မနေရဘူး။
- Main sequence က 00 ကနေ 16 အထိ gap မရှိရဘူး။
- Existing broken-link နဲ့ unresolved-placeholder rules မပျက်ရဘူး။

`tests/test_check_book.py` မှာ mismatch၊ duplicate/gap နဲ့ valid 00–16 sequence cases ထည့်မယ်။ Navigation reciprocity နဲ့ chapter-number cross-reference audit ကို manuscript verification commands နဲ့ သီးခြားစစ်မယ်။

### 8.2 Verification commands

Implementation အပြီးမှာ အနည်းဆုံးအောက်က checks run ရမယ်။

```bash
python3 -m py_compile scripts/check_book.py tests/test_check_book.py
python3 -m unittest discover -s tests -v
python3 scripts/check_book.py
rg -n "^Previous:|^Next:" book/chapters
rg -n "^# Chapter|^## [၀-၉]+\." book/chapters/[0-9][0-9]-*.md
rg -n "Planned Chapter|TODO|TBD" book README.md GLOSSARY.md
git diff --check
```

Chapter 03 အတွက် word count၊ required headings၊ Source Notes IDs၊ fictional boundary နဲ့ editorial phrase scans သီးခြား run မယ်။

### 8.3 Targeted upstream evidence

Pinned source revisions မပြောင်းပေမယ့် final report အတွက် Travis234 clone မှာ အောက်က targeted verifier ကိုပြန် run မယ်။

```bash
python3 scripts/verify_acceptance.py --parity-json
```

ဒီ verifier ကို full Travis234 test-suite run လို့မဖော်ပြဘူး။ Live provider၊ PyPI installation နဲ့ Docker pull ကိုမပြန်စမ်းရင် Review Report မှာ တိတိကျကျရေးမယ်။

## 9. Navigation and Reading Flow

Final navigation chain က:

```text
00 → 01 → 02 → 03 (new) → 04 → … → 16 → Appendix A
```

Chapter 02 အဆုံးမှာ anatomy ကနေ chronological walkthrough ဆီ bridge လုပ်မယ်။ Chapter 03 အဆုံးမှာ semantic-port chapter အသစ် Chapter 04 ဆီဆက်မယ်။ Chapter 03 ရဲ့ forward references က current-edition numbers ကိုသုံးမယ်။

- Tool Execution deep dive → Chapter 05
- Minimal Runtime Lab → Chapter 09
- Steering/Follow-up/Abort story → Chapter 12
- Tool failure story → Chapter 13
- Trace debugging story → Chapter 15
- Contract workshop → Chapter 16

## 10. Review and Release Artifacts

- Chapter 03 prose/spec review: natural Burmese၊ story/teaching balance၊ source accuracy၊ overlap control
- Renumbering review: path/H1/H2/navigation/cross-reference changes only for existing chapters
- Whole-book review: SUMMARY၊ ledger၊ README၊ Review Report နဲ့ appendices
- Fresh local test and checker results
- Fresh targeted parity-verifier result
- Clean committed `main` branch
- Commit-specific ZIP archive under `/workspace/scratch/b03ff60760ed`
- ZIP integrity test and SHA-256

## 11. Success Criteria

Implementation အောင်မြင်တယ်လို့ဆိုဖို့ အောက်ကအချက်အားလုံးပြည့်ရမယ်။

1. Main sequence မှာ Chapter 00–16 ရှိပြီး number gap/duplicate မရှိဘူး။
2. Chapter 03 အသစ်က 1,800–2,300 words အတွင်းရှိပြီး approved 15-section structure ကိုသုံးတယ်။
3. Lewis scenario က control-flow question ကိုစပေးပြီး teaching/source explanation က chapter ကိုအဓိကထိန်းတယ်။
4. စာဖတ်သူက request → first model → tool → result message → second model → completion flow ကို state snapshots နဲ့ရှင်းပြနိုင်တယ်။
5. Chapter 03 claims အားလုံး pinned source IDs နဲ့ evidence limits ရှိတယ်။
6. Current Chapter 03–15 prose က mechanical numbering/navigation/cross-reference edits ကလွဲပြီးမပြောင်းဘူး။
7. SUMMARY၊ navigation၊ ledger နဲ့ Review Report က current filenames/numbers ကိုပဲညွှန်တယ်။
8. Local tests၊ book checker၊ editorial scans နဲ့ diff checks အားလုံးအောင်တယ်။
9. Targeted upstream verifier boundary ကို Review Report မှာမှန်ကန်စွာ label တပ်တယ်။
10. Final commit-specific archive က HEAD နဲ့ကိုက်ပြီး integrity/hash validation အောင်တယ်။

## 12. Explicit Non-goals

- လက်ရှိ chapters တွေကို story/technical အလှည့်ကျဖြစ်အောင်ပြန်စီခြင်း
- လက်ရှိ Lewis chapters တွေကိုပြန်ရေးခြင်း သို့မဟုတ် ပေါင်းခြင်း
- Agent Runtime feature အကုန်လုံးကို catalog လုပ်ခြင်း
- Tool execution၊ cancellation၊ Compaction နဲ့ tracing chapters ရဲ့ deep-dive အကြောင်းအရာကို Chapter 03 ထဲပြန်ကူးခြင်း
- Pi/Travis234 source ကို line-by-line ပြန်ဆိုခြင်း
- Upstream revisions upgrade လုပ်ခြင်း
- GitHub remote ဖန်တီးခြင်း၊ push လုပ်ခြင်း သို့မဟုတ် PR ဖွင့်ခြင်း

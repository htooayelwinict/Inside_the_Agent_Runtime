# Travis234 Book — Lewis Story Expansion Design

**Status:** Approved

**Date:** 2026-07-18

**Extends:** `2026-07-18-travis234-book-design.md`

## 1. Purpose

လက်ရှိ Chapter 00–09 က Pi Agent Loop port၊ Hermes-style Compaction နဲ့ Travis234 integration ကို teaching-first ပုံစံနဲ့ ရှင်းထားပြီးဖြစ်တယ်။ ဒီ expansion က အဲဒီအခန်းတွေကို ပြန်ရေးဖို့မဟုတ်ဘူး။ Reader က သင်ခဲ့ပြီးသား concept တွေကို developer တစ်ယောက်ကြုံရတဲ့ ဆက်စပ်ဖြစ်ရပ်တွေထဲမှာ ပြန်မြင်နိုင်ဖို့ story-driven case study၊ debugging နဲ့ workshop အလွှာအသစ် ထပ်ထည့်မှာဖြစ်တယ်။

Expansion ပြီးရင် main sequence က Chapter 00–15 အထိ စုစုပေါင်း ၁၆ ခန်းရှိမယ်။ Chapter အသစ် ၆ ခန်းက Pi/Hermes Python port scope ကိုပဲ နက်ရှိုင်းစေမယ်။ Travis234 feature catalog အဖြစ် မချဲ့ဘူး။

## 2. Existing manuscript boundary

- Chapter 00–09 ရဲ့ approved prose ကို မပြန်ရေးဘူး။
- Chapter 09 ရဲ့ `Next` link နဲ့ Appendix A ရဲ့ `Previous` link ကို sequence အသစ်နဲ့ကိုက်အောင် navigation-only edit လုပ်နိုင်တယ်။
- `SUMMARY.md`၊ repository status၊ glossary၊ source map၊ claim ledger နဲ့ review report ကို chapter အသစ်တွေပါဝင်အောင် update လုပ်မယ်။
- Existing `examples/minimal_runtime.py` နဲ့ သူ့ tests ကို မပြင်ဘူး။ Story workshop အတွက် example အသစ်တွေ သီးခြားထည့်မယ်။

## 3. Narrative design

### Recurring character

ဇာတ်ကောင်နာမည်က **Lewis** ဖြစ်တယ်။ Lewis က repository ဖတ်၊ test run၊ error ရှာပေးနိုင်တဲ့ local Python coding Agent တစ်ခုကို တည်ဆောက်နေတဲ့ developer ဖြစ်တယ်။

Project တစ်ခုတည်းကို ခြောက်ခန်းလုံး ဆက်သုံးမယ်။ ဒါပေမယ့် chapter တစ်ခန်းစီမှာ incident တစ်ခုကို အစအဆုံးဖြေရှင်းပြီး သီးခြားဖတ်လို့ရမယ်။ Lewis ရဲ့အဖြစ်အပျက်က fictional teaching scenario ဖြစ်ကြောင်း ရှင်းထားမယ်။ Runtime behavior၊ code flow နဲ့ test result တွေက pinned source evidence ကိုပဲ အခြေခံမယ်။

### Story-to-teaching transition

Chapter အသစ်တိုင်းက ဒီ rhythm ကို default အဖြစ်သုံးမယ်။

1. Lewis ကြုံရတဲ့ မြင်ကွင်းတို ၂–၄ ပိုဒ်
2. Dialogue သို့မဟုတ် terminal output တိုတစ်ခု
3. Runtime က ဘာလုပ်သွားသလဲဆိုတဲ့ bridge question
4. Mental model နဲ့ simplified code/flow
5. State change နဲ့ design reason
6. Safe trace သို့မဟုတ် offline lab
7. Failure modes
8. **Lewis ရဲ့မှတ်စု**
9. အနှစ်ချုပ်
10. Source Notes

ဇာတ်လမ်းက chapter ရဲ့ ၁၅–၂၀% ဝန်းကျင်ပဲဖြစ်မယ်။ ကျန်တာကို code သင်ခန်းစာနဲ့ လက်တွေ့လေ့လာမှုအတွက် သုံးမယ်။ ဒီရာခိုင်နှုန်းက editorial target ဖြစ်ပြီး စက်နဲ့တင်းကျပ်စစ်မယ့် rule မဟုတ်ဘူး။

Dialogue ကို အတိုချုံးသုံးမယ်။ ဝတ္ထုဆန်အောင် အလွန်အကျွံဆွဲခြင်း၊ technical fact ကို drama အတွက်ပြောင်းခြင်းနဲ့ Lewis ကို source project ရဲ့ အမှန်တကယ် contributor လို့ထင်စေနိုင်တဲ့ ရေးသားပုံကို ရှောင်မယ်။

## 4. Part and chapter structure

### Part V — Lewis နှင့် Runtime ထဲက ဖြစ်ရပ်များ

#### Chapter 10 — ညတစ်ည၊ မပြီးသေးတဲ့ Bug

**File:** `book/chapters/10-one-night-unfinished-bug.md`

Lewis က သောကြာညမှာ failing test တစ်ခုကို Agent အားရှာခိုင်းတယ်။ Agent က file ဖတ်၊ command run၊ result ပြန်ယူပြီး final answer ပေးပေမယ့် complete turn ဘယ်လိုလည်သွားသလဲ မမြင်ရသေးဘူး။

Learning scope:

- user prompt ကနေ final response အထိ complete Agent turn
- model stream → Tool Call → Tool Result → next model call
- event timeline ဖတ်နည်း
- existing minimal runtime နဲ့ production Travis234 ကြား boundary
- fake model/fake tool နဲ့ end-to-end trace

ဒီ chapter က Chapter 01၊ 02၊ 04၊ 07 နဲ့ 08 မှာ ခွဲသင်ခဲ့တဲ့ idea တွေကို case study တစ်ခုထဲ ပြန်ဆုံစေမယ်။ အဲဒီ chapters ရဲ့ theory ကို ထပ်ရေးမှာမဟုတ်ဘူး။

#### Chapter 11 — Agent ကို လမ်းပြန်ညွှန်ရတဲ့အချိန်

**File:** `book/chapters/11-steering-followup-cancellation.md`

Agent က file မှားဖတ်နေချိန် Lewis ဆီ အချက်အလက်အသစ်ရောက်လာတယ်။ Run ကိုသတ်မလား၊ steering message ပို့မလား၊ နောက် turn အတွက် follow-up ထားမလားဆိုတာ incident ရဲ့အဓိကမေးခွန်းဖြစ်မယ်။

Learning scope:

- pending message queue
- steering နဲ့ follow-up drain points
- inner loop နဲ့ outer loop ownership
- abort၊ cancellation၊ continue boundaries
- tool run နေချိန် message အသစ်ဝင်လာခြင်း
- race condition နဲ့ run ownership

#### Chapter 12 — Tool က အမှားပြန်လာတဲ့အခါ

**File:** `book/chapters/12-when-tools-fail.md`

Lewis ရဲ့ Agent က မရှိတဲ့ Tool ကိုခေါ်တယ်။ နောက်တစ်ကြိမ် arguments မှားတယ်။ Tool body တကယ် run တဲ့အခါလည်း failure ဖြစ်တယ်။ Error အားလုံးကို exception တစ်မျိုးတည်းလို ကိုင်တွယ်လို့မရကြောင်း ဒီ sequence နဲ့ပြမယ်။

Learning scope:

- unknown tool
- invalid arguments
- before-hook block
- invoked tool failure
- prepare → execute → finalize boundary
- immediate outcome နဲ့ invoked failure ရဲ့ after-hook behavior
- model ဆီ protocol-valid Tool Result ပြန်ပို့ခြင်း

#### Chapter 13 — ပြန်ဖွင့်လိုက်တော့ အလုပ်ဘယ်ကဆက်မလဲ

**File:** `book/chapters/13-session-resume-after-restart.md`

Lewis ရဲ့ terminal ပိတ်သွားပြီး နောက်နေ့ session ပြန်ဖွင့်တဲ့အခါ မနေ့ကဆုံးဖြတ်ချက်တွေကို Agent က ဘယ်လိုပြန်ရသလဲဆိုတာကနေ persistence နဲ့ restore ကို သင်မယ်။

Learning scope:

- in-memory context နဲ့ persisted session
- session entries နဲ့ active branch
- Compaction summary၊ first-kept anchor နဲ့ token metadata
- persisted entries ကနေ active context ပြန်တည်ဆောက်ခြင်း
- runtime state နဲ့ stored state မကွဲစေရန်
- active run နဲ့ manual Compaction ပြိုင်နိုင်တဲ့ boundary

#### Chapter 14 — မှားသွားတဲ့လမ်းကို ခြေရာပြန်ကောက်ခြင်း

**File:** `book/chapters/14-debugging-agent-trajectory.md`

Agent က “ပြီးပါပြီ” လို့ပြောပေမယ့် test မအောင်သေးဘူး။ Lewis က message၊ Tool Call နဲ့ event trace ကို နောက်ပြန်ဖတ်ပြီး လမ်းလွဲသွားတဲ့ boundary ကို ရှာမယ်။

Learning scope:

- event stream ကို debugging trace အဖြစ်ဖတ်ခြင်း
- message events နဲ့ Tool execution events
- completion order နဲ့ result insertion order
- trace ကနေ failure boundary ပြန်တည်ဆောက်ခြင်း
- log လုပ်သင့်တဲ့ state နဲ့ မလုပ်သင့်တဲ့ secret/large output
- trace ကသက်သေပြနိုင်တာနဲ့ မပြနိုင်တာ

### Part VI — Lewis ၏ Runtime Workshop

#### Chapter 15 — ယုံကြည်ရတဲ့ Python Port တစ်ခုဖြစ်လာဖို့

**File:** `book/chapters/15-building-a-trustworthy-port.md`

Lewis ရဲ့ runtime က demo မှာ အလုပ်လုပ်ပေမယ့် Pi/Hermes behavior နဲ့ တကယ်တူသလား မသေချာသေးဘူး။ “အလုပ်လုပ်တယ်” ဆိုတဲ့အဆင့်ကနေ “evidence နဲ့ယုံနိုင်တယ်” ဆိုတဲ့အဆင့်ကို ပြောင်းမယ်။

Learning scope:

- fake model နဲ့ deterministic test
- fake Tool နဲ့ safe failure injection
- event-order နဲ့ result-order contracts
- cancellation နဲ့ iteration-limit tests
- parity manifest ဖတ်နည်း
- intentional divergence အတွက် reason နဲ့ safety evidence
- reader ရဲ့ ကိုယ်ပိုင် runtime milestone နဲ့ final exercises

## 5. Offline workshop artifacts

Existing minimal runtime ကို မပြောင်းဘဲ concept တစ်ခုစီကို သီးခြားစမ်းနိုင်တဲ့ teaching artifacts လေးခု ထည့်မယ်။

| Artifact | Chapter | Observable lesson |
|---|---|---|
| `examples/lewis_message_control.py` | 11 | Steering က current turn boundary မှာဝင်ပြီး Follow-up က နောက် outer turn ကိုစတင်ပုံ |
| `examples/lewis_tool_outcomes.py` | 12 | Unknown/invalid/blocked immediate outcomes နဲ့ invoked failure ကို ခွဲပြပုံ |
| `examples/lewis_session_restore.py` | 13 | Persisted entries ကနေ compacted active context ပြန်တည်ဆောက်ပုံ |
| `examples/lewis_trace_reader.py` | 14 | Event trace ကနေ completion order၊ result order နဲ့ failure boundary ကို ပြန်ဖတ်ပုံ |

Chapter 10 က existing `examples/minimal_runtime.py` ကို ပြန်သုံးမယ်။ Chapter 15 က example ငါးခုလုံးရဲ့ behavior ကို contract assertions နဲ့ပြန်ချိတ်မယ်။ New tests ကို `tests/test_lewis_workshop.py` တစ်ဖိုင်ထဲထားပြီး artifact တစ်ခုချင်းအတွက် focused test class သို့မဟုတ် test group ခွဲမယ်။

Artifacts တွေက network၊ API key နဲ့ provider account မလိုရဘူး။ Session restore example က standard-library temporary directory ကို default သုံးပြီး user workspace ကိုမပြောင်းရဘူး။ Sample တိုင်းမှာ deterministic expected output သို့မဟုတ် assertion ပါရမယ်။ Existing minimal runtime ကို duplicated production implementation အဖြစ် မချဲ့ရဘူး။

## 6. Evidence and claim policy

New chapters က current pinned revisions ကိုပဲ baseline အဖြစ်သုံးမယ်။

| Source | Revision |
|---|---|
| Agentic AI Book | `7eed5ca1c4b21ab766dda2df4e039ab745cdc30f` |
| Travis234 | `68b1831691b8ec93f9550ce63b80cdcb7a591b2e` |
| Pi | `1f0dbc008c9b3e88017d42e8a1b46d416ad2b6b6` |
| Hermes Agent | `af250d84948179834820a62bfd870c0df6f264a1` |

Chapter 12 က current `C-HOOK-BOUNDARY` ကို ပြန်သုံးမယ်။ အောက်ပါ claim IDs အသစ်တွေကို chapter scope နဲ့အညီ ထည့်မယ်။

- `C-MESSAGE-DRAIN` — steering နဲ့ follow-up drain points
- `C-ABORT-OWNERSHIP` — abort/continue နဲ့ run ownership boundary
- `C-SESSION-RESTORE` — persisted entries ကနေ active context restore
- `C-TRACE-ORDER` — completion event နဲ့ result insertion ordering
- `C-CONTRACT-TESTS` — fake-model behavioral contracts ရဲ့ evidence boundary

Source map မှာ `T-AGENT`၊ `T-RUN-LEASE`၊ `T-SESSION-STORE`၊ `T-SESSION-PERSISTENCE`၊ `T-EVAL-TRACE` နဲ့ `T-EVENT-STREAM` IDs ကို သက်ဆိုင်ရာ Travis234 files/tests နဲ့ချိတ်မယ်။ ID ရှိပြီးသားဆို duplicate မဖန်တီးဘဲ mapping ကိုချဲ့မယ်။ Runtime claim တိုင်းမှာ Source Notes သို့မဟုတ် Claim Ledger link ပါရမယ်။

Fictional dialogue၊ terminal scene နဲ့ Lewis ရဲ့ခံစားချက်တွေကို source-backed fact အဖြစ် မဖော်ပြဘူး။ Locally rerun မထားတဲ့ test result ကို rerun ထားသလို မရေးဘူး။

## 7. Writing and language policy

- Chapter တစ်ခန်း ၁,၂၀၀–၁,၈၀၀ words ဝန်းကျင်ကို target ထားမယ်။ Concept ပြည့်စုံရင် count ဖြည့်ဖို့မဆွဲဘူး။
- Natural Burmese ကို ဦးစားပေးပြီး canonical English technical terms ကို လက်ရှိ style guide အတိုင်းသုံးမယ်။
- `လက်နဲ့လိုက်ခြင်း` လို မသဘာဝကျတဲ့ စကားလုံးတွဲတွေကို chapter အသစ်နဲ့ manuscript အားလုံးမှာ scan လုပ်မယ်။
- Agentic AI Book ရဲ့ story/analogy rhythm နဲ့ Software Engineering reference ရဲ့ problem-first teaching pattern ကို high-level reference အဖြစ်သာသုံးမယ်။ စာကြောင်း၊ ဇာတ်ကောင်၊ ထူးခြားတဲ့ဥပမာနဲ့ author voice ကို မကူးဘူး။
- Diagram က ordering သို့မဟုတ် state transition ကို prose ထက်သိသိသာသာရှင်းစေမှ သုံးမယ်။
- **Lewis ရဲ့မှတ်စု** က အချက် ၃–၅ ချက်ပါပြီး chapter lesson ကို character perspective နဲ့ ပြန်ချုပ်မယ်။ Source claim အသစ် ထည့်တဲ့နေရာမဖြစ်ရဘူး။

## 8. Navigation and repository updates

`book/SUMMARY.md` မှာ Part V နဲ့ Part VI ထည့်ပြီး Chapter 15 နောက်မှ Appendices ဆက်မယ်။ Chapter navigation chain က:

`09 → 10 → 11 → 12 → 13 → 14 → 15 → Appendix A`

Navigation-only updates အပြင် existing Chapter 00–09 prose ကို မထိဘူး။ Repository `README.md`၊ `book/README.md` နဲ့ `book/REVIEW_REPORT.md` ကို expansion status၊ chapter count နဲ့ final verification boundary ပါဝင်အောင် update လုပ်မယ်။

## 9. Out of scope

- provider-by-provider configuration
- TUI command walkthrough
- extension inventory
- authentication/OAuth setup
- package manager catalog
- Travis234 feature အကုန်ကို manual အဖြစ်ပြန်ရေးခြင်း
- Lewis ကိုသုံးပြီး fictional production benchmark သို့မဟုတ် security guarantee ဖန်တီးခြင်း
- existing approved chapter prose ကို story voice နဲ့ပြန်ရေးခြင်း

## 10. Verification and acceptance

Expansion complete ဖြစ်ဖို့:

- Chapter 10–15 ဖိုင် ၆ ခုရှိရမယ်။
- Main sequence က ၁၆ ခန်းဖြစ်ပြီး SUMMARY နဲ့ Previous/Next links အားလုံးမှန်ရမယ်။
- New chapter တိုင်းမှာ Lewis opening၊ teaching transition၊ Lewis ရဲ့မှတ်စု၊ အနှစ်ချုပ်နဲ့ Source Notes ပါရမယ်။
- Story scene နဲ့ technical claim boundary ရှင်းရမယ်။
- New executable artifacts compile/run ရမယ်။
- Existing 7 tests နဲ့ new tests အားလုံး pass ရမယ်။
- Book checker၊ link checker နဲ့ `git diff --check` pass ရမယ်။
- Source claims ကို pinned files/contracts နဲ့ပြန်စစ်ရမယ်။
- Burmese terminology၊ unnatural phrase နဲ့ repeated report-tone scan လုပ်ရမယ်။
- Final review report မှာ rerun ထားတဲ့ command နဲ့ မပြေးထားတဲ့ upstream full suite ကို ခွဲရေးရမယ်။
- Commit-specific ZIP archive ဖန်တီးပြီး compressed-data verification လုပ်ရမယ်။

## 11. Delivery sequence

1. Source/claim expansion နဲ့ navigation skeleton
2. Chapter 10 end-to-end case study
3. Chapter 11–12 Pi control and Tool failure stories
4. Chapter 13 Hermes/session persistence story
5. Chapter 14 observability/debugging story
6. Chapter 15 workshop and contract testing
7. New offline artifacts and tests
8. End-to-end editorial, source and executable QA
9. Review report, final commit and versioned ZIP

Implementation မစခင် ဒီ design က user review gate ကို ဖြတ်ရမယ်။ Approved design ကနေ writing plan ပြောင်းတဲ့အခါ chapter တစ်ခန်းချင်းအတွက် source files၊ claims၊ story beat၊ lab နဲ့ verification command ကို task အဖြစ်ခွဲရမယ်။

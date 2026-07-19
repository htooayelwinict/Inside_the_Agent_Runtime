# Travis234 Book — Authoring Design

**Status:** Approved

**Date:** 2026-07-18

**Format:** Standalone sequel repository

## 1. Book identity

Working title:

> **Travis234 — Pi Agent Loop နှင့် Hermes Compaction ကို Python ဖြင့် ပြန်တည်ဆောက်ခြင်း**

ဒီစာအုပ်က `Agentic-AI-Book` ကို ဖတ်ပြီးသားသူတွေအတွက် ဆက်ရေးမယ့် sequel ဖြစ်တယ်။ Travis234 ရဲ့ feature အကုန်လုံးကို catalog လုပ်မှာ မဟုတ်ဘူး။ Pi ကနေ port လုပ်ထားတဲ့ agent runtime နဲ့ Hermes ကနေ port လုပ်ထားတဲ့ context compaction ကို Python code နဲ့ နားလည်နိုင်ဖို့ အဓိကထားမယ်။

## 2. Intended reader and promise

Reader က Python ကို အခြေခံသိပြီး agentic AI concept တွေကို ကြားဖူးသူ ဖြစ်နိုင်တယ်။ TypeScript, Pi သို့မဟုတ် Hermes source code ကို အရင်ဖတ်ထားဖို့ မလိုဘူး။

စာအုပ်ပြီးသွားတဲ့အခါ reader က—

- agent loop တစ်ခုရဲ့ control flow နဲ့ event ordering ကို ရှင်းပြနိုင်မယ်၊
- Pi ရဲ့ TypeScript semantics ကို Python `asyncio` နဲ့ ဘယ်လိုထိန်းထားသလဲ နားလည်မယ်၊
- sequential/parallel tool execution နဲ့ bounded concurrency ရဲ့ trade-off ကို သိမယ်၊
- context window ပြည့်လာချိန်မှာ Hermes-style compaction ဘယ်လိုအလုပ်လုပ်သလဲ သိမယ်၊
- agent loop နဲ့ compaction ကို runtime တစ်ခုထဲ ဘယ်လိုချိတ်သလဲ လက်တွေ့လေ့လာနိုင်မယ်။

## 3. Scope boundary

### In scope

- Pi agent loop anatomy and execution semantics
- TypeScript-to-Python semantic porting choices
- Tool execution, validation, hooks, event ordering and bounded concurrency
- Context-window pressure and Hermes-style compression policy
- Deterministic pruning, structured summaries, token-budgeted tails and anti-thrashing
- Pi loop + Hermes compaction integration in Travis234
- Small offline labs, parity evidence and intentional divergences
- Installation and npm Docker launcher as appendices

### Out of scope

- provider-by-provider configuration catalog
- full TUI walkthrough
- every extension, command and integration
- exhaustive API reference
- claims that the Docker launcher is a complete security sandbox
- long source dumps that can be replaced by a focused excerpt or flow diagram

## 4. Chapter structure

### Part I — Why this runtime exists

0. **မိတ်ဆက်၊ Attribution နှင့် Reader Guide**

   Sequel relationship, learning path, source licenses and pinned revisions.

1. **Pi နဲ့ Hermes ကို ဘာကြောင့် တွဲကြည့်ရတာလဲ**

   Agent loop handles action; compaction protects continuity. Explain the two problems before code.

### Part II — Porting the Pi agent loop

2. **Pi Agent Loop Anatomy**

   Outer follow-up loop, inner steering/tool loop, assistant streaming, tool results and termination.

3. **TypeScript ကနေ Python သို့ Semantic Port**

   `Promise`/callbacks/events versus `asyncio`, dataclasses, async iteration and abort handling. Preserve behavior, not syntax.

4. **Tool Execution နှင့် Bounded Concurrency**

   Sequential versus parallel execution, validation, hooks, source-ordered results, cancellation and Travis234's bounded worker policy.

### Part III — Porting Hermes compaction

5. **Context Window ပြည့်လာတဲ့ ပြဿနာ**

   Input/output token pressure, tool-output growth, overflow failure and why naive truncation loses state.

6. **Hermes-style Compaction**

   Deterministic prune, structured LLM summary, iterative summary update, head + budgeted tail and anti-thrashing thresholds.

### Part IV — A coherent Python runtime

7. **Pi နဲ့ Hermes တွေ့ဆုံရာ**

   Preflight, post-response, overflow and manual compaction paths around the agent session.

8. **Minimal Runtime Lab**

   A small fake-model/fake-tool runtime that works offline and exposes the important event sequence.

9. **Parity, Divergence နှင့် သင်ခန်းစာများ**

   What is intentionally the same, what differs in Python and how parity contracts prevent accidental drift.

### Appendices

- Installation and first run
- npm Docker launcher and its security boundaries
- Source map and pinned revisions
- Glossary, references and third-party notices

## 5. Chapter authoring template

Chapter တိုင်းကို တင်းကျပ်တဲ့ form တစ်ခုထဲ မထည့်ဘဲ အောက်ပါ learning sequence ကို default အဖြစ်သုံးမယ်။

1. **Problem / Question** — reader ကြုံနိုင်တဲ့ လက်တွေ့ပြဿနာနဲ့ စမယ်။
2. **Mental model** — code မဖတ်ခင် မှတ်မိလွယ်တဲ့ ပုံစံနဲ့ ရှင်းမယ်။
3. **Source mapping** — Pi, Hermes နဲ့ Travis234 ထဲက သက်ဆိုင်ရာ component တွေကို ချိတ်ပြမယ်။
4. **Execution flow** — ordering နဲ့ state change အရေးကြီးရင် diagram သုံးမယ်။
5. **Small lab** — dependency နည်းပြီး offline run နိုင်တဲ့ ဥပမာပေးမယ်။
6. **Failure modes** — ပုံမှန်နားလည်မှုလွဲနိုင်တာနဲ့ production risk ကို ဖော်ပြမယ်။
7. **Takeaways** — chapter ရဲ့ အဓိကအချက်ကို ချုံ့မယ်။
8. **Source notes** — exact files, revisions and attribution ထည့်မယ်။

## 6. Writing profile

`se.saturngod.net` ကို exact imitation မလုပ်ဘဲ high-level teaching patterns အဖြစ်သာ reference ယူမယ်။

- မေးခွန်း သို့မဟုတ် လက်တွေ့ပြဿနာနဲ့ subsection ကို စမယ်။
- အဓိကရှင်းလင်းချက်ကို natural Burmese နဲ့ရေးပြီး `Agent Loop`, `Tool Result`, `Context Window`, `Compaction` လို technical terms တွေကို English အတိုင်းထားမယ်။
- “ကျွန်တော်တို့”, “ဆိုပါစို့”, “ဒါပေမယ့်”, “ဥပမာ” လို conversational connectors ကို လိုအပ်သလောက်သာ သုံးမယ်။
- Definition → Why it matters → Example/analogy → Code/flow → Limitation → Takeaway အစီအစဉ်ကို ဦးစားပေးမယ်။
- Paragraph ကို short-to-medium length ထားပြီး numbered sections/subsections နဲ့ ဖတ်ရလွယ်အောင်ခွဲမယ်။
- Academic jargon အများကြီးနဲ့ word-for-word translation ကို ရှောင်မယ်။
- Website မှာတွေ့ရတဲ့ စာလုံးပေါင်း၊ spacing နဲ့ terminology မညီတာတွေကို မကူးဘဲ clean grammar နဲ့ standardized terms သုံးမယ်။
- မူရင်း `Agentic-AI-Book` ရဲ့ Burmese-first voice ကို ဆက်ထိန်းမယ်။ Saturngod ရဲ့ teaching structure ကို reference ယူပေမယ့် စာကြောင်းနဲ့ author voice ကို မတုပဘူး။

## 7. Technical evidence and source policy

Claims တွေကို pinned source revisions နဲ့ ချိတ်ထားမယ်။ Initial research baseline:

| Source | Revision |
|---|---|
| `htooayelwinict/Agentic-AI-Book` | `7eed5ca1c4b21ab766dda2df4e039ab745cdc30f` |
| `htooayelwinict/travis234` | `68b1831691b8ec93f9550ce63b80cdcb7a591b2e` |
| `earendil-works/pi` | `1f0dbc008c9b3e88017d42e8a1b46d416ad2b6b6` |
| `NousResearch/hermes-agent` | `af250d84948179834820a62bfd870c0df6f264a1` |

Source use rules:

- behavior claims must point to source files or parity contracts;
- code excerpts stay short and are followed by original explanation;
- Travis234's four intentional Pi divergences are described as divergences, not defects;
- test counts copied from repository documentation are labeled as recorded results unless rerun locally;
- diagrams are original reconstructions of execution flow;
- all third-party excerpts retain source and license attribution.

## 8. Known parity story

The book should explain the current parity contract as evidence, not marketing:

- Pi: 78 tracked contracts — 74 parity and 4 intentional divergences.
- Hermes compaction: 11 tracked contracts — all marked parity.
- The four Pi divergences cover bounded parallelism, project-package trust behavior in interactive and non-interactive modes, and a Pythonic async `AgentHarness` API.

These numbers are revision-specific and must be refreshed before publication.

## 9. Examples and diagrams

- Labs use fake model streams and fake tools so API keys are unnecessary.
- Each code sample demonstrates one concept and includes expected output or event order.
- Mermaid is used only when ordering, branching or state transitions are clearer visually.
- Production source is cited; simplified teaching code is clearly labeled as simplified.
- The minimal runtime lab is educational code, not a second Travis234 implementation.

## 10. Licensing and attribution

Recommended manuscript license: **CC BY-NC-SA 4.0**, matching the existing book unless the author chooses otherwise before publication.

Pi, Hermes Agent and Travis234 source material remains under its respective MIT notices. The repository will include:

- `LICENSE` for the manuscript,
- `THIRD_PARTY_NOTICES.md`,
- chapter-level source notes,
- a source map with pinned revisions.

## 11. Quality gates

A chapter is ready only when:

- the opening problem and learning outcome are clear;
- every non-obvious runtime claim has a source;
- code and diagrams match the described event order;
- the Burmese reads naturally and technical terms are consistent;
- the example runs offline or is explicitly marked pseudocode;
- source notes and attribution are present;
- unnecessary product detail has been removed.

Before publication, refresh the source pins, rerun available parity verification, test every lab and perform a full terminology/grammar pass.

## 12. Delivery strategy

Authoring proceeds in reviewable slices:

1. repository skeleton, style guide, terminology and source map;
2. Part I and the complete Chapter 2 as the tone/technical-depth benchmark;
3. Part II after benchmark review;
4. Part III;
5. Part IV and appendices;
6. end-to-end technical, language, attribution and link verification.

This sequence locks the voice and depth early while keeping later chapters consistent.

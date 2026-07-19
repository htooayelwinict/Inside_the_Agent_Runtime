# Pinned Source Map

ဒီ source map က chapter ထဲက runtime claim တွေကို source file တစ်ခုနဲ့ တိတိကျကျချိတ်ဖို့ သုံးပါတယ်။ ID တစ်ခုက file တစ်ခုလုံးမှန်ကြောင်း အာမခံတာမဟုတ်ဘဲ ဒီစာအုပ်က အဲဒီ file ကို ဘယ် evidence boundary အတွက်သုံးထားသလဲဆိုတာ သတ်မှတ်ပေးတာပါ။

## Research revisions

| Project | Pinned revision |
|---|---|
| Agentic AI Book | `7eed5ca1c4b21ab766dda2df4e039ab745cdc30f` |
| Travis234 | `68b1831691b8ec93f9550ce63b80cdcb7a591b2e` |
| Pi | `1f0dbc008c9b3e88017d42e8a1b46d416ad2b6b6` |
| Hermes Agent | `af250d84948179834820a62bfd870c0df6f264a1` |

## Travis234 sources

| ID | Pinned source | Evidence boundary |
|---|---|---|
| T-LOOP | [`travis/agent/agent_loop.py`](https://github.com/htooayelwinict/travis234/blob/68b1831691b8ec93f9550ce63b80cdcb7a591b2e/travis/agent/agent_loop.py) | Python loop control flow၊ event emission နဲ့ Tool Call continuation |
| T-AGENT | [`travis/agent/agent.py`](https://github.com/htooayelwinict/travis234/blob/68b1831691b8ec93f9550ce63b80cdcb7a591b2e/travis/agent/agent.py) | Agent runtime owner နဲ့ public control surface |
| T-TYPES | [`travis/agent/types.py`](https://github.com/htooayelwinict/travis234/blob/68b1831691b8ec93f9550ce63b80cdcb7a591b2e/travis/agent/types.py) | Python message၊ event နဲ့ tool contracts |
| T-ASYNC | [`travis/agent/async_utils.py`](https://github.com/htooayelwinict/travis234/blob/68b1831691b8ec93f9550ce63b80cdcb7a591b2e/travis/agent/async_utils.py) | Sync/async hook resolution နဲ့ sync entry boundary |
| T-TOOLS | [`travis/agent/tool_coordinator.py`](https://github.com/htooayelwinict/travis234/blob/68b1831691b8ec93f9550ce63b80cdcb7a591b2e/travis/agent/tool_coordinator.py) | Bounded worker coordination |
| T-COMPRESS | [`travis/compaction/compressor.py`](https://github.com/htooayelwinict/travis234/blob/68b1831691b8ec93f9550ce63b80cdcb7a591b2e/travis/compaction/compressor.py) | Deterministic pruning နဲ့ structured summary pipeline |
| T-POLICY | [`travis/compaction/policy.py`](https://github.com/htooayelwinict/travis234/blob/68b1831691b8ec93f9550ce63b80cdcb7a591b2e/travis/compaction/policy.py) | Threshold bands၊ output reserve နဲ့ auxiliary-model capacity |
| T-TIMING | [`travis/compaction/timing.py`](https://github.com/htooayelwinict/travis234/blob/68b1831691b8ec93f9550ce63b80cdcb7a591b2e/travis/compaction/timing.py) | Automatic compaction timing နဲ့ cooldown decisions |
| T-SESSION | [`travis/coding_agent/agent_session.py`](https://github.com/htooayelwinict/travis234/blob/68b1831691b8ec93f9550ce63b80cdcb7a591b2e/travis/coding_agent/agent_session.py) | Session owner နဲ့ runtime integration surface |
| T-HARNESS | [`travis/coding_agent/agent_harness.py`](https://github.com/htooayelwinict/travis234/blob/68b1831691b8ec93f9550ce63b80cdcb7a591b2e/travis/coding_agent/agent_harness.py) | Pythonic async SDK facade နဲ့ serialized owner delegation |
| T-COORD | [`travis/coding_agent/compaction_coordinator.py`](https://github.com/htooayelwinict/travis234/blob/68b1831691b8ec93f9550ce63b80cdcb7a591b2e/travis/coding_agent/compaction_coordinator.py) | Preflight၊ post-response၊ overflow နဲ့ manual coordination |
| T-ADAPTER | [`travis/coding_agent/compaction_adapter.py`](https://github.com/htooayelwinict/travis234/blob/68b1831691b8ec93f9550ce63b80cdcb7a591b2e/travis/coding_agent/compaction_adapter.py) | Compaction result ကို persistent session entry အဖြစ် apply လုပ်ပြီး active context ပြန်တည်ဆောက်ခြင်း |
| T-APP | [`travis/app.py`](https://github.com/htooayelwinict/travis234/blob/68b1831691b8ec93f9550ce63b80cdcb7a591b2e/travis/app.py) | Normal turn၊ post-response evaluation နဲ့ overflow-recovery integration order |
| T-PACKAGE | [`README.md`](https://github.com/htooayelwinict/travis234/blob/68b1831691b8ec93f9550ce63b80cdcb7a591b2e/README.md) နှင့် [`pyproject.toml`](https://github.com/htooayelwinict/travis234/blob/68b1831691b8ec93f9550ce63b80cdcb7a591b2e/pyproject.toml) | Documented Python install commands၊ version boundary နဲ့ npm launcher entry |
| T-LAUNCHER | [`packages/travis234-cli/bin/travis234.js`](https://github.com/htooayelwinict/travis234/blob/68b1831691b8ec93f9550ce63b80cdcb7a591b2e/packages/travis234-cli/bin/travis234.js) နှင့် [`packages/travis234-cli/package.json`](https://github.com/htooayelwinict/travis234/blob/68b1831691b8ec93f9550ce63b80cdcb7a591b2e/packages/travis234-cli/package.json) | Docker mounts၊ runtime controls၊ network default နဲ့ Node version boundary |
| T-PARITY | [`scripts/parity_contracts.py`](https://github.com/htooayelwinict/travis234/blob/68b1831691b8ec93f9550ce63b80cdcb7a591b2e/scripts/parity_contracts.py) | Pinned Pi/Hermes parity manifest နဲ့ intentional divergence reasons |
| T-VERIFY | [`scripts/verify_acceptance.py`](https://github.com/htooayelwinict/travis234/blob/68b1831691b8ec93f9550ce63b80cdcb7a591b2e/scripts/verify_acceptance.py) | Acceptance manifest validation entry point |
| T-RUN-LEASE | [`travis/agent/run_lease.py`](https://github.com/htooayelwinict/travis234/blob/68b1831691b8ec93f9550ce63b80cdcb7a591b2e/travis/agent/run_lease.py) | Active run ownership၊ wait နဲ့ idempotent release |
| T-SESSION-STORE | [`travis/coding_agent/session_store.py`](https://github.com/htooayelwinict/travis234/blob/68b1831691b8ec93f9550ce63b80cdcb7a591b2e/travis/coding_agent/session_store.py) | Session entries၊ branch lineage၊ Compaction metadata နဲ့ context reconstruction |
| T-SESSION-PERSISTENCE | [`travis/coding_agent/session_persistence.py`](https://github.com/htooayelwinict/travis234/blob/68b1831691b8ec93f9550ce63b80cdcb7a591b2e/travis/coding_agent/session_persistence.py) | Persistent session orchestration နဲ့ restored state integration |
| T-EVAL-TRACE | [`travis/coding_agent/eval_trace.py`](https://github.com/htooayelwinict/travis234/blob/68b1831691b8ec93f9550ce63b80cdcb7a591b2e/travis/coding_agent/eval_trace.py) | Evaluation/conversation trace writing နဲ့ secret redaction boundary |
| T-EVENT-STREAM | [`travis/ai/event_stream.py`](https://github.com/htooayelwinict/travis234/blob/68b1831691b8ec93f9550ce63b80cdcb7a591b2e/travis/ai/event_stream.py) | Provider-to-runtime assistant event stream boundary |

## Pi sources

| ID | Pinned source | Evidence boundary |
|---|---|---|
| P-LOOP | [`packages/agent/src/agent-loop.ts`](https://github.com/earendil-works/pi/blob/1f0dbc008c9b3e88017d42e8a1b46d416ad2b6b6/packages/agent/src/agent-loop.ts) | Upstream Agent Loop structure နဲ့ execution semantics |
| P-AGENT | [`packages/agent/src/agent.ts`](https://github.com/earendil-works/pi/blob/1f0dbc008c9b3e88017d42e8a1b46d416ad2b6b6/packages/agent/src/agent.ts) | Upstream Agent owner နဲ့ queue control surface |
| P-TYPES | [`packages/agent/src/types.ts`](https://github.com/earendil-works/pi/blob/1f0dbc008c9b3e88017d42e8a1b46d416ad2b6b6/packages/agent/src/types.ts) | Upstream message၊ event နဲ့ tool contracts |
| P-HARNESS | [`packages/agent/src/harness/agent-harness.ts`](https://github.com/earendil-works/pi/blob/1f0dbc008c9b3e88017d42e8a1b46d416ad2b6b6/packages/agent/src/harness/agent-harness.ts) | Upstream harness public shape |

## Hermes Agent sources

| ID | Pinned source | Evidence boundary |
|---|---|---|
| H-COMPRESS | [`agent/context_compressor.py`](https://github.com/NousResearch/hermes-agent/blob/af250d84948179834820a62bfd870c0df6f264a1/agent/context_compressor.py) | Upstream context compressor နဲ့ token-budget decisions |
| H-CONVERSATION | [`agent/conversation_compression.py`](https://github.com/NousResearch/hermes-agent/blob/af250d84948179834820a62bfd870c0df6f264a1/agent/conversation_compression.py) | Conversation compression workflow |
| H-CONTEXT | [`agent/context_engine.py`](https://github.com/NousResearch/hermes-agent/blob/af250d84948179834820a62bfd870c0df6f264a1/agent/context_engine.py) | Context construction နဲ့ compression integration |

## Usage rule

Chapter Source Notes မှာ အနည်းဆုံး source ID နဲ့ pinned revision ပါရမယ်။ Newer upstream source ကို reference လုပ်မယ်ဆိုရင် revision အသစ်ကို ledger ထဲအရင်ထည့်ပြီး claim ကို ပြန်စစ်ရပါမယ်။

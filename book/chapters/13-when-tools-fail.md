# Chapter 13 — Tool က အမှားပြန်လာတဲ့အခါ

## ၁၃.၁ Error သုံးခုက ဘာကြောင့် မတူတာလဲ

စနေနေ့ညနေမှာ Lewis က Agent ကို project note တစ်ဖိုင်ဖတ်ခိုင်းလိုက်ပါတယ်။ ပထမအကြိမ် model က registry ထဲမရှိတဲ့ `missing` Tool ကိုခေါ်တယ်။ Runtime က `unknown tool: missing` လို့ပြန်ပေးလိုက်တော့ model က နာမည်ကိုပြင်ပြီး `read` ကိုခေါ်ပေမယ့် ဒီတစ်ခါ `path` argument မပါလာပါဘူး။ ဒုတိယအဖြေက `path is required` ဖြစ်သွားပါတယ်။

တတိယအကြိမ်မှာတော့ call ပုံစံက မှန်သွားပါတယ်။ `read` Tool ရှိတယ်၊ `{"path": "notes.txt"}` လည်းပါလာတယ်။ ဒါပေမယ့် Tool body တကယ် run တဲ့အခါ ဒီလိုဖြစ်သွားတယ်။

```text
RuntimeError: disk unavailable
```

Lewis က error စာကြောင်းသုံးခုကို notebook ထဲကော်ပီကူးပြီး “အားလုံး Tool မအောင်တာပဲမဟုတ်လား” လို့ရေးလိုက်ပါတယ်။ ခဏနေတော့ မေးခွန်းကိုပြောင်းရေးလိုက်တယ်။ ဘယ် failure မှာ Tool body တကယ်စခဲ့သလဲ။ ဘယ် failure မှာ Runtime က body မခေါ်ခင်တားခဲ့သလဲ။

`Lewis နဲ့ ဒီ incident ဟာ Tool failure boundary ကိုလေ့လာဖို့ ဖန်တီးထားတဲ့ စိတ်ကူးယဉ်ဇာတ်လမ်းပါ။ တကယ့် Travis234 production incident သို့မဟုတ် contributor တစ်ယောက်ရဲ့ဖြစ်ရပ် မဟုတ်ပါဘူး။ အောက်က Runtime behavior claim တွေကတော့ Source Notes မှာဖော်ပြထားတဲ့ pinned source၊ claim နဲ့ parity contracts အပေါ်အခြေခံထားပါတယ်။`

ပထမ error နှစ်ခုက Tool body မစခင် ရလာတဲ့ `immediate outcome` ဖြစ်ပါတယ်။ တတိယ error က valid Tool ကိုတကယ်ခေါ်ပြီးမှ ရလာတဲ့ `invoked failure` ပါ။ User အတွက် “မဖတ်နိုင်ဘူး” ဆိုတဲ့နောက်ဆုံးအဓိပ္ပာယ်တူနိုင်ပေမယ့် Runtime lifecycle အတွက်တော့ ဒီခွဲခြားမှုက hook ခေါ်မခေါ်၊ event ဘယ်လို finalize လုပ်မလဲနဲ့ model ဆီဘာပြန်ပို့မလဲကို ဆုံးဖြတ်ပေးပါတယ်။

## ၁၃.၂ Prepare → Execute → Finalize

Tool Call တစ်ခုရတာနဲ့ function ကိုတန်းခေါ်လိုက်ရင် failure ရဲ့နေရာပျောက်သွားပါတယ်။ စာပို့ပစ္စည်းတစ်ခုကို လက်ခံ၊ ပို့ဆောင်၊ အတည်ပြုသလို Tool lifecycle ကို `Prepare → Execute → Finalize` ဆိုပြီး သုံးပိုင်းခွဲကြည့်နိုင်ပါတယ်။ Analogy က အစီအစဉ်ကိုမှတ်ဖို့သာဖြစ်ပြီး production implementation အတိအကျကို အစားမထိုးပါဘူး။

`Prepare` မှာ Runtime က Tool name ကို active catalog ထဲရှာတယ်၊ arguments ကိုပြင်ဆင်ပြီး schema နဲ့စစ်တယ်၊ ပြီးရင် before hook ရဲ့ဆုံးဖြတ်ချက်ကိုယူတယ်။ ဒီ gate တစ်ခုခုမှာမအောင်ရင် body မခေါ်ဘဲ error outcome ကိုချက်ချင်းတည်ဆောက်နိုင်ပါတယ်။ “ချက်ချင်း” ဆိုတာ model ကိုအဖြေပြန်တဲ့ latency အာမခံချက်မဟုတ်ဘဲ execution phase မဝင်ခဲ့ကြောင်းပြောတာပါ။

`Execute` မှာမှ valid ဖြစ်ပြီးခွင့်ပြုထားတဲ့ Tool body ကိုတကယ် invoke လုပ်ပါတယ်။ Body က content အောင်မြင်စွာပြန်နိုင်သလို exception လည်းတက်နိုင်ပါတယ်။ Invoke စပြီးပြီဆိုတာနဲ့ outcome က immediate မဟုတ်တော့ပါဘူး။ Success ဖြစ်ဖြစ် failure ဖြစ်ဖြစ် invoked path ထဲရောက်နေပါပြီ။

`Finalize` က result content၊ error state နဲ့ lifecycle ကို Runtime ဘက်ပြန်ယူတဲ့အပိုင်းပါ။ Invoked outcome အတွက် after hook ကို တစ်ကြိမ်ခေါ်ပြီး Tool Result တည်ဆောက်နိုင်ပါတယ်။ ဒီ mental model က “error ဖြစ်လား” တစ်ခုတည်းမမေးဘဲ “ဘယ် phase အထိရောက်ခဲ့လဲ” ကိုပါ မေးစေပါတယ်။

```text
Prepare ── rejected ───────────────→ immediate outcome ──→ no after hook
   │
   └─ allowed → Execute → success ─→ invoked outcome ────→ after hook once
                       └→ failure ─→ invoked outcome ────→ after hook once
```

## ၁၃.၃ Unknown Tool နဲ့ Invalid Arguments

Lewis ရဲ့ပထမ call မှာ `missing` ဆိုတဲ့ name ကို catalog ထဲရှာမတွေ့ပါဘူး။ ခေါ်စရာ function မရှိသေးလို့ Tool body စတယ်လို့ပြောစရာမရှိပါဘူး။ Runtime က unknown-tool error outcome တည်ဆောက်ပြီး ဒီ call ကိုအဲဒီနေရာမှာရပ်ပါတယ်။

ဒုတိယ call မှာတော့ `read` ကိုရှာတွေ့ပါတယ်။ ဒါပေမယ့် arguments က အသုံးပြုနိုင်တဲ့ပုံစံမဖြစ်သေးပါဘူး။ Validation ရဲ့အဓိကတာဝန်က body ဆီမပြည့်စုံတဲ့ input မပို့ဖို့ပါ။ Unknown Tool နဲ့ invalid arguments က အကြောင်းရင်းမတူပေမယ့် execution မဝင်သေးတာတူပါတယ်။ ဒါကြောင့် နှစ်ခုလုံး immediate outcomes ဖြစ်ပြီး after hook ကိုမခေါ်ပါဘူး။

ဒီခွဲခြားမှုက observability အတွက်လည်း အသုံးဝင်ပါတယ်။ Unknown count များရင် model ထုတ်တဲ့ Tool name သို့မဟုတ် catalog exposure ကိုစစ်ရမယ်။ Invalid count များရင် schema description၊ argument generation သို့မဟုတ် preparation ကိုစစ်ရမယ်။ Error အားလုံးကို `tool failed` တစ်မျိုးတည်းမှတ်ထားရင် ပြင်ရမယ့်နေရာကို မမြင်နိုင်တော့ပါဘူး။

## ၁၃.၄ Before-hook က တားလိုက်တဲ့အချိန်

Name နဲ့ arguments မှန်တာတစ်ခုတည်းကြောင့် Tool ကို run ခွင့်ရပြီလို့ မဆိုနိုင်ပါဘူး။ `before hook` ဆိုတာ execution မစခင် current context နဲ့ validated arguments ကိုကြည့်ပြီး call ကိုခွင့်ပြုမလား ဆုံးဖြတ်နိုင်တဲ့ policy gate ပါ။ ဥပမာ read path တစ်ခုကို policy အရပိတ်ထားနိုင်ပါတယ်။

Before hook က block လိုက်ရင် outcome က `blocked` ဖြစ်ပေမယ့် invoked failure မဟုတ်ပါဘူး။ Body မစခဲ့လို့ side effect ဖြစ်ပြီးသားလို့လည်း မယူဆရပါဘူး။ ဒီ path မှာ after hook မခေါ်တာက “hook ကိုမေ့သွားခြင်း” မဟုတ်ဘဲ invocation မရှိခဲ့ကြောင်း lifecycle က ထိန်းထားခြင်းပါ။

တားသင့်တာကို after hook ဆီရွှေ့ထားလို့မရပါဘူး။ After hook ဝင်ချိန်မှာ body က run ပြီးသားဖြစ်နိုင်လို့ file write သို့မဟုတ် external mutation ကို rollback လုပ်ပေးမယ့် boundary မဟုတ်ပါဘူး။ Permission နဲ့ approval လိုဆုံးဖြတ်ချက်ကို before hook သို့မဟုတ် Tool ကိုယ်ပိုင် safety check မှာထားရပါတယ်။

## ၁၃.၅ Tool Body တကယ် Run ပြီးမှ Fail ဖြစ်ခြင်း

Lewis ရဲ့တတိယ call က prepare gates အားလုံးကိုဖြတ်သွားပါတယ်။ `read` ကိုတွေ့တယ်၊ path ပါတယ်၊ before hook ကလည်းခွင့်ပြုတယ်။ Runtime က Tool body ကို invoke လုပ်ပြီးမှ body က `RuntimeError("disk unavailable")` တက်ပါတယ်။ ဒီနေရာက invoked failure ပါ။

Exception ရှိတာတစ်ခုတည်းကြောင့် Agent Loop တစ်ခုလုံးကို unhandled exception နဲ့ဖြုတ်ချရမယ်လို့ မဆိုလိုပါဘူး။ Tool execution boundary က failure ကို error outcome အဖြစ်ဖမ်း၊ finalize လုပ်ပြီး protocol-valid Tool Result အဖြစ် model ဆီပြန်ပို့နိုင်ပါတယ်။ Model က disk မရကြောင်းသိပြီး နောက်ရွေးချယ်မှုတစ်ခုတောင်းနိုင်ဖို့ error ကို context ထဲသယ်ပေးတာပါ။

ဒါပေမယ့် error result ဖြစ်သွားတာက Tool က ဘာ side effect မှမလုပ်ခဲ့ဘူးလို့ အာမမခံပါဘူး။ Body က file တစ်ဝက်ရေးပြီးမှ exception တက်နိုင်ပါတယ်။ After hook က failure ကိုကြည့်နိုင်ပေမယ့် transaction rollback မဟုတ်ပါဘူး။ Mutation လုပ်တဲ့ Tool ကိုရေးရင် atomic operation၊ cleanup နဲ့ idempotency ကို Tool design ထဲမှာပဲ သီးခြားစဉ်းစားရပါတယ်။

## ၁၃.၆ After-hook ကို ဘယ်အချိန်ခေါ်သလဲ

Lewis က notebook မှာ outcome ငါးမျိုးကို table တစ်ခုနဲ့ပြန်စီလိုက်ပါတယ်။ Exact comparison ဖြစ်လို့ ဒီနေရာမှာ table က lifecycle boundary ကိုရှင်းစေပါတယ်။

| Outcome | Body invoke ဖြစ်သလား | After hook |
|---|---:|---:|
| Unknown Tool | မဖြစ် | မခေါ် |
| Invalid arguments | မဖြစ် | မခေါ် |
| Before-hook blocked | မဖြစ် | မခေါ် |
| Invoked success | ဖြစ် | တစ်ကြိမ် |
| Invoked failure | ဖြစ် | တစ်ကြိမ် |

Rule ကို “success ဖြစ်မှ after hook ခေါ်တယ်” လို့မှတ်ရင်မှားပါတယ်။ မှန်တဲ့ boundary က invocation ပါ။ Body ကိုတကယ်ခေါ်ခဲ့ရင် success နဲ့ failure နှစ်မျိုးလုံး after hook တစ်ကြိမ်ဝင်ပါတယ်။ Body မခေါ်ခဲ့တဲ့ immediate outcomes သုံးမျိုးကတော့ after hook ကိုကျော်ပါတယ်။

ဒီ contract က audit၊ metrics နဲ့ extension behavior ကိုတည်ငြိမ်စေပါတယ်။ After hook count ကို invocation count လို့ဖတ်နိုင်ပြီး validation rejection count နဲ့ မရောတော့ပါဘူး။ ဒါပေမယ့် after hook တစ်ခုတည်းက production behavior အားလုံးမှန်ကြောင်း မသက်သေပြပါဘူး။ ဒီ chapter က pinned contracts ဖုံးထားတဲ့ invocation boundary ကိုသာ claim လုပ်ပါတယ်။

## ၁၃.၇ Model ဆီ Error Result ပြန်ပို့ခြင်း

Tool error ကို terminal log ထဲပဲရေးထားရင် model က နောက်ဆုံး request မှာဘာဖြစ်ခဲ့သလဲ မသိနိုင်ပါဘူး။ Model က Python exception object ကိုတိုက်ရိုက်မြင်တာလည်း မဟုတ်ပါဘူး။ Runtime က call နဲ့ချိတ်နိုင်တဲ့ Tool Result message တစ်ခုတည်ဆောက်ပြီး error ဖြစ်ကြောင်းနဲ့ ဖတ်လို့ရတဲ့ content ကို context ထဲပြန်ထည့်ရပါတယ်။

Unknown Tool၊ invalid arguments၊ before-hook block နဲ့ invoked exception အားလုံးဟာ model ဆီ error Tool Results အဖြစ်ရောက်နိုင်ပါတယ်။ ဒါက outcome အားလုံး lifecycle တူတယ်လို့ မဆိုလိုပါဘူး။ Model-facing protocol shape ကိုတူအောင်ထားနိုင်ပေမယ့် Runtime က immediate နဲ့ invoked state ကိုခွဲထိန်းထားရပါတယ်။ Protocol-valid ဖြစ်ခြင်းနဲ့ execution-history တူခြင်းဟာ မေးခွန်းနှစ်ခုပါ။

Error content ကို model ဆီပြန်ပို့တာက recovery အခွင့်ပေးပေမယ့် retry ကိုအမြဲခွင့်ပြုရမယ်လို့မဆိုပါဘူး။ Unknown name ကိုပြင်ပြီးထပ်ခေါ်တာက သင့်တော်နိုင်ပေမယ့် mutation Tool တစ်ခု invoked fail ဖြစ်ရင် အလုပ်တစ်စိတ်တစ်ပိုင်းပြီးထားနိုင်ပါတယ်။ Retry policy က outcome reason၊ Tool semantics နဲ့ idempotency ကိုကြည့်ပြီးမှဆုံးဖြတ်ရပါတယ်။

## ၁၃.၈ Offline Tool-outcome Lab

Boundary ကို API key မလိုဘဲစမ်းချင်ရင် [`examples/lewis_tool_outcomes.py`](../../examples/lewis_tool_outcomes.py) ကိုသုံးနိုင်ပါတယ်။ Lab ရဲ့အဓိက API က `ToolOutcome` ပြန်ပေးတဲ့ `execute_tool_call()` ပါ။ Signature ကိုတိုက်ရိုက်ကြည့်ရင် input boundary က ဒီလိုပါ။

```python
def execute_tool_call(
    name: str,
    arguments: dict[str, object],
    tools: dict[str, Tool],
    *,
    before_allowed: bool = True,
    after_hook: Callable[[ToolOutcome], None] | None = None,
) -> ToolOutcome:
```

`ToolOutcome` မှာ `phase`, `reason`, `content`, `after_hook_called` fields ပါပါတယ်။ Repository root ကနေ default demo ကို run ပါ။

```bash
python3.13 examples/lewis_tool_outcomes.py
```

လက်ရှိ output သုံးကြောင်းအတိအကျက:

```text
immediate:unknown_tool:unknown tool: missing
immediate:invalid_arguments:path is required
invoked:success:read:notes.txt
```

Default demo ရဲ့တတိယ call က Lewis ဇာတ်လမ်းထဲက failure မဟုတ်ဘဲ invoked success ကိုပြထားတာပါ။ Invoked failure ကိုစမ်းဖို့ valid body နေရာမှာ test သုံးထားတဲ့ fake Tool ကိုထည့်နိုင်ပါတယ်။

```python
def fail(_arguments):
    raise RuntimeError("disk unavailable")

outcome = execute_tool_call(
    "read",
    {"path": "notes.txt"},
    {"read": fail},
    after_hook=lambda result: print(f"after:{result.reason}"),
)
print(f"{outcome.phase}:{outcome.reason}:{outcome.content}")
```

ဒီ snippet ရဲ့ output က:

```text
after:failure
invoked:failure:RuntimeError: disk unavailable
```

`before_allowed=False` နဲ့ valid call ပေးရင် `immediate:blocked` ရပြီး after hook မဝင်ပါဘူး။ Focused tests က immediate သုံးမျိုးအတွက် after-call list အလွတ်ဖြစ်ကြောင်း၊ invoked success နဲ့ failure အတွက် တစ်ကြိမ်စီဝင်ကြောင်း စစ်ထားပါတယ်။

အရေးကြီးတဲ့ lab limitation တစ်ခုရှိပါတယ်။ ဒီ example က arguments ထဲက `path` ဟာ empty မဟုတ်တဲ့ string ဖြစ်ရမယ်လို့ Python code နည်းနည်းနဲ့စစ်ထားပါတယ်။ ဒီ `path` validation ဟာ fake `read` Tool တစ်ခုအတွက်ရေးထားတဲ့ teaching rule သာဖြစ်ပြီး Travis234 ရဲ့ general schema validator မဟုတ်ပါဘူး။ Production validation behavior အားလုံးကို ဒီ function တစ်ခုနဲ့ကိုယ်စားမပြုပါဘူး။ Network၊ provider၊ real filesystem နဲ့ production hooks တွေကိုလည်း lab ကမစမ်းပါဘူး။

## ၁၃.၉ Lewis ရဲ့မှတ်စု

- “Tool မအောင်ဘူး” ဆိုတာနဲ့မရပ်ဘဲ body မစခင်လား၊ စပြီးနောက်လား အရင်မေးမယ်။
- Unknown၊ invalid နဲ့ blocked က immediate outcomes ဖြစ်လို့ after hook မဝင်ဘူး။
- Invoked success နဲ့ invoked failure နှစ်မျိုးလုံး after hook တစ်ကြိမ်ဝင်တယ်။
- Error Tool Result က model ကို recovery လုပ်ခွင့်ပေးပေမယ့် safe retry ကိုအလိုအလျောက်အာမခံမပေးဘူး။
- Lab ရဲ့ `path` rule ကို production schema system တစ်ခုလုံးလို့ မယူဆဘူး။

## ၁၃.၁၀ အနှစ်ချုပ်

- Tool lifecycle ကို Prepare → Execute → Finalize လို့ခွဲရင် failure ဘယ် boundary မှာဖြစ်သလဲ မြင်နိုင်တယ်။
- Unknown Tool၊ invalid arguments နဲ့ before-hook block မှာ body မ run ဘဲ immediate error outcome ပြန်တယ်။
- Valid Tool body က `RuntimeError("disk unavailable")` တက်ရင် invoked failure ဖြစ်တယ်။
- Immediate outcomes က after hook ကိုမခေါ်ဘဲ invoked success/failure က တစ်ကြိမ်ခေါ်တယ်။
- Model-facing error Tool Result shape နဲ့ Runtime ရဲ့ invocation history ကို မရောသင့်ဘူး။
- Offline lab က boundary ကို deterministic စမ်းပေးပေမယ့် production schema validation၊ filesystem နဲ့ provider behavior ကို မဖုံးပါဘူး။

## ၁၃.၁၁ Source Notes

- Executable teaching model: [`examples/lewis_tool_outcomes.py`](../../examples/lewis_tool_outcomes.py)
- Focused executable tests: [`tests/test_lewis_workshop.py`](../../tests/test_lewis_workshop.py) ထဲက `ToolOutcomeTests`
- `C-HOOK-BOUNDARY` — `T-LOOP`, `pi.loop.immediate_outcome_hook_boundary`, `pi.loop.invoked_failure_after_hook_once`; immediate outcomes က after hook ကိုကျော်ပြီး invoked failure က တစ်ကြိမ်ခေါ်တဲ့ boundary
- Runtime message နဲ့ Tool contracts: `T-TYPES`
- Pi revision: `1f0dbc008c9b3e88017d42e8a1b46d416ad2b6b6`
- Travis234 revision: `68b1831691b8ec93f9550ce63b80cdcb7a591b2e`

Exact source links နဲ့ evidence boundary ကို [Pinned Source Map](../references/SOURCE_MAP.md) မှာ ကြည့်နိုင်ပါတယ်။ Claim ရဲ့ verification scope ကို [Technical Claim Ledger](../references/CLAIM_LEDGER.md) မှာဖတ်နိုင်ပါတယ်။ Lewis ရဲ့ incident နဲ့ dialogue က fictional ဖြစ်ပြီး pinned claims သို့မဟုတ် local test result အဖြစ် မယူရပါဘူး။

---

Previous: [Chapter 12 — Agent ကို လမ်းပြန်ညွှန်ရတဲ့အချိန်](12-steering-followup-cancellation.md)

Next: [Chapter 14 — ပြန်ဖွင့်လိုက်တော့ အလုပ်ဘယ်ကဆက်မလဲ](14-session-resume-after-restart.md)

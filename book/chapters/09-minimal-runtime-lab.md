# Chapter 09 — Minimal Runtime Lab

Agent Loop အကြောင်းဖတ်ပြီးသွားရင် flow ကို နားလည်သလိုထင်ပေမယ့် event ရှစ်ခုလောက်ကို ကိုယ်တိုင် trace လိုက်ကြည့်တဲ့အခါ မရှင်းသေးတဲ့နေရာတွေ ပေါ်လာတတ်ပါတယ်။ Model က Tool Call ထုတ်ပြီးနောက် Tool Result ဘယ်အချိန် context ထဲဝင်သလဲ။ Parallel tool က အရင်ပြီးသွားရင် result order ပြောင်းသွားသလား။ Model ကို ဘယ်အချိန်ပြန်ခေါ်သလဲ။

Production Travis234 ကို debugger နဲ့စဖတ်ရင် provider adapter၊ extension hooks၊ session persistence နဲ့ streaming events တွေပါ တစ်ပြိုင်နက်မြင်ရလို့ Agent Loop ရဲ့အရိုးစုကို လွတ်သွားနိုင်ပါတယ်။ ဒီအတွက် `examples/minimal_runtime.py` ဆိုတဲ့ offline teaching model တစ်ခုရေးထားပါတယ်။ API key မလိုပါဘူး။ Network မခေါ်ပါဘူး။ Fake model နဲ့ fake tools ပဲသုံးပါတယ်။

ဒီ lab ရဲ့ရည်ရွယ်ချက်က Travis234 အသစ်တစ်ခုထပ်ရေးဖို့ မဟုတ်ပါဘူး။ Chapter 02 နဲ့ Chapter 05 မှာရှင်းခဲ့တဲ့ model → tools → ordered results → model flow ကို လက်တွေ့ run ကြည့်ပြီး လေ့လာဖို့ပါ။

## ၉.၁ Lab က ဘာကိုပြသလဲ

Minimal Runtime မှာ concept လေးခုပဲထားပါတယ်။

1. Model call တစ်ကြိမ်စတိုင်း `assistant_start`၊ ပြီးတိုင်း `assistant_end` ထုတ်တယ်။
2. Parallel Tool Calls တွေကို worker limit အတွင်း run တယ်။
3. Tool bodies တကယ်ပြီးတဲ့ order ကွာနိုင်ပေမယ့် Tool Results ကို source order နဲ့ ပြန်ထည့်တယ်။
4. Model က Tool Call မရပ်ဘဲ ဆက်ထုတ်နေရင် iteration ceiling နဲ့ ရပ်တယ်။

Streaming text delta၊ hooks၊ argument schema validation၊ cancellation၊ persistent session နဲ့ real Compaction မပါပါဘူး။ အဲဒီအရာတွေကို ဖျောက်ထားတာ မပြည့်စုံလို့မဟုတ်ဘဲ ပထမဆုံးလေ့လာရမယ့် state transition ကို ရှင်းရှင်းမြင်ဖို့ပါ။

## ၉.၂ Data သုံးမျိုးကို အရင်သိမယ်

Runtime ထဲမှာ အဓိကဖြတ်သန်းမယ့် data ကို immutable dataclass သုံးမျိုးနဲ့ ဖော်ပြထားပါတယ်။

```python
@dataclass(frozen=True)
class ToolCall:
    id: str
    name: str
    arguments: dict[str, object]
    parallel: bool

@dataclass(frozen=True)
class AssistantTurn:
    text: str
    tool_calls: tuple[ToolCall, ...]

@dataclass(frozen=True)
class RuntimeEvent:
    kind: str
    detail: str
```

`ToolCall` က model တောင်းတဲ့အလုပ်ကို ကိုင်ထားပါတယ်။ `AssistantTurn` က model response တစ်ကြိမ်ရဲ့ text နဲ့ Tool Calls တွေကို တွဲထားပါတယ်။ `RuntimeEvent` က lab run ပြီးနောက် အစီအစဉ်ပြန်စစ်ဖို့ trace ဖြစ်ပါတယ်။

Dataclass ကို `frozen=True` ထားလို့ event ထုတ်ပြီးနောက် တခြား code က field ကို မတော်တဆပြန် assign မလုပ်နိုင်ပါဘူး။ Nested `arguments` dictionary ကို deep immutable လုပ်ပေးတာတော့ မဟုတ်ပါဘူး။ Production event system အပြည့်မဟုတ်ပေမယ့် “ထွက်ပြီးသား event က snapshot တစ်ခု” ဆိုတဲ့ mental model ကို ထိန်းပေးပါတယ်။

## ၉.၃ Fake Model က ဘယ်လိုအလုပ်လုပ်သလဲ

Real model တစ်ခုက messages ကိုဖတ်ပြီး text သို့မဟုတ် Tool Calls ပြန်ပေးပါတယ်။ Lab မှာ behavior ကို ကြိုသတ်မှတ်ထားတဲ့ async function တစ်ခုနဲ့ အစားထိုးပါတယ်။ ပထမခေါ်ချိန်မှာ `slow` နဲ့ `fast` tools နှစ်ခုတောင်းပြီး၊ ဒုတိယခေါ်ချိန်မှာ final text ပြန်ပေးပါတယ်။

```python
async def fake_model(messages):
    if first_call:
        return AssistantTurn(
            text="I will check both sources.",
            tool_calls=(slow_call, fast_call),
        )
    return AssistantTurn(
        text="Both results are ready.",
        tool_calls=(),
    )
```

Sample ကို ချုံ့ပြထားတာဖြစ်လို့ `first_call` state နဲ့ Tool Call တည်ဆောက်ပုံအပြည့် မပါပါဘူး။ အဓိကက ဒုတိယ model call မတိုင်ခင် tools နှစ်ခုရဲ့ results ကို messages ထဲပြန်ထည့်ပြီးသားဖြစ်ရမယ်ဆိုတာပါ။ Tool function ပြီးတာနဲ့ model က အလိုအလျောက်သိတာမဟုတ်ပါဘူး။ Updated messages နဲ့ model ကို ပြန်ခေါ်မှ သိပါတယ်။

## ၉.၄ Loop တစ်ကြိမ်ကို လက်တွေ့လေ့လာကြည့်ခြင်း

`run_agent_loop()` က user input ကို ပထမ message အဖြစ်ထည့်ပြီး iteration စပါတယ်။ Model မခေါ်ခင် `assistant_start` ထုတ်တယ်။ Response ရလာတာနဲ့ `assistant_end` ထုတ်ပြီး assistant message ကို history ထဲထည့်ပါတယ်။

Tool Calls မရှိရင် အဲဒီနေရာမှာ events ကိုပြန်ပေးပြီး loop ရပ်ပါတယ်။ Tool Calls ရှိရင် `tool_start` events တွေကို source order နဲ့အရင်ထုတ်ပြီး tool batch ကို run ပါတယ်။ Results ရလာတာနဲ့ `tool_end` ထုတ်ကာ Tool Result messages ကို history ထဲထည့်ပါတယ်။ ပြီးရင် နောက် iteration မှာ model ကို ထပ်ခေါ်ပါတယ်။

Flow ကို code မပါဘဲရေးရင်:

```text
user message
    ↓
assistant_start → model → assistant_end
    ↓
tool_start → execute → tool_end
    ↓
append Tool Results
    ↓
assistant_start → model → assistant_end
```

ဒီ trace မှာ Tool Result နဲ့ final assistant answer ကြား model call တစ်ကြိမ်ရှိတာကို သတိထားပါ။ Tool output ကို Python code ကရပြီးတာနဲ့ model က သိပြီးသားလို့ ယူဆလို့မရပါဘူး။

## ၉.၅ Parallel ဖြစ်ပေမယ့် Result Order မပြောင်းဘူး

Lab ရဲ့ `slow` tool က အချိန်ပိုစောင့်ပြီး `fast` tool က ချက်ချင်းနီးပါးပြီးပါတယ်။ တကယ့် completion order က `fast`၊ `slow` ဖြစ်ပါတယ်။ ဒါပေမယ့် model က Tool Calls ကို `slow`၊ `fast` လို့ထုတ်ထားတာကြောင့် Tool Results ကို အဲဒီ source order နဲ့ ပြန်တည်ဆောက်ပါတယ်။

ဒီ behavior ရဲ့အဓိက code ကိုကြည့်ရင်:

```python
semaphore = asyncio.Semaphore(max_parallel_tools)

async def invoke(call):
    async with semaphore:
        return await tools[call.name](call.arguments)

results = await asyncio.gather(
    *(invoke(call) for call in turn.tool_calls)
)

for call, result in zip(turn.tool_calls, results, strict=True):
    append_tool_result(call, result)
```

`Semaphore` က တစ်ချိန်တည်း tool body ဘယ်နှခုဝင်ခွင့်ရှိသလဲကို ထိန်းပါတယ်။ `asyncio.gather()` က tasks တွေကို concurrent run ပေမယ့် returned results ကို input awaitables အစီအစဉ်အတိုင်း စီပေးပါတယ်။ ဒါကြောင့် second loop က `turn.tool_calls` နဲ့ `results` ကို တစ်တွဲချင်း source order အတိုင်း ပြန်ပေါင်းနိုင်ပါတယ်။

Tool Call တစ်ခုခုက `parallel=False` ဖြစ်ရင် lab က batch တစ်ခုလုံးကို sequential run ပါတယ်။ Production Travis234 ရဲ့ batch-level sequential rule ကို ရိုးရှင်းစွာ ထိန်းထားတာပါ။

Test က order နှစ်မျိုးကို သီးခြားစစ်ပါတယ်။ Tool bodies တကယ်ပြီးတဲ့ list က `fast`, `slow` ဖြစ်ရပြီး `tool_end` result details က `slow:slow-result`, `fast:fast-result` ဖြစ်ရပါတယ်။ အလုပ်ပြီးချိန်နဲ့ context ပြန်စီချိန် မတူနိုင်ကြောင်း code နဲ့မြင်နိုင်ပါတယ်။

## ၉.၆ Worker Limit ကို ကိုယ်တိုင်ပြောင်းကြည့်ခြင်း

Test တစ်ခုမှာ parallel Tool Calls ငါးခုထုတ်ပြီး `max_parallel_tools=2` လို့ထားပါတယ်။ Tool body ဝင်တိုင်း active counter တိုးပြီးထွက်တိုင်းလျှော့ပါတယ်။ Run တစ်လျှောက် အမြင့်ဆုံး active count က နှစ်ခုပဲ ဖြစ်ရပါတယ်။

ဒီ test က runtime မြန်တယ်ဆိုတာမစစ်ပါဘူး။ Limit တကယ်ထိန်းထားသလား စစ်တာပါ။ Tool တစ်ခုချင်းရဲ့ sleep time ကိုပြောင်းလည်း peak က နှစ်ခုမကျော်သင့်ပါဘူး။

`max_parallel_tools` ကို ၁ ပြောင်းပြီး test ကို စမ်းကြည့်နိုင်ပါတယ်။ Parallel flag တွေ `True` ဖြစ်နေလည်း semaphore တစ်ခုပဲခွင့်ပြုလို့ လက်တွေ့မှာ sequential လိုဖြစ်သွားပါမယ်။ Flag က eligibility ကိုပြောပြီး worker limit က capacity ကိုပြောတာဖြစ်ပါတယ်။

Limit က capacity ဖြစ်တာကြောင့် သုည သို့မဟုတ် အနုတ်က valid configuration မဟုတ်ပါဘူး။ Lab က `max_parallel_tools <= 0` ကို `ValueError("max_parallel_tools must be greater than zero")` နဲ့ ချက်ချင်းငြင်းပါတယ်။ သုညပါတဲ့ semaphore မှာ Tool batch အဆုံးမရှိစောင့်မနေစေဖို့ configuration boundary မှာစစ်ထားတာပါ။

## ၉.၇ Failure နှစ်မျိုးကို မဖျောက်ထားဘူး

Model က registry ထဲမရှိတဲ့ tool name ထုတ်ရင် lab က `KeyError("unknown tool: missing")` ပြန်ပါတယ်။ Production Runtime မှာ unknown tool ကို error Tool Result ပြောင်းပြီး model ဆီပြန်ပေးနိုင်ပေမယ့် ဒီ lab က failure boundary ကို မြင်သာစေဖို့ exception နဲ့ရပ်ထားပါတယ်။ ဒါကြောင့် sample behavior ကို Travis234 အပြည့်အစုံနဲ့ မရောသင့်ပါဘူး။

Model က iteration တိုင်း Tool Call ဆက်ထုတ်နေရင် loop က ဘယ်တော့မှ final text မရနိုင်ပါဘူး။ `max_iterations` ပြည့်တာနဲ့ `RuntimeError("iteration limit reached")` ထုတ်ပါတယ်။ Ceiling က bug ကိုဖြေရှင်းပေးတာမဟုတ်ပေမယ့် runaway loop ကို bounded failure အဖြစ်ပြောင်းပေးပါတယ်။

## ၉.၈ Lab ကို Run ကြည့်ခြင်း

Repository root ကနေ ဒီ command ကို run ပါ။

```bash
python3.13 examples/minimal_runtime.py
```

Event kinds ကိုပဲယူကြည့်ရင် အစီအစဉ်က:

```text
assistant_start
assistant_end
tool_start
tool_start
tool_end
tool_end
assistant_start
assistant_end
```

Output အပြည့်မှာ `tool_end` details ကို `slow` ပြီးမှ `fast` လို့မြင်ရပါမယ်။ ဒါက slow tool တကယ်အရင်ပြီးတာမဟုတ်ပါဘူး။ Model context အတွက် source-ordered result trace ကို ပြထားတာပါ။ Lab ထဲက `tool_end` ကို Travis234 production runtime ရဲ့ real-time `tool_execution_end` event နဲ့ အတူတူလို့ မယူရပါဘူး။ တကယ့် completion order ပြောင်းသွားတာကို test ထဲက သီးခြား counter နဲ့ အတည်ပြုထားပါတယ်။

Tests ကို run ဖို့:

```bash
python3.13 -m unittest tests.test_minimal_runtime -v
```

Test ငါးခုက source-ordered results၊ worker limit၊ invalid worker limit၊ unknown tool error နဲ့ iteration ceiling ကို စစ်ပါတယ်။ Network နဲ့ API key မလိုပါဘူး။

## ၉.၉ Compaction ကို ဘယ်နေရာထည့်မလဲ

ဒီ lab ထဲ real Compaction မထည့်ထားပါဘူး။ ထည့်မယ်ဆိုရင် model မခေါ်ခင် messages ကိုပြောင်းပေးတဲ့ preflight boundary နဲ့ completed turn အပြီး usage စစ်တဲ့ post-response boundary လိုပါတယ်။ Chapter 08 မှာ လေ့လာခဲ့တဲ့ lifecycle ကို ဒီ loop ပေါ်တင်ကြည့်ရင် ဘယ်နေရာဝင်မလဲ စိတ်ထဲပေါ်လာရပါမယ်။

Compaction code ကို lab ထဲထပ်ရေးလိုက်ရင် summary prompt၊ token policy၊ persistence နဲ့ recovery behavior တွေပါလာပြီး Agent Loop ရဲ့အရိုးစု ပြန်ရှုပ်သွားပါမယ်။ ဒါကြောင့် executable example က loop နဲ့ bounded tools ကိုပဲ တာဝန်ယူပြီး real compaction behavior ကို Travis234 source ဆီ ပြန်ညွှန်ပါတယ်။

## ၉.၁၀ Travis234 က ဘာတွေထပ်ဖြည့်ထားသလဲ

Minimal Lab ကို production substitute အဖြစ်မသုံးသင့်တဲ့အကြောင်းကို exact boundary နဲ့ကြည့်ရင် ပိုရှင်းပါတယ်။

| Minimal Lab | Travis234 |
|---|---|
| Assistant start/end ပဲ | Text၊ thinking နဲ့ Tool Call streaming deltas ပါတဲ့ event lifecycle |
| Tool name lookup ပဲ | Argument schema validation နဲ့ structured error Tool Results |
| Before/after policy မရှိ | Before/after Tool Call hooks နဲ့ extension lifecycle |
| Semaphore limit ပဲ | Bounded executor၊ batch policy နဲ့ richer completion events |
| Cancellation မရှိ | Cooperative abort signal နဲ့ stream/tool cancellation boundaries |
| In-memory messages ပဲ | Persistent session tree၊ Compaction entries နဲ့ resume behavior |
| Real Compaction မရှိ | Preflight၊ post-response၊ overflow နဲ့ manual Compaction |

Table ရဲ့ဘယ်ဘက်က မကောင်းတဲ့ implementation လို့ မဆိုလိုပါဘူး။ သင်ခန်းစာတစ်ခုကို concept တစ်ခုချင်းမြင်ရအောင် အလွှာတွေဖြုတ်ထားတာပါ။ Production code ဖတ်တဲ့အခါ ဘယ်အလွှာကို ဘာကြောင့်ပြန်ထည့်ထားသလဲ ဆက်မေးနိုင်ဖို့ ဒီ lab ကို သုံးရပါတယ်။

## ၉.၁၁ အနှစ်ချုပ်

- Offline fake model နဲ့ fake tools သုံးလို့ API key မလိုဘဲ Agent Loop ကို trace လုပ်နိုင်တယ်။
- Assistant boundary၊ Tool execution နဲ့ နောက် model call အစီအစဉ်ကို event ရှစ်ခုနဲ့ မြင်နိုင်တယ်။
- `asyncio.Semaphore` က parallel tool capacity ကိုကန့်သတ်တယ်။
- Tool completion order ပြောင်းနိုင်ပေမယ့် `asyncio.gather()` result list နဲ့ source order ကို ဆက်ထိန်းနိုင်တယ်။
- Unknown tool နဲ့ endless loop ကို bounded၊ testable failures အဖြစ်ထားတယ်။
- Lab က Pi-style loop အရိုးစုကို သင်ဖို့ဖြစ်ပြီး Travis234 ရဲ့ streaming၊ hooks၊ persistence နဲ့ Hermes-style Compaction ကို အစားမထိုးဘူး။

## ၉.၁၂ Source Notes

- Executable teaching model: [`examples/minimal_runtime.py`](../../examples/minimal_runtime.py)
- Executable tests: [`tests/test_minimal_runtime.py`](../../tests/test_minimal_runtime.py)
- `C-RESULT-ORDER` — `T-LOOP`, `pi.loop.parallel_result_source_order`
- `C-BOUND` — `T-TOOLS`, `T-LOOP`, `pi.loop.bounded_parallelism`
- Pi revision: `1f0dbc008c9b3e88017d42e8a1b46d416ad2b6b6`
- Travis234 revision: `68b1831691b8ec93f9550ce63b80cdcb7a591b2e`

Exact source links နဲ့ evidence boundary ကို [Pinned Source Map](../references/SOURCE_MAP.md) မှာ ကြည့်နိုင်ပါတယ်။

---

Previous: [Chapter 08 — Pi နဲ့ Hermes တွေ့ဆုံရာ](08-pi-meets-hermes.md)

Next: [Chapter 10 — Parity, Divergence နှင့် သင်ခန်းစာများ](10-parity-divergence-lessons.md)

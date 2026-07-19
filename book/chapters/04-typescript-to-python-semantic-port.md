# Chapter 04 — TypeScript ကနေ Python သို့ Semantic Port

TypeScript code တစ်ခုကို Python ပြောင်းမယ်ဆိုရင် `{}` ကို indentation ပြောင်း၊ `Promise` ကို coroutine ပြောင်းပြီး ပြီးသွားမယ်လို့ ထင်ရလွယ်ပါတယ်။ Function နှစ်ခုက input တူတယ်၊ output တူတယ်ဆိုရင် port အောင်မြင်ပြီလို့လည်း ယူဆမိနိုင်ပါတယ်။

Agent Runtime မှာတော့ ဒီလောက်နဲ့ မလုံလောက်ပါဘူး။ Event တစ်ခု စောထွက်သွားတာ၊ exception တစ်ခု မှားတဲ့ boundary ကနေထွက်လာတာ၊ abort ဖြစ်ပြီးနောက် model ကို ထပ်ခေါ်မိတာတွေက output အဆုံးမှာတူနေရင်တောင် runtime behavior ကို ပြောင်းသွားစေပါတယ်။ Port လုပ်ရာမှာ syntax ထက် semantics ကို အရင်ထိန်းရတာ ဒီအကြောင်းကြောင့်ပါ။

## ၄.၁ Port ဆိုတာ ဘာသာပြန်တာမဟုတ်ဘူး

စာရွက်စာတမ်းတစ်ခုကို ဘာသာပြန်ရင် စာလုံးပြောင်းပေမယ့် အဓိပ္ပာယ်မပျောက်အောင် ထိန်းရပါတယ်။ Software port လည်း ဒီသဘောနဲ့တူပါတယ်။ TypeScript ရဲ့ language feature တစ်ခုချင်းကို Python feature တစ်ခုနဲ့ အတင်းတွဲစရာမလိုပါဘူး။ ပြင်ပကမြင်ရတဲ့ behavior ကို မပျက်အောင် ထိန်းရမှာပါ။

Agent Loop အတွက် ထိန်းထားရမယ့် behavior တွေက:

- user message နဲ့ assistant message event order
- Tool Call ပြီးရင် model ကို ဆက်ခေါ်ခြင်း
- Tool Results ကို source order နဲ့ ပြန်ထည့်ခြင်း
- steering နဲ့ follow-up queue drain points
- error၊ abort နဲ့ termination boundaries
- hook တစ်ခုကို ဘယ်အချိန် ဘယ်နှကြိမ်ခေါ်သလဲ

ဒါတွေကို invariant လို့ ခေါ်နိုင်ပါတယ်။ Invariant ဆိုတာ implementation ဘယ်လိုပြောင်းပြောင်း မပျက်သင့်တဲ့အချက်ပါ။ TypeScript ကနေ Python ပြောင်းရာမှာ အရင်ဆုံး ဒီစာရင်းကို ထုတ်ထားမှ code တူပေမယ့် behavior လွဲတာကို ဖမ်းနိုင်ပါတယ်။

## ၄.၂ `Promise` ကနေ coroutine သို့

TypeScript နဲ့ Python နှစ်ခုလုံးမှာ `await` ဆိုတဲ့စာလုံးကို တွေ့ရပါတယ်။ ဒါပေမယ့် runtime model က တူတာမဟုတ်ပါဘူး။ JavaScript က Promise နဲ့ event loop ပေါ်မှာ အလုပ်လုပ်ပြီး Python က coroutine နဲ့ `asyncio` event loop ကို သုံးပါတယ်။

အောက်က code က loop boundary တစ်ခုကို ချုံ့ထားတဲ့ teaching comparison ဖြစ်ပါတယ်။

```typescript
await emit({ type: "turn_start" });
const message = await streamAssistantResponse(context, config);
const results = await executeToolCalls(context, message, config);
```

```python
await _emit_event(emit, TurnStartEvent())
message = await _stream_assistant_response(context, config, signal, emit, stream_fn)
results = await _execute_tool_calls(context, message, config, signal, emit)
```

စာကြောင်းပုံစံဆင်တူနေပေမယ့် အရေးကြီးတာက `await` သုံးထားတာမဟုတ်ပါဘူး။ `turn_start` ပြီးမှ stream စရမယ်၊ assistant message အပြီးမှ tools execute လုပ်ရမယ်ဆိုတဲ့ order ကို ထိန်းထားတာပါ။ Python version မှာ function name နဲ့ argument shape ပြောင်းနိုင်ပေမယ့် ဒီအစီအစဉ် ပြောင်းလို့မရပါဘူး။

Travis234 မှာ hook တချို့က sync function ဖြစ်နိုင်သလို async function လည်း ဖြစ်နိုင်ပါတယ်။ `resolve()` helper က return value ဟာ awaitable ဖြစ်ရင် `await` လုပ်ပြီး သာမန် value ဆိုရင် တိုက်ရိုက်ပြန်ပေးပါတယ်။ ဒီလိုလုပ်ထားလို့ extension ရေးသူကို async တစ်မျိုးတည်းသုံးခိုင်းစရာမလိုဘဲ loop အတွင်းမှာ result တစ်မျိုးတည်းလို ဆက်ကိုင်နိုင်ပါတယ်။

## ၄.၃ Interface ကနေ dataclass သို့

TypeScript မှာ message၊ event နဲ့ configuration shape တွေကို interface နဲ့ type alias သုံးပြီး ဖော်ပြပါတယ်။ Python မှာ Travis234 က dataclass တွေကို အဓိကသုံးထားပါတယ်။

ဥပမာ Tool Execution စတင်တဲ့ event ကို ချုံ့ကြည့်ရင်:

```python
@dataclass
class ToolExecutionStartEvent:
    tool_call_id: str
    tool_name: str
    args: Any
    type: Literal["tool_execution_start"] = "tool_execution_start"
```

ဒီ dataclass က data ထည့်ထားတဲ့ container လို့ပဲ မမြင်သင့်ပါဘူး။ Event consumer က `type` ကိုကြည့်ပြီး event အမျိုးအစားခွဲနိုင်တယ်။ `tool_call_id` နဲ့ start၊ update၊ end events တွေကို ပြန်ချိတ်နိုင်တယ်။ `args` က execution စတင်ချိန်မှာ runtime မြင်ခဲ့တဲ့ arguments ကို ပြတယ်။

Python က compile-time interface enforcement ကို TypeScript လို တစ်ပုံစံတည်းမပေးပါဘူး။ ဒါကြောင့် dataclass အမည်တူနေရုံနဲ့ contract တူပြီလို့ မဆိုနိုင်ပါဘူး။ Field name၊ default value၊ event `type` နဲ့ consumer မြင်ရတဲ့ serialization shape တွေကို test နဲ့ ထိန်းရပါတယ်။

`AgentTool` dataclass မှာတော့ object တည်ဆောက်ချိန် `__post_init__()` က tool schema ကို compile လုပ်ပါတယ်။ Schema မှားနေရင် Tool Call ရောက်လာတဲ့အထိ စောင့်မနေဘဲ tool registration boundary မှာ fail စေပါတယ်။ Python adaptation က data shape တစ်ခုတည်းမဟုတ်ဘဲ validation timing ကိုပါ ရွေးချယ်ထားတာပါ။

## ၄.၄ Stream ကို async iterator နဲ့ ဖတ်ခြင်း

Assistant response က တစ်ခါတည်းရလာတဲ့ string မဟုတ်ပါဘူး။ Start၊ text delta၊ thinking delta၊ Tool Call delta နဲ့ done/error events တွေအဖြစ် တဖြည်းဖြည်းရောက်လာနိုင်ပါတယ်။ Python loop က response ကို async iterator အဖြစ်ဖတ်ပါတယ်။

```python
async for event in _iter_response_events(response, signal):
    if event.type == "start":
        start_partial_message(event.partial)
    elif event.type in UPDATE_EVENT_TYPES:
        update_partial_message(event.partial)
    elif event.type in ("done", "error"):
        return await finalize_message(response)
```

ဒါက production code ကို ချုံ့ပြထားတဲ့ teaching version ပါ။ Reader အနေနဲ့ `async for` syntax ကို မှတ်ထားဖို့ထက် partial message ရဲ့ state ပြောင်းပုံကို ကြည့်သင့်ပါတယ်။ Start event မှာ context ထဲစဝင်တယ်။ Delta တစ်ခုရတိုင်း နောက်ဆုံး snapshot ကိုအစားထိုးတယ်။ Done boundary မှာ final message အဖြစ်ပိတ်တယ်။

Adapter က async iterator မဟုတ်တဲ့ stream-like object တစ်ခု ပြန်ပေးနိုင်တဲ့ path ကိုလည်း `_iter_response_events()` က ကိုင်ထားပါတယ်။ Python ecosystem ထဲက provider shape မတူတာတွေကို loop core ဆီမပို့ဘဲ adapter boundary မှာ normalize လုပ်ထားတာဖြစ်ပါတယ်။

## ၄.၅ `AbortSignal` ကို Python မှာ ဘယ်လိုယူထားသလဲ

Pi ဘက်မှာ DOM `AbortSignal` ကို သုံးနိုင်ပါတယ်။ Python standard library မှာ အတိအကျတူတဲ့ object မရှိပါဘူး။ Travis234 က `threading.Event` နဲ့ callback registry သုံးထားတဲ့ minimal `AbortSignal` တစ်ခုတည်ဆောက်ထားပါတယ်။

```python
signal = AbortSignal()

if signal.aborted:
    return

unsubscribe = signal.add_callback(close_stream)
```

`abort()` ကိုခေါ်ရင် internal event ကို set လုပ်ပြီး register လုပ်ထားတဲ့ callbacks တွေကို တစ်ကြိမ်ခေါ်ပါတယ်။ နောက်မှ callback ထည့်တဲ့အချိန် signal က aborted ဖြစ်ပြီးသားဆိုရင် callback ကို ချက်ချင်းခေါ်ပါတယ်။ ဒီ behavior ကြောင့် race တစ်ခုအတွင်း callback ပျောက်သွားတာကို လျှော့နိုင်ပါတယ်။

ဒါပေမယ့် abort က thread ကို အတင်းသတ်ပစ်တာမဟုတ်ပါဘူး။ Tool body နဲ့ provider stream က signal ကိုပူးပေါင်းစစ်ပြီး ရပ်ရတာပါ။ Cooperative cancellation ဖြစ်တဲ့အတွက် signal ပေးလိုက်တာနဲ့ running sync tool ချက်ချင်းရပ်မယ်လို့ မယူဆသင့်ပါဘူး။

## ၄.၆ Sync API နဲ့ async API နှစ်ခုထားရတဲ့အကြောင်း

Python script သေးသေးတစ်ခုက Agent Loop ကိုခေါ်ချင်ရင် `asyncio` setup အပြည့်ရေးစရာမလိုအောင် `run_agent_loop()` ဆိုတဲ့ sync entry ရှိပါတယ်။ အတွင်းမှာတော့ canonical runtime ဖြစ်တဲ့ `run_agent_loop_async()` ကိုပဲ ခေါ်ပါတယ်။

```python
def run_agent_loop(...):
    return run_sync(run_agent_loop_async(...))
```

အပြင်မှာ running event loop မရှိရင် `run_sync()` က `asyncio.run()` နဲ့ coroutine ကို မောင်းပေးတယ်။ Running event loop ရှိပြီးသားဆိုရင် nested loop တည်ဆောက်ဖို့မကြိုးစားဘဲ async API ကိုသုံးဖို့ error ပြန်ပေးပါတယ်။ Notebook၊ web server နဲ့ async application ထဲမှာ sync wrapper ကိုမှားခေါ်မိတာကို ဒီ boundary က တားပေးပါတယ်။

Sync နဲ့ async implementation နှစ်ခု သီးခြားရေးထားတာမဟုတ်တာလည်း အရေးကြီးပါတယ်။ Runtime logic တစ်ခုတည်းရှိပြီး sync entry က bridge အဖြစ်ပဲရှိလို့ behavior နှစ်မျိုးကွဲသွားမယ့်အန္တရာယ် နည်းပါတယ်။

## ၄.၇ Pythonic `AgentHarness`

Port လုပ်တယ်ဆိုတာ public API အမည်တိုင်းကို upstream အတိုင်း ကူးရမယ်လို့ မဆိုလိုပါဘူး။ Travis234 ရဲ့ `AgentHarness` က Python async context manager အဖြစ် သုံးနိုင်ပြီး `prompt()`၊ `continue_agent()`၊ `compact()` နဲ့ session operations တွေကို coroutine အဖြစ်ပေးထားပါတယ်။

```python
async with AgentHarness.create(config) as harness:
    answer = await harness.prompt("ဒီ project ကို ရှင်းပြပါ")
```

ဒီ sample က usage shape ကိုပဲ ပြထားတာဖြစ်ပြီး model configuration details မပါသေးပါဘူး။ Harness က production `CodingApp` နဲ့ `AgentSession` owners တွေကို ပြန်သုံးထားတယ်။ Operation တစ်ခုချင်းကို async lock နဲ့ serialize လုပ်ပြီး synchronous owner call ကို `asyncio.to_thread()` နဲ့ မောင်းပါတယ်။

ဒါကြောင့် parity manifest မှာ ဒီ API ကို intentional divergence လို့ မှတ်ထားပါတယ်။ TypeScript class signature ကို မကူးဘဲ Python developer သုံးရသဘာဝကျတဲ့ async facade တစ်ခုလုပ်ထားတာပါ။ အရေးကြီးတာက session tree၊ clone၊ rename နဲ့ runtime owner behavior တွေကို facade က အသစ်ပြန်တီထွင်မနေဘဲ ရှိပြီးသား owners ဆီ delegate လုပ်တာဖြစ်ပါတယ်။

## ၄.၈ မှားလွယ်တဲ့နေရာများ

### `await` ပါရုံနဲ့ semantics တူပြီထင်ခြင်း

Coroutine အကုန် `await` လုပ်ထားပေမယ့် event အရင်နောက်မှားနေရင် port မမှန်ပါဘူး။ Order ကို test trace နဲ့စစ်ရပါတယ်။

### Exception ကို အလွယ်တကူမျိုချခြင်း

Provider failure၊ hook failure နဲ့ tool failure တို့ရဲ့ boundary မတူပါဘူး။ Error အားလုံးကို generic result တစ်ခုအဖြစ် ပြောင်းလိုက်ရင် normal `message_end`/`turn_end` sequence နဲ့ recovery policy ပျက်နိုင်ပါတယ်။

### Sync wrapper ကို running loop ထဲခေါ်ခြင်း

Event loop တစ်ခုအတွင်း `asyncio.run()` ထပ်ခေါ်လို့မရပါဘူး။ Async application ထဲမှာ canonical async API ကိုပဲသုံးရပါတယ်။

### Abort ကို force-stop လို့ယူဆခြင်း

Abort signal က cooperation တောင်းတာပါ။ Blocking tool က signal ကိုမစစ်ရင် အလုပ်ပြီးတဲ့အထိ ဆက်ပြေးနိုင်ပါတယ်။

## ၄.၉ အနှစ်ချုပ်

- Semantic porting က syntax ကိုကူးတာမဟုတ်ဘဲ observable behavior ကို ထိန်းတာဖြစ်တယ်။
- Promise ကို coroutine ပြောင်းရာမှာ `await` စာလုံးထက် event နဲ့ state order က ပိုအရေးကြီးတယ်။
- Dataclass က interface အစားထိုးအမည်တစ်ခုသာမဟုတ်ဘဲ runtime data contract ဖြစ်တယ်။
- Async iteration က partial assistant message ကို final message ဖြစ်လာအောင် အဆင့်ဆင့်ထိန်းပေးတယ်။
- Python `AbortSignal` က cooperative cancellation ပေးပေမယ့် running thread ကို force-stop မလုပ်ဘူး။
- Pythonic `AgentHarness` က intentional API divergence ဖြစ်ပေမယ့် production owners ကို delegate လုပ်ပြီး behavior ကို ဆက်ထိန်းထားတယ်။

## ၄.၁၀ Source Notes

- `C-SEMANTIC-PORT` — `P-LOOP`, `P-TYPES`, `T-LOOP`, `T-TYPES`, `T-ASYNC`
- `C-HARNESS` — `P-HARNESS`, `T-HARNESS`, `pi.sdk.agent_harness`
- Pi revision: `1f0dbc008c9b3e88017d42e8a1b46d416ad2b6b6`
- Travis234 revision: `68b1831691b8ec93f9550ce63b80cdcb7a591b2e`

Exact links ကို [Pinned Source Map](../references/SOURCE_MAP.md) မှာ ကြည့်နိုင်ပါတယ်။

---

Previous: [Chapter 03 — Agent Runtime Loop ကို အစအဆုံးဖတ်ခြင်း](03-agent-runtime-loop-walkthrough.md)

Next: [Chapter 05 — Tool Execution နှင့် Bounded Concurrency](05-tool-execution-bounded-concurrency.md)

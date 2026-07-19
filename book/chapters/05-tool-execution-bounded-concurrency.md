# Chapter 05 — Tool Execution နှင့် Bounded Concurrency

Model က file သုံးဖိုင်ကို တစ်ပြိုင်နက်ဖတ်ခိုင်းလိုက်တယ်ဆိုပါစို့။ ပထမ file ကကြီးလို့ နှေးနေပြီး ဒုတိယနဲ့ တတိယ file က ချက်ချင်းပြီးသွားနိုင်ပါတယ်။ အားလုံးကို တစ်ခုချင်းစောင့်ဖတ်ရင် အချိန်ပိုကုန်မယ်။ တစ်ပြိုင်နက် run လိုက်ရင် မြန်မယ်။ ဒါပေမယ့် ဘယ်နှခုအထိ run ခွင့်ပေးမလဲ၊ result ကို ဘယ်အစီအစဉ်နဲ့ model ဆီပြန်ပို့မလဲဆိုတဲ့ မေးခွန်းတွေ ပေါ်လာပါတယ်။

Parallelism က “ပိုမြန်တယ်” ဆိုတဲ့ feature တစ်ခုတည်းမဟုတ်ပါဘူး။ Resource limit၊ mutation safety နဲ့ deterministic context order တွေကို တွဲစဉ်းစားရတဲ့ policy ဖြစ်ပါတယ်။

## ၅.၁ Sequential နဲ့ Parallel ဘာကွာသလဲ

Sequential mode မှာ Tool Call တစ်ခုကို prepare၊ execute၊ finalize လုပ်ပြီးမှ နောက်တစ်ခုကို စပါတယ်။ Tool A ကပြီးမှ Tool B စမယ်။ Order ရှင်းပြီး shared state ကိုပြောင်းတဲ့ tool တွေအတွက် စဉ်းစားရလွယ်ပါတယ်။ ဒါပေမယ့် independent read-only tools များလာရင် စောင့်ရတဲ့အချိန်တွေ စုပေါင်းသွားပါတယ်။

Parallel mode မှာ Tool Calls တွေကို အရင်စစ်ပြီး run ခွင့်ရတဲ့ tool bodies ကို တစ်ပြိုင်နက် execute လုပ်နိုင်ပါတယ်။ File သုံးဖိုင်ဖတ်တာ၊ search query အများကြီးလုပ်တာလို independent work တွေအတွက် အချိန်သက်သာနိုင်ပါတယ်။

ဒါပေမယ့် model က Tool Call ဆယ်ခုထုတ်လိုက်တာနဲ့ ဆယ်ခုလုံးကို မစဉ်းစားဘဲ run ခွင့်ပေးတာကို parallelism ကောင်းတယ်လို့ မခေါ်နိုင်ပါဘူး။ Database connection၊ file descriptor၊ CPU thread နဲ့ external API quota တွေက အကန့်အသတ်ရှိပါတယ်။ Parallel ဖြစ်ရမယ့်အပြင် bounded လည်း ဖြစ်ရပါတယ်။

## ၅.၂ Tool မ run ခင် ဘာတွေစစ်သလဲ

Tool Call ရလာတာနဲ့ body ကိုချက်ချင်းမခေါ်ပါဘူး။ Travis234 loop က call တစ်ခုချင်းကို preparation boundary ဖြတ်စေပါတယ်။

```python
tool = find_tool(tool_call.name)
prepared_call = await prepare_arguments(tool, tool_call)
validated_args = validate_tool_arguments(tool, prepared_call)
decision = await before_tool_call(context, validated_args)
```

ဒီ code က production flow ကို ချုံ့ထားတဲ့ teaching version ပါ။ ပထမဆုံး active tool catalog ထဲမှာ name ရှိမရှိစစ်တယ်။ Tool က argument preparation ပေးထားရင် raw arguments ကို ပြင်ဆင်တယ်။ ပြီးမှ compiled schema နဲ့ validate လုပ်တယ်။ နောက်ဆုံးမှာ before hook က policy အရ block လုပ်နိုင်ပါတယ်။

Unknown tool၊ invalid arguments နဲ့ before-hook block တွေမှာ tool body မ run ပါဘူး။ Runtime က error Tool Result တစ်ခုတည်ဆောက်ပြီး model ကို ပြန်ပေးပါတယ်။ ဒီလို outcome ကို immediate outcome လို့ မြင်နိုင်ပါတယ်။ Tool body မခေါ်ခဲ့တဲ့အတွက် after hook ကိုလည်း မခေါ်ပါဘူး။

တကယ် invoke လုပ်ထားတဲ့ tool က exception တက်ရင်တော့ failure result အဖြစ် finalize လုပ်ပြီး after hook ကို တစ်ကြိမ်ခေါ်ပါတယ်။ Policy hook က “run မလုပ်ခဲ့တာ” နဲ့ “run လုပ်ပြီး fail ဖြစ်တာ” ကို ခွဲသိနိုင်ဖို့ ဒီ boundary က အရေးကြီးပါတယ်။

## ၅.၃ Batch တစ်ခုလုံး Sequential ဖြစ်သွားနိုင်တဲ့အချိန်

Config မှာ `tool_execution = "sequential"` လို့ သတ်မှတ်ထားရင် call အားလုံးကို တစ်ခုချင်း run ပါမယ်။ Parallel mode ဖြစ်နေတောင် batch ထဲက tool တစ်ခုကို `execution_mode = "sequential"` လို့ mark လုပ်ထားရင် batch တစ်ခုလုံး sequential path သို့ပြောင်းပါတယ်။

ဘာကြောင့် tool တစ်ခုတည်းကိုပဲ sequential လုပ်ပြီး ကျန်တာ parallel မလုပ်သလဲလို့ မေးနိုင်ပါတယ်။ Batch ထဲမှာ order-sensitive tool တစ်ခုပါလာပြီဆိုရင် ကျန် calls တွေနဲ့ အပြိုင် run ခွင့်ပေးတာက အဲဒီ tool ရဲ့ safety intent ကို ပျက်စေနိုင်ပါတယ်။ Batch တစ်ခုလုံး sequential ပြောင်းတာက ပိုရှင်းပြီး ခန့်မှန်းရလွယ်တဲ့ rule ဖြစ်ပါတယ်။

ဒီနေရာမှာ low-level loop က tool name ကြည့်ပြီး mutation ဖြစ်မဖြစ် အလိုအလျောက်ဆုံးဖြတ်ပေးတာမဟုတ်ပါဘူး။ Tool owner က execution mode ကို မှန်မှန်သတ်မှတ်ရပါတယ်။ Write၊ edit နဲ့ shell tool တွေကို independent လို့ မှားသတ်မှတ်ရင် bounded concurrency ရှိနေလည်း race condition ဖြစ်နိုင်ပါတယ်။

## ၅.၄ Bounded Concurrency ကို ဘယ်လိုထိန်းသလဲ

လက်မှတ်ရောင်းတဲ့ကောင်တာမှာ လူတစ်ရာတန်းစီနေပေမယ့် counter လေးခုပဲ ဖွင့်ထားတယ်ဆိုပါစို့။ လူတစ်ရာလုံး တစ်ပြိုင်နက် counter ထဲဝင်တာမဟုတ်ပါဘူး။ တစ်ကြိမ်မှာ လေးယောက်ပဲ service ရပြီး တစ်ယောက်ပြီးမှ နောက်တစ်ယောက်ဝင်ပါတယ်။ Bounded Concurrency က ဒီသဘောပါပဲ။

Travis234 ရဲ့ `ToolCoordinator` ကို ချုံ့ကြည့်ရင်:

```python
class ToolCoordinator:
    def __init__(self, max_parallel_tools=8):
        self._semaphore = asyncio.Semaphore(max_parallel_tools)
        self._executor = ThreadPoolExecutor(max_workers=max_parallel_tools)

    async def execute(self, function, *args):
        async with self._semaphore:
            return await run_async_or_in_executor(function, *args)
```

ဒါက teaching version ဖြစ်ပါတယ်။ Semaphore က တစ်ပြိုင်နက်ဝင်နိုင်တဲ့ tool bodies အရေအတွက်ကို ထိန်းတယ်။ Async tool ဆိုရင် owner event loop ပေါ်မှာ await လုပ်ပြီး sync tool ဆိုရင် bounded `ThreadPoolExecutor` ထဲပို့ပါတယ်။ Pinned revision မှာ default limit က 8 ဖြစ်ပေမယ့် config ကနေ ပြောင်းနိုင်ပါတယ်။

Tool Calls 12 ခုနဲ့ limit 3 ထားတဲ့ parity test မှာ active tool အများဆုံး 3 ခုပဲရှိကြောင်း စစ်ထားပါတယ်။ Tool bodies က worker threads ပေါ်မှာ run နိုင်ပေမယ့် update events၊ end events နဲ့ after hooks ကို owner loop ဘက်မှာ ပြန်ထိန်းထားပါတယ်။ Policy နဲ့ event callbacks ကို worker thread အမျိုးမျိုးကနေ မတည်ငြိမ်စွာခေါ်တာကို ရှောင်ထားတာပါ။

Pi parity manifest မှာ bounded parallelism ကို intentional divergence လို့ မှတ်ထားပါတယ်။ Upstream behavior ကို ပျက်ကွက်ပြီးမတူတာမဟုတ်ဘဲ host concurrency ကို အကန့်အသတ်မရှိမဖွင့်ဖို့ ရည်ရွယ်ချက်ရှိရှိကွာထားတာဖြစ်ပါတယ်။

## ၅.၅ ပြီးတဲ့အစီအစဉ်နဲ့ Result ပြန်စီတဲ့အစီအစဉ်

Slow tool ကိုအရင်ခေါ်ပြီး fast tool ကိုနောက်မှခေါ်ထားတယ်ဆိုပါစို့။ Parallel run လိုက်ရင် fast tool က အရင်ပြီးပါမယ်။ UI မှာ fast tool ပြီးသွားတာကို ချက်ချင်းပြချင်တယ်။ Model context ထဲမှာတော့ Tool Calls မူလအစီအစဉ်အတိုင်း slow result၊ fast result လို့ ပြန်ထည့်ချင်တယ်။

ဒီလို order နှစ်မျိုးကို ခွဲထားပါတယ်။

| Order | ဘာကိုပြသလဲ |
|---|---|
| Source order | Model က Tool Calls ထုတ်ခဲ့တဲ့အစီအစဉ် |
| Start order | Coordinator ဆီ execution စတင်တင်ပို့တဲ့အစီအစဉ် |
| Completion order | Tool bodies တကယ်ပြီးသွားတဲ့အချိန်အစီအစဉ် |
| Result order | Context ထဲ Tool Result messages ပြန်ထည့်တဲ့အစီအစဉ် |

Parallel tasks တွေက finalize ဖြစ်တာနဲ့ `tool_execution_end` ထုတ်နိုင်လို့ completion event မှာ fast tool ကိုအရင်မြင်ရနိုင်ပါတယ်။ ဒါပေမယ့် tasks ကို source order နဲ့စုထားပြီး result messages တည်ဆောက်တဲ့အခါ အဲဒီ order အတိုင်းပြန်စီပါတယ်။

```text
Tool Calls:       slow, fast
Completion:       fast, slow
Tool End Events:  fast, slow
Result Messages:  slow, fast
```

ဒီလိုခွဲထားလို့ UI က လက်ရှိအခြေအနေကို အချိန်မီပြနိုင်ပြီး model က stable transcript ကိုရပါတယ်။ Event log ကိုကြည့်တဲ့အခါ end-event order နဲ့ context order တူမယ်လို့တော့ မယူဆသင့်ပါဘူး။

## ၅.၆ Hook နှစ်ခုရဲ့တာဝန်

`before_tool_call` က execution မစခင်ဝင်ပါတယ်။ Validated arguments နဲ့ လက်ရှိ context ကိုကြည့်ပြီး tool ကို block လုပ်နိုင်တယ်။ Permission၊ policy နဲ့ human approval လို gate တွေအတွက် သုံးနိုင်ပါတယ်။

`after_tool_call` က tool body invoke လုပ်ပြီး result ရလာတဲ့နောက် ဝင်ပါတယ်။ Result content၊ details၊ error flag နဲ့ terminate hint ကို field အလိုက်ပြင်နိုင်တယ်။ Tool exception တက်လို့ error result ဖြစ်နေရင်တောင် tool ကို တကယ်ခေါ်ခဲ့တာကြောင့် after hook ဝင်ပါတယ်။

ဒါပေမယ့် after hook ကို rollback လို့ မယူဆသင့်ပါဘူး။ Tool က file ရေးပြီးသွားမှ hook ဝင်တာဖြစ်လို့ mutation ကို အလိုအလျောက်ပြန်ဖျက်မပေးနိုင်ပါဘူး။ မလုပ်သင့်တဲ့ operation ကို တားဖို့ before hook နဲ့ tool-level permission boundary ကို သုံးရပါတယ်။

## ၅.၇ Cancellation ရဲ့ အကန့်အသတ်

Abort signal ရောက်လာရင် loop က နောက် model call မစဖို့နဲ့ stream ကိုပိတ်ဖို့ ကြိုးစားနိုင်ပါတယ်။ Tool ကိုလည်း signal ပေးထားပါတယ်။ Async tool က signal ကိုစစ်ပြီး coroutine ကို ရပ်နိုင်သလို sync tool ကလည်း signal ကိုပူးပေါင်းစစ်ရပါတယ်။

ThreadPoolExecutor ထဲဝင်ပြီးသား blocking function ကို Python က လုံခြုံစွာ force-kill မလုပ်ပေးနိုင်ပါဘူး။ ဒါကြောင့် abort ခေါ်လိုက်တာနဲ့ sync tool body ချက်ချင်းပျောက်သွားမယ်လို့ မယူဆသင့်ပါဘူး။ Long-running tool တစ်ခုက signal ကိုအဆင့်ဆင့်စစ်ခြင်း၊ subprocess ကို terminate လုပ်နိုင်တဲ့ ownership ရှိခြင်းနဲ့ timeout သတ်မှတ်ခြင်းတို့ လိုပါတယ်။

Bounded concurrency က တစ်ပြိုင်နက်အလုပ်အရေအတွက်ကို ထိန်းပေမယ့် cancellation ပြီးပြည့်စုံအောင် မလုပ်ပေးပါဘူး။ Resource control နဲ့ cancellation က ဆက်စပ်ပေမယ့် သီးခြားပြဿနာနှစ်ခုဖြစ်ပါတယ်။

## ၅.၈ မှားလွယ်တဲ့နေရာများ

### Unbounded fan-out

Model ထုတ်သမျှ Tool Calls အားလုံးကို တစ်ပြိုင်နက် run လိုက်ရင် thread၊ memory၊ connection နဲ့ quota တွေ ကုန်နိုင်ပါတယ်။ Semaphore သို့မဟုတ် worker limit မရှိတဲ့ parallelism ကို production default မထားသင့်ပါဘူး။

### Mutation tools ကို parallel ခွင့်ပေးခြင်း

File နှစ်ခုရေးတာက အမြဲ independent မဟုတ်ပါဘူး။ တူညီတဲ့ index၊ config သို့မဟုတ် working tree ကို ထိနိုင်ပါတယ်။ Tool owner က sequential requirement ကို မသတ်မှတ်ရင် low-level loop က intent ကို ခန့်မှန်းပေးမှာမဟုတ်ပါဘူး။

### Completion order နဲ့ Result order ရောခြင်း

အမြန်ပြီးတဲ့ tool result ကို အရင် context ထဲထည့်လိုက်ရင် Tool Calls နဲ့ Tool Results အစီအစဉ် မတည်ငြိမ်တော့ပါဘူး။ Live events နဲ့ transcript artifacts ကို သီးခြားစီထိန်းရပါတယ်။

### Abort က running thread ကိုသတ်မယ်ထင်ခြင်း

Cooperative signal ကို force-stop လို့ယူဆရင် destructive sync tool တစ်ခုက abort ပြီးနောက်လည်း ဆက်လုပ်နေနိုင်ပါတယ်။ Tool ကိုယ်တိုင် cancellation နဲ့ timeout ကို support လုပ်ရပါတယ်။

## ၅.၉ အနှစ်ချုပ်

- Sequential mode က order ရှင်းပြီး mutation-sensitive work အတွက် သင့်တော်တယ်။
- Parallel mode က independent work ကို မြန်စေပေမယ့် limit မရှိဘဲ မဖွင့်သင့်ဘူး။
- Travis234 က semaphore နဲ့ bounded executor သုံးပြီး parallel tool bodies ကို ကန့်သတ်ထားတယ်။
- Unknown tool၊ invalid arguments နဲ့ before-hook block တွေက body မ run ဘဲ error Tool Result ပြန်တယ်။
- Tool end events က completion order ကို ပြနိုင်ပေမယ့် Result messages က source order ကို ထိန်းထားတယ်။
- Bounded concurrency၊ mutation safety နဲ့ cancellation ကို ပြဿနာတစ်ခုတည်းလို မရောသင့်ဘူး။

## ၅.၁၀ Source Notes

- `C-RESULT-ORDER` — `T-LOOP`, `pi.loop.parallel_result_source_order`
- `C-BOUND` — `T-TOOLS`, `T-LOOP`, `pi.loop.bounded_parallelism`
- `C-HOOK-BOUNDARY` — `T-LOOP`, `pi.loop.immediate_outcome_hook_boundary`, `pi.loop.invoked_failure_after_hook_once`
- Pi revision: `1f0dbc008c9b3e88017d42e8a1b46d416ad2b6b6`
- Travis234 revision: `68b1831691b8ec93f9550ce63b80cdcb7a591b2e`

Exact source links နဲ့ evidence boundary ကို [Pinned Source Map](../references/SOURCE_MAP.md) မှာ ကြည့်နိုင်ပါတယ်။

---

Previous: [Chapter 04 — TypeScript ကနေ Python သို့ Semantic Port](04-typescript-to-python-semantic-port.md)

Next: [Chapter 06 — Context Window ပြည့်လာတဲ့ပြဿနာ](06-context-window-pressure.md)

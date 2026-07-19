# Chapter 11 — တစ်ညနဲ့မပြီးတဲ့ Bug

သောကြာနေ့ည ၁၀ နာရီ ၄၃ မိနစ်မှာ Lewis ရဲ့ screen ပေါ်က test တစ်ခုပဲ နီနေပါတယ်။ Model က `slow` ကိုအရင်တောင်းပြီး `fast` ကိုနောက်မှတောင်းထားပေမယ့် `fast` က အရင်ပြီးသွားတယ်။ Agent က result နှစ်ခုလုံးကိုသုံးပြီး အဖြေမှန်ပြန်ထားတာကြောင့် Lewis က ပထမတော့ timing နည်းနည်းကွာသွားတာပဲလို့ ထင်ခဲ့ပါတယ်။ ဒါပေမယ့် failing output က မေးခွန်းတစ်မျိုးကို ပြနေပါတယ်။

```text
FAIL: test_tool_results_keep_source_order
expected source order:    ["slow", "fast"]
observed completion order: ["fast", "slow"]
```

Lewis က coffee အေးသွားတာကိုတောင် သတိမထားမိတော့ပါဘူး။ “နှစ်ခုလုံးရပြီးသားဆို ဘာကွာသလဲ” လို့သူစဉ်းစားတယ်။ နောက်တစ်မိနစ်မှာတော့ test က result ပါမပါကို စစ်နေတာမဟုတ်ဘဲ result ဘယ်အစီအစဉ်နဲ့ model ဆီပြန်ဝင်သလဲကို စစ်နေကြောင်း သတိထားမိသွားပါတယ်။

Lewis နဲ့ ဒီသောကြာညအဖြစ်အပျက်ဟာ Agent Runtime ကို လေ့လာဖို့ ဖန်တီးထားတဲ့ စိတ်ကူးယဉ်ဇာတ်လမ်းဖြစ်ပါတယ်။ တကယ့်လူ၊ တကယ့် incident သို့မဟုတ် Travis234 production failure တစ်ခုကို မှတ်တမ်းတင်ထားတာ မဟုတ်ပါဘူး။

## ၁၁.၁ Failing Test တစ်ခုက စတင်ပေးတဲ့မေးခွန်း

Lewis က failure စာကြောင်းနှစ်ကြောင်းကို ပြန်ဖတ်ပါတယ်။ `expected` က model ထုတ်ခဲ့တဲ့ Tool Call အစီအစဉ်ဖြစ်ပြီး `observed` က tools တကယ်ပြီးသွားတဲ့ wall-clock အစီအစဉ်ဖြစ်နေပါတယ်။ စာရင်းနှစ်ခုလုံးမှာ နာမည်တူတူပါပေမယ့် အဓိပ္ပာယ်မတူပါဘူး။

သူ့ရဲ့ပထမဆုံးအမှားက “အရင်ပြီးတဲ့ result ကို အရင်ထည့်တာ သဘာဝကျတယ်” လို့ယူဆထားခြင်းပါ။ Parallel work မှာ completion order ပြောင်းနိုင်ပါတယ်။ ဒါပေမယ့် model က `slow` call ကို `call-slow` ID နဲ့အရင်ထုတ်ပြီး `fast` call ကို `call-fast` ID နဲ့နောက်မှထုတ်ခဲ့ရင် Runtime က Tool Results ကို မူလ calls တွေနဲ့ stable ဖြစ်အောင် ပြန်တွဲပေးရပါတယ်။ မြန်မြန်ပြီးတာက context ထဲအရင်နေရာရမယ်လို့ မဆိုလိုပါဘူး။

Test ကို ordering test လို့ခေါ်ထားပေမယ့် တကယ်က data ownership ကိုမေးနေတာပါ။ Tool body က completion time ကိုပိုင်တယ်။ Loop က model context ထဲပြန်ဝင်မယ့် message order ကိုပိုင်တယ်။ Observability consumer က real-time completion ကိုမြင်ချင်နိုင်ပြီး model ကတော့ မူလ call order အတိုင်းပြန်ဖတ်ဖို့လိုပါတယ်။ ဒီ boundary သုံးခုရဲ့ “အရင်” ဆိုတဲ့စကားက တစ်မျိုးတည်းမဟုတ်ပါဘူး။

Lewis က Agent ရဲ့နောက်ဆုံးစာသားကိုကြည့်လိုက်တော့ answer က ရောက်နေပါပြီ။ ဒါပေမယ့် Agent က အဖြေတစ်ခုဆီရောက်ခဲ့တဲ့အချိန် Runtime ရဲ့ ဘယ် boundaries တွေကို ဖြတ်ကျော်ခဲ့သလဲ။

## ၁၁.၂ Prompt တစ်ခု Runtime ထဲဝင်သွားတဲ့ခရီး

User က “sources နှစ်ခုကို နှိုင်းယှဉ်ပါ” လို့ပို့လိုက်တဲ့အချိန်မှာ model ကို တန်းခေါ်တာတစ်ခုပဲ မဖြစ်ပါဘူး။ Runtime က အဲဒီစာသားကို user message အဖြစ် context ထဲအရင်ထည့်ပါတယ်။ ဒီ insertion ကြောင့် နောက်ခေါ်မယ့် model က ဘယ်သူပြောထားတာလဲဆိုတဲ့ role နဲ့ content ကို တွဲဖတ်နိုင်ပါတယ်။

ပြီးမှ ပထမ model boundary ကိုဝင်ပါတယ်။ Chapter 09 ရဲ့ Minimal Runtime မှာ model မခေါ်ခင် `assistant_start` ထုတ်ပြီး response ပြန်လာတဲ့အခါ `assistant_end` ထုတ်ပါတယ်။ ပထမ response က final answer မဟုတ်သေးပါဘူး။ “sources နှစ်ခုစစ်မယ်” ဆိုတဲ့ assistant text နဲ့ `slow`, `fast` Tool Calls နှစ်ခုပါလာပါတယ်။ Runtime က ဒီ assistant response ကို history ထဲထည့်တာကြောင့် calls တွေဟာ နောက်ပိုင်း Tool Results နဲ့ချိတ်နိုင်မယ့် မူလတောင်းဆိုချက်ဖြစ်လာပါတယ်။

Tool Call ဆိုတာ model က အလုပ်တစ်ခုလုပ်ပေးဖို့ structured request ထုတ်ခြင်းပါ။ Model ကိုယ်တိုင် tool body ကို run တာမဟုတ်ပါဘူး။ Runtime က tool name ကိုရှာ၊ arguments ကိုပေးပြီး execution စီမံပါတယ်။ Calls နှစ်ခုလုံး parallel လုပ်ခွင့်ရှိရင် တစ်ပြိုင်နက် run နိုင်လို့ `fast` ကအရင်ပြီးပြီး `slow` ကနောက်မှပြီးနိုင်ပါတယ်။

ဒီနေရာမှာ Lewis မျက်စိလွဲခဲ့တာ ပေါ်လာပါတယ်။ Completion ရလာတိုင်း context ထဲတန်း append မလုပ်ရပါဘူး။ Batch ပြီးတဲ့အခါ Runtime က results ကို model ထုတ်ခဲ့တဲ့ source order—`slow` ပြီးမှ `fast`—နဲ့ Tool Result messages အဖြစ်ပြန်တည်ဆောက်ပါတယ်။ Call ID တစ်ခုချင်းနဲ့ result ကိုချိတ်ပြီး context ထဲထည့်ပြီးမှ နောက် model call ကိုခေါ်ပါတယ်။

နောက် model call က အရင်ခေါ်ခဲ့တဲ့ model instance တစ်ခုကို နိုးလိုက်တာမျိုးမဟုတ်ပါဘူး။ Updated context ကို input အဖြစ်ပေးတဲ့ request အသစ်ပါ။ အဲဒီ context ထဲမှာ user message၊ Tool Calls ပါတဲ့ assistant message နဲ့ ordered Tool Results ရှိပြီးသားဖြစ်လို့ model က “နှစ်ခုလုံးရပြီ” ဆိုတဲ့ final answer ကိုရေးနိုင်တာပါ။ Travis234 ရဲ့ loop structure က Tool Call continuation ကိုဒီလို model → tools → ordered results → model အစီအစဉ်နဲ့ ထိန်းထားပါတယ်။

Production lifecycle မှာ provider request မတိုင်ခင် active context ကိုကြည့်တဲ့ preflight Compaction boundary ရှိနိုင်ပြီး successful turn ပြီးနောက် real usage ကိုကြည့်တဲ့ post-response boundary လည်းရှိပါတယ်။ အဲဒီ timing paths က context ကို ဘယ်ပုံစံနဲ့နောက် request ဆီသယ်မလဲ ပြောင်းနိုင်ပေမယ့် Minimal Runtime ထဲမှာတော့ Compaction မပါပါဘူး။ Lewis ရဲ့ ordering test ကိုနားလည်ဖို့ အဲဒီအလွှာကို ခဏဘေးဖယ်ထားရပါတယ်။

## ၁၁.၃ Turn တစ်ခုကို Timeline နဲ့ဖတ်ခြင်း

Lewis က log တစ်ကြောင်းချင်းမဖတ်တော့ဘဲ state boundary အလိုက် timeline ပြန်ရေးပါတယ်။ “အချိန်” ဆိုတာတစ်မျိုးတည်းမဟုတ်ကြောင်း မြင်လာတာနဲ့ failing test က ပိုရှင်းသွားပါတယ်။

| အချိန် | Runtime မှာဖြစ်နေတဲ့အရာ | Context ထဲက state |
|---|---|---|
| T0 | User prompt ကိုလက်ခံတယ် | user message ထည့်ပြီးပြီ |
| T1 | ပထမ model call စတယ် | user message ကို model မြင်တယ် |
| T2 | Assistant response နဲ့ Tool Calls ရတယ် | assistant message ထည့်ပြီးပြီ |
| T3 | `slow` နဲ့ `fast` ကို parallel execute လုပ်တယ် | Tool Results မရှိသေးဘူး |
| T4 | `fast` အရင်ပြီးတယ် | completion သိပေမယ့် result order မတည်ဆောက်သေးဘူး |
| T5 | `slow` ပြီးတယ် | batch result နှစ်ခုလုံးရပြီ |
| T6 | Results ကို `slow`, `fast` အတိုင်း append လုပ်တယ် | Tool Result messages နှစ်ခုရှိပြီ |
| T7 | ဒုတိယ model call စတယ် | updated context အားလုံးကို model မြင်တယ် |
| T8 | Final assistant answer ရတယ် | completed assistant message ထည့်ပြီးပြီ |

Production Travis234 မှာ `tool_execution_end` က tool တစ်ခုချင်း finalize ဖြစ်တဲ့ completion event ဖြစ်လို့ T4 မှာ `fast` ကိုအရင်မြင်နိုင်ပါတယ်။ ဒါက source order ပျက်သွားတယ်လို့ မဆိုလိုပါဘူး။ Model context အတွက် Tool Results ကို T6 ရောက်မှ source order နဲ့ပြန်တည်ဆောက်နိုင်ပါတယ်။ Real-time event order နဲ့ message insertion order ကို trace တစ်မျိုးတည်းလိုဖတ်မိရင် Lewis ကြုံခဲ့တဲ့ confusion ပြန်ဖြစ်ပါမယ်။

Assistant boundary လည်း ထိုနည်းတူပါပဲ။ ပထမ `assistant_end` က Agent အလုပ်အားလုံးပြီးသွားတာမဟုတ်ဘဲ Tool Calls ပါတဲ့ model response တစ်ကြိမ်ပြီးသွားတာကိုသာ ပြပါတယ်။ Tool Results ထည့်ပြီး ဒုတိယ `assistant_start` ဝင်လာတာက loop ဆက်နေသေးကြောင်းပြပါတယ်။ Final response မှာ Tool Calls မရှိတော့မှ ဒီ lab ရဲ့ loop ကရပ်ပါတယ်။

## ၁၁.၄ Minimal Runtime ကို ပြန် Run ကြည့်ခြင်း

Lewis ရဲ့ timeline ကို ကိုယ်တိုင်စစ်ချင်ရင် [`examples/minimal_runtime.py`](../../examples/minimal_runtime.py) ကို repository root ကနေ run နိုင်ပါတယ်။ ဒီ code က offline fake model နဲ့ fake tools သုံးထားတဲ့ educational model ဖြစ်ပြီး production Travis234 မဟုတ်ပါဘူး။ Network သို့မဟုတ် API key မလိုပါဘူး။

```bash
python3.13 examples/minimal_runtime.py
```

လက်ရှိ example ကထုတ်ပေးတဲ့ event ရှစ်ခုအတိအကျက:

```text
assistant_start: 1
assistant_end: I will check both sources.
tool_start: slow
tool_start: fast
tool_end: slow:slow-result
tool_end: fast:fast-result
assistant_start: 2
assistant_end: Both results are ready.
```

Run မလုပ်ခင် `fast` ကပိုမြန်တယ်ဆိုတော့ `tool_end: fast` အရင်ထွက်မယ်လို့ ခန့်မှန်းမိနိုင်ပါတယ်။ ဒါပေမယ့် ဒီ lab ရဲ့ `tool_end` က wall-clock completion event မဟုတ်ပါဘူး။ `asyncio.gather()` က input awaitables အစီအစဉ်နဲ့ results ပြန်ပေးပြီး loop က source order အတိုင်း `tool_end` trace ထုတ်ကာ Tool Result messages ထည့်ထားတာပါ။ ဒါကြောင့် output မှာ `slow` အရင်တွေ့ရပါတယ်။

ဒီ `tool_end` ကို production `tool_execution_end` နဲ့ အမည်ကွာရုံလို့ မယူဆသင့်ပါဘူး။ Production event က actual completion ကိုဖော်ပြနိုင်ပြီး lab event က source-ordered result insertion ကိုသင်ဖို့ရည်ရွယ်ထားပါတယ်။ Completion order တကယ် `fast`, `slow` ဖြစ်ကြောင်းကို example output ရှစ်ကြောင်းတစ်ခုတည်းနဲ့ မသက်သေပြဘဲ Chapter 09 မှာဖော်ပြထားတဲ့ focused test က သီးခြားမှတ်တမ်းနဲ့ စစ်ထားပါတယ်။

## ၁၁.၅ State ဘယ်နေရာတွေမှာ ပြောင်းသွားသလဲ

Trace ကို event စာရင်းတစ်ခုလိုပဲကြည့်ရင် Runtime state ပျောက်သွားနိုင်ပါတယ်။ Lewis က notebook ထဲမှာ messages state ကို snapshot လေးခုနဲ့ ပြန်ရေးလိုက်ပါတယ်။

1. အစမှာ `messages` ထဲ user message တစ်ခုပဲရှိတယ်။
2. ပထမ model response နောက်မှာ text နဲ့ Tool Calls ပါတဲ့ assistant message တစ်ခုတိုးလာတယ်။
3. Tool batch ပြီးတဲ့နောက် `slow` နဲ့ `fast` Tool Result messages နှစ်ခု source order အတိုင်းတိုးလာတယ်။
4. ဒုတိယ model response နောက်မှာ Tool Call မပါတဲ့ final assistant message တစ်ခုတိုးလာတယ်။

`events` list က သီးခြား state ဖြစ်ပါတယ်။ UI သို့မဟုတ် test က lifecycle ကိုဖတ်နိုင်အောင် `assistant_start`, `assistant_end`, `tool_start`, `tool_end` တွေကိုမှတ်ထားပါတယ်။ Messages က model ရဲ့နောက် request အတွက် input ဖြစ်ပြီး events က Runtime ကိုကြည့်နေတဲ့ consumer အတွက် observation ဖြစ်ပါတယ်။ နှစ်ခုကို list တစ်ခုတည်းလို စဉ်းစားလို့မရပါဘူး။

State ပြောင်းတဲ့အချိန်နဲ့ external work ဖြစ်တဲ့အချိန်လည်း ခွဲရပါတယ်။ `fast` tool ပြီးသွားတာက ပြင်ပအလုပ်တစ်ခုပြီးခြင်းပါ။ အဲဒီ result ကို `call-fast` နဲ့ချိတ်ပြီး messages ထဲထည့်တာက Runtime state transition ပါ။ ဒီနှစ်ခုကြားမှာ ordering policy ရှိလို့ parallel completion ဖြစ်နေလည်း context ကို stable ပြန်တည်ဆောက်နိုင်ပါတယ်။

ဒုတိယ model call က state ပြောင်းပြီးနောက် ဖြစ်ရပါတယ်။ Tool Results မထည့်ခင် model ကိုပြန်ခေါ်လိုက်ရင် model က tool output ကိုမမြင်ရသေးပါဘူး။ Results ထည့်ပြီး model မခေါ်တော့ရင်လည်း Runtime မှာ data ရှိပေမယ့် assistant answer အသစ်မထွက်နိုင်ပါဘူး။ Lewis ရဲ့ test က order ကိုပဲပြပေမယ့် နောက်ကွယ်မှာ insertion နဲ့ next-call boundary နှစ်ခုလုံးကို သတိပေးနေပါတယ်။

## ၁၁.၆ Trace ရှိရုံနဲ့ မသက်သေပြနိုင်တဲ့အရာ

Event ရှစ်ကြောင်းကိုမြင်ရတာက mental model တည်ဆောက်ဖို့ကောင်းပါတယ်။ ဒါပေမယ့် ဒီ trace တစ်ခုတည်းနဲ့ production Runtime အားလုံးမှန်တယ်လို့ မဆိုနိုင်ပါဘူး။

- `slow` နဲ့ `fast` တကယ်ပြီးတဲ့ wall-clock order ကို lab output မပြပါဘူး။
- Production streaming deltas၊ validation၊ hooks၊ cancellation နဲ့ persistent session behavior ကို မဖုံးပါဘူး။
- Preflight၊ post-response၊ overflow recovery နဲ့ manual Compaction paths အလုပ်မှန်ကြောင်းကို မစစ်ပါဘူး။
- Live provider response၊ network failure၊ latency နဲ့ resource usage ကို မတိုင်းပါဘူး။
- Ordering case တစ်ခု pass ဖြစ်တာက unknown tool နဲ့ iteration limit အပါအဝင် test suite အားလုံး pass ဖြစ်ကြောင်း မသက်သေပြပါဘူး။

Trace က “ဘာ order ကို ဒီ example ထုတ်သလဲ” ဆိုတာကိုပဲ တိတိကျကျပြပါတယ်။ Production claim တစ်ခုလုပ်မယ်ဆိုရင် pinned source၊ focused test နဲ့ event semantics ကိုပါ ပြန်တိုက်ရပါတယ်။ Lewis အတွက် ဒီကန့်သတ်ချက်က အားနည်းချက်မဟုတ်ပါဘူး။ မေးခွန်းတစ်ခုကို evidence တစ်မျိုးနဲ့ပဲ ဖြေနိုင်ကြောင်း သိသွားတာပါ။

## ၁၁.၇ Lewis ရဲ့မှတ်စု

ညသန်းခေါင်ကျော်လာတဲ့အခါ Lewis က failing assertion ကို ချက်ချင်းပြင်မယ့်အစား notebook ရဲ့စာမျက်နှာသစ်မှာ ဒီလိုရေးထားပါတယ်။

- Final answer မှန်တာနဲ့ Runtime order မှန်တာ မတူဘူး။
- “အရင်” လို့ရေးတိုင်း source၊ start၊ completion သို့မဟုတ် result order ဘယ်ဟာလဲ ထည့်ရေးမယ်။
- Tool Call ID က request နဲ့ result ကြားက ချိတ်ဆက်မှုဖြစ်တယ်။ List position တစ်ခုတည်းကို အားမကိုးဘူး။
- Completion event ကို live observation အဖြစ်ဖတ်ပြီး Tool Result message ကို next model input အဖြစ်ဖတ်မယ်။
- Trace တစ်ခုရဲ့အပြင်ဘက်မှာရှိတဲ့ behavior ကို အဲဒီ trace နဲ့သက်သေပြပြီးသားလို့ မရေးဘူး။

သူ့ bug က တစ်ညတည်းနဲ့မပြီးသေးပါဘူး။ Ordering assertion ကိုရှင်းလိုက်တာနဲ့ steering message၊ abort၊ tool failure နဲ့ session resume တို့မှာလည်း အလားတူ boundary မေးခွန်းတွေရှိနေကြောင်း သူမြင်သွားပါတယ်။ ဒါပေမယ့် မနက်ဖြန်စဖတ်ရမယ့်နေရာတော့ ရှင်းသွားပြီ—answer စာသားကနေ နောက်ပြန်လိုက်မယ့်အစား state ပြောင်းတဲ့ boundary တစ်ခုချင်းကနေ ရှေ့ကိုလိုက်ဖတ်ရမှာပါ။

## ၁၁.၈ အနှစ်ချုပ်

- User prompt က user message အဖြစ် context ထဲဝင်ပြီးမှ ပထမ model call စတယ်။
- ပထမ assistant response မှာ Tool Calls ပါလာရင် Runtime က tool bodies ကို execute လုပ်ပြီး assistant message နဲ့ results ကိုချိတ်တယ်။
- Parallel tools ရဲ့ completion order ပြောင်းနိုင်ပေမယ့် Tool Results ကို source order နဲ့ model context ထဲပြန်ထည့်တယ်။
- Ordered Tool Results ထည့်ပြီးနောက် model ကို request အသစ်နဲ့ပြန်ခေါ်မှ final answer ထွက်တယ်။
- Lab ရဲ့ source-ordered `tool_end` နဲ့ production completion event `tool_execution_end` ကို မရောသင့်ဘူး။
- Minimal trace က loop အရိုးစုကိုပြပေမယ့် production streaming၊ hooks၊ persistence နဲ့ Compaction behavior ကို မသက်သေပြဘူး။

## ၁၁.၉ Source Notes

- Executable educational model: [`examples/minimal_runtime.py`](../../examples/minimal_runtime.py)
- `C-LOOP-ORDER` — `T-LOOP`; Tool Call continuation နဲ့ model → tools → model control flow
- `C-RESULT-ORDER` — `T-LOOP`, `pi.loop.parallel_result_source_order`; completion order ကွာနိုင်ပေမယ့် Tool Results ကို source order နဲ့ပြန်ထည့်ခြင်း
- `C-TIMING` — `T-APP`; normal turn နဲ့ post-response integration order
- Pi revision: `1f0dbc008c9b3e88017d42e8a1b46d416ad2b6b6`
- Travis234 revision: `68b1831691b8ec93f9550ce63b80cdcb7a591b2e`

Exact source links နဲ့ evidence boundary ကို [Pinned Source Map](../references/SOURCE_MAP.md) မှာ ကြည့်နိုင်ပါတယ်။ Claim တစ်ခုချင်းရဲ့ verification scope ကို [Technical Claim Ledger](../references/CLAIM_LEDGER.md) မှာ ဖတ်နိုင်ပါတယ်။

---

Previous: [Chapter 10 — Parity, Divergence နှင့် သင်ခန်းစာများ](10-parity-divergence-lessons.md)

Next: [Chapter 12 — Agent ကို လမ်းပြန်ညွှန်ရတဲ့အချိန်](12-steering-followup-cancellation.md)

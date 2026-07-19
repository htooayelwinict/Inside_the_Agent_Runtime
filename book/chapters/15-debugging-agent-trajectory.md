# Chapter 15 — Agent ရဲ့လမ်းကြောင်းကို Trace နဲ့ Debug လုပ်ခြင်း

## ၁၅.၁ “ပြီးပါပြီ” ဆိုတဲ့စကားကို ဘာကြောင့် မလုံလောက်တာလဲ

တနင်္လာနေ့မနက်မှာ Lewis က parser bug တစ်ခုကို Agent နဲ့ပြင်နေပါတယ်။ Agent က source ဖတ်တယ်၊ file ကိုပြင်တယ်၊ focused test ကိုခေါ်တယ်။ ခဏအကြာမှာ နောက်ဆုံးစာကြောင်းတစ်ကြောင်းပြန်လာပါတယ်။

```text
Fix applied. The focused test now passes.
```

စာကြောင်းက ယုံကြည်စရာကောင်းပေမယ့် Lewis က test ကို terminal ကနေပြန် run လိုက်တဲ့အခါ အနီရောင် failure တစ်ခုရှိနေဆဲပါ။ သူက final answer ကိုပြန်ဖတ်ရုံနဲ့ “Agent ဘာကြောင့်မှားပြောသလဲ” ဆိုတာမသိနိုင်ပါဘူး။ Source ကိုတကယ်ဖတ်ခဲ့သလား၊ edit Tool အောင်မြင်ခဲ့သလား၊ test Tool က error ပြန်ခဲ့သလား၊ error နောက်မှာ model ကိုဘယ် result ပြန်ပို့ခဲ့သလဲဆိုတာ ပြန်တည်ဆောက်ရပါမယ်။

Lewis က message နဲ့ Tool events ကို index အလိုက်စီလိုက်တော့ ပထမဆုံးပျက်တဲ့နေရာကိုတွေ့သွားပါတယ်။ Edit ကအောင်မြင်ခဲ့ပေမယ့် focused test က fail ဖြစ်ထားပြီး model ရဲ့နောက်ဆုံးစာသားက အဲဒီ result နဲ့မကိုက်ပါဘူး။ “ပြီးပါပြီ” ဆိုတာ Agent ရဲ့ claim ဖြစ်ပြီး test result က observable evidence ဖြစ်ပါတယ်။ နှစ်ခုကိုတစ်ခုတည်းလို မယူရပါဘူး။

`Lewis နဲ့ ဒီ false-success incident ဟာ tracing ကိုလေ့လာဖို့ ဖန်တီးထားတဲ့ စိတ်ကူးယဉ်ဇာတ်လမ်းပါ။ တကယ့် contributor၊ production incident သို့မဟုတ် Travis234 မှာဖြစ်ခဲ့တဲ့ failure တစ်ခု မဟုတ်ပါဘူး။ အောက်က Runtime behavior တွေကတော့ Source Notes မှာဖော်ပြထားတဲ့ pinned source၊ claim နဲ့ tests အပေါ်အခြေခံထားပါတယ်။`

## ၁၅.၂ Event Trace ဆိုတာ Runtime ရဲ့ခြေရာ

Agent ကိုကြည့်တဲ့အခါ final assistant message တစ်ခုတည်းသာမြင်ရင် အစနဲ့အဆုံးပဲရှိတဲ့ခရီးစဉ်လိုဖြစ်နေပါတယ်။ အလယ်မှာ model response ဘယ်နှကြိမ်ရခဲ့သလဲ၊ ဘယ် Tool Calls စခဲ့သလဲ၊ ဘယ်ဟာအရင်ပြီးသလဲနဲ့ ဘယ် result ကို context ထဲပြန်ထည့်ခဲ့သလဲ မမြင်ရပါဘူး။

`Event Trace` ဆိုတာ Runtime က observer ဆီထုတ်ပေးခဲ့တဲ့ lifecycle ဖြစ်ရပ်တွေကို အစီအစဉ်နဲ့မှတ်ထားတဲ့ခြေရာပါ။ Event တစ်ခုမှာ type၊ call ID၊ status နဲ့ sequence index လို metadata ပါနိုင်ပါတယ်။ ဒီခြေရာက “Agent ကဘာပြောသလဲ” ထက် “Runtime boundary တွေမှာဘာတွေကို မှတ်တမ်းတင်ခဲ့သလဲ” ဆိုတဲ့မေးခွန်းကို ဖြေပေးပါတယ်။

Trace ဖတ်တဲ့အခါ event သုံးခုကိုအရင်စစ်နိုင်ပါတယ်။ ဘယ် boundary စခဲ့သလဲ၊ ဘယ် boundary ပြီးခဲ့သလဲ၊ failure flag ပထမဆုံးဘယ်မှာပေါ်သလဲ။ Timestamp တစ်ခုတည်းကိုမယုံဘဲ stable sequence index ရှိရင် index အလိုက်အရင်စီရပါတယ်။ ဒီလိုစီခြင်းက file ထဲက lines ရောနေသော်လည်း recorded order ကိုပြန်ယူနိုင်စေပါတယ်။

ဒါပေမယ့် trace က Runtime ရဲ့ဖြစ်ရပ်ကိုအလိုအလျောက်ဖမ်းယူပေးတဲ့ မှော်မှန်တစ်ချပ်မဟုတ်ပါဘူး။ Code က event ထုတ်ထားတဲ့နေရာနဲ့ writer ကလက်ခံထားတဲ့ field တွေပဲပါနိုင်ပါတယ်။ Instrumentation မထည့်ထားတဲ့ boundary ကို trace ကနေ နောက်မှပြန်ဖန်တီးလို့မရပါဘူး။

## ၁၅.၃ Message Event နဲ့ Tool Event

Lewis ရဲ့ trace ထဲမှာ `message_end` နဲ့ `tool_execution_end` နှစ်မျိုးစလုံး “end” လို့ရှိတာကြောင့် ပထမတော့ရောဖတ်မိပါတယ်။ ဒါပေမယ့် သူတို့ပြီးဆုံးစေတဲ့ object မတူပါဘူး။ Message Event က model context သို့မဟုတ် assistant stream ဘက်က message lifecycle ကိုဖော်ပြပြီး Tool Event က Tool invocation lifecycle ကိုဖော်ပြပါတယ်။

Travis234 ရဲ့ Agent event contract မှာ `message_start`, `message_update`, `message_end` ရှိပါတယ်။ Assistant response စလာတာ၊ streaming update ရလာတာနဲ့ completed message ရလာတာကို consumer က ဒီ boundaries နဲ့ခွဲကြည့်နိုင်ပါတယ်။ Provider ဘက်က assistant event stream က start/delta/done/error events ကို queue ကနေယူနိုင်စေပြီး `done` သို့မဟုတ် `error` ရောက်ရင် final Assistant Message နဲ့ stream ကိုအဆုံးသတ်ပါတယ်။ ဒီ stream behavior ကို `T-EVENT-STREAM` ကဖုံးထားပါတယ်။

Tool ဘက်မှာ `tool_execution_start`, `tool_execution_update`, `tool_execution_end` ရှိပါတယ်။ Start က call ID နဲ့ Tool name ကို execution boundary ဆီသယ်လာတယ်။ Update ရှိရင် partial progress ကိုပြနိုင်တယ်။ End က result၊ error state နဲ့ reason code လို execution outcome ကိုဖော်ပြနိုင်ပါတယ်။

Tool Result ကို model context ထဲပြန်ထည့်တဲ့အခါ `message_start` နဲ့ `message_end` အဖြစ်လည်းထုတ်နိုင်ပါတယ်။ ဒါကြောင့် Tool တစ်ခုအတွက် `tool_execution_end` မြင်ပြီးနောက် Tool Result message event ထပ်မြင်ရတာ duplicate မဟုတ်ပါဘူး။ ပထမ event က invocation ပြီးခြင်း၊ ဒုတိယ event က result message ပြန်ထည့်ခြင်းကိုပြပါတယ်။ Debug လုပ်တဲ့အခါ event type နဲ့ call ID နှစ်ခုလုံးတွဲဖတ်ရပါတယ်။

## ၁၅.၄ Completion Order နဲ့ Result Order

Tool နှစ်ခုကို parallel run လိုက်ရင် source မှာအရင်ရေးထားတဲ့ call က နောက်မှပြီးနိုင်ပါတယ်။ Lewis ရဲ့ trace မှာ model က `slow` ကိုအရင်တောင်းပြီး `fast` ကိုနောက်မှတောင်းပေမယ့် completion က ဒီလိုဖြစ်ပါတယ်။

```text
tool_execution_end: fast
tool_execution_end: slow
```

`Completion Order` ဆိုတာ Tool bodies တကယ် finalize ဖြစ်တဲ့အစီအစဉ်ပါ။ Real-time progress၊ latency နဲ့ first failure ကိုကြည့်တဲ့ consumer အတွက် ဒီ order ကအသုံးဝင်ပါတယ်။ Travis234 ရဲ့ parallel path မှာ task တစ်ခု finalize ဖြစ်ချိန် `tool_execution_end` ထုတ်နိုင်လို့ `fast`, `slow` ကိုမြင်ရပါတယ်။

`Result Order` ဆိုတာ Tool Result messages ကို model context ထဲပြန်ပို့တဲ့အစီအစဉ်ပါ။ Parallel tasks ပြီးနောက် Runtime က entries ကို မူလ Tool Calls အစီအစဉ်နဲ့ await လုပ်ပြီး messages တည်ဆောက်တာကြောင့် ဒီလိုဖြစ်နိုင်ပါတယ်။

```text
tool_result: slow
tool_result: fast
```

Order နှစ်မျိုးက မတူပေမယ့် ဆန့်ကျင်နေခြင်းမဟုတ်ပါဘူး။ Completion events က wall-clock behavior ကိုထိန်းပြီး Result messages က source order နဲ့ call/result pairing ကိုထိန်းပါတယ်။ `C-TRACE-ORDER` က trace reader ဟာ event kind နှစ်မျိုးကိုခွဲဖတ်ရမယ့် boundary ကိုဖော်ပြပြီး `C-RESULT-ORDER` က model context ထဲ Tool Results ကို source order နဲ့ထိန်းတဲ့ contract ကိုဖော်ပြပါတယ်။ Completion list တစ်ခုကိုကြည့်ပြီး context order ပျက်တယ်လို့ချက်ချင်းမဆုံးဖြတ်သင့်ပါဘူး။

## ၁၅.၅ Failure Boundary ကို နောက်ပြန်ရှာခြင်း

Final answer မှားနေတဲ့အခါ Lewis က နောက်ဆုံး event ကနေအကြောင်းပြချက်ခန့်မှန်းမယ့်အစား trace အစကနေ stable order နဲ့ပြန်တည်ဆောက်ပါတယ်။ Debugging question က “နောက်ဆုံးဘာဖြစ်သလဲ” မဟုတ်ဘဲ “expected state နဲ့ပထမဆုံးဘယ်မှာကွာသွားသလဲ” ဖြစ်ပါတယ်။

ပထမဦးဆုံး events ကို index အလိုက်စီပါ။ ပြီးရင် call ID တူတဲ့ Tool start၊ end နဲ့ Result message ကိုတွဲပါ။ `is_error=True` ပထမဆုံးဖြစ်တဲ့ event ကိုရှာပြီး အဲဒီမတိုင်ခင် input၊ အဲဒီ event ရဲ့ outcome နဲ့ အဲဒီနောက် model မြင်ခဲ့တဲ့ result ကိုခွဲစစ်ပါ။ Lewis ရဲ့ incident မှာ edit Tool ကအောင်မြင်ပြီး test Tool မှာပထမ failure ပေါ်ပါတယ်။ ဒါကြောင့် investigation ကို final prose generation ကနေစရာမလိုဘဲ test invocation boundary ကနေစနိုင်ပါတယ်။

First failure က root cause နဲ့အမြဲတူမနေပါဘူး။ Test failure ရဲ့အကြောင်းရင်းက အရင် edit မှားတာဖြစ်နိုင်သလို test environment ပြဿနာလည်းဖြစ်နိုင်ပါတယ်။ First-failure search က စစ်ဆေးရမယ့် boundary ကိုကျဉ်းပေးတာပါ။ Causality ကိုအပြီးသတ်သက်သေပြတာမဟုတ်ပါဘူး။

False success ကိုစစ်တဲ့အခါ နောက်ထပ်အဆင့်တစ်ခုလိုပါတယ်။ Final assistant claim ကို Tool Result နဲ့ပြန်တိုက်ပါ။ Agent က “test passes” လို့ပြောပြီး recorded test outcome က error ဖြစ်နေရင် claim ဟာ evidence နဲ့မကိုက်ကြောင်းပြနိုင်ပါတယ်။ ဒါပေမယ့် test တကယ်မခေါ်ခဲ့ဘဲ trace မှာလည်း event မရှိရင် pass ဖြစ်တယ်လို့သော်လည်းကောင်း fail ဖြစ်တယ်လို့သော်လည်းကောင်း trace တစ်ခုတည်းနဲ့ မဆုံးဖြတ်နိုင်ပါဘူး။

## ၁၅.၆ Offline Trace-reader Lab

ဒီမေးခွန်းသုံးခု—completion order၊ result order နဲ့ first failure—ကို network မလိုဘဲစမ်းချင်ရင် [`examples/lewis_trace_reader.py`](../../examples/lewis_trace_reader.py) ကို run နိုင်ပါတယ်။ ဒါဟာ production log parser မဟုတ်ဘဲ event semantics ကိုခွဲဖတ်ဖို့ရေးထားတဲ့ simplified teaching model ပါ။

```bash
python3 examples/lewis_trace_reader.py
```

Expected output က:

```text
completion_order:fast,slow,test
result_order:slow,fast
first_failure:test
```

`analyze_trace()` က input tuple ရဲ့လက်ရှိနေရာကိုမယုံဘဲ `index` နဲ့အရင်စီပါတယ်။ ပြီးရင် `tool_execution_end` events ကို completion list ထဲ၊ `tool_result` events ကို result list ထဲ သီးခြားထည့်ပြီး `is_error` ပါတဲ့ပထမ event ရဲ့ call ID ကိုရွေးပါတယ်။ Default fixture မှာ parallel pair ရဲ့ completion က `fast`, `slow` ဖြစ်ပေမယ့် results က `slow`, `fast` ဖြစ်ပြီး နောက်ထပ် `test` completion က first failure ဖြစ်ပါတယ်။

ဒီ boundary ကို focused test နဲ့အတိအကျစစ်နိုင်ပါတယ်။

```bash
python3 -m unittest tests.test_lewis_workshop.TraceReaderTests.test_completion_and_result_order_are_reported_separately -v
```

Test fixture မှာ index ၁ က `fast` completion၊ index ၂ က `slow` completion၊ index ၃ က `slow` result နဲ့ index ၄ က `fast` result ဖြစ်ပါတယ်။ Input lines ကို shuffled order နဲ့ပေးထားလည်း expected report က completion `("fast", "slow")` နဲ့ result `("slow", "fast")` ဖြစ်ရပါတယ်။ ဒီ test က sorting နဲ့ order separation ကိုသာစစ်ပြီး production JSONL schema၊ duplicate index၊ missing event သို့မဟုတ် payload redaction ကိုမစစ်ပါဘူး။

## ၁၅.၇ ဘာကို Log လုပ်ပြီး ဘာကိုဖျောက်မလဲ

Trace အသေးစိတ်လေလေ debug လုပ်ရလွယ်မယ်လို့ထင်နိုင်ပေမယ့် prompt၊ Tool arguments နဲ့ response အကုန်ရေးထားခြင်းက secret နဲ့ private data အန္တရာယ်ကိုတိုးစေပါတယ်။ Debuggability နဲ့ data minimization ကို field တစ်ခုချင်းရွေးပြီးညှိရပါတယ်။

Pinned `T-EVAL-TRACE` source ထဲက `EvalTraceWriter` က event types နဲ့ fields ကို allowlist လုပ်ထားပါတယ်။ Allowlist မပါတဲ့ event သို့မဟုတ် field ကို reject လုပ်ပြီး configured secret value သို့မဟုတ် `sk-…`, `Bearer …` ပုံစံတွေတွေ့ရင် lifecycle record ကိုမရေးပါဘူး။ File ကို `0600` permission နဲ့ဖန်တီးပြီး prompt/result content ထက် Tool name၊ status၊ duration နဲ့ token counts လို metadata ကိုဦးစားပေးပါတယ်။ ဒီ design ကြောင့် order နဲ့ lifecycle ကို raw content မသိမ်းဘဲစစ်နိုင်ပါတယ်။

`ConversationLogWriter` ကတော့ explicitly authorized evaluation အတွက် opt-in semantic turn capture ဖြစ်ပါတယ်။ Prompt နဲ့ final response ကိုရေးနိုင်တာကြောင့် configured secret strings နဲ့သတ်မှတ်ထားတဲ့ secret shapes ကို `[REDACTED]` နဲ့အစားထိုးပြီး file permission ကိုလည်း `0600` ထားပါတယ်။ Lifecycle trace နဲ့ conversation log ကိုတူတယ်လို့ မယူသင့်ပါဘူး။ ပထမတစ်ခုက strict metadata ဖြစ်ပြီး ဒုတိယတစ်ခုကပိုအရေးကြီးတဲ့ semantic content ပါနိုင်ပါတယ်။

Logs တွေဟာ အလိုအလျောက် safe သို့မဟုတ် complete မဖြစ်ပါဘူး။ Pattern redaction က မသိသေးတဲ့ credential format၊ personal data နဲ့ business secret အားလုံးကိုသိနိုင်တာမဟုတ်သလို configured list ထဲမပါတဲ့ secret ကိုလည်း လွတ်သွားနိုင်ပါတယ်။ `0600` က local file access ကိုကျဉ်းပေမယ့် retention၊ backup၊ upload နဲ့ authorized user ရဲ့အသုံးပြုပုံကိုမထိန်းပါဘူး။ Content log ကိုလိုအပ်မှသာဖွင့်၊ secret inventory ကိုပြင်ဆင်၊ retention ကိုကန့်သတ်ပြီး output ကို sensitive artifact အဖြစ်ကိုင်တွယ်ရပါတယ်။

## ၁၅.၈ Trace က မသက်သေပြနိုင်တဲ့အရာ

Lewis က first failure ကိုတွေ့သွားတာနဲ့ bug အားလုံးရှင်းသွားတာမဟုတ်ပါဘူး။ Trace evidence ရဲ့အတိုင်းအတာကိုမကန့်သတ်ရင် event တစ်စင်းကနေ system guarantee ကြီးတစ်ခုထုတ်မိနိုင်ပါတယ်။

- Trace က ထုတ်ထားတဲ့ events ရဲ့ recorded order ကိုပြနိုင်ပေမယ့် event မထုတ်ထားတဲ့ internal step ကိုမပြနိုင်ပါဘူး။ Missing instrumentation ကို trace ကနေ ပြန်တည်ဆောက်လို့မရပါဘူး။
- `tool_execution_end` ရှိတာက Runtime က outcome တစ်ခု finalize လုပ်ခဲ့ကြောင်းပြနိုင်ပေမယ့် external side effect အားလုံးမှန်ကြောင်း မအာမခံပါဘူး။
- Error event မတွေ့တာက success သက်သေမဟုတ်ပါဘူး။ Writer မချိတ်ထားခြင်း၊ dropped event သို့မဟုတ် process crash ရှိနိုင်ပြီး အဲဒီအခြေအနေကို သီးခြားစစ်ရပါတယ်။
- Result order မှန်တာက result content မှန်ခြင်း၊ model ကမှန်ကန်စွာအသုံးချခြင်း သို့မဟုတ် final answer မှန်ခြင်းကို မသက်သေပြပါဘူး။
- Redacted lifecycle metadata က prompt/response semantics ကိုမပြသလို conversation log ကလည်း provider အတွင်းပိုင်း reasoning သို့မဟုတ် မရေးထားတဲ့ Tool state ကိုမဖော်ပြပါဘူး။

ဒါကြောင့် trace ကို source inspection၊ focused test၊ reproducible command နဲ့ actual artifact တို့နဲ့တွဲသုံးရပါတယ်။ Trace က investigation ကိုလမ်းညွှန်ပေးတဲ့ evidence တစ်မျိုးဖြစ်ပြီး complete ground truth မဟုတ်ပါဘူး။

## ၁၅.၉ Lewis ရဲ့မှတ်စု

- Final sentence ကို outcome evidence လို့မယူဘဲ test result နဲ့ပြန်တိုက်မယ်။
- Message Event နဲ့ Tool Event ကို type နဲ့ call ID အလိုက်ခွဲဖတ်မယ်။
- Completion Order နဲ့ Result Order ကို list နှစ်ခုအဖြစ်သီးခြားတည်ဆောက်မယ်။
- Events ကို index အလိုက်စီပြီး `is_error` ပထမဆုံးပေါ်တဲ့ boundary ကနေစစ်မယ်။
- Metadata trace ကိုဦးစားပေးပြီး content log ဖွင့်ရင် authorization၊ redaction နဲ့ retention ကိုသီးခြားဆုံးဖြတ်မယ်။
- Event မရှိခြင်းကို “မဖြစ်ခဲ့ဘူး” လို့မကောက်ချက်ချဘဲ instrumentation coverage ကိုအရင်စစ်မယ်။

## ၁၅.၁၀ အနှစ်ချုပ်

- Event Trace က Runtime ထုတ်ထားတဲ့ lifecycle events ကို order နဲ့ပြန်ဖတ်နိုင်စေတယ်။
- Message events က assistant/message lifecycle ကိုဖော်ပြပြီး Tool events က invocation lifecycle ကိုဖော်ပြတယ်။ Tool Result message emission က သီးခြား boundary ဖြစ်တယ်။
- Parallel execution မှာ completion `fast`, `slow` ဖြစ်နေလည်း model context အတွက် Result Order က `slow`, `fast` ဖြစ်နိုင်တယ်။
- First failure ကိုရှာခြင်းက investigation boundary ကိုကျဉ်းစေပေမယ့် root cause ကိုအလိုအလျောက်သက်သေမပြပါဘူး။
- Offline trace reader က index sorting၊ order separation နဲ့ first-error selection ကို deterministic သင်ပေးတယ်။
- Strict lifecycle metadata နဲ့ opt-in conversation content ဟာ sensitivity မတူပါဘူး။ Redaction နဲ့ file permission ရှိတာတစ်ခုတည်းကြောင့် log က safe သို့မဟုတ် complete မဖြစ်ပါဘူး။
- Missing instrumentation၊ မသိမ်းထားတဲ့ content နဲ့ external side effects ကို trace နောက်မှပြန်တည်ဆောက်လို့မရပါဘူး။

## ၁၅.၁၁ Source Notes

- Executable teaching model: [`examples/lewis_trace_reader.py`](../../examples/lewis_trace_reader.py)
- Focused executable tests: [`tests/test_lewis_workshop.py`](../../tests/test_lewis_workshop.py) ထဲက `TraceReaderTests`
- `C-TRACE-ORDER` — `T-LOOP`, `T-EVAL-TRACE`, `tests/test_agent_loop.py::test_parallel_tool_end_events_follow_completion_order_while_results_keep_source_order`, `tests/test_eval_trace.py::test_eval_trace_records_lifecycle_without_sensitive_content`; Tool completion events နဲ့ Result message order ကိုခွဲဖတ်ရတဲ့ boundary
- `C-RESULT-ORDER` — `T-LOOP`, `pi.loop.parallel_result_source_order`; parallel completion ကွာနေလည်း Tool Results ကို source order နဲ့ model context ထဲပြန်ထည့်တဲ့ contract
- `T-EVENT-STREAM` — provider-to-runtime assistant event stream က events ကို push/iterate လုပ်ပြီး `done` သို့မဟုတ် `error` မှာ final Assistant Message နဲ့ resolve လုပ်တဲ့ boundary
- `T-EVAL-TRACE` — strict lifecycle event/field allowlist၊ configured-secret rejection၊ `0600` file boundary နဲ့ opt-in conversation-log redaction
- Pi revision: `1f0dbc008c9b3e88017d42e8a1b46d416ad2b6b6`
- Travis234 revision: `68b1831691b8ec93f9550ce63b80cdcb7a591b2e`

Exact source links နဲ့ evidence boundary ကို [Pinned Source Map](../references/SOURCE_MAP.md) မှာ ကြည့်နိုင်ပါတယ်။ Claim ရဲ့ verification scope ကို [Technical Claim Ledger](../references/CLAIM_LEDGER.md) မှာဖတ်နိုင်ပါတယ်။ Lewis ရဲ့ဇာတ်လမ်းနဲ့ dialogue က fictional ဖြစ်ပြီး source-backed production incident သို့မဟုတ် locally rerun test result အဖြစ် မယူရပါဘူး။

---

Previous: [Chapter 14 — ပြန်ဖွင့်လိုက်တော့ အလုပ်ဘယ်ကဆက်မလဲ](14-session-resume-after-restart.md)

Next: [Chapter 16 — ယုံကြည်ရတဲ့ Python Port တစ်ခုဖြစ်လာဖို့](16-building-a-trustworthy-port.md)

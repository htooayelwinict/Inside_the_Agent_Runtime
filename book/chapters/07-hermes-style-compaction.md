# Chapter 07 — Hermes-style Compaction

စားပွဲပေါ်မှာ project တစ်ခုအတွက် စာရွက်တွေ တစ်ရွက်ပြီးတစ်ရွက် စုပုံလာတယ်ဆိုပါစို့။ စာရွက်အားလုံးကို စားပွဲပေါ်မှာ ဖြန့်ထားရင် အသစ်တစ်ရွက်ရေးဖို့ နေရာမကျန်တော့ပါဘူး။ အဟောင်းအားလုံးကို အမှိုက်ပုံးထဲပစ်လိုက်ရင်လည်း ဘာလုပ်ပြီးပြီ၊ ဘာဆက်လုပ်ရမယ်ဆိုတာ မသိတော့ပါဘူး။

ပိုကောင်းတဲ့နည်းက အပြီးသတ်ထားတဲ့အပိုင်းတွေကို မှတ်စုတစ်ရွက်အဖြစ် ချုံ့ရေးပြီး၊ လက်ရှိကြည့်နေတဲ့စာရွက်တွေကို မူရင်းအတိုင်းထားတာပါ။ Agent Runtime ရဲ့ Compaction ကလည်း ဒီသဘောနဲ့တူပါတယ်။ Transcript တစ်ခုလုံးကို ထပ်ခါထပ်ခါပို့မယ့်အစား အဟောင်းအလယ်ပိုင်းကို summary ပြောင်းပြီး လတ်တလော context ကို ဆက်ထိန်းပါတယ်။

Hermes-style Compaction ရဲ့ အားသာချက်က “အဟောင်းကို summarize လုပ်တယ်” ဆိုတဲ့အချက်တစ်ခုတည်းမဟုတ်ပါဘူး။ Summary model ကိုမခေါ်ခင် စက်နည်းကျရှင်းလင်းခြင်း၊ summary အဟောင်းကို update လုပ်ခြင်း၊ token budget နဲ့ recent tail ရွေးခြင်းနဲ့ Tool Call/Result structure မပျက်အောင် ပြန်စစ်ခြင်းတို့ကို pipeline တစ်ခုအဖြစ် ပေါင်းထားတာပါ။ Travis234 က ဒီ behavior ကို Python runtime ထဲ port ထားပါတယ်။

## ၇.၁ Compaction က Delete လုပ်တာမဟုတ်ဘူး

Compaction ဆိုတာ active model context ကို ပိုသေးတဲ့ပုံစံနဲ့ ပြန်တည်ဆောက်တာပါ။ Conversation အဟောင်းတစ်ခုချင်းကို model ဆီပြန်ပို့မယ့်အစား အဓိပ္ပာယ်ရှိတဲ့ handoff summary တစ်ခုအဖြစ် ပြောင်းပေးပါတယ်။ Persistent session database သို့မဟုတ် log အားလုံးကို ဖျက်တယ်လို့ မဆိုလိုပါဘူး။

အလွယ်ဆုံးပုံစံနဲ့ကြည့်ရင်:

```text
Before
  system + setup + old turns + tool logs + recent turns

After
  protected head + structured summary + recent tail
```

`protected head` က system နဲ့ မဖြစ်မနေဆက်ထားရမယ့် အစပိုင်း context ပါ။ `structured summary` က ချုံ့လိုက်တဲ့အလယ်ပိုင်းရဲ့ handoff note ဖြစ်ပါတယ်။ `recent tail` က လက်ရှိအလုပ်နဲ့ အနီးဆုံး messages တွေကို မူရင်းအတိုင်းထိန်းထားတဲ့အပိုင်းပါ။

ဒီနည်းမှာ အချက်အလက်အားလုံး byte-for-byte မကျန်ပါဘူး။ Compaction က lossless archive မဟုတ်ပါဘူး။ ဒါပေမယ့် လက်ရှိအလုပ်ဆက်လုပ်ဖို့ လိုအပ်တဲ့ goal၊ progress၊ decision၊ file နဲ့ pending question တွေကို raw transcript ထက် ပိုသေးတဲ့ပုံစံနဲ့ ထိန်းဖို့ကြိုးစားတာပါ။

## ၇.၂ Pass 1 — Deterministic Pruning

Tool Result အကြီးကြီးကို summary model ဆီ အတိုင်းသားပို့ပြီး “တိုအောင်ရေးပေး” လို့ ခိုင်းနိုင်ပါတယ်။ ဒါပေမယ့် ထပ်နေတဲ့ log၊ image data နဲ့ argument အကြီးတွေကို model token အကုန်ခံပြီး ဖတ်ခိုင်းစရာမလိုပါဘူး။ Rule နဲ့ လုံလောက်တဲ့အရာကို code နဲ့အရင်ရှင်းနိုင်ပါတယ်။

Deterministic Pruning ဆိုတာ model ရဲ့အဓိပ္ပာယ်ဖော်မှုမလိုဘဲ သတ်မှတ်ထားတဲ့ rule အတိုင်း payload ကို လျှော့ခြင်းပါ။ Simplified teaching version ကို ကြည့်ရင် ဒီလိုဖြစ်ပါတယ်။

```python
def prepare_for_summary(messages):
    messages = copy_messages(messages)
    deduplicate_old_tool_outputs(messages)
    reduce_large_old_tool_results(messages)
    sanitize_large_tool_arguments(messages)
    return messages
```

ဒီ code မှာ အရေးကြီးတာက မူရင်း messages ကို တိုက်ရိုက်မပြင်ဘဲ copy လုပ်ထားတာပါ။ Pruned copy ကို summary ရေးဖို့ input အဖြစ်သုံးပြီး၊ နောက်ဆုံး model ဆီ မူရင်းအတိုင်းပြန်ပို့မယ့် protected head နဲ့ recent tail ကို raw transcript ကနေယူပါတယ်။

ဘာကြောင့် ဒီလိုခွဲရသလဲ။ Write tool တစ်ခုရဲ့ argument ထဲမှာ file content အကြီးကြီးပါနေရင် summary input အတွက် hash နဲ့ metadata လောက်ချန်ပြီး content ကိုဖြုတ်နိုင်ပါတယ်။ ဒါပေမယ့် အဲဒီ Tool Call က recent tail ထဲမှာရှိပြီး provider ဆီပြန်ပို့ရမယ်ဆိုရင် schema-valid argument မူရင်းလိုနိုင်ပါတယ်။ Pruned copy ကို provider replay အတွက်ပါသုံးလိုက်ရင် internal placeholder ကို model က တကယ့် Tool Call argument လို့ မြင်သွားနိုင်ပါတယ်။

Pass 1 မှာ အဓိကဖြေရှင်းတဲ့အရာတွေက:

- တူညီတဲ့ Tool Result အကြီးတွေထပ်နေရင် နောက်ဆုံးတစ်ခုကိုထားပြီး အဟောင်းကို duplicate marker ပြောင်းတယ်။
- Protected tail မတိုင်ခင်က Tool Result အကြီးတွေကို tool name၊ character count နဲ့ line count ပါတဲ့ အတိုချုပ် marker ပြောင်းတယ်။
- Historical Tool Call arguments အရမ်းကြီးရင် path နဲ့ လိုအပ်တဲ့ metadata ကိုထားပြီး content field ကို hash/size metadata ပြောင်းတယ်။
- နောက်ဆုံး context assemble လုပ်ပြီးနောက် historical image နဲ့ media payload တွေကို ဖြုတ်ပြီး လတ်တလောသက်ဆိုင်တဲ့ media anchor ကို ကာကွယ်တယ်။

ဒီအဆင့်က အဓိပ္ပာယ်အသစ်မရေးပါဘူး။ “ဒီ log က ဘာကိုဆိုလိုသလဲ” လို့ မဆုံးဖြတ်ဘဲ ထပ်နေခြင်း၊ အရွယ်အစားနဲ့ အသက်အဟောင်းကိုသာ ကြည့်ပါတယ်။ ဒါကြောင့် မြန်ပြီး ရလဒ်ကိုလည်း ကြိုတင်ခန့်မှန်းရလွယ်ပါတယ်။

## ၇.၃ Pass 2 — Structured Summary

Deterministic Pruning ပြီးသွားလည်း conversation အလယ်ပိုင်းမှာ user requirement၊ assistant decision နဲ့ လုပ်ပြီးသားအလုပ်တွေ ကျန်နေပါသေးတယ်။ ဒီအရာတွေကို character count နဲ့ပဲ လျှော့လို့မရပါဘူး။ အဓိပ္ပာယ်ကိုဖတ်ပြီး handoff note ပြန်ရေးရပါတယ်။ ဒါက Pass 2 ရဲ့အလုပ်ပါ။

“အပေါ်ကစကားတွေကို အတိုချုပ်ပါ” လို့ပဲ prompt ပေးရင် summary တစ်ပုဒ်ရနိုင်ပါတယ်။ ဒါပေမယ့် Agent ဆက်အလုပ်လုပ်ဖို့လိုတဲ့အချက်တွေ ထိန်းထားမယ်လို့ အာမခံမရပါဘူး။ လုပ်ပြီးသားအရာနဲ့ လုပ်ဖို့ကျန်တာ ရောနိုင်တယ်။ User ရဲ့ မေးခွန်းဟောင်းကို လက်ရှိမေးခွန်းလို ပြန်ဖတ်နိုင်တယ်။ File path နဲ့ verification result ပျောက်နိုင်ပါတယ်။

Structured Summary က summary ထဲမှာ အခန်းကဏ္ဍခွဲထားပါတယ်။ Conceptual ပုံစံက ဒီလိုပါ။

```text
Historical Task Snapshot
Historical In-Progress State
Historical Pending User Asks
Relevant Files
Historical Remaining Work
Critical Context
```

Heading အမည်ထဲမှာ `Historical` ထည့်ထားတာဟာ အလှဆင်တာမဟုတ်ပါဘူး။ Summary ထဲက “နောက်တစ်ဆင့် test ပြေးရန်” ဆိုတဲ့စာကို model က active instruction လို့ မယူဆစေဖို့ ဖြစ်ပါတယ်။ Summary ရဲ့ရှေ့မှာလည်း reference-only handoff ဖြစ်ကြောင်း၊ summary နောက်က latest user message ကိုပဲ လက်ရှိအမိန့်အဖြစ်ယူရကြောင်း boundary ထည့်ထားပါတယ်။

ဥပမာ summary ထဲမှာ “user က file ကိုဖျက်ခိုင်းထားသည်” လို့ပါနေပြီး နောက်ဆုံး user message က “မဖျက်နဲ့၊ ဘာဖြစ်နေလဲပဲ စစ်ပါ” လို့ပြောထားတယ်ဆိုပါစို့။ Latest message က အနိုင်ရရပါမယ်။ Compaction က context အဟောင်းကို ထိန်းပေးသလို stale instruction ပြန်အသက်ဝင်မလာအောင်လည်း ခွဲခြားပေးရပါတယ်။

## ၇.၄ Summary အသစ်နဲ့ Summary Update

ပထမဆုံး Compaction မှာ အဟောင်း summary မရှိသေးပါဘူး။ ဒါကြောင့် compressible middle ကိုဖတ်ပြီး structured summary အသစ်ရေးပါတယ်။ Conversation ဆက်ရှည်လာပြီး ဒုတိယအကြိမ် compact လုပ်ချိန်မှာတော့ summary အဟောင်းနဲ့ အဲဒီနောက်တိုးလာတဲ့ turns အသစ်တွေ ရှိနေပါပြီ။

ဒီအခါ အစကနေ transcript အကုန်ပြန် summarize မလုပ်ပါဘူး။ Summary အဟောင်းကို starting point အဖြစ်ယူပြီး new middle turns နဲ့ update လုပ်ပါတယ်။

```python
# simplified teaching version
if previous_summary:
    summary = update(previous_summary, newly_compacted_turns)
else:
    summary = create_summary(newly_compacted_turns)
```

`newly_compacted_turns` က previous summary နောက်ပိုင်းမှာ tail ကနေ အဟောင်းဖြစ်လာတဲ့ messages တွေပါ။ ဒါကြောင့် conversation တိုးလာတိုင်း အစကနေအဆုံးထိ ပြန်ဖတ်စရာမလိုဘဲ rolling handoff တစ်ခုရပါတယ်။

ဥပမာ ပထမ summary မှာ “parser bug ကို reproduce လုပ်ပြီး test file တွေဖတ်ထားသည်” လို့ရှိတယ်ဆိုပါစို့။ နောက်အပိုင်းမှာ implementation ပြင်ပြီး test pass သွားပြီဆိုရင် updated summary က အဟောင်း status ကို မျက်စိမှိတ်ထပ်ကူးမထားသင့်ပါဘူး။ “Bug fixed; tests passed” ဆိုတဲ့ state အသစ်နဲ့ ပြန်ညှိရပါတယ်။ Summary Update ဆိုတာ summary နှစ်ပုဒ်ကို ဆက်ကပ်တာမဟုတ်ဘဲ state ကို ပြန်ပေါင်းစည်းတာပါ။

ဒီနေရာမှာ information drift အန္တရာယ်ရှိပါတယ်။ Summary တစ်ကြိမ်ချင်းက exact wording နဲ့ detail တချို့ကို လျှော့သွားနိုင်ပါတယ်။ ဒါကြောင့် recent tail ကို raw messages အတိုင်းဆက်ထားခြင်းနဲ့ relevant file operations ကို သီးခြားထိန်းခြင်းက အရေးကြီးပါတယ်။

## ၇.၅ Head + Token-budgeted Tail

Summary ရပြီးရုံနဲ့ compacted context မပြီးသေးပါဘူး။ ဘယ် messages ကို မူရင်းအတိုင်းပြန်ထည့်မလဲ ရွေးရပါတယ်။ Travis234 ရဲ့ assembly ကို ချုံ့ရေးရင် ဒီလိုပါ။

```python
# simplified teaching version
compacted = raw_head + [summary_message] + raw_tail
compacted = repair_tool_call_result_pairs(compacted)
compacted = strip_old_media(compacted)
```

ဒီ sample မှာ `raw_head` နဲ့ `raw_tail` ဆိုတဲ့နာမည်ကို သတိထားပါ။ Pass 1 ကပြင်ထားတဲ့ pruned messages မဟုတ်ဘဲ မူရင်း transcript ကနေယူတာကို ဖော်ပြထားပါတယ်။ Pruned middle က summarizer ကိုကူညီဖို့ဖြစ်ပြီး provider ဆီ replay လုပ်မယ့် boundaries က raw data ဖြစ်ပါတယ်။

Tail ကို message count တစ်ခုတည်းနဲ့ မရွေးပါဘူး။ နောက်ဆုံးကနေ ပြန်တွက်ပြီး token budget မကျော်အောင် စုပါတယ်။ Budget အနည်းငယ်ကျော်သော်လည်း user/assistant role anchor နဲ့ Tool Call boundary မပျက်ဖို့ soft ceiling အတွင်း ချိန်ညှိနိုင်ပါတယ်။ Recent messages အနည်းဆုံးအချို့ကို ဆက်ထားပေမယ့် Tool Result တစ်ခုအရမ်းကြီးလို့ middle လုံးဝချုံ့မရတာကိုလည်း တားရပါတယ်။

Compaction ဖြတ်တဲ့နေရာက Tool Call နဲ့ Tool Result ကြားကျသွားရင် provider transcript ပျက်နိုင်ပါတယ်။ ဒါကြောင့် assembly ပြီးနောက် pair ကို ပြန်စစ်ပါတယ်။ Tool Call မရှိတော့တဲ့ orphan Tool Result ကို ဖြုတ်ပြီး၊ Tool Call ရှိပေမယ့် result က compacted middle ထဲပါသွားရင် historical result placeholder တစ်ခုထည့်ပါတယ်။ ဒီ placeholder က result အပြည့်ကို ပြန်ဖန်တီးတာမဟုတ်ပေမယ့် message protocol ကို valid ဖြစ်အောင် ထိန်းပေးပါတယ်။

## ၇.၆ Threshold Bands နဲ့ Anti-thrashing

Compaction က free operation မဟုတ်ပါဘူး။ Summary model ခေါ်ရတယ်၊ latency တိုးတယ်၊ detail တချို့ဆုံးရှုံးနိုင်တယ်။ ဒါကြောင့် context နည်းနည်းကြီးလာတိုင်း မလုပ်သင့်ပါဘူး။ Window ပြည့်ခါနီးမှပဲလုပ်မယ်ဆိုရင်လည်း recovery space မကျန်နိုင်ပါဘူး။ Threshold policy က ဒီနှစ်ဖက်ကြားကို ချိန်ပေးပါတယ်။

Travis234 မှာ configured threshold ကို 10% နဲ့ 95% ကြား ကန့်သတ်ပါတယ်။ 512K အောက် Context Window တွေအတွက် default 50% ကို အနည်းဆုံး 75% ထိမြှင့်ထားပါတယ်။ Window သေးတဲ့ model မှာ 50% ရောက်တိုင်း compact လုပ်နေရင် system prompt၊ Tool schemas၊ protected tail နဲ့ summary ကိုယ်တိုင်က နေရာယူထားလို့ turn တစ်ကြိမ်၊ နှစ်ကြိမ်အတွင်း ပြန် trigger ဖြစ်နိုင်လို့ပါ။

64K minimum trigger က effective input ထက်ကြီးသွားရင်တော့ မရောက်နိုင်တဲ့ threshold မထားဘဲ 85% fallback သုံးပါတယ်။ Summary ရေးမယ့် auxiliary model က main context ထက်သေးရင်လည်း auxiliary model ဖတ်နိုင်တဲ့ input အောက်ကို trigger လျှော့ပါတယ်။ Main model overflow မဖြစ်သေးပေမယ့် summarizer ကိုယ်တိုင် input မဆံ့တာမျိုး မဖြစ်စေဖို့ပါ။

Anti-thrashing ဆိုတာ အကျိုးမရှိတဲ့ Compaction ကို ဆက်တိုက်ပြန်လုပ်နေခြင်းအား တားတဲ့ guard ပါ။ Compaction ပြီးနောက် real provider prompt usage က threshold အောက်ကျသွားသလား စစ်ပါတယ်။ နှစ်ကြိမ်ဆက်တိုက် threshold အပေါ်မှာပဲကျန်နေရင် automatic compaction ကို ဆက်မခေါ်တော့ပါဘူး။ နောက်ပိုင်း real usage အောက်ကျလာတာ သို့မဟုတ် context window configuration ပြောင်းတာနဲ့ guard state ကို ပြန်ညှိနိုင်ပါတယ်။

Summary generation fail ဖြစ်ရင်လည်း ချက်ချင်းအကြိမ်ကြိမ်ပြန်ခေါ်မနေဘဲ cooldown သုံးပါတယ်။ Manual force compaction က cooldown ကိုရှင်းပြီး ပြန်ကြိုးစားနိုင်ပေမယ့် automatic path က နားထားပါတယ်။ Runtime တစ်ခုရဲ့ safety က “အလုပ်ဖြစ်တဲ့အချိန် ဘာလုပ်သလဲ” တင်မကဘဲ “အလုပ်မဖြစ်တဲ့ operation ကို ဘယ်အချိန်ရပ်သလဲ” ပေါ်လည်း မူတည်ပါတယ်။

## ၇.၇ Before နဲ့ After ကို လက်တွေ့နှိုင်းယှဉ်ကြည့်ခြင်း

အောက်ကဥပမာက token အတိအကျတိုင်းထားတဲ့ production trace မဟုတ်ပါဘူး။ ဘာက summary ထဲဝင်ပြီး ဘာက raw tail အဖြစ်ကျန်မလဲ မြင်ဖို့ synthetic example ဖြစ်ပါတယ်။

| Before | After |
|---|---|
| System prompt | System prompt |
| User က parser bug ပြင်ခိုင်းသည် | Structured summary: goal၊ reproduced bug၊ ဖတ်ထားသော files |
| Source file သုံးဖိုင်ရဲ့ Tool Results | Summary ထဲ relevant file list |
| Test log အကြီးနှစ်ခု၊ တစ်ခုနဲ့တစ်ခုတူ | Duplicate/reduced historical output |
| Assistant က implementation ပြင်သည် | Structured summary: change နဲ့ verification state |
| User က “error case တစ်ခုထပ်စစ်” ဟုပြောသည် | Recent user message ကို raw tail အဖြစ်ထားသည် |
| နောက်ဆုံး test result | Recent Tool Result ကို raw tail အဖြစ်ထားသည် |

After context ကို model ဖတ်တဲ့အခါ parser bug ရဲ့ history ကို summary ကနေသိနိုင်ပါတယ်။ နောက်ဆုံး user instruction နဲ့ latest test result ကိုတော့ မူရင်းအတိုင်းဖတ်ရပါတယ်။ Test log အဟောင်းရဲ့ line တိုင်းကို မသိတော့ပေမယ့် လက်ရှိဆက်လုပ်ဖို့လိုတဲ့ state ကို နေရာနည်းနည်းနဲ့ ယူလာနိုင်ပါတယ်။

ဒီ example က Compaction ရဲ့ရွေးချယ်မှုကို ပြပါတယ်။ အဟောင်းအကုန်မဖျက်သလို အကုန်လည်းမထိန်းပါဘူး။ Exact detail ထက် continuity ကို ဦးစားပေးပါတယ်။

## ၇.၈ ဘာတွေ ဆုံးရှုံးနိုင်သလဲ

Compaction က အားကောင်းပေမယ့် memory အပြည့်အစုံ မဟုတ်ပါဘူး။ အောက်ပါအချက်တွေ ဆုံးရှုံးနိုင်ပါတယ်။

### Exact wording

User ရဲ့စကားတစ်ကြောင်းကို summary က အဓိပ္ပာယ်တူအောင် ပြန်ရေးနိုင်ပေမယ့် သတ်မှတ်ချက်သေးသေးတစ်ခု ပျောက်နိုင်ပါတယ်။ “မဖျက်ရ” နဲ့ “မဖျက်သေးရ” လို nuance တွေက အရေးကြီးပါတယ်။ လတ်တလော instruction ကို raw tail ထဲထားရတဲ့အကြောင်းက ဒါပါ။

### Tool output အသေးစိတ်

Old test log ကို line count နဲ့ result marker ပြောင်းပြီးနောက် exact stack frame ကို ပြန်မေးရင် context ထဲမရှိတော့နိုင်ပါဘူး။ လိုအပ်နိုင်တဲ့ evidence ကို artifact သို့မဟုတ် file အဖြစ် သိမ်းထားပြီး summary ထဲ path ထည့်တာက ပိုကောင်းပါတယ်။

### Summary model ရဲ့အမှား

LLM summary က state တစ်ခုကို မှားပေါင်းနိုင်ပါတယ်။ Summary generation မရတဲ့အခါ deterministic fallback က continuity anchors ကို ကယ်နိုင်ပေမယ့် semantic summary လောက် မပြည့်စုံပါဘူး။ Auth သို့မဟုတ် network failure လို အခြေအနေတချို့မှာ transcript မဆုံးရှုံးစေဖို့ compaction ကို abort လုပ်ပြီး မူရင်း messages ကို ဆက်ထားနိုင်ပါတယ်။

### Media context

Historical image ကိုဖြုတ်လိုက်ရင် အဲဒီပုံထဲက pixel-level detail ကို summary က အပြည့်ပြန်မပေးနိုင်ပါဘူး။ လက်ရှိအလုပ်အတွက်လိုသေးတဲ့ image ကို recent anchor အဖြစ်ထားရပါတယ်။

ဒီအန္တရာယ်တွေကြောင့် Compaction summary ကို archive လို့ မယူဆသင့်ပါဘူး။ Continuation အတွက် handoff ဖြစ်ပါတယ်။ Exact evidence လိုအပ်ရင် file၊ test report၊ commit နဲ့ artifact လို ပြန်ဖတ်နိုင်တဲ့နေရာကို ချိတ်ထားရပါတယ်။

## ၇.၉ အနှစ်ချုပ်

- Compaction က conversation database အကုန်ဖျက်တာမဟုတ်ဘဲ active model context ကို head + summary + tail ပုံစံနဲ့ ပြန်တည်ဆောက်တာဖြစ်တယ်။
- Pass 1 က duplicate Tool Results၊ old outputs နဲ့ large arguments တွေကို deterministic rule နဲ့ လျှော့တယ်။
- Pruned transcript ကို summarizer input အဖြစ်ပဲသုံးပြီး provider replay အတွက် head နဲ့ tail ကို raw transcript ကနေယူတယ်။
- Pass 2 က task state၊ progress၊ pending asks နဲ့ relevant files ကို structured handoff အဖြစ်ရေးတယ်။
- နောက် compaction တွေမှာ summary အဟောင်းကို turns အသစ်နဲ့ iterative update လုပ်တယ်။
- Recent tail ကို fixed count တစ်ခုတည်းမဟုတ်ဘဲ token budget နဲ့ protocol boundaries နှစ်ခုလုံးကြည့်ပြီး ရွေးတယ်။
- Anti-thrashing နဲ့ failure cooldown က အကျိုးမရှိတဲ့ Compaction ကို အကြိမ်ကြိမ်မလုပ်စေဘူး။
- Compaction က continuity ကိုကူညီပေမယ့် exact transcript နဲ့ artifact တွေကို အစားမထိုးနိုင်ဘူး။

## ၇.၁၀ Source Notes

- `C-PRUNE` — `T-COMPRESS`, `H-COMPRESS`
- `C-SUMMARY` — `T-COMPRESS`, `H-COMPRESS`, `H-CONVERSATION`
- `C-TAIL` — `T-COMPRESS`, `T-POLICY`, `hermes.compaction.tail_budget`, `hermes.compaction.protected_head_decay`
- `C-BUDGET` — `T-POLICY`, `H-COMPRESS`
- `C-PAIR-SAFETY` — `T-COMPRESS`
- `C-ANTI-THRASH` — `T-COMPRESS`, `T-TIMING`
- Travis234 revision: `68b1831691b8ec93f9550ce63b80cdcb7a591b2e`
- Hermes Agent revision: `af250d84948179834820a62bfd870c0df6f264a1`

Exact source links နဲ့ evidence boundary ကို [Pinned Source Map](../references/SOURCE_MAP.md) မှာ ကြည့်နိုင်ပါတယ်။

---

Previous: [Chapter 06 — Context Window ပြည့်လာတဲ့ပြဿနာ](06-context-window-pressure.md)

Next: [Chapter 08 — Pi နဲ့ Hermes တွေ့ဆုံရာ](08-pi-meets-hermes.md)

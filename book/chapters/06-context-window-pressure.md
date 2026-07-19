# Chapter 06 — Context Window ပြည့်လာတဲ့ပြဿနာ

Agent နဲ့ စကားပြောတာကြာလာရင် မေးခွန်းဟောင်းတွေကို screen ပေါ်မှာ ပြန်ဆွဲကြည့်လို့ရပါတယ်။ ဒါကြောင့် model ကလည်း အစကနေ အဆုံးအထိ အကုန်မှတ်မိနေမယ်လို့ ထင်လွယ်ပါတယ်။ တကယ်တမ်း model က မြင်ရတာက chat screen မဟုတ်ပါဘူး။ Request တစ်ကြိမ်ပို့တိုင်း ထည့်ပေးလိုက်တဲ့ context ပဲ ဖြစ်ပါတယ်။

ဒီ context ထဲမှာ user နဲ့ assistant ရဲ့စာသားတင် မဟုတ်ပါဘူး။ System prompt၊ Tool definition၊ Tool Call၊ Tool Result၊ image နဲ့ နောက်ဆုံးအဖြေအတွက်ချန်ထားတဲ့ output space တွေပါ နေရာယူပါတယ်။ Coding Agent တစ်ခုမှာ file အကြီးတစ်ဖိုင်ဖတ်လိုက်တာ၊ test log ရှည်ရှည်တစ်ခုရလိုက်တာနဲ့ chat စာကြောင်းဆယ်ကြောင်းထက် context ပိုမြန်မြန်ကြီးသွားနိုင်ပါတယ်။

Context Window ပြည့်လာတာကို ဖြေရှင်းဖို့ Compaction ကို နားလည်ရပါမယ်။ ဒါပေမယ့် ဘာကိုချုံ့နေတာလဲ မသိဘဲ Compaction code ကို တန်းဖတ်ရင် threshold နဲ့ token formula တွေကြားမှာပဲ လမ်းပျောက်သွားတတ်ပါတယ်။ ဒါကြောင့် Context Window ထဲမှာ ဘာတွေဝင်နေသလဲဆိုတာကနေ စကြည့်ပါမယ်။

## ၆.၁ Model မြင်ရတဲ့ စာမျက်နှာ

Context Window ဆိုတာ model က request တစ်ကြိမ်အတွင်း ဖတ်နိုင်တဲ့ token စုစုပေါင်း အကန့်အသတ်ပါ။ Notebook စာမျက်နှာတစ်ရွက်လို စဉ်းစားနိုင်ပါတယ်။ အရင်ရေးထားတာတွေ များလာရင် စာအသစ်ရေးဖို့နေရာ နည်းလာပါတယ်။

Notebook ဥပမာနဲ့ မတူတဲ့အချက်က Agent Runtime က စာမျက်နှာပေါ်မှာ ဘာထည့်ပေးမလဲဆိုတာ တစ်ကြိမ်ချင်း ပြန်တည်ဆောက်နိုင်တာပါ။ Chat history အကုန်ကို အစဉ်လိုက်ပို့နိုင်သလို၊ အဟောင်းတချို့ကို summary ပြောင်းပြီး recent messages ကို အပြည့်အစုံပို့နိုင်ပါတယ်။ Model မှာ conversation database တစ်ခုလုံးကို ကိုယ်တိုင်ပြန်ဖတ်နိုင်တဲ့ အခွင့်အရေးမရှိပါဘူး။ Runtime ထည့်ပေးတဲ့ context ကိုပဲ မြင်ရပါတယ်။

ပုံမှန် Agent request တစ်ခုကို ချုံ့ကြည့်ရင် ဒီလိုပါ။

```text
system instructions
+ tool schemas
+ conversation messages
+ tool calls and tool results
+ images or other media
+ space reserved for the next answer
-------------------------------------
context window
```

Screen ပေါ်မှာ user message နှစ်ကြောင်းပဲရှိနေလို့ request သေးမယ်လို့ မပြောနိုင်ပါဘူး။ Tool schemas အများကြီးရှိတာ၊ system prompt ရှည်တာနဲ့ အရင် Tool Results တွေကို ပြန်ပို့နေရတာက မမြင်သာတဲ့ကုန်ကျစရိတ် ဖြစ်ပါတယ်။

## ၆.၂ Token ဆိုတာ စာလုံးအရေအတွက် မဟုတ်ဘူး

Model က text ကို character တစ်လုံးချင်း မဖတ်ပါဘူး။ Token လို့ခေါ်တဲ့ အပိုင်းငယ်တွေခွဲပြီး ဖတ်ပါတယ်။ English word တစ်လုံးက token တစ်ခုဖြစ်နိုင်သလို၊ punctuation နဲ့ code fragment တွေက သီးခြား token ဖြစ်နိုင်ပါတယ်။ မြန်မာစာလည်း tokenizer အလိုက် စာလုံး၊ အသံစုနဲ့ byte အပိုင်းတွေကွဲနိုင်လို့ “စာလုံးလေးထောင်ဆို token တစ်ထောင်” လို့ ဘာသာစကားတိုင်းအတွက် တိတိကျကျမတွက်နိုင်ပါဘူး။

Runtime က request မပို့ခင် exact provider tokenizer အမြဲမရှိနိုင်ပါဘူး။ ဒါကြောင့် character count၊ message overhead နဲ့ image estimate တွေကိုသုံးပြီး rough token count တစ်ခုတွက်တတ်ပါတယ်။ Rough estimate က ဆုံးဖြတ်ချက်အတွက် အသုံးဝင်ပေမယ့် provider တကယ်လက်ခံခဲ့တဲ့ prompt token နဲ့ တစ်ထပ်တည်းဖြစ်မယ်လို့ မယူဆရပါဘူး။

ဒီကွာခြားချက်ကြောင့် Travis234 က တိုင်းတာချက်နှစ်မျိုးကို သီးခြားစဉ်းစားပါတယ်။

- Request မပို့ခင် context ကြီးနေပြီလားသိဖို့ estimated tokens ကိုသုံးတယ်။
- Response ပြန်ရပြီးနောက် compaction တကယ်လုံလောက်သလားသိဖို့ provider ရဲ့ prompt usage ကိုသုံးတယ်။

Estimate က မီးခိုးမြင်ပြီး မီးရှိနိုင်တယ်လို့ သတိပေးတာပါ။ Provider usage က အပူချိန်ကို တကယ်တိုင်းတာပေးတာနဲ့တူပါတယ်။ နှစ်ခုထဲက တစ်ခုကိုပဲယုံရင် စောလွန်းတဲ့ compaction သို့မဟုတ် နောက်ကျလွန်းတဲ့ overflow ဖြစ်နိုင်ပါတယ်။

## ၆.၃ Output အတွက် နေရာချန်ထားရတယ်

Model ရဲ့ context limit က input အတွက်ပဲ သီးသန့်မဟုတ်ပါဘူး။ Provider နဲ့ model configuration ပေါ်မူတည်ပြီး နောက်ထုတ်မယ့် output အတွက်ပါ capacity ကို စဉ်းစားရပါတယ်။ Input က window အပြည့်နီးပါးယူထားရင် model မှာ အဖြေရှည်ရေးဖို့ နေရာမကျန်တော့ပါဘူး။

အလွယ်ဆုံးတွက်ပုံက:

```python
# simplified teaching version
effective_input = context_window - reserved_output
trigger = int(effective_input * threshold_ratio)
```

`effective_input` က request payload သုံးနိုင်တဲ့နေရာပါ။ `trigger` က အဲဒီနေရာ ဘယ်လောက်သုံးပြီးချိန်မှာ Compaction စဉ်းစားမလဲဆိုတာကို မှတ်ထားပါတယ်။

Context Window က 128,000 tokens ဖြစ်ပြီး output အတွက် 8,000 tokens ချန်ထားတယ်ဆိုပါစို့။ Effective input က 120,000 tokens ဖြစ်ပါတယ်။ Small-context policy အရ 75% မှာ trigger လုပ်မယ်ဆိုရင် 90,000 tokens ဝန်းကျင်ရောက်ချိန်မှာ Compaction စဉ်းစားပါမယ်။

```text
128,000  full context
- 8,000  reserved output
--------
120,000  effective input
x  0.75  threshold ratio
--------
 90,000  compaction trigger
```

ဒီ 90,000 က model အားလုံးအတွက် သတ်မှတ်ထားတဲ့ ပုံသေကိန်းမဟုတ်ပါဘူး။ Context Window အရွယ်အစား၊ output reserve၊ configured ratio နဲ့ summary ရေးမယ့် auxiliary model ရဲ့ capacity အလိုက် ပြောင်းပါတယ်။ Formula ရဲ့ရည်ရွယ်ချက်က “ပြည့်မှလုပ်မယ်” မဟုတ်ဘဲ အဖြေရေးဖို့နဲ့ ပြန်လည်ပြင်ဆင်ဖို့ headroom ချန်ထားဖို့ ဖြစ်ပါတယ်။

Window အရမ်းသေးလို့ minimum trigger ကို မရောက်နိုင်တဲ့အခါလည်း ရှိပါတယ်။ ဥပမာ effective input 28,000 ပဲရှိတဲ့ model ကို minimum 64,000 ရောက်မှ compact လုပ်မယ်ဆိုရင် အဲဒီ trigger က ဘယ်တော့မှ မရောက်နိုင်ပါဘူး။ ဒီလိုအခါ Travis234 policy က effective input ရဲ့ 85% ဝန်းကျင်ကို reachable fallback အဖြစ်ပြောင်းပါတယ်။ Policy တစ်ခုက သင်္ချာအရမှန်ရုံနဲ့ မလုံလောက်ဘဲ လက်တွေ့ရောက်နိုင်ရပါမယ်။

## ၆.၄ Tool Result က ဘာကြောင့် context ကို မြန်မြန်ပြည့်စေတာလဲ

Coding Agent တစ်ခုက user နဲ့ စကားပြောတာထက် tools နဲ့ အလုပ်လုပ်တဲ့အချိန်ပိုများနိုင်ပါတယ်။ `read_file` က source file တစ်ခုလုံးပြန်ပေးတယ်။ Test runner က stack trace ရှည်ရှည်ထုတ်တယ်။ Search tool က တူညီတဲ့စာကြောင်းတွေကို file အများကြီးကနေ ပြန်ပေးတယ်။ ဒီ output တွေအားလုံးက နောက် model call မှာ history အဖြစ်ပြန်ပါလာနိုင်ပါတယ်။

User က “test ကိုပြင်ပေး” လို့ လေးလုံးလောက်ပဲပြောပေမယ့် Agent က ဒီလိုအလုပ်လုပ်နိုင်ပါတယ်။

1. Test file ကိုဖတ်တယ်။
2. Implementation file သုံးဖိုင်ဖတ်တယ်။
3. Test suite ပြေးပြီး log ရှည်ရှည်ရတယ်။
4. File ပြင်တယ်။
5. Test suite ထပ်ပြေးတယ်။

အဆင့်တိုင်းရဲ့ Tool Result ကို အပြည့်အစုံပြန်ပို့နေရင် တူညီတဲ့ source နဲ့ log အပိုင်းတွေ context ထဲမှာ ထပ်နေပါမယ်။ Conversation ရဲ့အဓိပ္ပာယ်က အများကြီးမပြောင်းပေမယ့် payload က မြန်မြန်ကြီးလာပါတယ်။

Image ကလည်း ပြဿနာတူပါတယ်။ Text လို character count တိုက်ရိုက်မရလို့ runtime က token cost တစ်ခု ခန့်မှန်းရပါတယ်။ Historical screenshot တွေကို turn တိုင်းပြန်ပို့နေရင် user မြင်တဲ့စာအရေအတွက် မတိုးပေမယ့် model request က ကြီးလာနိုင်ပါတယ်။

ဒါကြောင့် Compaction ရဲ့ ပထမဆုံး target က user ရဲ့အဓိကစကား မဟုတ်ဘဲ အဟောင်းဖြစ်သွားတဲ့ Tool Results၊ ထပ်နေတဲ့ output နဲ့ historical media တွေဖြစ်တတ်ပါတယ်။

## ၆.၅ History ကို ဖြေရှင်းနိုင်တဲ့နည်းလေးမျိုး

Context ပြည့်လာတဲ့အခါ Runtime က ရွေးချယ်နိုင်တဲ့နည်းတွေကို အလွယ်ကနေ စကြည့်ပါမယ်။

### ဘာမှမလုပ်ဘဲ ဆက်ပို့ခြင်း

Conversation တိုနေရင် ဒါကအကောင်းဆုံးပါပဲ။ Compaction လုပ်တိုင်း အချက်အလက်ဆုံးရှုံးနိုင်ပြီး summary model ခေါ်ရတဲ့ကုန်ကျစရိတ်လည်းရှိပါတယ်။ ပြဿနာမရှိသေးဘဲ ကြိုချုံ့နေတာက အကျိုးမရှိပါဘူး။

### အဟောင်းဆုံး message ကို ဖြုတ်ခြင်း

အလွယ်ဆုံး sliding window ပုံစံပါ။ ဒါပေမယ့် အစက user requirement၊ file path နဲ့ design decision တို့ အဟောင်းထဲပါသွားရင် အဓိက context ပျောက်နိုင်ပါတယ်။ Tool Call ကိုထားပြီး သူ့ Tool Result ကိုဖြုတ်မိတာလို transcript structure ပျက်တာလည်း ဖြစ်နိုင်ပါတယ်။

### ကြီးတဲ့ output တွေကို ဖြတ်ခြင်း

Old Tool Result ကို “result အဟောင်းကိုချုံ့ထားသည်” ဆိုတဲ့ placeholder ပြောင်းခြင်း၊ duplicate output ကိုတစ်ခုတည်းထားခြင်းနဲ့ historical image ဖြုတ်ခြင်းတို့က token အများကြီးသက်သာစေပါတယ်။ ဒါပေမယ့် အရင် result ထဲက exact error line ကို နောက်မှပြန်လိုရင် မရှိတော့နိုင်ပါဘူး။

### Structured Compaction လုပ်ခြင်း

အဟောင်းဆုံး message ကို မျက်စိမှိတ်ဖြုတ်မယ့်အစား conversation အလယ်ပိုင်းကို structured summary ပြောင်းပါတယ်။ အစပိုင်းက system နဲ့ setup context တချို့၊ နောက်ဆုံး recent messages နဲ့ လက်ရှိ user focus ကို အပြည့်အစုံထားပါတယ်။ ဒီနည်းက အဓိပ္ပာယ်ကို ဆက်သယ်နိုင်ပေမယ့် summary မှာမပါသွားတဲ့အသေးစိတ်ကိုတော့ ပြန်မရနိုင်ပါဘူး။

Travis234 က နောက်ဆုံးနည်းကို deterministic cleanup နဲ့ တွဲသုံးပါတယ်။ ဘာကို ဘယ်လိုချုံ့သလဲဆိုတာ Chapter 07 မှာ တစ်ဆင့်ချင်းကြည့်ပါမယ်။

## ၆.၆ Head၊ Middle နဲ့ Tail

Conversation ကို Compaction အမြင်နဲ့ကြည့်ရင် အပိုင်းသုံးပိုင်းခွဲနိုင်ပါတယ်။

```text
[ protected head ] [ compressible middle ] [ recent tail ]
```

`head` မှာ system message နဲ့ အစပိုင်း setup အချို့ ပါနိုင်ပါတယ်။ `middle` က အဟောင်းဖြစ်သွားတဲ့ turns တွေဖြစ်ပြီး summary အဖြစ်ပြောင်းနိုင်ပါတယ်။ `tail` က လက်ရှိအလုပ်နဲ့အနီးဆုံး recent messages တွေဖြစ်လို့ မူရင်းအတိုင်းထားဖို့ကြိုးစားပါတယ်။

Tail ကို “နောက်ဆုံး message ၂၀ ခု” လို့ message count တစ်ခုတည်းနဲ့ ထိန်းရင် tool output အကြီးတစ်ခုက budget အကုန်စားနိုင်ပါတယ်။ ဒါကြောင့် token budget ကို အဓိကထားပြီး message boundary နဲ့ Tool Call/Result pair မပျက်အောင် ချိန်ညှိရပါတယ်။ Tail က budget ထဲဝင်ရုံမက conversation အဓိပ္ပာယ်ကို ဆက်ဖတ်လို့ရအောင် user နဲ့ assistant role anchors တွေလည်း လိုပါတယ်။

အစပိုင်း setup ကို အမြဲအပြည့်ထားရင် အဲဒီစာတွေက ချုံ့လို့မရတဲ့အပိုင်းအဖြစ် ဆက်နေရာယူပါတယ်။ Travis234 ရဲ့ rolling compaction မှာ summary ရှိပြီးနောက် အစပိုင်း message တွေကို ထိန်းထားတဲ့ protection ကို လျှော့နိုင်ပေမယ့် system boundary နဲ့ recent context ကို ဆက်ကာကွယ်ပါတယ်။ ဒီနေရာမှာ “ဘာမှမပျောက်စေဘဲ အရွယ်အစားလျှော့မယ်” ဆိုတာ မဖြစ်နိုင်ပါဘူး။ လက်ရှိအလုပ်အတွက် ဘာကအရေးကြီးသလဲကို ရွေးပေးရတာပါ။

## ၆.၇ Rough Estimate နဲ့ Real Usage

Compaction မလုပ်ခင် runtime က request မပို့ရသေးတဲ့အတွက် estimated tokens ကိုသုံးရပါတယ်။ Estimate က trigger ကျော်နေပြီဆိုရင် preflight compaction လုပ်နိုင်ပါတယ်။ ဒါပေမယ့် estimate က provider tokenizer နဲ့ကွာနိုင်လို့ compaction လုပ်ပြီးချက်ချင်း ထပ်လုပ်နေမိတာမျိုး ဖြစ်နိုင်ပါတယ်။

ဒါကိုရှောင်ဖို့ compaction ပြီးနောက် provider ရဲ့ real prompt usage ကို စောင့်ကြည့်ပါတယ်။ Real usage က threshold အောက်ကျသွားရင် အလုပ်ဖြစ်တယ်လို့ ယူဆနိုင်ပါတယ်။ Threshold အပေါ်မှာပဲ ဆက်ရှိနေရင် protected context ကိုယ်တိုင်ကြီးနေတာ သို့မဟုတ် summary က လုံလောက်အောင်မချုံ့နိုင်တာ ဖြစ်နိုင်ပါတယ်။ အဲဒီအချိန်မှာ တူညီတဲ့ operation ကို မရပ်မနားပြန်လုပ်တာထက် anti-thrashing guard နဲ့ ခဏရပ်ဖို့လိုပါတယ်။

ဒီ flow ကို ချုံ့ကြည့်ရင်:

```text
rough estimate crosses trigger
              ↓
        compact context
              ↓
send the next provider request
              ↓
check real prompt usage
       ↙                 ↘
below trigger        still above trigger
reset guard          record ineffective pass
```

Estimate နဲ့ real usage ကို ခွဲထားတာက implementation detail သက်သက်မဟုတ်ပါဘူး။ Runtime က မသေချာတဲ့အချက်နဲ့ ကြိုတင်ဆုံးဖြတ်ပြီး၊ အလုပ်ပြီးမှ အမှန်တကယ်တိုင်းတာချက်နဲ့ ကိုယ့်ဆုံးဖြတ်ချက်ကို ပြန်စစ်တဲ့ feedback loop ဖြစ်ပါတယ်။

## ၆.၈ မှားလွယ်တဲ့နေရာများ

### Context Window နဲ့ chat history ကို တူတယ်ထင်ခြင်း

UI မှာ history ရှိနေခြင်းက request တိုင်း model ဆီ အပြည့်အစုံပို့နေတယ်လို့ မဆိုလိုပါဘူး။ Compacted summary၊ database history နဲ့ current provider context က သီးခြားအလွှာတွေဖြစ်နိုင်ပါတယ်။

### Limit ပြည့်မှ စတင်ဖြေရှင်းခြင်း

Output space မချန်ထားဘဲ input ကို capacity အပြည့်နီးပါးပို့ရင် request reject ဖြစ်နိုင်သလို အဖြေတိုသွားနိုင်ပါတယ်။ Trigger ကို effective input အောက်မှာထားရပါတယ်။

### Token estimate ကို exact count လို့ယူဆခြင်း

Character-based estimate က language၊ provider နဲ့ media cost အလိုက်လွဲနိုင်ပါတယ်။ Available ဖြစ်တဲ့အခါ provider prompt usage နဲ့ ပြန်တိုက်ရပါတယ်။

### Oldest message ကို မျက်စိမှိတ်ဖြုတ်ခြင်း

အဟောင်းဖြစ်တာနဲ့ မလိုအပ်တော့တာ မတူပါဘူး။ အစက requirement နဲ့ file decision က recent chatter ထက် ပိုအရေးကြီးနိုင်ပါတယ်။

## ၆.၉ အနှစ်ချုပ်

- Context Window က chat screen မဟုတ်ဘဲ request တစ်ကြိမ်မှာ model ဖတ်နိုင်တဲ့ token capacity ဖြစ်တယ်။
- System prompt၊ Tool schemas၊ messages၊ Tool Results၊ images နဲ့ output reserve တွေအားလုံးက window ကို မျှသုံးတယ်။
- Coding Agent မှာ Tool Results နဲ့ repeated logs က context ကို အမြန်ဆုံးကြီးစေတတ်တယ်။
- Trigger ကို full window ပေါ်မတွက်ဘဲ output ချန်ထားပြီး effective input ပေါ်တွက်ရတယ်။
- Rough token estimate က preflight ဆုံးဖြတ်ချက်အတွက်ဖြစ်ပြီး provider usage က compaction ထိရောက်မှုကို ပြန်စစ်ဖို့ဖြစ်တယ်။
- Safe Compaction က protected head၊ summarized middle နဲ့ recent token-budgeted tail ကို ခွဲစဉ်းစားရတယ်။

## ၆.၁၀ Source Notes

- `C-BUDGET` — `T-POLICY`, `T-COMPRESS`
- `C-TAIL` — `T-COMPRESS`, `T-POLICY`, `hermes.compaction.tail_budget`, `hermes.compaction.protected_head_decay`
- `C-ANTI-THRASH` — `T-COMPRESS`, `T-TIMING`
- Travis234 revision: `68b1831691b8ec93f9550ce63b80cdcb7a591b2e`
- Hermes Agent revision: `af250d84948179834820a62bfd870c0df6f264a1`

Exact source links နဲ့ evidence boundary ကို [Pinned Source Map](../references/SOURCE_MAP.md) မှာ ကြည့်နိုင်ပါတယ်။

---

Previous: [Chapter 05 — Tool Execution နှင့် Bounded Concurrency](05-tool-execution-bounded-concurrency.md)

Next: [Chapter 07 — Hermes-style Compaction](07-hermes-style-compaction.md)

# Writing Style Guide

ဒီ guide က Travis234 Book ရဲ့ Burmese-first author voice နဲ့ technical accuracy ကို တစ်သမတ်တည်းဖြစ်စေဖို့ သုံးတာပါ။ Chapter တွေကို စက်ရုပ်ဆန်တဲ့ပုံစံတစ်မျိုးတည်းဖြစ်အောင် ဖိအားပေးဖို့မဟုတ်ပါဘူး။

## 1. Problem နဲ့ စပါ

ခက်ခဲတဲ့ concept တစ်ခုကို definition ကြီးနဲ့ ချက်ချင်းမစပါနဲ့။ Reader ကြုံနိုင်တဲ့ problem သို့မဟုတ် question ကို အရင်ပေးပါ။

```text
မကောင်း: Compaction is a process that reduces context size.
ကောင်း: Tool result တွေများလာပြီး Context Window ပြည့်တော့မယ်ဆိုရင် ဘာလုပ်မလဲ။
```

ပုံမှန် learning flow က အောက်ပါအတိုင်းဖြစ်ပါတယ်။

1. Problem သို့မဟုတ် question
2. Mental model
3. Source mapping
4. Execution flow
5. Small example သို့မဟုတ် lab
6. Failure modes
7. Takeaways
8. Source Notes

Chapter အကြောင်းအရာပေါ်မူတည်ပြီး မလိုအပ်တဲ့အပိုင်းကို ချန်ထားနိုင်ပါတယ်။

## 2. Natural Burmese ကို သုံးပါ

Explanation နဲ့ sentence flow ကို မြန်မာလိုရေးပါ။ English technical term ကို မဖြစ်မနေဘာသာပြန်လို့ စာကြောင်းဖတ်ရခက်သွားရင် English အတိုင်းထားပါ။

```text
မကောင်း: ကိုယ်စားလှယ် လည်ပတ်ကွင်းသည် ကိရိယာရလဒ်ကို ထည့်သွင်းသည်။
ကောင်း: Agent Loop က Tool Result ကို context ထဲ ပြန်ထည့်ပြီး model ကို ဆက်ခေါ်တယ်။
```

“ကျွန်တော်တို့”, “ဆိုပါစို့”, “ဒါပေမယ့်”, “ဥပမာ” လို conversational connectors တွေကို လိုအပ်သလောက် သုံးနိုင်ပါတယ်။ Paragraph တိုင်းမှာ အတင်းထည့်ဖို့ မလိုပါဘူး။

## 3. Reference style ကို မတုပပါနဲ့

[Software Engineering](https://se.saturngod.net/) စာအုပ်ရဲ့ problem-first structure၊ numbered subsections၊ analogy နဲ့ natural Burmese explanation ကို high-level teaching reference အဖြစ် ယူထားပါတယ်။ မူရင်းစာကြောင်း၊ ထူးခြားတဲ့ဖော်ပြပုံနဲ့ typo/spacing တွေကို မကူးပါဘူး။ Travis234 Book က မူရင်း `Agentic-AI-Book` ရဲ့ author voice ကိုပဲ ဆက်ထိန်းပါတယ်။

Reference ရဲ့ အဓိကအားသာချက်က term တစ်ခုကို academic definition နဲ့ မစဘဲ developer တွေကြုံနေကျအခြေအနေတစ်ခုကနေ စတာပါ။ ပြီးမှ “ဒါကို ဘာလို့ခေါ်သလဲ”၊ “ဘာကြောင့်လိုသလဲ” နဲ့ “လက်တွေ့မှာ ဘယ်လိုသုံးသလဲ” ဆိုတဲ့အစီအစဉ်အတိုင်း ဆက်သွားပါတယ်။ Travis234 Book မှာလည်း ဒီ teaching rhythm ကို ဦးစားပေးရပါမယ်။

### Main prose rules

- Section တစ်ခုရဲ့ ပထမ paragraph မှာ reader သိပြီးသားအခြေအနေ၊ မေးခွန်း သို့မဟုတ် ရိုးရိုးဥပမာတစ်ခု ပါရမယ်။
- Technical term ကို ပထမဆုံးသုံးတဲ့အခါ “`Term` ဆိုတာ…” ပုံစံနဲ့ တိုက်ရိုက်ရှင်းပါ။ Definition အပြီးမှာ ဘာကြောင့်အရေးကြီးသလဲ ဆက်ပြောပါ။
- Paragraph တစ်ပိုဒ်မှာ idea တစ်ခုကိုပဲ အဓိကထားပါ။ Exception နဲ့ caveat အများကြီးရှိရင် နောက် paragraph သို့မဟုတ် Failure Modes section ကို ရွှေ့ပါ။
- အိမ်ဆောက်ခြင်း၊ လူတန်းစီခြင်း၊ အလုပ်လွှဲစာနဲ့ လမ်းကြောင်းလို everyday analogy တွေကို concept ရှင်းစေမှ သုံးပါ။ Analogy ကို အကြာကြီးဆက်မဆွဲပါနဲ့။
- “အောက်ပါအတိုင်းဖြစ်သည်” လို report tone ထက် “ဆိုပါစို့”၊ “ဒီနေရာမှာ”၊ “ဒါကြောင့်” လို natural transition ကို ဦးစားပေးပါ။
- Table ကို exact comparison အတွက်ပဲ သုံးပါ။ ရိုးရိုး explanation ကို bullet နဲ့ table အများကြီးခွဲပြီး textbook summary လို မဖြစ်စေပါနဲ့။
- Section အဆုံးမှာ reader မှတ်ထားသင့်တဲ့အချက်တစ်ခုကို natural sentence နဲ့ပိတ်ပါ။ “မှတ်ထားရမည့်အချက်” ဆိုတဲ့ phrase ကို အခန်းတစ်လျှောက် ထပ်ခါထပ်ခါမသုံးပါနဲ့။
- Source ID၊ revision နဲ့ evidence boundary တွေကို Source Notes မှာထားပါ။ Main prose ထဲမှာ ရင်းမြစ်အကြောင်းပြောရမယ်ဆို reader flow မပျက်အောင် file name လောက်သာသုံးပါ။

### Sentence rhythm

စာကြောင်းတိုချည်း ဆက်ရေးရင် note စာရင်းလိုဖြစ်သွားနိုင်ပြီး စာကြောင်းရှည်ချည်းရေးရင် ဖတ်ရခက်ပါတယ်။ အကြောင်းအရာဖွင့်တဲ့စာကြောင်းကို တိုတိုထားပြီး နောက်စာကြောင်းမှာ အကြောင်းရင်းရှင်းပါ။ တတိယစာကြောင်းမှာ ဥပမာပေးတဲ့ short–medium–short rhythm ကို သဘာဝကျသလောက် သုံးနိုင်ပါတယ်။

```text
Agent Loop က model ကို ပြန်ခေါ်ပေးရုံ မဟုတ်ပါဘူး။ Tool Result ဘယ်အချိန်ပြန်ထည့်မလဲ၊ turn ဘယ်အချိန်ပြီးမလဲဆိုတာပါ ထိန်းရပါတယ်။ Order မှားသွားရင် result မှန်နေလည်း runtime behavior မှားနိုင်ပါတယ်။
```

### စာအုပ်ရေးခြင်းနဲ့ Architecture Review ကို ခွဲပါ

Main chapter က repository assessment report မဟုတ်ပါဘူး။ Component အမည်၊ file path နဲ့ parity status တွေကို တန်းစီပြောတာထက် reader က concept ကို သူ့စိတ်ထဲမှာ တည်ဆောက်နိုင်အောင် သင်ပြရပါမယ်။ Architecture review အတွက်လိုတဲ့ evidence ကို မဖျောက်ဘဲ Source Notes နဲ့ appendix ဆီ ရွှေ့ထားပါ။

```text
Review tone: `_execute_parallel()` က tasks တွေကို coordinator ထဲပို့ပြီး source-ordered results ပြန်တည်ဆောက်ထားသည်။

Teaching tone: Tool နှစ်ခုကို တစ်ပြိုင်နက် run လိုက်ရင် နောက်မှစတဲ့ tool က အရင်ပြီးနိုင်ပါတယ်။ ဒါပေမယ့် model ဆီ result ပြန်ပို့တဲ့အခါ မူလ Tool Call အစီအစဉ်ကို မပျက်စေရပါဘူး။ Travis234 က အလုပ်ပြီးတဲ့အချိန်နဲ့ result ပြန်စီတဲ့အချိန်ကို ခွဲထားတာ ဒီအကြောင်းကြောင့်ပါ။
```

Main prose ရဲ့ဦးစားပေးအစီအစဉ်က:

1. Reader ကြုံနိုင်တဲ့အခြေအနေ
2. ရိုးရိုးရှင်းရှင်းရှင်းလင်းချက်
3. အသေးစား code sample သို့မဟုတ် flow
4. Code ထဲမှာ state ဘယ်လိုပြောင်းသွားသလဲ
5. ဒီ design ကို ဘာကြောင့်ရွေးထားသလဲ
6. မှားရေးမိရင် ဘာဖြစ်နိုင်သလဲ

File inventory၊ claim IDs နဲ့ revision details တွေက ဒီ learning flow ပြီးမှ လာရပါမယ်။

### Code sample ကို ဘယ်လိုသင်ပြမလဲ

Code block မပြခင် “ဒီ code က ဘယ်မေးခွန်းကို ဖြေမလဲ” ဆိုတာ တစ်ပိုဒ်နဲ့ရှင်းပါ။ Code block အပြီးမှာ line တစ်ကြောင်းချင်း ဘာသာပြန်မနေဘဲ state change နဲ့ execution flow ကို ပြောပါ။

- Sample တစ်ခုကို ၅ ကြောင်းမှ ၂၀ ကြောင်းအတွင်းထားနိုင်သလောက်ထားပါ။
- Production source ကို ချုံ့ထားရင် `simplified teaching version` လို့ label တပ်ပါ။
- Variable name တစ်ခုကို စတင်သုံးတဲ့အခါ သူက ဘာကိုမှတ်ထားသလဲ ရှင်းပါ။
- Output သို့မဟုတ် event order ကို reader ကြိုတင်ခန့်မှန်းကြည့်နိုင်အောင် မေးခွန်းသေးသေးတစ်ခုထည့်ပါ။
- Code ပြပြီးနောက် “ဒါကြောင့်ဘာဖြစ်သွားလဲ” ဆိုတဲ့ consequence ကို ပြန်ချိတ်ပါ။

## 4. Canonical terms

| Use | Avoid as the primary term |
|---|---|
| Agent Loop | Agent စက်ဝိုင်း |
| Tool Call | ကိရိယာခေါ်ဆိုမှု only |
| Tool Result | ကိရိယာရလဒ် only |
| Context Window | ဆက်စပ်အကြောင်းအရာ ပြတင်းပေါက် |
| Compaction | အပြည့်အဝ မြန်မာဘာသာပြန်ထားသော term |
| Bounded Concurrency | limit မရှင်းသော parallelism |

Term ကို ပထမဆုံးသုံးတဲ့နေရာမှာ မြန်မာလိုအဓိပ္ပာယ်ရှင်းပြနိုင်ပါတယ်။ နောက်ပိုင်းမှာ canonical English term ကိုပဲ ဆက်သုံးပါ။

## 5. Code နဲ့ Source

- Code excerpt က concept တစ်ခုတည်းကို ပြနိုင်အောင်တိုပါစေ။
- Upstream code ကိုအများကြီးကူးမထည့်ဘဲ original explanation နဲ့ diagram ကို ဦးစားပေးပါ။
- Simplified code ကို production implementation လို့ မဖော်ပြပါနဲ့။
- Runtime behavior claim တိုင်းမှာ Source Notes သို့မဟုတ် Claim Ledger reference ပါရမယ်။
- Test မပြေးထားရင် ပြေးထားသလို မရေးပါနဲ့။ Repository ထဲက recorded result နဲ့ locally verified result ကို ခွဲရေးပါ။

## 6. Diagram နဲ့ Example

Ordering၊ branching နဲ့ state change ကို prose ထက် ပိုရှင်းစေမှ Mermaid diagram သုံးပါ။ Diagram တစ်ခုထဲမှာ concept အများကြီး မထည့်ပါနဲ့။

Example တွေက:

- API key မလိုဘဲ run နိုင်ရမယ်၊ သို့မဟုတ် pseudocode လို့ ရှင်းရှင်းလင်းလင်းပြောရမယ်၊
- real system ကို default အနေနဲ့ mutate မလုပ်ရဘူး၊
- expected result သို့မဟုတ် event order ပါရမယ်၊
- limitation ကို ဖော်ပြရမယ်။

## 7. Final language pass

Chapter ပြီးတိုင်း အောက်ပါအချက်တွေကို ပြန်စစ်ပါ။

- sentence တစ်ကြောင်း အရမ်းရှည်နေသလား
- English/Burmese spacing မညီတာရှိသလား
- term တစ်ခုကို နာမည်အမျိုးမျိုးနဲ့ ခေါ်ထားသလား
- direct translation လို robotic ဖြစ်နေသလား
- analogy က implementation အမှန်နဲ့ ရောထွေးနိုင်သလား
- claim ကို source က တကယ်ထောက်ခံသလား
- paragraph တွေက documentation bullet list လို အလွန်ကွဲနေသလား
- “ဒီ chapter မှာ”၊ “မှတ်ထားရမယ့်အချက်” နဲ့ “အရေးကြီးပါတယ်” ကို မလိုအပ်ဘဲ ထပ်သုံးထားသလား
- section အစမှာ term definition မတိုင်ခင် reader နားလည်နိုင်တဲ့ context ရှိသလား
- main prose က source audit report လိုဖြစ်နေပြီး သင်ခန်းစာ flow ပျောက်နေသလား
- code မပြခင် ဖြေရှင်းမယ့်မေးခွန်းကို ပြောထားသလား
- code အပြီးမှာ syntax ထက် state change နဲ့ design reason ကို ရှင်းထားသလား

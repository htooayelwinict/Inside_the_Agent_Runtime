# Chapter 00 — မိတ်ဆက်၊ Attribution နှင့် Reader Guide

## ၁။ ဒီစာအုပ်ကို ဘာကြောင့် ဆက်ရေးတာလဲ

[Agentic AI အခမဲ့လမ်းညွှန်](https://github.com/htooayelwinict/Agentic-AI-Book) မှာ Agent, Tool Calling, Context Engineering, Memory နဲ့ Agent Harness စတဲ့ concept တွေကို အခြေခံကနေ လေ့လာခဲ့ပါတယ်။ Concept ကို နားလည်လာပြီးတဲ့အခါ မေးခွန်းအသစ်တစ်ခု ပေါ်လာတတ်ပါတယ်။

> တကယ့် Agent Runtime တစ်ခုထဲမှာ ဒီ concept တွေ ဘယ်လိုဆက်စပ်ပြီး အလုပ်လုပ်ကြသလဲ။

ဒီစာအုပ်က အဲဒီမေးခွန်းကို [Travis234](https://github.com/htooayelwinict/travis234) source code ကနေ ဖြေကြည့်မယ့် sequel ဖြစ်ပါတယ်။ [Travis234](https://github.com/htooayelwinict/travis234) ထဲမှာ ပါသမျှအရာအားလုံးကို documentation ပြန်ရေးမှာ မဟုတ်ပါဘူး။ Pi ကနေ port လုပ်ထားတဲ့ Agent Loop နဲ့ Hermes Agent ကနေ port လုပ်ထားတဲ့ Compaction ကိုသာ အဓိကထားပါမယ်။

ဒီနှစ်ခုကို ရွေးထားတာ အကြောင်းရှိပါတယ်။ Agent Loop က model response၊ Tool Call နဲ့ Tool Result တွေကို အစီအစဉ်မှန်မှန် ဆက်လက်လုပ်ဆောင်စေတယ်။ Compaction က conversation ကြီးလာတဲ့အခါ အလုပ်ဆက်လုပ်ဖို့လိုတဲ့ state ကို Context Window အတွင်း ပြန်စီပေးတယ်။ တစ်ခုက action flow ကို ထိန်းပြီး နောက်တစ်ခုက context continuity ကို ကာကွယ်ပါတယ်။

## ၂။ ဘယ်သူတွေ ဖတ်သင့်လဲ

ဒီစာအုပ်က `Python` အခြေခံသိပြီး `Agentic AI` အတွင်းပိုင်းကို ဆက်လေ့လာချင်သူတွေအတွက် ရေးထားပါတယ်။ `async`/`await` ကို မြင်ဖူးရင် ပိုအဆင်ပြေပေမယ့် Pi ရဲ့ TypeScript source ကို အရင်ဖတ်ထားဖို့ မလိုပါဘူး။ Hermes Agent ကို သုံးဖူးဖို့လည်း မလိုပါဘူး။

အထူးသဖြင့် အောက်ပါမေးခွန်းတွေ ရှိနေသူတွေအတွက် အသုံးဝင်ပါလိမ့်မယ်။

- Agent Loop က သာမန် `while` loop နဲ့ ဘာကွာသလဲ။
- Tool နှစ်ခု parallel run ရင် result order ကို ဘယ်လိုထိန်းမလဲ။
- TypeScript code ကို Python ပြန်ရေးတဲ့အခါ syntax တူအောင်လုပ်ရမှာလား၊ behavior တူအောင်လုပ်ရမှာလား။
- Context Window ပြည့်တော့မယ်ဆိုရင် message အဟောင်းတွေ ဖြတ်ပစ်ရုံနဲ့ မလုံလောက်တာ ဘာကြောင့်လဲ။
- Compaction ကို Agent Session ရဲ့ ဘယ်အချိန်တွေမှာ ခေါ်သင့်သလဲ။

စာအုပ်ပြီးသွားတဲ့အခါ [Travis234](https://github.com/htooayelwinict/travis234) ရဲ့ feature အကုန်ကို မှတ်မိနေရမယ်လို့ မမျှော်လင့်ပါဘူး။ Runtime flow ကို source code နဲ့လိုက်ဖတ်နိုင်မယ်၊ porting decision တစ်ခုကို parity လား divergence လား ခွဲစဉ်းစားနိုင်မယ်၊ context pressure ဖြစ်လာရင် compaction design ကို အကြောင်းပြချက်နဲ့ ဆွေးနွေးနိုင်မယ်ဆိုရင် လုံလောက်ပါတယ်။

## ၃။ ဘာတွေ မပါဘူးလဲ

စာအုပ်က ရှင်းဖို့ကြိုးစားရင်း အရာအားလုံးထည့်လိုက်ရင် ပိုရှုပ်သွားနိုင်ပါတယ်။ ဒါကြောင့် အောက်ပါအကြောင်းအရာတွေကို main chapters ထဲ မချဲ့ပါဘူး။

- provider တစ်ခုချင်းစီရဲ့ configuration အပြည့်အစုံ
- TUI command နဲ့ screen တစ်ခုချင်းစီ
- extension၊ skill နဲ့ integration catalog အကုန်
- [Travis234](https://github.com/htooayelwinict/travis234) API reference အပြည့်အစုံ
- production security guarantee

npm Docker launcher လို reader အတွက် လက်တွေ့အသုံးဝင်တဲ့အပိုင်းကို appendix မှာ ချုံ့ရေးပါမယ်။ Docker flags အချို့ရှိတာကို “လုံခြုံရေးပြီးပြည့်စုံပြီ” လို့တော့ မပြောပါဘူး။ Security boundary တစ်ခုကို runtime configuration တစ်ခုတည်းနဲ့ အာမခံလို့မရတာကို ထည့်ပြောပါမယ်။

## ၄။ Source Code ကို ဘယ်လိုဖတ်မလဲ

ဒီစာအုပ်မှာ code ကို တစ်ကြောင်းချင်း ဘာသာပြန်မှာ မဟုတ်ပါဘူး။ အရင်ဆုံး problem ကို သတ်မှတ်မယ်။ ပြီးရင် မှတ်မိလွယ်တဲ့ mental model ပေးမယ်။ နောက်မှ Pi၊ Hermes နဲ့ [Travis234](https://github.com/htooayelwinict/travis234) source တွေကို ချိတ်ကြည့်ပါမယ်။

ဥပမာ `agent_loop.py` ကိုဖတ်တဲ့အခါ function တစ်ခုချင်း ဘာလုပ်တယ်ဆိုတာထက် အောက်ပါအရာတွေကို ဦးစားပေးမယ်။

1. Control က ဘယ်နေရာက စသလဲ။
2. State က ဘယ်အချိန်ပြောင်းသလဲ။
3. Event ဘယ်အစီအစဉ်နဲ့ ထွက်သလဲ။
4. Tool Result ကို model context ထဲ ဘယ်အချိန်ပြန်ထည့်သလဲ။
5. Loop က ဘယ်အခြေအနေမှာ ရပ်သလဲ။

Code excerpt တွေကိုလည်း concept တစ်ခုရှင်းဖို့လိုသလောက်ပဲ သုံးပါမယ်။ Ordering နဲ့ branching ကို prose ထက် diagram က ပိုရှင်းစေမှ Mermaid diagram သုံးပါမယ်။ Chapter 09 မှာ API key မလိုတဲ့ simplified runtime lab ပါမယ်။ အဲဒီ lab က [Travis234](https://github.com/htooayelwinict/travis234) ကို ပြန်ရေးထားတာမဟုတ်ဘဲ အဓိက flow ကို လက်တွေ့စမ်းကြည့်နိုင်ဖို့ ရည်ရွယ်ထားတဲ့ educational model ဖြစ်ပါတယ်။

## ၅။ Attribution နှင့် License

ဒီစာအုပ်ရဲ့ မူရင်းစာမူ၊ မူရင်း diagram နဲ့ မူရင်း educational examples တွေကို CC BY-NC-SA 4.0 နဲ့ ဖြန့်ချိထားပါတယ်။ Pi၊ Hermes Agent နဲ့ [Travis234](https://github.com/htooayelwinict/travis234) source တွေက သူတို့ရဲ့ MIT license notices အောက်မှာပဲ ရှိပါတယ်။ အသေးစိတ်ကို [Third-Party Notices](../../THIRD_PARTY_NOTICES.md) မှာ ဖတ်နိုင်ပါတယ်။

Initial research အတွက် အသုံးပြုထားတဲ့ revisions တွေက:

| Project | Revision |
|---|---|
| [Agentic AI Book](https://github.com/htooayelwinict/Agentic-AI-Book) | `7eed5ca1c4b21ab766dda2df4e039ab745cdc30f` |
| [Travis234](https://github.com/htooayelwinict/travis234) | `68b1831691b8ec93f9550ce63b80cdcb7a591b2e` |
| [Pi](https://github.com/earendil-works/pi) | `1f0dbc008c9b3e88017d42e8a1b46d416ad2b6b6` |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | `af250d84948179834820a62bfd870c0df6f264a1` |

Revision pin လုပ်ထားတာက reader တစ်ယောက် စာအုပ်ရေးချိန်က source အခြေအနေကို ပြန်ကြည့်နိုင်ဖို့ပါ။ Newer release မှာ behavior ပြောင်းသွားနိုင်ပါတယ်။ ဒါကြောင့် source claim တိုင်းကို “အမြဲတမ်းဒီလိုပဲ” လို့ မယူဆဘဲ pinned revision နဲ့တွဲဖတ်သင့်ပါတယ်။

## ၆။ ဒီစာအုပ်ကို ဘယ်လိုဖတ်မလဲ

Beginner ဆိုရင် အစဉ်လိုက်ဖတ်တာ အကောင်းဆုံးပါ။ Chapter 01 က Pi နဲ့ Hermes ကို ဘာကြောင့် တွဲလေ့လာရသလဲရှင်းပြမယ်။ Chapter 02 မှ 05 အထိ Pi Agent Loop port ကို လေ့လာမယ်။ Chapter 06 နဲ့ 07 မှာ Context Window နဲ့ Hermes-style Compaction ကို ခွဲကြည့်မယ်။ Chapter 08 မှာ နှစ်ခုကို ပြန်ချိတ်ပြီး Chapter 09 မှာ minimal runtime နဲ့ စမ်းကြည့်မယ်။

Agent Loop သိပြီးသားဆိုရင် Chapter 04 ရဲ့ semantic porting သို့မဟုတ် Chapter 06 ရဲ့ context pressure ကနေ စဖတ်နိုင်ပါတယ်။ ဒါပေမယ့် code ကို တန်းခုန်မဖတ်ခင် Chapter 01 ရဲ့ mental model ကို တစ်ခေါက်ဖတ်ထားရင် နောက်ပိုင်းချိတ်ဆက်ရ ပိုလွယ်ပါတယ်။

---

Next: [Chapter 01 — Pi နဲ့ Hermes ကို ဘာကြောင့် တွဲကြည့်ရတာလဲ](01-why-pi-and-hermes.md)

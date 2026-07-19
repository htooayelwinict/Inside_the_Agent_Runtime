# Travis234

## Pi Agent Loop နှင့် Hermes Compaction ကို Python ဖြင့် ပြန်တည်ဆောက်ခြင်း

ဒီစာအုပ်က [Agentic AI အခမဲ့လမ်းညွှန်](https://github.com/htooayelwinict/Agentic-AI-Book) ကို ဖတ်ပြီး Agent Runtime အတွင်းပိုင်းကို ဆက်လေ့လာချင်သူတွေအတွက် ရေးထားတဲ့ sequel ဖြစ်ပါတယ်။ Travis234 ထဲမှာ Pi ရဲ့ Agent Loop ကို Python နဲ့ ဘယ်လို port လုပ်ထားသလဲ၊ Hermes Agent ရဲ့ Compaction idea ကို ဘယ်လိုယူသုံးထားသလဲဆိုတာ source code အထောက်အထားနဲ့ ရှင်းပြပါမယ်။

Travis234 ရဲ့ feature အကုန်လုံးကို စာရင်းလုပ်ပြမယ့် product manual မဟုတ်ပါဘူး။ Agent Loop, Tool Execution, Bounded Concurrency, Context Window နဲ့ Compaction ကို reader နားလည်ဖို့လိုတဲ့အပိုင်းပဲ ရွေးထားပါတယ်။ ရည်ရွယ်ချက်က code ကို တစ်ကြောင်းချင်းဘာသာပြန်ဖို့မဟုတ်ဘဲ runtime က ဘာကြောင့် ဒီလိုအလုပ်လုပ်ရတာလဲဆိုတာ မြင်လာစေဖို့ပါ။

## ဘယ်သူတွေဖတ်သင့်လဲ

- Python အခြေခံသိပြီး Agentic AI ကို ဆက်လေ့လာချင်သူ
- Agent Loop နဲ့ Tool Calling အတွင်းပိုင်းကို နားလည်ချင်သူ
- TypeScript implementation တစ်ခုကို Python သို့ port လုပ်ရာမှာ syntax ထက် behavior ကို ဘယ်လိုထိန်းမလဲ သိချင်သူ
- Context Window ပြည့်လာတဲ့အခါ conversation state ကို ဘယ်လိုချုံ့မလဲ လေ့လာချင်သူ

Pi, Hermes သို့မဟုတ် Travis234 source ကို အရင်ဖတ်ထားဖို့ မလိုပါဘူး။

## အဓိကပါဝင်မည့်အကြောင်းအရာ

- Pi Agent Loop ရဲ့ outer loop နဲ့ inner loop
- Prompt ကနေ completion အထိ Agent Runtime Run တစ်ခုကို chronological walkthrough လုပ်ခြင်း
- TypeScript မှ Python သို့ semantic porting
- Sequential/parallel Tool Execution နဲ့ Bounded Concurrency
- Context Window pressure နဲ့ naive truncation ရဲ့ ပြဿနာ
- Hermes-style two-pass Compaction
- Agent Loop နဲ့ Compaction integration
- Offline run နိုင်တဲ့ minimal runtime lab
- Parity contracts နဲ့ intentional divergences
- Chapter 00–16 ပါတဲ့ main sequence ၁၇ ခန်း
- Lewis ရဲ့ fictional case studies နဲ့ runtime workshop

Provider configuration အမျိုးမျိုး၊ TUI command အကုန်နဲ့ extension catalog တွေကို မချဲ့ပါဘူး။

## စဖတ်ရန်

[စာအုပ်မာတိကာ](book/SUMMARY.md) ကနေ အစဉ်လိုက်ဖတ်နိုင်ပါတယ်။ Agent Loop ရဲ့ chronological flow ကို Chapter 03၊ semantic porting ကို Chapter 04၊ Context Window pressure ကို Chapter 06 ကနေ စဖတ်လို့ရပေမယ့် Chapter 01 က ဒီစာအုပ်ရဲ့ mental model ကို သတ်မှတ်ပေးထားပါတယ်။

## Source နှင့် Attribution

ဒီစာအုပ်မှာ အသုံးပြုထားတဲ့ runtime claims တွေကို pinned revisions နဲ့ ချိတ်ထားပါမယ်။ Pi, Hermes Agent နဲ့ Travis234 source material တွေဟာ သက်ဆိုင်ရာ MIT license notices အောက်မှာ ရှိပါတယ်။ စာမူကို CC BY-NC-SA 4.0 နဲ့ ဖြန့်ချိထားပါတယ်။

## လက်ရှိအခြေအနေ

Chapter 00–16 ပါတဲ့ main sequence ၁၇ ခန်း၊ Lewis ရဲ့ case studies နဲ့ runtime workshop အပါအဝင် manuscript နဲ့ appendix တွေကို pinned source revisions အပေါ် အခြေခံပြီး စာတည်းဖြတ်မှု၊ claim audit နဲ့ executable lab checks ပြီးထားပါတယ်။ ဒီစာမူက source revisions တွေနဲ့ ချိတ်ထားတာဖြစ်လို့ upstream project အသစ်တင်အခြေအနေအတွက် သက်ဆိုင်ရာ documentation ကို ပြန်စစ်သင့်ပါတယ်။ နောက်ဆုံး QA boundary နဲ့ result တွေကို [Review Report](book/REVIEW_REPORT.md) မှာ ဖတ်နိုင်ပါတယ်။

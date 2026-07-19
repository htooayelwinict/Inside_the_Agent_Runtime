# Chapter 01 — Pi နဲ့ Hermes ကို ဘာကြောင့် တွဲကြည့်ရတာလဲ

Agent တစ်ခုက file ကိုဖတ်နိုင်တယ်။ Command ကို run နိုင်တယ်။ Error တက်ရင် tool ပြောင်းသုံးပြီး ဆက်ကြိုးစားနိုင်တယ်။ အစပိုင်းမှာ အလုပ်ဖြစ်နေပေမယ့် conversation ရှည်လာတာနဲ့ user ရဲ့ မူလရည်ရွယ်ချက်၊ စမ်းပြီးသားနည်းလမ်းနဲ့ မပြောင်းရမယ့် constraint တွေ တဖြည်းဖြည်းပျောက်သွားတယ်ဆိုပါစို့။

ဒီ Agent မှာ Tool Calling ရှိပါတယ်။ Agent Loop လည်း ရှိပါတယ်။ ဒါပေမယ့် အလုပ်ကို ဆက်လုပ်နိုင်ဖို့လိုတဲ့ context ကို ရေရှည်မထိန်းနိုင်သေးပါဘူး။ Tool သုံးတတ်တာနဲ့ runtime ပြည့်စုံတာ မတူကြောင်း ဒီဥပမာက ပြပါတယ်။

## ၁.၁ Tool သုံးတတ်ရုံနဲ့ Agent Runtime မပြည့်စုံသေးဘူး

Model က Tool Call ထုတ်ပေးလိုက်တာနဲ့ အလုပ်မပြီးသေးပါဘူး။ Runtime က tool name နဲ့ arguments ကို validate လုပ်ရမယ်။ Tool ကို execute လုပ်ရမယ်။ Result ကို model နားလည်နိုင်တဲ့ message အဖြစ် ပြန်ထည့်ရမယ်။ ပြီးမှ model ကို နောက်တစ်ကြိမ်ခေါ်ပြီး ဆက်လုပ်စေရမယ်။

ဒီ flow ထဲမှာ order မှားသွားရင် result မှန်နေလည်း behavior မှားနိုင်ပါတယ်။ Tool Result ကို assistant message မတိုင်ခင် ထည့်မိတာ၊ parallel tools တွေရဲ့ result ကို model ထုတ်ပေးခဲ့တဲ့ order မဟုတ်ဘဲ completion order နဲ့ ပြန်ထည့်မိတာ၊ abort ဖြစ်ပြီးနောက် model ကို ထပ်ခေါ်မိတာတွေက ဥပမာတွေပါ။

တစ်ဖက်မှာ flow မှန်နေလည်း Context Window က အကန့်အသတ်ရှိပါတယ်။ Tool output ကြီးတွေ၊ system instruction၊ conversation history နဲ့ reserved output tokens တွေက capacity တစ်ခုတည်းကို မျှဝေသုံးရပါတယ်။ အလုပ်ရှည်လာတာနဲ့ runtime မှာ မေးခွန်းနှစ်ခုရှိလာပါတယ်။

1. အခု turn ကို ဘယ်အစီအစဉ်နဲ့ ဆက်လုပ်မလဲ။
2. နောက် turn တွေ ဆက်လုပ်နိုင်ဖို့ ဘာကိုသိမ်းပြီး ဘာကိုချုံ့မလဲ။

Pi နဲ့ Hermes ကို တွဲလေ့လာရတာ ဒီမေးခွန်းနှစ်ခုကြောင့်ပါ။

## ၁.၂ Pi က ဖြေရှင်းပေးတဲ့ ပြဿနာ

Pi ရဲ့ Agent Loop ကို “လုပ်ဆောင်နိုင်တဲ့လက်” လို့ ယာယီစဉ်းစားနိုင်ပါတယ်။ User message ကို model ဆီပို့တယ်။ Model က Tool Call ထုတ်ရင် tool ကို run တယ်။ Tool Result ကို conversation ထဲ ပြန်ထည့်တယ်။ Model က final response ပေးတဲ့အထိ သို့မဟုတ် runtime ကို ရပ်စေတဲ့အခြေအနေတစ်ခုရောက်တဲ့အထိ ဆက်လုပ်တယ်။

ဒီ analogy က မှတ်မိဖို့ပဲ အသုံးဝင်ပါတယ်။ လက်တစ်ဖက်လို သာမန် action executor တစ်ခုတည်းလို့ ယူဆရင် မပြည့်စုံပါဘူး။ Pi Agent Loop က model streaming၊ event boundaries၊ steering messages၊ follow-up messages၊ tool validation၊ hooks၊ cancellation နဲ့ termination ကို အစီအစဉ်တကျ ထိန်းတဲ့ control flow ဖြစ်ပါတယ်။

Travis234 ရဲ့ `travis/agent/agent_loop.py` က Pi `packages/agent/src/agent-loop.ts` ရဲ့ syntax ကို Python လိုပြောင်းရေးထားရုံမဟုတ်ပါဘူး။ Outer follow-up loop နဲ့ inner steering/tool loop လို behavior structure ကို Python async runtime ထဲ ထိန်းထားပါတယ်။ Chapter 02 မှာ ဒီ loop နှစ်ထပ်ကို event တစ်ခုချင်းနဲ့ ခွဲကြည့်ပါမယ်။

Pi ဘက်က ကြည့်ရင် အဓိကမေးခွန်းက “Agent က နောက်ဘာလုပ်မလဲ” ဆိုတာပါ။

## ၁.၃ Hermes က ဖြေရှင်းပေးတဲ့ ပြဿနာ

Agent က အလုပ်ကို မှန်မှန်ဆက်လုပ်နေပေမယ့် context က အမြဲကြီးလာပါတယ်။ Tool output တစ်ခုက user message ဆယ်ခုထက်တောင် ကြီးနိုင်ပါတယ်။ Screenshot၊ file content နဲ့ command output တွေပါလာရင် Context Window ကို ပိုမြန်မြန်သုံးမိပါတယ်။

Hermes-style Compaction ကို “ဆက်လုပ်ဖို့လိုတဲ့မှတ်စု” လို့ ယာယီစဉ်းစားနိုင်ပါတယ်။ အလုပ်စတင်ခဲ့တဲ့အကြောင်းရင်း၊ ဆုံးဖြတ်ထားပြီးသားအချက်၊ စမ်းပြီးသားနည်းလမ်း၊ အရေးကြီးတဲ့ result နဲ့ နောက်လုပ်ရမယ့်အဆင့်တွေကို ချုံ့ရေးထားတဲ့ handoff note တစ်ခုလိုပါပဲ။

ဒီ analogy လည်း implementation အပြည့်အစုံမဟုတ်ပါဘူး။ Compaction က summary တစ်ပိုဒ်ရေးတာတစ်ခုတည်း မဟုတ်ပါဘူး။ Travis234 ရဲ့ compressor မှာ အရင်ဆုံး deterministic pruning လုပ်တယ်။ ထပ်နေတဲ့ Tool Results တွေကို လျှော့တယ်၊ အဟောင်းတွေကို ချုံ့တယ်၊ image data ကို ဖယ်တယ်၊ အရမ်းရှည်တဲ့ arguments ကို ဖြတ်တယ်။ ပြီးမှ structured summary အသစ်ဖန်တီးတာ သို့မဟုတ် ရှိပြီးသား summary ကို update လုပ်တာ ဆက်လုပ်တယ်။ နောက်ဆုံးမှာ protected head နဲ့ recent tail ကို token budget အတွင်း ပြန်စီတယ်။

Hermes ဘက်က မေးခွန်းဟာ “Agent က ဆက်လုပ်ဖို့ ဘာကို မှတ်ထားရမလဲ” ဆိုတာပါ။

## ၁.၄ Travis234 မှာ နှစ်ခု ဘယ်လိုဆုံသလဲ

Agent Loop နဲ့ Compaction ကို သီးခြား feature နှစ်ခုလိုမြင်ရင် integration အရေးကြီးပုံ မပေါ်ပါဘူး။ တကယ်တမ်းမှာ Compaction က model request မတိုင်ခင် ဝင်နိုင်တယ်။ Response ပြီးသွားတဲ့နောက် context pressure ကို ပြန်စစ်နိုင်တယ်။ Provider က overflow ပြန်ပေးတဲ့အခါ recovery path အဖြစ် ဝင်နိုင်တယ်။ User က manual compact တောင်းတဲ့အခါလည်း ဝင်နိုင်တယ်။

အလွယ်မြင်ရင် flow က ဒီလိုပါ။

1. Agent Session က လက်ရှိ messages နဲ့ token pressure ကို ကြည့်တယ်။
2. လိုအပ်ရင် preflight Compaction လုပ်တယ်။
3. Agent Loop က model နဲ့ tools ကို အစီအစဉ်အတိုင်း run တယ်။
4. Response ပြီးရင် context ကို ပြန်တိုင်းတယ်။
5. Threshold ကျော်လာရင် နောက် turn အတွက် Compaction စီစဉ်တယ်။
6. Overflow ဖြစ်ရင် recovery rule အတိုင်း compact လုပ်ပြီး retry လုပ်နိုင်တယ်။

ဒီနေရာမှာ “လုပ်နိုင်တယ်” ဆိုတာ path ရှိတယ်လို့ ပြောတာပါ။ Compaction တိုင်းအောင်မြင်မယ်၊ information မဆုံးရှုံးဘူး၊ retry တိုင်းပြန်ကောင်းမယ်လို့ အာမခံတာမဟုတ်ပါဘူး။ Summary မှားနိုင်တယ်။ Detail အရေးကြီးတာတစ်ခု ပြုတ်နိုင်တယ်။ Compaction ကို မကြာခဏပြန်လုပ်ရင် summary rewrite တွေက အရည်အသွေးကျနိုင်သလို token လည်း ထပ်ကုန်နိုင်ပါတယ်။ ဒါကြောင့် threshold နဲ့ cooldown လို anti-thrashing policy တွေလိုပါတယ်။

Pi ရဲ့ action flow နဲ့ Hermes ရဲ့ context continuity ကို Travis234 က session lifecycle တစ်ခုထဲ ချိတ်ထားတာ ဒီစာအုပ်ရဲ့ အဓိကလေ့လာမယ့်နေရာဖြစ်ပါတယ်။

## ၁.၅ မရောထွေးသင့်တဲ့ အရာများ

### Context နဲ့ Long-term Memory

Context က လက်ရှိ model request ထဲ ပို့ထားတဲ့ information ဖြစ်ပါတယ်။ Long-term Memory က session ကျော်ပြီး ပြန်ရှာသုံးနိုင်တဲ့ preference၊ fact သို့မဟုတ် experience store ဖြစ်နိုင်ပါတယ်။ Compaction summary တစ်ခုကို persistence လုပ်ထားလို့ memory လိုအသုံးဝင်နိုင်ပေမယ့် Compaction နဲ့ Long-term Memory က ရည်ရွယ်ချက်တူတာ မဟုတ်ပါဘူး။

ဒီစာအုပ်မှာ အဓိကစိတ်ဝင်စားတာက model request အတွက် context ကို ထိန်းတာပါ။ User profile store၊ vector database နဲ့ cross-session memory architecture တွေကို မချဲ့ပါဘူး။

### Compaction နဲ့ Raw Truncation

Raw truncation က token မဝင်တော့ရင် message အဟောင်းကို ဖြတ်ပစ်တာမျိုးပါ။ လွယ်ပေမယ့် initial goal၊ safety constraint နဲ့ စမ်းပြီးသား failure တွေ ပျောက်သွားနိုင်ပါတယ်။

Compaction က အရွယ်အစားလျှော့တာတူပေမယ့် ဘာကိုထိန်းရမလဲဆိုတဲ့ policy ပါတယ်။ Deterministic prune လုပ်တယ်။ Summary structure သုံးတယ်။ Recent tail အတွက် token budget သတ်မှတ်တယ်။ Information loss မရှိဘူးလို့တော့ မဆိုနိုင်ပေမယ့် မျက်ကန်းဖြတ်ပစ်တာထက် ဆက်လုပ်နိုင်မယ့် state ကို ထိန်းဖို့ ကြိုးစားထားပါတယ်။

### Parity နဲ့ Line-for-line Copy

Port တစ်ခု behavior တူဖို့ source language ရဲ့ syntax ကို line-for-line ကူးစရာမလိုပါဘူး။ TypeScript က Promise၊ callback နဲ့ event type သုံးတဲ့နေရာမှာ Python က coroutine၊ dataclass နဲ့ async iterator သုံးနိုင်ပါတယ်။ အရေးကြီးတာက observable ordering၊ error behavior၊ cancellation နဲ့ result shape လို invariants တွေပါ။

Travis234 က Pi နဲ့ parity ထိန်းထားတဲ့ contract တွေရှိသလို Python runtime နဲ့ safety policy ကြောင့် intentional divergence လုပ်ထားတာတွေလည်း ရှိပါတယ်။ Divergence ရှိတာနဲ့ port ပျက်တယ်လို့ မဆိုနိုင်ပါဘူး။ ဘာကြောင့်ကွာသလဲ၊ အဲဒီကွာခြားမှုကို test နဲ့ ဘယ်လိုထိန်းထားသလဲဆိုတာ ပိုအရေးကြီးပါတယ်။

## ၁.၆ အနှစ်ချုပ်

- Pi Agent Loop က model၊ tools နဲ့ follow-up flow ကို အစီအစဉ်တကျ ဆက်လုပ်စေတယ်။
- Hermes-style Compaction က Context Window pressure တက်လာတဲ့အခါ ဆက်လုပ်ဖို့လိုတဲ့ state ကို ချုံ့ထိန်းဖို့ ကြိုးစားတယ်။
- Agent Loop က “နောက်ဘာလုပ်မလဲ” ကို ဖြေပြီး Compaction က “ဆက်လုပ်ဖို့ ဘာမှတ်ထားမလဲ” ကို ဖြေတယ်။
- Context နဲ့ Long-term Memory မတူသလို Compaction နဲ့ raw truncation လည်း မတူပါဘူး။
- Travis234 ကို လေ့လာရာမှာ syntax similarity ထက် behavioral parity နဲ့ documented divergence ကို ကြည့်ရမယ်။

## ၁.၇ Source Notes

ဒီ chapter ရဲ့ runtime claims တွေကို အောက်ပါ evidence နဲ့ ချိတ်ထားပါတယ်။

- `C-LOOP-ORDER` — `P-LOOP`, `T-LOOP`
- `C-PRUNE` — `T-COMPRESS`, `H-COMPRESS`
- `C-SUMMARY` — `T-COMPRESS`, `H-COMPRESS`, `H-CONVERSATION`
- `C-TIMING` — `T-SESSION`, `T-COORD`, `T-TIMING`

Exact files နဲ့ pinned links တွေကို [Pinned Source Map](../references/SOURCE_MAP.md) မှာ ကြည့်နိုင်ပါတယ်။ Claim တစ်ခုချင်းရဲ့ verification boundary ကို [Technical Claim Ledger](../references/CLAIM_LEDGER.md) မှာ ဖတ်နိုင်ပါတယ်။

---

Previous: [မိတ်ဆက်၊ Attribution နှင့် Reader Guide](00-preface-attribution.md)

Next: [Chapter 02 — Pi Agent Loop Anatomy](02-pi-agent-loop-anatomy.md)

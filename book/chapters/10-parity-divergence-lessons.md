# Chapter 10 — Parity, Divergence နှင့် သင်ခန်းစာများ

TypeScript code ကို Python ပြောင်းရေးတဲ့အခါ class အမည်၊ function အရေအတွက်နဲ့ file structure တူနေရင် port ကောင်းတယ်လို့ ပြောလို့ရမလား။ စာကြောင်းတိုင်းနီးပါး တူပေမယ့် Tool Result order ပြောင်းသွားရင် behavior မတူတော့ပါဘူး။ တစ်ဖက်မှာ code ပုံစံလုံးဝကွာပေမယ့် user မြင်ရတဲ့ event၊ result နဲ့ error boundary တူနေရင် faithful port ဖြစ်နိုင်ပါတယ်။

ဒီနေရာမှာ `Parity` ဆိုတဲ့စကားကို တိတိကျကျသုံးဖို့လိုပါတယ်။ “Pi နဲ့တူတယ်” သို့မဟုတ် “Hermes ကို port ထားတယ်” လို့ အကျယ်ကြီးပြောတာထက် ဘယ် behavior ကို ဘာနဲ့တိုက်ထားသလဲ ပြောနိုင်ရပါမယ်။ Travis234 ရဲ့ parity manifest က ဒီအတွက် contract တစ်ခုချင်းနဲ့ evidence test တစ်ခုချင်းကို ချိတ်ထားပါတယ်။

## ၁၀.၁ တူခြင်းသုံးမျိုးကို မရောသင့်ဘူး

Port တစ်ခုကိုကြည့်တဲ့အခါ mechanical similarity၊ behavioral parity နဲ့ intentional divergence ဆိုပြီး သုံးမျိုးခွဲစဉ်းစားနိုင်ပါတယ်။

### Mechanical Similarity

Function အမည်၊ module layout၊ class hierarchy နဲ့ code အစီအစဉ်တူတာကို ဆိုလိုပါတယ်။ Source နှစ်ခုဘေးချင်းယှဉ်ဖတ်ရလွယ်စေနိုင်ပေမယ့် Runtime behavior မှန်တယ်လို့ အာမခံမပေးပါဘူး။ TypeScript Promise chain ကို Python coroutine အဖြစ်ပြောင်းရင် code ပုံစံက သဘာဝအတိုင်းကွာပါမယ်။

### Behavioral Parity

တူညီတဲ့အခြေအနေတစ်ခုမှာ အပြင်ကကြည့်လို့ရတဲ့ result နဲ့ boundary တူတာပါ။ Event order၊ Tool Result order၊ cancellation response၊ session state နဲ့ compaction output shape တို့ကို စစ်နိုင်ပါတယ်။ Implementation ဘယ်လိုရေးထားသလဲထက် caller က ဘာမြင်ရသလဲကို ဦးစားပေးပါတယ်။

### Intentional Divergence

Upstream behavior နဲ့ ကွာနေကြောင်း သိသိသာသာမှတ်ထားပြီး ဘာကြောင့်ကွာရသလဲ၊ ဘယ် test က အဲဒီရွေးချယ်မှုကို ကာကွယ်သလဲ ဖော်ပြထားတာပါ။ Divergence ဆိုတာ မပြီးသေးတဲ့ port လို့ အလိုအလျောက်မဆိုလိုပါဘူး။ Reason နဲ့ safety evidence မရှိရင်တော့ design choice လို့ခေါ်ဖို့ ခက်ပါတယ်။

## ၁၀.၂ Parity Contract ဆိုတာ မေးခွန်းတစ်ခုလိုပါပဲ

Contract တစ်ခုကို စာမေးပွဲမေးခွန်းတစ်ခုလို စဉ်းစားကြည့်နိုင်ပါတယ်။ “Parallel tools တကယ်ပြီးတဲ့ order ပြောင်းသွားရင် Tool Results ကို model ဆီ ဘယ် order နဲ့ပြန်ပို့သလဲ” ဆိုတာ မေးခွန်းပါ။ Evidence test က အဲဒီမေးခွန်းကို code နဲ့စမ်းပြတာဖြစ်ပါတယ်။

Manifest entry တစ်ခုမှာ အဓိကအားဖြင့်:

- contract ID၊
- loop၊ session၊ SDK သို့မဟုတ် compaction လို category၊
- evidence test path နဲ့ test name၊
- `parity` သို့မဟုတ် `divergence` status၊
- divergence ဖြစ်ရင် reason နဲ့ safety evidence ပါပါတယ်။

`pi.loop.parallel_result_source_order` ဆိုတဲ့ contract က Chapter 05 နဲ့ Chapter 09 မှာ လေ့လာခဲ့တဲ့ behavior ကို နာမည်ပေးထားတာပါ။ ဒီလို ID ရှိလို့ “parallel tools support လုပ်တယ်” ဆိုတဲ့ အကျယ်ကြီး claim ထက် “completion order ကွာပေမယ့် result order ကို source order နဲ့ထိန်းတယ်” လို့ တိတိကျကျပြောနိုင်ပါတယ်။

## ၁၀.၃ Pinned Manifest က ပြောတဲ့အရေအတွက်

ဒီစာအုပ်က research လုပ်ထားတဲ့ Travis234 revision မှာ Pi contracts ၇၈ ခုရှိပါတယ်။ ၇၄ ခုကို parity လို့မှတ်ထားပြီး ၄ ခုကို intentional divergence လို့မှတ်ထားပါတယ်။ Hermes Compaction contracts ၁၁ ခုကတော့ ၁၁ ခုလုံး parity ဖြစ်ပါတယ်။

| Source | Total | Parity | Divergence |
|---|---:|---:|---:|
| Pi | 78 | 74 | 4 |
| Hermes Compaction | 11 | 11 | 0 |

ဒီကိန်းတွေက project အားလုံးရဲ့ feature coverage percentage မဟုတ်ပါဘူး။ Manifest ထဲမှာ စာရင်းသွင်းထားတဲ့ contracts တွေရဲ့ count ပဲဖြစ်ပါတယ်။ Contract အသစ်ထည့်ရင် total ပြောင်းနိုင်ပါတယ်။ Upstream revision သို့မဟုတ် Travis234 revision ပြောင်းရင် status ပြန်စစ်ရပါမယ်။

`verify_acceptance.py --parity-json` ကို ဒီစာအုပ်ရေးချိန်မှာ local source clone ပေါ် run လုပ်ခဲ့ပြီး exit code 0 ရပါတယ်။ ဒီ command က contract ID မထပ်ကြောင်း၊ status မှန်ကြောင်း၊ divergence မှာ reason နဲ့ safety evidence ရှိကြောင်း၊ ညွှန်ထားတဲ့ test function တကယ်ရှိကြောင်း စစ်ပါတယ်။ Travis234 test suite အကုန်ကို run ပေးတာတော့ မဟုတ်ပါဘူး။

## ၁၀.၄ Intentional Divergence လေးခု

Pi ဘက်က divergence လေးခုကို အကျဉ်းချုပ်မဟုတ်ဘဲ ဘာကြောင့်ရွေးထားသလဲနဲ့ တွဲကြည့်ပါမယ်။

### Parallel tools ကို အကန့်အသတ်ထားခြင်း

Travis234 က parallel Tool Calls ကို host ကခွင့်ပြုသလောက် အကန့်အသတ်မဲ့မဖွင့်ဘဲ bounded worker pool သုံးပါတယ်။ ဒီအတွက် အလုပ်အားလုံးတစ်ပြိုင်နက်စမယ့် upstream behavior နဲ့ mechanical parity မရှိနိုင်ပါဘူး။ ဒါပေမယ့် resource exhaustion ကိုလျှော့ပြီး result ordering contract ကို ဆက်ထိန်းထားပါတယ်။ Chapter 05 ရဲ့ Bounded Concurrency က ဒီ divergence ကို အသေးစိတ်ရှင်းထားပါတယ်။

### Project package mutation ကို trust မရသေးခင်ပိတ်ထားခြင်း

Project-local package install၊ remove သို့မဟုတ် update လို mutation က workspace code နဲ့ configuration ကို သက်ရောက်နိုင်ပါတယ်။ Travis234 မှာ project trust မဆုံးဖြတ်ရသေးရင် ဒီ mutation ကို ခွင့်မပြုဘဲ fail closed လုပ်ပါတယ်။ “အဖြေမသိသေးလို့ခွင့်ပြုလိုက်တယ်” မဟုတ်ဘဲ “အဖြေမသိသေးလို့မလုပ်သေးဘူး” ဆိုတဲ့ safety choice ပါ။

### Non-interactive unknown project ကို fail closed လုပ်ခြင်း

Interactive TUI မှာ user ကို trust မေးနိုင်ပေမယ့် print၊ JSON သို့မဟုတ် RPC လို non-interactive mode မှာ prompt ထုတ်လိုက်ရင် automation ပိတ်နေနိုင်ပါတယ်။ Travis234 က policy decision မရှိသေးတဲ့ unknown project ရဲ့ executable resources ကို တိတ်တဆိတ်မ run ပါဘူး။ Operator က explicit flag သို့မဟုတ် saved policy နဲ့ ဆုံးဖြတ်ပေးရပါတယ်။

Project package mutation divergence နဲ့ ဒီ divergence က trust အကြောင်းတူပေမယ့် boundary မတူပါဘူး။ ပထမတစ်ခုက package ကိုပြောင်းတဲ့ operation ကိုကာကွယ်တာဖြစ်ပြီး ဒုတိယတစ်ခုက UI မရှိတဲ့ startup မှာ project resources ကို execute လုပ်မလား ဆုံးဖြတ်တာပါ။

### Pythonic async `AgentHarness`

TypeScript harness signature ကို Python မှာ အမည်အတိုင်းကူးမထားပါဘူး။ `async with`၊ coroutine methods နဲ့ async lock သုံးတဲ့ Pythonic facade လုပ်ထားပါတယ်။ API shape က divergence ဖြစ်ပေမယ့် session tree၊ clone နဲ့ rename လို production owners ဆီ delegate လုပ်ကြောင်း safety evidence နဲ့ ချိတ်ထားပါတယ်။ Chapter 04 မှာ semantic porting အမြင်နဲ့ ကြည့်ခဲ့ပြီးသားပါ။

## ၁၀.၅ Hermes ၁၁ ခုလုံး Parity ဆိုတာ ဘာကိုဆိုလိုသလဲ

Hermes contract ၁၁ ခုက threshold bands၊ small-window fallback၊ request accounting၊ provider prompt usage၊ tail budget၊ protected-head decay၊ Tool Call/Result boundary၊ cooldown၊ fallback summary နဲ့ auxiliary-model capacity တို့လို Compaction behavior တွေကို ဖုံးထားပါတယ်။ Pinned manifest အရ အားလုံး `parity` status ရှိပါတယ်။

ဒါက Hermes Agent source တစ်ခုလုံးကို line-for-line port ထားတယ်လို့ မဆိုလိုပါဘူး။ Travis234 ရဲ့ message types၊ session store နဲ့ lifecycle integration က Python Runtime ပိုင်အလွှာတွေပါ။ Contract က သူမေးထားတဲ့ observable behavior ကိုပဲ သက်သေပြဖို့ကြိုးစားပါတယ်။ မမေးထားတဲ့ behavior ကိုတော့ အလိုအလျောက်မဖုံးပါဘူး။

## ၁၀.၆ Contract တွေက ဘာကို မသက်သေပြနိုင်သလဲ

Evidence ရှိတာက ကောင်းပါတယ်။ ဒါပေမယ့် evidence boundary ကို ကျော်ပြီး claim မချဲ့သင့်ပါဘူး။

Parity manifest တစ်ခုတည်းနဲ့:

- test စာရင်းထဲမပါသေးတဲ့ behavior မှန်ကြောင်း၊
- live provider အားလုံးနဲ့ integration အမြဲအလုပ်လုပ်ကြောင်း၊
- performance က upstream ထက်တူ သို့မဟုတ်ပိုကောင်းကြောင်း၊
- security vulnerability မရှိကြောင်း၊
- future revision တွေမှာ count နဲ့ behavior မပြောင်းကြောင်း မသက်သေပြနိုင်ပါဘူး။

Test function ရှိတာနဲ့ အဲဒီ test ကို လက်ရှိ environment မှာ run ပြီး pass တယ်ဆိုတာလည်း မတူပါဘူး။ ဒီစာအုပ်ရဲ့ local verification က manifest structure နဲ့ evidence references ကို စစ်ထားတာဖြစ်ပြီး full Travis234 suite ကို ပြန် run မထားပါဘူး။ ဒီကန့်သတ်ချက်ကို ရှင်းရှင်းရေးထားတာက number ကို လျှော့တွက်တာမဟုတ်ဘဲ ယုံကြည်ရတဲ့ claim ဖြစ်အောင် boundary တပ်တာပါ။

## ၁၀.၇ Port တစ်ခုကို ကိုယ်တိုင်ပြန်စစ်တဲ့နည်း

Language တစ်ခုကနေတစ်ခု port လုပ်တဲ့အခါ ဒီမေးခွန်းလေးခုနဲ့ စနိုင်ပါတယ်။

1. Caller သို့မဟုတ် user က မြင်နိုင်တဲ့ behavior ကဘာလဲ။
2. အဲဒီ behavior ကို input နဲ့ expected output ပါတဲ့ test အဖြစ်ရေးလို့ရသလား။
3. Language သဘာဝကြောင့် API shape ပြောင်းဖို့လိုသလား။
4. ကွာမယ်ဆိုရင် reason နဲ့ safety evidence ကို ဘယ်မှာမှတ်မလဲ။

ဒီမေးခွန်းတွေက code တူအောင်ဖိအားမပေးပါဘူး။ Behavior ကို မတော်တဆပြောင်းမိတာနဲ့ ရည်ရွယ်ချက်ရှိရှိပြောင်းတာကို ခွဲပေးပါတယ်။ Porting ရဲ့ရည်ရွယ်ချက်က source ကို အရိပ်လိုလိုက်ဖို့မဟုတ်ဘဲ contract ကို နားလည်ပြီး target language ထဲမှာ တာဝန်ရှိရှိပြန်တည်ဆောက်ဖို့ပါ။

## ၁၀.၈ အနှစ်ချုပ်

- Mechanical similarity က code ပုံစံတူတာဖြစ်ပြီး behavioral parity ကို အာမခံမပေးဘူး။
- Behavioral parity က caller မြင်နိုင်တဲ့ result၊ order နဲ့ failure boundary ကို contract အလိုက်တိုက်တာဖြစ်တယ်။
- Intentional divergence မှာ reason နဲ့ safety evidence နှစ်ခုလုံးလိုတယ်။
- Pinned manifest မှာ Pi ၇၈ ခုအနက် ၇၄ parity၊ ၄ divergence နဲ့ Hermes ၁၁ ခုလုံး parity လို့ မှတ်ထားတယ်။
- Divergence လေးခုက bounded parallelism၊ trust မရသေးတဲ့ project package mutation၊ non-interactive unknown-project policy နဲ့ Pythonic `AgentHarness` ဖြစ်တယ်။
- Manifest verification pass ဖြစ်တာကို full test suite pass ဖြစ်တယ်လို့ မရေးရဘူး။
- Parity count က revision-specific evidence ဖြစ်ပြီး product quality percentage မဟုတ်ဘူး။

## ၁၀.၉ Source Notes

- `C-PARITY` — `T-PARITY`, `T-VERIFY`
- `C-DIVERGENCES` — `T-PARITY`
- `C-BOUND` — `T-TOOLS`, `pi.loop.bounded_parallelism`
- `C-HARNESS` — `T-HARNESS`, `pi.sdk.agent_harness`
- Manifest verification: `python3 scripts/verify_acceptance.py --parity-json` exited 0 on 2026-07-18
- Travis234 revision: `68b1831691b8ec93f9550ce63b80cdcb7a591b2e`

Exact source links နဲ့ evidence boundary ကို [Pinned Source Map](../references/SOURCE_MAP.md) မှာ ကြည့်နိုင်ပါတယ်။

---

Previous: [Chapter 09 — Minimal Runtime Lab](09-minimal-runtime-lab.md)

Next: [Chapter 11 — တစ်ညနဲ့မပြီးတဲ့ Bug](11-one-night-unfinished-bug.md)

# Glossary

ဒီ glossary မှာ စာအုပ်တစ်လျှောက် တစ်သမတ်တည်းသုံးမယ့် technical terms တွေကို စုထားပါတယ်။ Term ကို အတင်းဘာသာပြန်တာထက် reader နားလည်မယ့် မြန်မာရှင်းလင်းချက်ကို ပေးထားပါတယ်။

## Agent Loop

Model ကိုခေါ်ခြင်း၊ response stream ကို လက်ခံခြင်း၊ Tool Call ကို execute လုပ်ခြင်း၊ Tool Result ကို context ထဲပြန်ထည့်ခြင်းနဲ့ နောက်တစ်ကြိမ် model ကို ဆက်ခေါ်ခြင်းတို့ကို ထိန်းတဲ့ runtime control flow ဖြစ်ပါတယ်။

## Tool Call

Model က သတ်မှတ်ထားတဲ့ tool တစ်ခုကို arguments နဲ့ အသုံးပြုလိုကြောင်း ထုတ်ပေးတဲ့ structured request ဖြစ်ပါတယ်။

## Tool Result

Tool execute လုပ်ပြီးနောက် model context ထဲ ပြန်ပို့မယ့် success သို့မဟုတ် error result ဖြစ်ပါတယ်။

## Immediate Tool Outcome

မသိတဲ့ Tool name၊ မမှန်တဲ့ arguments သို့မဟုတ် blocked permission ကြောင့် Tool body ကိုမခေါ်ခင် Runtime က ချက်ချင်းဖန်တီးပေးတဲ့ Tool Result ကို Immediate Tool Outcome လို့ခေါ်ပါတယ်။

## Context Window

Model က request တစ်ကြိမ်မှာ လက်ခံစဉ်းစားနိုင်တဲ့ input နဲ့ output token capacity ဖြစ်ပါတယ်။ Conversation history တစ်ခုတည်းမဟုတ်ဘဲ system prompt၊ tool definitions၊ Tool Results နဲ့ reserved output space တွေလည်း သက်ရောက်ပါတယ်။

## Compaction

Context အရွယ်အစားကို လျှော့ရင်း နောက်အဆင့်ဆက်လုပ်ဖို့လိုတဲ့ goal၊ decisions၊ progress နဲ့ constraints တွေကို တတ်နိုင်သလောက် ထိန်းထားတဲ့လုပ်ငန်းစဉ် ဖြစ်ပါတယ်။ Message အဟောင်းတွေကို မျက်ကန်းဖြတ်ပစ်တာနဲ့ မတူပါဘူး။

## Bounded Concurrency

Parallel အလုပ်လုပ်ခွင့်ပေးပေမယ့် တစ်ပြိုင်နက် run နိုင်တဲ့ task အရေအတွက်ကို သတ်မှတ်ထားတဲ့ limit နဲ့ ထိန်းခြင်းဖြစ်ပါတယ်။ Resource exhaustion နဲ့ uncontrolled fan-out ကို လျှော့ပေးနိုင်ပါတယ်။

## Semantic Port

Source language ရဲ့ syntax နဲ့ file structure ကို line-for-line ကူးတာထက် observable behavior၊ event order နဲ့ failure boundary ကို target language ရဲ့ သဘာဝကျတဲ့ abstraction တွေနဲ့ ပြန်တည်ဆောက်ခြင်း ဖြစ်ပါတယ်။

## Source Order

Model သို့မဟုတ် caller က items တွေကို မူလထုတ်ပေးခဲ့တဲ့ အစီအစဉ် ဖြစ်ပါတယ်။ Parallel Tool Calls တွေရဲ့ result messages ကို stable ဖြစ်အောင် ပြန်စီရာမှာ အသုံးဝင်ပါတယ်။

## Completion Order

Concurrent အလုပ်တွေ wall-clock အရ တကယ်ပြီးသွားတဲ့ အစီအစဉ် ဖြစ်ပါတယ်။ Source order နဲ့ မတူနိုင်ပါဘူး။

## Event Trace

Runtime လည်ပတ်နေစဉ် ဖြစ်လာတဲ့ lifecycle events တွေကို order နဲ့ metadata ပါအောင် မှတ်တမ်းတင်ထားတဲ့ debugging/evaluation record ကို Event Trace လို့ခေါ်ပါတယ်။ ဒီ record က system အတွင်း ဖြစ်ပျက်သမျှရဲ့ complete truth မဟုတ်ပါဘူး။

## Steering

Agent run နေချိန် နောက် assistant response မတိုင်ခင် direction ပြောင်းဖို့ queue ထဲထည့်တဲ့ message ဖြစ်ပါတယ်။ Running tool ကို အလိုအလျောက် force-stop လုပ်ပေးတာမဟုတ်ပါဘူး။

## Follow-up

လက်ရှိ tool chain နဲ့ response ပြီးသွားတဲ့နောက် ဆက်လုပ်ဖို့ queue ထဲထည့်ထားတဲ့ message ဖြစ်ပါတယ်။ Steering နဲ့ဝင်မယ့် boundary မတူပါဘူး။

## Abort Signal

Provider stream၊ Agent Loop သို့မဟုတ် tool ကို အလုပ်ရပ်ဖို့အသိပေးတဲ့ cooperative signal ဖြစ်ပါတယ်။ Blocking thread ကို လုံခြုံစွာ force-kill လုပ်ပေးမယ့် guarantee မဟုတ်ပါဘူး။

## Run Lease

တစ်ချိန်တည်းမှာ Agent run တစ်ခုကို owner တစ်ယောက်ပဲ ကိုင်နိုင်အောင် serialise လုပ်ပြီး concurrent prompt owners မဝင်လာစေဖို့ ထိန်းတဲ့ runtime primitive ကို Run Lease လို့ခေါ်ပါတယ်။

## Semaphore

Concurrent code ထဲကို တစ်ချိန်တည်းဝင်နိုင်တဲ့ task အရေအတွက်ကို permit count နဲ့ ထိန်းတဲ့ synchronization primitive ဖြစ်ပါတယ်။

## Compaction Threshold

Context usage ဘယ်အရွယ်ရောက်ချိန်မှာ automatic Compaction စဉ်းစားမလဲဆိုတဲ့ token boundary ဖြစ်ပါတယ်။ Output reserve၊ Context Window အရွယ်အစားနဲ့ summarizer capacity အလိုက် ပြောင်းနိုင်ပါတယ်။

## Protected Head

Compaction လုပ်တဲ့အခါ မူရင်းအတိုင်းထိန်းထားဖို့ရွေးထားတဲ့ system နဲ့ အစပိုင်း context ဖြစ်ပါတယ်။ Rolling Compaction နောက်ပိုင်းမှာ initial-message protection လျော့နိုင်ပါတယ်။

## Recent Tail

Compaction summary နောက်မှာ မူရင်းအတိုင်းဆက်ထားတဲ့ recent messages ဖြစ်ပါတယ်။ Fixed message count တစ်ခုတည်းထက် token budget နဲ့ Tool Call/Result boundaries ကိုပါ ကြည့်ရပါတယ်။

## Structured Summary

Task state၊ progress၊ pending asks၊ relevant files နဲ့ remaining work တို့ကို heading အလိုက်ခွဲထားတဲ့ Compaction handoff ဖြစ်ပါတယ်။ Exact transcript archive မဟုတ်ပါဘူး။

## Preflight Compaction

Provider request မပို့ခင် rough context estimate နဲ့ threshold ကိုတိုက်ပြီး လိုအပ်ရင် ကြိုချုံ့တဲ့ lifecycle path ဖြစ်ပါတယ်။

## Post-response Compaction

Successful assistant turn ရပြီးနောက် provider ရဲ့ real prompt usage ကိုသုံးကာ နောက် turn အတွက် active context ကို ချုံ့တဲ့ lifecycle path ဖြစ်ပါတယ်။

## Overflow Recovery

Provider က context capacity ကြောင့် request ကိုငြင်းတဲ့အခါ failed error message ကိုဖယ်၊ forced Compaction လုပ်ပြီး bounded retry နဲ့ Agent ကို ပြန်ဆက်တဲ့ path ဖြစ်ပါတယ်။

## Persistent Session

Messages၊ model state၊ Compaction entries နဲ့ branch lineage ကို process ပိတ်ပြီးနောက် ပြန်တည်ဆောက်နိုင်အောင် durable store ထဲမှတ်ထားတဲ့ session ဖြစ်ပါတယ်။ Active Context Window နဲ့ session history အပြည့်အစုံက တူချင်မှတူပါမယ်။

## Parity Contract

Upstream နဲ့ port ကြား observable behavior တစ်ခုကို ID၊ evidence test နဲ့ status တို့နဲ့ သတ်မှတ်ထားတဲ့ စစ်ဆေးနိုင်သော claim ဖြစ်ပါတယ်။

## Behavioral Contract

သတ်မှတ်ထားတဲ့ observable input နဲ့ state အတွက် ရလာရမယ့် output၊ ordering သို့မဟုတ် failure boundary ကို test လုပ်နိုင်အောင် ရေးထားတဲ့ သတ်မှတ်ချက်ကို Behavioral Contract လို့ခေါ်ပါတယ်။

## Intentional Divergence

Upstream behavior နဲ့ သိသိသာသာကွာအောင် ရွေးထားပြီး reason နဲ့ safety evidence ကို မှတ်ထားတဲ့ design choice ဖြစ်ပါတယ်။ မပြီးသေးတဲ့ parity work နဲ့ မရောသင့်ပါဘူး။

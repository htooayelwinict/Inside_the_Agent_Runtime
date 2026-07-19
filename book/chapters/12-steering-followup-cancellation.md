# Chapter 12 — Agent ကို လမ်းပြန်ညွှန်ရတဲ့အချိန်

## ၁၂.၁ အချက်အလက်အသစ်က Run အလယ်ရောက်လာတဲ့အခါ

စနေနေ့မနက်မှာ Lewis က မနေ့ညက failing test ကို Agent အား ပြန်စစ်ခိုင်းလိုက်ပါတယ်။ Agent က `tests/unit/` အောက်က file ဟောင်းတွေကို ဖတ်ပြီး parser ရဲ့ result order ကို လိုက်စစ်နေတယ်။ အဲဒီအချိန်မှာ Lewis က CI log အပြည့်ကို ပြန်ဖွင့်ကြည့်လိုက်တော့ failure က အဲဒီ path မှာမဟုတ်ဘဲ `tests/integration/` အောက်က focused test မှာဖြစ်နေကြောင်း တွေ့သွားပါတယ်။

```text
Lewis: Failure က integration path မှာ။ unit path ကို ဆက်မကြည့်နဲ့။
Agent: inspecting tests/unit/test_parser.py ...
```

အချက်အလက်အသစ်က မှန်ပေမယ့် ဘယ်အချိန်အသုံးဝင်မလဲဆိုတာ မရှင်းသေးပါဘူး။ Lewis မှာ လုပ်ချင်စရာသုံးခု ချက်ချင်းပေါ်လာတယ်။ လက်ရှိ Run ကို လမ်းပြန်ညွှန်ဖို့ steering ပို့မလား။ ဒီအလုပ်ပြီးမှ focused test run ခိုင်းဖို့ follow-up ထားမလား။ လမ်းမှားသွားပြီဆိုပြီး abort လုပ်မလား။

ဒီသုံးခုက စာသားတစ်ကြောင်းပို့တာနဲ့ Run တစ်ခုကိုရပ်တာလောက်ပဲလို့ ထင်ရနိုင်ပါတယ်။ တကယ်တော့ အချိန် boundary နဲ့ ownership မတူပါဘူး။ Lewis လိုချင်တာက “နောက် model call က path အသစ်ကိုသိစေချင်တယ်” ဆိုရင် steering ဖြစ်ပါတယ်။ “လက်ရှိအဖြေပြီးရင် focused test ကို သီးခြားဆက်လုပ်စေချင်တယ်” ဆိုရင် follow-up ဖြစ်ပါတယ်။ လက်ရှိ Run က ဘေးကင်းစွာဆက်မသွားသင့်တော့ဘူးဆိုရင်မှ abort ကို စဉ်းစားရပါတယ်။

Lewis နဲ့ ဒီဖြစ်ရပ်က concept သင်ဖို့ ဖန်တီးထားတဲ့ စိတ်ကူးယဉ်ဇာတ်လမ်းပါ။ တကယ့် Travis234 incident သို့မဟုတ် source project contributor တစ်ယောက်ရဲ့အဖြစ်အပျက် မဟုတ်ပါဘူး။ အောက်မှာရှင်းမယ့် queue drain၊ abort နဲ့ RunLease behavior တွေကိုတော့ pinned Pi နဲ့ Travis234 source evidence အပေါ် အခြေခံထားပါတယ်။

## ၁၂.၂ Queue ဆိုတာ Message စုပုံထားတာထက် ပိုတယ်

Message အသစ်ရောက်လာတာနဲ့ model က ချက်ချင်းသိသွားတယ်လို့ ယူဆမိရင် boundary အားလုံးရောသွားပါတယ်။ Model က live conversation တစ်ခုကို နောက်ကွယ်ကနေ အမြဲနားထောင်နေသူမဟုတ်ပါဘူး။ Runtime က request တစ်ကြိမ်အတွက်ပေးလိုက်တဲ့ context ကိုသာ အဲဒီ model call က မြင်ပါတယ်။ Queue ထဲဝင်လာတဲ့ message က context ထဲမဝင်သေးသရွေ့ လက်ရှိ request က မသိနိုင်ပါဘူး။

`Queue` ဆိုတာ မစီမံရသေးတဲ့ Message တွေစုပုံထားတဲ့နေရာတစ်ခုတည်း မဟုတ်ပါဘူး။ “ဒီ message ကို ဘယ် control-flow boundary မှာယူမလဲ” ဆိုတဲ့ intent ကိုပါ ခွဲထားပေးပါတယ်။ Steering queue နဲ့ follow-up queue နှစ်ခုလုံးမှာ user စာသားရှိနိုင်ပေမယ့် drain point မတူလို့ Runtime behavior မတူတာပါ။

Message arrival နဲ့ message consumption ကို ခွဲမှတ်ရပါတယ်။ Arrival က queue ထဲသို့ enqueue လုပ်တဲ့အချိန်ပါ။ Consumption က loop က queue ကိုစစ်၊ message ကိုယူပြီး model မြင်မယ့် context ထဲထည့်တဲ့အချိန်ပါ။ ဒီနှစ်ခုကြားမှာ assistant stream သို့မဟုတ် Tool Call တစ်ခု run နေနိုင်ပါတယ်။ ဒါကြောင့် UI မှာ “sent” လို့မြင်ရတာကို “current tool က direction အသစ်အတိုင်းပြောင်းပြီးပြီ” လို့မဖတ်သင့်ပါဘူး။

Queue ကိုခွဲထားခြင်းရဲ့အကျိုးက စာသားကိုမပျောက်စေရုံမဟုတ်ပါဘူး။ လက်ရှိ reasoning chain ထဲဝင်သင့်တာနဲ့ နောက်အလုပ်တစ်ခုအဖြစ်စသင့်တာကို Runtime က မရောစေဖို့ပါ။

## ၁၂.၃ Steering ဝင်တဲ့ Inner-loop Boundary

Agent က file တစ်ခုဖတ်ပြီး Tool Result ပြန်ရတော့မယ့်အချိန် Lewis ဆီ path အသစ်ရောက်လာတယ်ဆိုပါစို့။ `Steering` ဆိုတာ လက်ရှိ Run ရဲ့ ဦးတည်ချက်ကို နောက် model boundary မှာ ပြောင်းပေးမယ့် Message ပါ။ Inner loop က လက်ရှိ assistant/tool turn ကို သတ်မှတ်ထားတဲ့ boundary အထိရောက်အောင် ကိုင်တွယ်ပြီး pending steering ကို drain လုပ်တယ်။ ပြီးမှ အဲဒီ Message ပါတဲ့ updated context နဲ့ model ကို ထပ်ခေါ်ပါတယ်။

Flow ကို ချုံ့ကြည့်ရင် ဒီလိုဖြစ်ပါတယ်။

```text
assistant response → requested tool work → turn boundary
                                      ↓
                         drain steering message
                                      ↓
                     next model call with new context
```

ဒီ order ကြောင့် Lewis ရဲ့ “integration path ကိုစစ်” ဆိုတဲ့အချက်က နောက် assistant response ကို လမ်းပြနိုင်ပါတယ်။ Agent က file ဟောင်းကိုအခြေခံပြီး နောက်ထပ် Tool Call မထုတ်ခင် path အသစ်ကို ဖတ်နိုင်သွားတယ်။ Steering ကို current Run ရဲ့ continuation အဖြစ်ယူတာကြောင့် outer follow-up အလုပ်အသစ်တစ်ခုလို မစောင့်ရပါဘူး။

ဒါပေမယ့် steering message က run နေပြီးသား tool body ကို ပြန်ရေးပေးတာမဟုတ်ပါဘူး။ Tool က file ဟောင်းကိုဖတ်နေပြီးသားဆိုရင် steering enqueue လုပ်ခြင်းတစ်ခုတည်းနဲ့ အဲဒီ I/O ပျက်မသွားပါဘူး။ Tool ပြီးခြင်း သို့မဟုတ် cooperative cancellation ကိုတုံ့ပြန်ခြင်းက သီးခြား boundary ဖြစ်ပါတယ်။ Steering ရဲ့အာမခံချက်ကို “နောက် model call မတိုင်ခင် direction အသစ်ထည့်ပေးခြင်း” အဖြစ်ပဲ မှတ်ရပါမယ်။

## ၁၂.၄ Follow-up စတင်တဲ့ Outer-loop Boundary

Lewis က “လက်ရှိစစ်ဆေးချက်ပြီးရင် focused test ကို run ပေး” လို့ပြောချင်ရင် လက်ရှိ reasoning ကိုကြားဖြတ်စရာမလိုပါဘူး။ `Follow-up` ဆိုတာ လက်ရှိ inner-loop အလုပ်ပြီးသွားတဲ့နောက် outer loop ကယူပြီး နောက် turn ကိုစတင်ပေးမယ့် Message ပါ။

Inner loop မှာ ဆက်လုပ်ရမယ့် Tool Call မရှိ၊ pending steering လည်းမရှိတော့မှ Runtime က outer boundary ဆီရောက်ပါတယ်။ အဲဒီအချိန် follow-up ရှိရင် inner loop ကို Message အသစ်နဲ့ ပြန်ဝင်စေပါတယ်။ မရှိမှ Run က အဆုံးသတ်ဖို့ အဆင်သင့်ဖြစ်ပါတယ်။ ဒီအတွက် follow-up က “နောက်ဆုံး answer ထွက်ပြီးနောက် user က နောက်တစ်ခါ button နှိပ်ရမယ်” ဆိုတဲ့ UI convenience တစ်ခုထက်ပိုပါတယ်။ Run မပိတ်ခင် ဆက်စပ်အလုပ်တစ်ခုကို စနစ်တကျ လွှဲပေးတဲ့ outer-loop control ဖြစ်ပါတယ်။

Steering နဲ့ follow-up ကို စာသားအကြောင်းအရာနဲ့မခွဲနိုင်ပါဘူး။ “focused test ကို run ပါ” ဆိုတဲ့စာသားတူတူကို လက်ရှိ tool chain ရဲ့ နောက် model call မတိုင်ခင်သိစေချင်ရင် steering ဖြစ်ပြီး၊ လက်ရှိ answer ပြီးမှ နောက်အလုပ်အဖြစ်စေချင်ရင် follow-up ဖြစ်ပါတယ်။ ခွဲပေးတာက စာသားမဟုတ်ဘဲ drain boundary ပါ။

## ၁၂.၅ Abort၊ Cancel နဲ့ Continue ကို မရောခြင်း

လမ်းမှားနေတဲ့ Run တစ်ခုကိုမြင်ရင် abort က အမြန်ဆုံးဖြေရှင်းချက်လို ထင်ရပါတယ်။ ဒါပေမယ့် `Abort` ဆိုတာ active Run ကို ဆက်မစေလိုကြောင်း cooperative signal ပေးခြင်းပါ။ Signal ကို loop၊ provider adapter သို့မဟုတ် tool က သက်ဆိုင်ရာ boundary မှာ သတိပြုပြီးမှ ရပ်နိုင်ပါတယ်။ Abort က operating-system process ကို `force-kill` လုပ်တာမဟုတ်ပါဘူး။ Running tool တစ်ခုလည်း message ရောက်တာနဲ့ အလိုအလျောက် ချက်ချင်းရပ်သွားမယ်လို့ မဆိုနိုင်ပါဘူး။

`Cancellation` က အဲဒီ signal ကို ongoing operation တစ်ခုက ဘယ်လိုလက်ခံပြီး ပြီးဆုံးမလဲဆိုတဲ့ ပိုကျယ်တဲ့ mechanism ပါ။ Provider stream က cancellation ကိုလက်ခံနိုင်ပေမယ့် blocking tool တစ်ခုက signal ကိုမစစ်ရင် ပြန်လာတဲ့အထိစောင့်ရနိုင်ပါတယ်။ Source-backed contract က abort ကိုသိပြီးနောက် model သို့မဟုတ် tool work အသစ်မစရဘူးဆိုတာပါ။ လုပ်နေပြီးသား external work ကို အတင်းဖျက်နိုင်တယ်ဆိုတဲ့ အာမခံချက် မပါပါဘူး။

`Continue` ကတော့ ရပ်ခိုင်းတာမဟုတ်ပါဘူး။ Steering သို့မဟုတ် follow-up ရှိလို့ loop က နောက် model boundary သို့မဟုတ် နောက် outer turn ဆီ ဆက်သွားခြင်းကို ဆိုလိုပါတယ်။ Path အသစ်သိရုံနဲ့ လက်ရှိ read က အန္တရာယ်မရှိဘူးဆိုရင် Lewis က steering သုံးနိုင်တယ်။ မှားတဲ့ Tool Call က irreversible mutation လုပ်တော့မယ်ဆိုရင် abort လိုနိုင်တယ်။ လက်ရှိ result ကိုယူပြီးမှ focused test သီးခြား run ချင်ရင် follow-up က ပိုမှန်ပါတယ်။

## ၁၂.၆ RunLease က ဘာကိုပိုင်ခွင့်ပေးသလဲ

User က request နှစ်ခုမြန်မြန်ပို့လိုက်တဲ့အခါ Agent state ကို Run နှစ်ခုက တစ်ပြိုင်နက်ပြင်လို့ရမလား။ ဒီမေးခွန်းကို `RunLease` က ဖြေပါတယ်။ RunLease ဆိုတာ active Run ownership ကို serialise လုပ်ဖို့သုံးတဲ့ lease ဖြစ်ပါတယ်။ Owner တစ်ခုက lease ကိုကိုင်ထားစဉ် နောက် requester က ownership ရဖို့စောင့်ရပြီး၊ လက်ရှိ owner က release လုပ်ပြီးမှ နောက်တစ်ခုက active ဖြစ်နိုင်ပါတယ်။

ဒီ ownership ကြောင့် shared messages၊ queue drain နဲ့ lifecycle end ကို Run နှစ်ခုက ရောယှက်ကိုင်တွယ်မယ့်အန္တရာယ် လျော့သွားပါတယ်။ Release ကို idempotent ဖြစ်အောင်ထားခြင်းက cleanup path နှစ်ခုက release ပြန်ခေါ်မိလည်း ownership state ကို နှစ်ခါဖျက်မသွားစေပါတယ်။ ဒါက error နဲ့ cancellation path တွေမှာ အထူးအသုံးဝင်ပါတယ်။

RunLease က execution လုပ်ခွင့်ကို စီပေးတာပါ။ Tool ကိုရပ်ပစ်နိုင်တဲ့စွမ်းအား မပေးပါဘူး။ Abort signal ပို့ခြင်းနဲ့ lease release လုပ်ခြင်းလည်း တူတာမဟုတ်ပါဘူး။ Active Run က cleanup မပြီးခင် ownership ကိုစောစောလွှတ်လိုက်ရင် နောက် Run က မပြီးသေးတဲ့ state ပေါ်ဝင်လာနိုင်ပါတယ်။ ဒါကြောင့် “ဘယ်သူ run နေတာလဲ” ကို RunLease က ဖြေပြီး “အဲဒီ run ဘယ်လိုရပ်မလဲ” ကို cooperative cancellation က ဖြေပါတယ်။

## ၁၂.၇ Offline Message-control Lab

Drain point ကွာတာကို provider မပါဘဲမြင်ချင်ရင် [`examples/lewis_message_control.py`](../../examples/lewis_message_control.py) ကို repository root ကနေ run နိုင်ပါတယ်။ Run မလုပ်ခင် steering နဲ့ follow-up ဘယ်စာကြောင်းရဲ့ ရှေ့နောက်မှာပေါ်မလဲ ခန့်မှန်းကြည့်ပါ။

```bash
python3.13 examples/lewis_message_control.py
```

Output ခြောက်ကြောင်းအတိအကျက:

```text
model:inspect source
turn_end
steering:check tests first
model:continue with steering
turn_end
follow_up:run focused test
```

Lab က deque နှစ်ခုထဲ Message တစ်ခုစီထည့်ပြီး ပထမ `turn_end` နောက်မှာ steering ကို drain လုပ်ကာ steered model continuation ကိုစပါတယ်။ အဲဒီ inner work ရဲ့ `turn_end` နောက်မှ follow-up ကို outer boundary မှာယူပါတယ်။ `drain_one()` က တစ်ကြိမ်မှာ Message တစ်ခုသာယူလို့ boundary ကို output ကနေ လွယ်လွယ်မြင်နိုင်ပါတယ်။ ဒီ example က queue drain placement ကိုသာ model လုပ်ထားတာပါ။

ဒါက production Agent Loop မဟုတ်ပါဘူး။ Live provider cancellation၊ threads၊ concurrent arrival၊ Tool Call execution၊ RunLease ownership သို့မဟုတ် network timing ကို မ simulate လုပ်ပါဘူး။ Output ခြောက်ကြောင်းမှန်တာက steering/follow-up placement သင်ခန်းစာကိုသာ စစ်ပေးပြီး production cancellation အလုပ်မှန်ကြောင်း မသက်သေပြပါဘူး။

## ၁၂.၈ မှားလွယ်တဲ့ Race Conditions

Message-control code မှာ bug တချို့က အမြဲမဖြစ်ဘဲ timing တိုက်ဆိုင်မှပေါ်ပါတယ်။ `Race condition` ဆိုတာ outcome က concurrent events တွေရဲ့ မသေချာတဲ့အချိန်အစီအစဉ်ပေါ် မတော်တဆမှီခိုသွားခြင်းပါ။ ဒီနေရာမှာ အောက်ကအမှားတွေကို သတိထားရပါတယ်။

- Queue ကို empty လို့စစ်ပြီး model ခေါ်မယ့်ကြားမှာ steering အသစ်ဝင်နိုင်ပါတယ်။ ဒီ Message ကို လက်ရှိ snapshot ထဲအတင်းထည့်မယ်လို့မယူဆဘဲ သတ်မှတ်ထားတဲ့ နောက် drain boundary မှာယူရပါမယ်။
- Tool run နေချိန် abort ရောက်လာနိုင်ပါတယ်။ Result ပြန်လာပြီးနောက် abort state ကိုပြန်မစစ်ဘဲ Tool Call အသစ်စလိုက်ရင် “abort သိပြီးနောက် work အသစ်မစ” ဆိုတဲ့ contract ပျက်ပါတယ်။
- Drain လုပ်ပြီး context ထဲမထည့်ခင် exception ဖြစ်ရင် Message ပျောက်နိုင်ပါတယ်။ Queue mutation နဲ့ context insertion ဘယ်အပိုင်းက ownership ယူသလဲ ရှင်းရပါမယ်။
- Run အဟောင်းရဲ့ cleanup က နောက် Run ရဲ့ ownership state ကို release လုပ်မိရင် active owner မှားသွားနိုင်ပါတယ်။ Owner identity နဲ့ idempotent release မရှိရင် ဒီ bug ကို log order တစ်ခုတည်းနဲ့ရှာရခက်ပါတယ်။

Race ကိုဖြေရှင်းဖို့ queue အားလုံးကို lock တစ်ခုနဲ့ပိတ်ထားရုံ မလုံလောက်ပါဘူး။ Drain point၊ abort check နဲ့ lease ownership တို့ရဲ့ contract ကို သီးခြားရေးပြီး boundary အလိုက် test လုပ်ရပါတယ်။ Timing ပြောင်းလဲမှုကို ခံနိုင်တာက တစ်ကြောင်းချင်းမြန်ခြင်းထက် ပိုအရေးကြီးပါတယ်။

## ၁၂.၉ Lewis ရဲ့မှတ်စု

Lewis က integration path ကို steering အဖြစ်ပို့ပြီး focused test ကို follow-up အဖြစ်ထားလိုက်ပါတယ်။ Notebook မှာတော့ ဒီလိုချုပ်ထားတယ်။

- Message ရောက်ချိန်နဲ့ model မြင်ချိန်ကို တစ်ချိန်တည်းလို့ မယူဆဘူး။
- Steering က inner-loop ရဲ့ next model boundary၊ follow-up က completed inner work နောက် outer-loop boundary မှာဝင်တယ်။
- Abort ကို tool အတင်းပိတ်မယ့်ခလုတ်လို မသုံးဘဲ cooperative signal လို့ယူမယ်။
- RunLease က active owner ကိုစီပေးတာဖြစ်ပြီး cancellation mechanism မဟုတ်ဘူး။
- Lab output က drain placement ကိုပဲပြတယ်ဆိုတဲ့ boundary ကို output နဲ့တွဲမှတ်မယ်။

အချက်အလက်အသစ်ရတာထက် အဲဒီအချက်ကို ဘယ် boundary မှာသုံးမလဲ ဆုံးဖြတ်နိုင်တာက Runtime ကိုပိုယုံကြည်ရစေပါတယ်။

## ၁၂.၁၀ အနှစ်ချုပ်

- Steering Message ကို inner loop က drain လုပ်ပြီး နောက် model call ရဲ့ context ထဲထည့်တယ်။ Running tool ကို သူ့ဘာသာမရပ်စေဘူး။
- Follow-up Message ကို လက်ရှိ inner work ပြီးနောက် outer loop ကယူပြီး နောက် turn စတင်တယ်။
- Abort က cooperative signal ဖြစ်ပြီး သိရှိပြီးနောက် model/tool work အသစ်မစရဘူး။ လုပ်နေပြီးသား work ချက်ချင်းပျက်မယ်လို့ အာမမခံဘူး။
- RunLease က active Run တစ်ခုချင်းရဲ့ ownership၊ wait နဲ့ idempotent release ကိုထိန်းပြီး abort ကိုယ်စားမလုပ်ဘူး။
- Offline lab က steering/follow-up drain placement ကိုသာပြပြီး live provider cancellation၊ threads နဲ့ RunLease ကို မစမ်းဘူး။

## ၁၂.၁၁ Source Notes

- Executable teaching model: [`examples/lewis_message_control.py`](../../examples/lewis_message_control.py)
- `C-MESSAGE-DRAIN` — `P-LOOP`, `P-AGENT`, `T-LOOP`, `T-AGENT`; steering inner-loop drain နဲ့ follow-up outer-loop drain boundary
- `C-ABORT-OWNERSHIP` — `T-LOOP`, `T-AGENT`, `T-RUN-LEASE`; cooperative abort၊ active owner wait နဲ့ idempotent release boundary
- Pi revision: `1f0dbc008c9b3e88017d42e8a1b46d416ad2b6b6`
- Travis234 revision: `68b1831691b8ec93f9550ce63b80cdcb7a591b2e`

Exact source links နဲ့ evidence boundary ကို [Pinned Source Map](../references/SOURCE_MAP.md) မှာ ကြည့်နိုင်ပါတယ်။ Claim တစ်ခုချင်းရဲ့ verification scope ကို [Technical Claim Ledger](../references/CLAIM_LEDGER.md) မှာ ဖတ်နိုင်ပါတယ်။ Lewis ရဲ့ incident နဲ့ dialogue က fictional ဖြစ်ပြီး source-backed production history မဟုတ်ပါဘူး။

---

Previous: [Chapter 11 — တစ်ညနဲ့မပြီးတဲ့ Bug](11-one-night-unfinished-bug.md)

Next: [Chapter 13 — Tool က အမှားပြန်လာတဲ့အခါ](13-when-tools-fail.md)

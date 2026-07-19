# Chapter 14 — ပြန်ဖွင့်လိုက်တော့ အလုပ်ဘယ်ကဆက်မလဲ

ည ၁၁ နာရီကျော်တော့ Lewis ရဲ့ Agent က ordering bug အတွက် စုထားတဲ့ context ကို compact လုပ်ပြီးပါပြီ။ Summary ထဲမှာ goal နဲ့ တွေ့ထားတဲ့ evidence ရှိတယ်။ Recent tail ထဲမှာ `fast` Tool က အရင်ပြီးခဲ့ပေမယ့် results ကို source order နဲ့ ပြန်ထည့်ရမယ်ဆိုတဲ့ နောက်ဆုံးတွေ့ရှိချက်ရှိတယ်။ Lewis က focused test မအောင်သေးကြောင်း message တစ်ကြောင်းထပ်ပို့ပြီး terminal ကိုပိတ်လိုက်ပါတယ်။

နောက်မနက် process အသစ်စချိန်မှာ မနေ့ညက Python objects တွေ memory ထဲမရှိတော့ပါဘူး။ Lewis က “Agent က မနေ့ကအလုပ်ကို မှတ်မိသေးလား” လို့ မမေးတော့ဘဲ “Session store ထဲက ဘယ် entries တွေကိုယူပြီး active context ကို ပြန်တည်ဆောက်မလဲ” လို့ မေးလိုက်ပါတယ်။ စကားလုံးနည်းနည်းပြောင်းလိုက်တာနဲ့ တာဝန်ရှိတဲ့ component ကို ရှင်းရှင်းမြင်လာပါတယ်။

Terminal အသစ်မှာ in-memory messages အရေအတွက်က သုညကနေစပါတယ်။ ဒါပေမယ့် မနေ့ညက session file ကိုရွေးလိုက်တဲ့အခါ entries တွေက ရှိနေသေးတယ်။ Lewis က prompt အသစ်မပို့သေးဘဲ restore result ကိုအရင်ကြည့်လိုက်ပါတယ်။ Goal နဲ့ evidence ပါတဲ့ summary က ပထမ၊ ordering evidence က ဒုတိယ၊ focused test မအောင်သေးကြောင်းစာက နောက်ဆုံးမှာ ရှိရပါမယ်။ မနေ့က inspection အဟောင်းတချို့ ပြန်ပေါ်လာရင် Compaction boundary ပျက်နေပြီဖြစ်ပါတယ်။

Output အစီအစဉ်သုံးခု မှန်နေတာကိုမြင်မှ Lewis က “test failure ကနေဆက်စစ်ပါ” လို့ prompt အသစ်ပို့တယ်။ သူ့အတွက် အလုပ်ဆက်နိုင်ခြင်းရဲ့အကြောင်းရင်းက model တစ်ခုက ညလုံးပေါက်အဖြေကိုသိမ်းထားလို့ မဟုတ်ပါဘူး။ Process အသစ်က durable records ကိုမှန်တဲ့ boundary နဲ့ ပြန်ဖတ်ပေးထားလို့ပါ။

`ဒီ Lewis incident က persistence boundary ကိုသင်ဖို့ ဖန်တီးထားတဲ့ စိတ်ကူးယဉ်ဇာတ်လမ်းပါ။ Lewis ဟာ Travis234 သို့မဟုတ် Pi ရဲ့ contributor တစ်ယောက်မဟုတ်သလို ဒီ terminal ပိတ်သွားမှုက production incident မှတ်တမ်းလည်း မဟုတ်ပါဘူး။ အောက်မှာရှင်းမယ့် restore behavior ကတော့ Source Notes ထဲက pinned source နဲ့ tests အပေါ် အခြေခံထားပါတယ်။`

## ၁၄.၁ Process ပိတ်သွားပေမယ့် အလုပ်မပျောက်သင့်ဘူး

Process တစ်ခုအဆုံးသတ်တာနဲ့ model က ပိုင်ဆိုင်ထားတဲ့ ကိုယ်ပိုင်မှတ်ဉာဏ်တစ်ခုကို ပြန်နိုးရမယ်လို့ ယူဆရင် restart ကို မှားတဲ့နေရာမှာရှာမိပါမယ်။ Model request တစ်ကြိမ်က Runtime ပို့ပေးတဲ့ context ကိုဖတ်တာပါ။ မနေ့ညက task၊ Tool Result နဲ့ဆုံးဖြတ်ချက်တွေကို နောက်နေ့ request က မြင်ရခြင်းဟာ model က session memory ကိုပိုင်လို့မဟုတ်ဘဲ Runtime က persisted entries တွေကနေ input ကို ပြန်တည်ဆောက်ပေးလို့ ဖြစ်ပါတယ်။

Lewis အတွက် ရင်ဆိုင်နေရတဲ့မေးခွန်းက transcript file ရှိမရှိတစ်ခုတည်း မဟုတ်ပါဘူး။ ရှည်လွန်းတဲ့ history ကို compact လုပ်ထားပြီးသားဖြစ်လို့ raw messages အားလုံးကို ပြန်တင်လိုက်ရင် မနေ့ညက ချုံ့ထားတဲ့ boundary ပျက်သွားနိုင်ပါတယ်။ Summary တစ်ခုတည်းပြန်တင်ရင်လည်း လတ်တလော evidence နဲ့ Compaction ပြီးမှပို့ထားတဲ့ “focused test still fails” message ပျောက်နိုင်ပါတယ်။ Restore မှန်ဖို့ summary၊ retained tail နဲ့ နောက်မှထပ်ဝင်လာတဲ့ messages သုံးပိုင်းစလုံး လိုပါတယ်။

## ၁၄.၂ In-memory Context နဲ့ Persistent Session

စာရေးနေတုန်း clipboard ထဲကစာနဲ့ disk ပေါ်က document ကို စဉ်းစားကြည့်ပါ။ Clipboard က ချက်ချင်းသုံးရလွယ်ပေမယ့် application ပိတ်ရင် ပျောက်နိုင်တယ်။ Disk document ကတော့ နောက်တစ်ကြိမ်ပြန်ဖွင့်ဖို့ ရည်ရွယ်ထားတယ်။ Agent Runtime မှာလည်း လက်ရှိ process သုံးနေတဲ့ `in-memory context` နဲ့ restart ကျော်ပြီး ပြန်ဖတ်နိုင်တဲ့ `persistent session` ကို ခွဲမြင်ရပါတယ်။

In-memory context ဆိုတာ နောက် model request ဆီပို့ဖို့ Runtime က လက်ရှိထိန်းထားတဲ့ messages ပါ။ Tool Call တစ်ခုပြီးရင် Tool Result ထည့်ခြင်း၊ Compaction ပြီးရင် compacted context နဲ့အစားထိုးခြင်းတို့ကို ဒီ runtime state မှာမြင်ရပါတယ်။ မြန်ပေမယ့် process lifetime နဲ့ချည်ထားပါတယ်။

Persistent session ဆိုတာ conversation ရဲ့ durable entries နဲ့ သူတို့ရဲ့ဆက်နွယ်မှုကို store မှာမှတ်ထားခြင်းပါ။ Persistence ရဲ့ရည်ရွယ်ချက်က memory list တစ်ခုကို JSON ပြောင်းရေးရုံမဟုတ်ပါဘူး။ နောက် process က ဘယ်လမ်းကြောင်းကို active လို့ယူရမလဲ၊ Compaction boundary ဘယ်မှာရှိသလဲနဲ့ အဲဒီ boundary ကနေ context ဘယ်လိုဆောက်ရမလဲ ပြန်ဆုံးဖြတ်နိုင်ဖို့ပါ။ ဒါကြောင့် store က archive ဖြစ်သလို reconstruction input လည်း ဖြစ်ပါတယ်။

## ၁၄.၃ Session Entry နဲ့ Active Branch

Session ကို messages တန်းစီထားတဲ့ list တစ်ခုတည်းလို့မြင်ရင် branch ပြောင်းထားတဲ့ conversation မှာ ဘာကိုပြန်တင်ရမလဲ မရှင်းတော့ပါဘူး။ `Session Entry` ဆိုတာ store ထဲက durable record တစ်ခုပါ။ Message ဖြစ်နိုင်သလို Compaction၊ model setting သို့မဟုတ် session metadata လည်း ဖြစ်နိုင်ပါတယ်။ Entry တစ်ခုရဲ့ parent ဆက်နွယ်မှုက conversation lineage ကိုဖော်ပြပါတယ်။

`Active branch` ဆိုတာ လက်ရှိ leaf ဆီရောက်တဲ့ parent path ပါ။ Store ထဲမှာ branch အဟောင်းရဲ့ entries တွေရှိနေသေးနိုင်ပေမယ့် context ပြန်ဆောက်ချိန်မှာ file ထဲရှိသမျှကို ပေါင်းမထည့်ရပါဘူး။ Active leaf ကနေ parent links အတိုင်းရတဲ့ branch ကိုအရင်ရွေးပြီးမှ အဲဒီ branch ထဲက state နဲ့ messages ကိုဖတ်ရပါတယ်။ ဒီလိုမခွဲရင် စွန့်ထားတဲ့အဖြေတစ်ခု သို့မဟုတ် အဟောင်း prompt တစ်ခု နောက် request ထဲပြန်ဝင်နိုင်ပါတယ်။

Travis234 ရဲ့ session store က active branch ကိုယူပြီး context snapshot တည်ဆောက်ပါတယ်။ Snapshot မှာ messages တင်မက thinking level၊ model၊ session name နဲ့ generation parameters လို runtime settings တွေလည်း branch ပေါ်က latest entries အတိုင်း ပြန်ရနိုင်ပါတယ်။ ဒီ chapter က message restoration ကိုအဓိကထားပေမယ့် “resume” ဆိုတာ စာသားတစ်မျိုးတည်း ပြန်ဖတ်ခြင်းထက် ကျယ်ကြောင်း သိထားရပါမယ်။

## ၁၄.၄ Compaction Entry က ဘာတွေသိမ်းသလဲ

Context ကို compact လုပ်ပြီး compacted messages ကို memory ထဲပဲအစားထိုးထားရင် လက်ရှိ process အတွက် အလုပ်ဖြစ်နိုင်ပါတယ်။ Restart ပြီးရင်တော့ store က အဲဒီဆုံးဖြတ်ချက်ကို မသိပါဘူး။ Persistent flow မှာ Compaction ရလဒ်ကို သီးခြား entry အဖြစ် append လုပ်တာ ဒီအတွက်ပါ။

Compaction entry ရဲ့အဓိက fields ကို ဒီလိုဖတ်နိုင်ပါတယ်။

- `summary` က ချုံ့လိုက်တဲ့အဟောင်းအပိုင်းရဲ့ structured handoff ဖြစ်တယ်။
- `firstKeptEntryId` က raw ပုံစံအတိုင်း ဆက်ထားရမယ့် tail ရဲ့ပထမ entry ကိုညွှန်တယ်။
- `tokensBefore` က Compaction မတိုင်ခင် token estimate ကိုမှတ်ထားတယ်။
- `details` က read/modified files၊ summary provenance သို့မဟုတ် cooldown ဆိုင်ရာ metadata လို ထပ်ဆောင်းအချက်တွေ ပါနိုင်တယ်။

ဒီ fields အားလုံးကို model-facing message တစ်ကြောင်းထဲ အတိုင်းသားထည့်ရမယ်လို့ မဆိုလိုပါဘူး။ ဥပမာ provenance နဲ့ operational error detail တချို့က store မှာ evidence အဖြစ်ရှိနိုင်ပေမယ့် model context ထဲမပို့သင့်ပါဘူး။ Restore logic အတွက် အဓိက anchor နှစ်ခုက summary နဲ့ `firstKeptEntryId` ဖြစ်ပြီး `tokensBefore` က compacted state ရဲ့အရွယ်အစားကို ဖော်ပြတဲ့ metadata ပါ။

Compaction entry အသစ်ကို append လုပ်ခြင်းက အရင် lineage ကိုဖျက်ပစ်တာမဟုတ်ပါဘူး။ Active model context တိုသွားပေမယ့် store ထဲမှာ boundary ကို explicit record အဖြစ် သိမ်းထားနိုင်ပါတယ်။ Persist ပြီးတာနဲ့ adapter က store ကနေ context ပြန် build လုပ်ပြီး in-memory state ကိုညှိခြင်းကြောင့် လက်ရှိ process နဲ့ နောက် restart နှစ်ခုလုံး တူညီတဲ့ reconstruction rule ကိုသုံးနိုင်ပါတယ်။

## ၁၄.၅ First-kept Anchor ကနေ Tail ပြန်တည်ဆောက်ခြင်း

Lewis ရဲ့ stored branch ကို ရိုးရိုးပုံနဲ့ကြည့်ရင် anchor ရဲ့အလုပ်ကို မြင်လွယ်ပါတယ်။

```text
Stored active branch
m1 goal → m2 old inspection → m3 ordering evidence → c1 compaction → m4 test still fails
                              ↑ first-kept

Restored active context
summary(c1) → m3 ordering evidence → m4 test still fails
```

Restore လုပ်ချိန်မှာ active branch ထဲက `latest Compaction` ကိုအရင်ရှာပါတယ်။ Compaction တစ်ကြိမ်ထက်ပိုရှိရင် အဟောင်း summary ကိုပါ ထပ်ထည့်မယ့်အစား နောက်ဆုံး summary က active compressed history ရဲ့အစဖြစ်ရပါတယ်။ ပြီးရင် အဲဒီ entry ရဲ့ `firstKeptEntryId` ကို branch ရဲ့ Compaction မတိုင်ခင်အပိုင်းထဲရှာပြီး anchor ကစတဲ့ message entries ကို မူရင်းပုံစံအတိုင်းထည့်ပါတယ်။ ဒါက retained tail ပါ။

နောက်ဆုံးမှာ Compaction entry ပြီးမှ append လုပ်ထားတဲ့ messages တွေကို အစီအစဉ်မပျက် ဆက်ထည့်ပါတယ်။ Diagram ထဲက `m4` ဟာ Compaction ရဲ့ tail မဟုတ်ပါဘူး။ Compaction ပြီးမှအသစ်ဝင်လာတဲ့ later message ဖြစ်ပါတယ်။ ဒါပေမယ့် နောက် request အတွက် လတ်တလောအခြေအနေဖြစ်လို့ restore မှာ ပါရပါမယ်။ Latest summary၊ first-kept anchor ကစတဲ့ retained tail နဲ့ later messages သုံးခုကို ဒီအစီအစဉ်နဲ့ပေါင်းမှ pruned အဟောင်းကို ပြန်မဖော်ဘဲ active work ကိုဆက်နိုင်ပါတယ်။

Compaction မရှိသေးတဲ့ branch ဆိုရင် summary anchor မလိုပါဘူး။ Context အဖြစ်ပြောင်းနိုင်တဲ့ branch messages တွေကို အစီအစဉ်အတိုင်း ပြန်တည်ဆောက်နိုင်ပါတယ်။ တစ်ဖက်မှာ anchor မှားနေခြင်းကို မသိဘဲကျော်သွားမယ်ဆိုရင် လတ်တလော causal turn ပျောက်နိုင်လို့ persistence writer နဲ့ restore tests က boundary တူကြောင်း စစ်ရပါတယ်။

## ၁၄.၆ Restart ပြီး Active Context ပြန်ရခြင်း

နောက်နေ့ process က model ဆီ “မနေ့ကဘာလုပ်ခဲ့သလဲ” လို့ မေးပြီး context ကိုခန့်မှန်းခိုင်းတာ မဟုတ်ပါဘူး။ Restart restoration ရဲ့ flow ကို component တာဝန်နဲ့ခွဲကြည့်ရင် ဒီလိုဖြစ်ပါတယ်။

```text
session file load
    → active leaf နဲ့ branch ရွေး
    → latest Compaction ရှာ
    → summary + retained tail + later messages build
    → runtime state ထဲ snapshot တင်
    → နောက် user message နဲ့ model request အသစ်ခေါ်
```

ဒီအစီအစဉ်မှာ model က နောက်ဆုံးအဆင့်မတိုင်ခင် ပါဝင်စရာမလိုပါဘူး။ Store နဲ့ persistence layer က deterministic reconstruction လုပ်ပေးပြီး Runtime ကရလာတဲ့ messages ကို active state ထဲတင်ပါတယ်။ Lewis က prompt အသစ်ပို့တဲ့အခါမှ summary၊ raw tail၊ Compaction နောက် messages နဲ့ prompt အသစ်ကို model က input အဖြစ်မြင်ပါတယ်။ “Agent ကမှတ်မိတယ်” လို့ပြောနေကျစကားရဲ့နောက်မှာ Runtime က context ပြန်ပေးထားခြင်းပဲ ရှိပါတယ်။

Restore အောင်မြင်မှုကို file ဖွင့်နိုင်တာနဲ့ မတိုင်းသင့်ပါဘူး။ Summary ကအရင်ရောက်သလား၊ anchor မတိုင်ခင် pruned messages ပြန်ပေါ်လာသလား၊ later messages ကျန်သလားနဲ့ active branch မှန်သလား စစ်ရပါတယ်။ Restart မတိုင်ခင်နဲ့ပြီးနောက် provider ဆီပို့မယ့် effective context တူညီတဲ့ boundary ကိုထိန်းနိုင်မှ resume contract ပြည့်ပါတယ်။

## ၁၄.၇ Offline Session-restore Lab

ဒီ reconstruction ကို API key မလိုဘဲစမ်းချင်ရင် [`examples/lewis_session_restore.py`](../../examples/lewis_session_restore.py) ကို repository root ကနေ run နိုင်ပါတယ်။ Lab က `SessionEntry`, `save_entries()`, `load_entries()` နဲ့ `restore_context()` ဆိုတဲ့ သေးငယ်တဲ့ teaching API ကိုသုံးပါတယ်။ ဖြေချင်တဲ့မေးခွန်းက temporary file ထဲ round-trip လုပ်ပြီးနောက် pruned message ပြန်မပေါ်ဘဲ summary၊ retained tail နဲ့ later message ပြန်စီနိုင်သလားဆိုတာပါ။

```bash
python3 examples/lewis_session_restore.py
```

Expected output က:

```text
summary:Goal and evidence retained
message:Fast tool finished first
message:Focused test still fails
```

Code ထဲမှာ `restore_context()` က compaction indexes တွေထဲက နောက်ဆုံးတစ်ခုကိုရွေးပါတယ်။ ပြီးရင် summary ကိုအရင်ထည့်၊ Compaction မတိုင်ခင် entries ထဲမှာ first-kept ID ကိုတွေ့တဲ့နေရာကစပြီး messages ကိုထည့်၊ Compaction နောက် messages ကိုဆက်ထည့်ပါတယ်။ Compaction မရှိတဲ့ test က messages အားလုံး အစီအစဉ်အတိုင်းပြန်ရကြောင်း သီးခြားစစ်ပါတယ်။

Lab ရဲ့အကန့်အသတ်ကို မဖျောက်သင့်ပါဘူး။ ဒီ example က `TemporaryDirectory` အတွင်း temporary JSON file တစ်ခုကိုရေးပြီးဖျက်သွားတဲ့ teaching model သာဖြစ်ပါတယ်။ Travis234 ရဲ့ JSONL session entries၊ parent-linked complete session tree/store နဲ့ runtime integration တစ်ခုလုံးကို အစားမထိုးပါဘူး။ Branch ပြောင်းတဲ့ commands၊ file locking နဲ့ process နှစ်ခုကြား coordination၊ interrupted write အတွက် crash recovery တို့ကို မ implement လုပ်ထားပါဘူး။ ဒါကြောင့် output သုံးကြောင်းမှန်ခြင်းကို production persistence အားလုံးမှန်ကြောင်း သက်သေအဖြစ် မယူရပါဘူး။

## ၁၄.၈ Stored State နဲ့ Runtime State ကွဲနိုင်တဲ့အချိန်

Persistence bug တချို့က restart မှာပဲပေါ်တာမဟုတ်ပါဘူး။ Compaction summary ကို store ထဲ append လုပ်ပြီး in-memory messages ကိုပြန်မတည်ဆောက်ရင် လက်ရှိ process က raw history အဟောင်းနဲ့ဆက်နိုင်ပါတယ်။ နောက် restart ကတော့ store ထဲက compacted context ကိုရမယ်။ တစ် session တည်းမှာတောင် အခုနဲ့နောက်နေ့ context မတူသွားပါပြီ။

ပြောင်းပြန်အမှားလည်း ရှိပါတယ်။ Runtime messages ကို compacted list နဲ့အစားထိုးပေမယ့် Compaction entry ကို durable မရေးခဲ့ရင် လက်ရှိ turn ကမှန်နေပြီး restart အပြီး raw history ပြန်ပေါ်လာနိုင်ပါတယ်။ Store နဲ့ runtime နှစ်ဖက်ရေးပြီးသားဖြစ်ပေမယ့် active leaf မှားရွေးရင်လည်း စွန့်ထားတဲ့ branch ကိုဆက်မိနိုင်ပါတယ်။ ဒါကြောင့် “write succeeded” ထက် “write ပြီး store ကနေ rebuild လုပ်ထားတဲ့ snapshot ကို active state အဖြစ်သုံးတယ်” ဆိုတဲ့ transaction boundary က ပိုအရေးကြီးပါတယ်။

Active Agent run တစ်ခု messages ထည့်နေချိန် manual Compaction က တစ်ပြိုင်နက် store နဲ့ runtime ကိုပြောင်းရင် ဘယ် entry က first-kept ဖြစ်သလဲ မတည်ငြိမ်နိုင်ပါဘူး။ Production design မှာ ownership၊ serialization နဲ့ failure handling ကိုသီးခြားစဉ်းစားရပါတယ်။ ဒီ chapter ရဲ့ offline lab မှာ locking၊ concurrent run coordination နဲ့ crash recovery မရှိတာကြောင့် ဒီပြိုင်ဆိုင်မှုကို စမ်းသပ်တယ်လို့ မဆိုပါဘူး။ Lab က restart reconstruction rule တစ်ခုတည်းကို ထင်ရှားအောင်ထားပါတယ်။

## ၁၄.၉ Lewis ရဲ့မှတ်စု

- Model က session memory ကိုမပိုင်ဘူး။ Runtime က persisted state ကနေ active context ပြန်ပေးတယ်။
- Resume မစခင် active branch ကိုမှန်အောင်ရွေးပြီး latest Compaction ကိုရှာမယ်။
- Restore order က summary → first-kept retained tail → Compaction နောက် later messages ဖြစ်တယ်။
- Store ရေးပြီးတိုင်း အဲဒီ store ကနေ runtime context ပြန်တည်ဆောက်ထားသလား စစ်မယ်။
- Temporary JSON lab ရဲ့ရလဒ်ကို branch၊ locking နဲ့ crash recovery အာမခံချက်အဖြစ် မယူဘူး။

## ၁၄.၁၀ အနှစ်ချုပ်

- In-memory context က လက်ရှိ process သုံးတဲ့ model input state ဖြစ်ပြီး persistent session က restart ကျော်ပြီး reconstruction လုပ်နိုင်တဲ့ durable entries ဖြစ်တယ်။
- Session entries ရဲ့ parent path က active branch ကိုသတ်မှတ်ပြီး store ထဲရှိသမျှ branch ကို model context ထဲမထည့်ရဘူး။
- Compaction entry က summary၊ first-kept anchor၊ tokens-before နဲ့ details ကိုမှတ်ထားနိုင်တယ်။
- Latest Compaction summary၊ anchor ကစတဲ့ retained tail နဲ့ Compaction နောက် messages ကိုအစီအစဉ်တကျ ပေါင်းပြီး active context ပြန်ဆောက်တယ်။
- Persisted Compaction ပြီးတာနဲ့ store ကနေ runtime state ပြန် build လုပ်ခြင်းက လက်ရှိ process နဲ့ restart နှစ်ဖက်ကိုညှိပေးတယ်။
- Offline lab က restore algorithm ကို deterministic ပြပေမယ့် Travis234 ရဲ့ complete session tree/store၊ branch commands၊ locking နဲ့ crash recovery ကို မတုပထားဘူး။

## ၁၄.၁၁ Source Notes

- Executable teaching model: [`examples/lewis_session_restore.py`](../../examples/lewis_session_restore.py)
- Focused executable tests: [`tests/test_lewis_workshop.py`](../../tests/test_lewis_workshop.py) ထဲက `SessionRestoreTests`
- `C-COMPACTION-PERSIST` — `T-COORD`, `T-ADAPTER`; Compaction result ကို summary၊ first-kept entry anchor၊ tokens-before နဲ့ details ပါတဲ့ entry အဖြစ် persist လုပ်ပြီး store ကနေ active context ပြန်တည်ဆောက်တဲ့ boundary
- `C-SESSION-RESTORE` — `T-SESSION-STORE`, `T-SESSION-PERSISTENCE`, `T-ADAPTER`, `tests/test_coding_persistence_and_compaction.py::test_session_store_build_context_recreates_compaction_summary_message`, `tests/test_coding_persistence_and_compaction.py::test_agent_session_manual_compaction_persists_travis234_first_kept_boundary`, `tests/test_compaction_integration.py::test_persisted_compaction_does_not_resurrect_pruned_suffix`; latest summary၊ retained tail နဲ့ later entries က active context ပြန်တည်ဆောက်တဲ့ boundary
- Pi revision: `1f0dbc008c9b3e88017d42e8a1b46d416ad2b6b6`
- Travis234 revision: `68b1831691b8ec93f9550ce63b80cdcb7a591b2e`

Exact source links နဲ့ evidence boundary ကို [Pinned Source Map](../references/SOURCE_MAP.md) မှာ ကြည့်နိုင်ပါတယ်။ Claim ရဲ့ verification scope ကို [Technical Claim Ledger](../references/CLAIM_LEDGER.md) မှာဖတ်နိုင်ပါတယ်။ Lewis ရဲ့ဇာတ်လမ်းနဲ့ dialogue က fictional ဖြစ်ပြီး source-backed production incident သို့မဟုတ် locally rerun test result အဖြစ် မယူရပါဘူး။

---

Previous: [Chapter 13 — Tool က အမှားပြန်လာတဲ့အခါ](13-when-tools-fail.md)
Next: [Chapter 15 — Agent ရဲ့လမ်းကြောင်းကို Trace နဲ့ Debug လုပ်ခြင်း](15-debugging-agent-trajectory.md)

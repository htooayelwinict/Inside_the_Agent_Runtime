# Chapter 16 — ယုံကြည်ရတဲ့ Python Port တစ်ခုဖြစ်လာဖို့

## ၁၆.၁ Demo အောင်တာနဲ့ Port မှန်တာ မတူဘူး

Lewis က သူရေးထားတဲ့ Runtime ကို အလုပ်ဖော်ရှေ့မှာ တစ်ခါ run ပြလိုက်ပါတယ်။ Fake Model က Tool Calls နှစ်ခုထုတ်တယ်၊ fake tools နှစ်ခုလုံးအောင်တယ်၊ နောက်ဆုံးမှာ `Both results are ready.` လို့ပြန်တယ်။ Screen ပေါ်ကစာကြောင်းတွေက သပ်ရပ်ပြီး demo ကလည်းတစ်ကြိမ်တည်းနဲ့ပြီးသွားပါတယ်။

ဒါပေမယ့် အလုပ်ဖော်က ဒီလိုမေးပါတယ်။ “Tool run နေတုန်း abort လုပ်ရင်ရော၊ model ကမရှိတဲ့ Tool ကိုခေါ်ရင်ရော၊ process restart ပြီးရင်ရော၊ အရင်ပြီးတဲ့ Tool နဲ့ model ဆီအရင်ပြန်ဝင်တဲ့ Result order ပြောင်းနေရင်ရော ဘာဖြစ်မလဲ။” Lewis ရဲ့ terminal output တစ်ခုမှာ အဲဒီအဖြေတွေမပါပါဘူး။ Happy path ကိုတစ်ကြိမ်မြင်ရခြင်းက ဖြစ်နိုင်တဲ့လမ်းတစ်လမ်းကိုပြတာသာဖြစ်ပြီး Runtime contract အားလုံးကို မသက်သေပြနိုင်ပါဘူး။

Lewis က မေးခွန်းတစ်ခုချင်းကို input၊ observable event နဲ့ expected outcome အဖြစ်ပြောင်းရေးပါတယ်။ Abort သိပြီးနောက် work အသစ်မစရ၊ unknown Tool ကရှင်းလင်းတဲ့ failure ဖြစ်ရ၊ restart မှာ latest Compaction က context ကို anchor လုပ်ရ၊ completion order နဲ့ Result Order ကိုသီးခြားထိန်းရမယ်။ Caller မြင်နိုင်တဲ့ behavior ကို စမ်းသပ်နိုင်တဲ့စာချုပ်အဖြစ်ရေးထားတာကို `Behavioral Contract` လို့ခေါ်ပါတယ်။

`Lewis နဲ့ အလုပ်ဖော်ရဲ့ demo review ဟာ သင်ခန်းစာအတွက် ဖန်တီးထားတဲ့ fictional incident ပါ။ Lewis က upstream contributor မဟုတ်သလို ဒီဖြစ်ရပ်က Travis234 production incident မဟုတ်ပါဘူး။ အောက်က Runtime claim တွေကတော့ Source Notes မှာပြထားတဲ့ pinned sources၊ manifests နဲ့ focused tests အပေါ်အခြေခံထားပါတယ်။`

## ၁၆.၂ Fake Model က ဘာကြောင့်အသုံးဝင်တာလဲ

Real provider ကို test တစ်ခါခေါ်တိုင်း စာသား၊ Tool Calls နဲ့ timing ကပြောင်းနိုင်ပါတယ်။ Network၊ credential၊ quota နဲ့ model update ကလည်း result ကိုသက်ရောက်နိုင်လို့ failure တစ်ခုက Runtime ကြောင့်လား provider ကြောင့်လား ခွဲရခက်ပါတယ်။ Contract test မှာတော့ တူညီတဲ့ input ကိုတူညီတဲ့ output ပြန်ပေးနိုင်တဲ့ `Fake Model` သုံးခြင်းက မေးခွန်းကိုကျဉ်းပေးပါတယ်။

[`examples/minimal_runtime.py`](../../examples/minimal_runtime.py) ရဲ့ fake model က ပထမခေါ်မှုမှာ `slow`, `fast` Tool Calls နှစ်ခုနဲ့ assistant text ပြန်ပြီး ဒုတိယခေါ်မှုမှာ Tool Call မပါတဲ့ final answer ပြန်ပါတယ်။ [`tests/test_minimal_runtime.py`](../../tests/test_minimal_runtime.py) က Tool completion ကို list တစ်ခုမှာမှတ်ပြီး Runtime ထုတ်တဲ့ events ကို သီးခြားစစ်ပါတယ်။ ဒီ setup မှာ model output သိပြီးသားဖြစ်လို့ test fail ရင် loop ရဲ့ message insertion၊ scheduling သို့မဟုတ် limit boundary ကိုတိုက်ရိုက်စစ်နိုင်ပါတယ်။

Fake Model contract က response fixture တစ်ခုပဲမဟုတ်ပါဘူး။ Call count ကိုမှတ်ရမယ်၊ Runtime ပို့လိုက်တဲ့ messages snapshot ကိုလိုရင်ဖမ်းရမယ်၊ ဘယ် call မှာ Tool Calls ရပ်မလဲကို script လုပ်ရမယ်။ Assertion က final text တစ်ကြောင်းထက် state transition ကိုဦးစားပေးသင့်ပါတယ်။ ဥပမာ ဒုတိယ model call မတိုင်ခင် Tool Results နှစ်ခုလုံး source order နဲ့ messages ထဲရှိသလားဆိုတာ စစ်ရပါတယ်။

ဒီ fake က production model quality၊ streaming transport သို့မဟုတ် provider compatibility ကိုမတိုင်းပါဘူး။ သူ့အကျိုးက မတည်ငြိမ်တဲ့အလွှာကိုခဏပိတ်ပြီး Runtime ပိုင် behavior ကို deterministic ပြန်လုပ်နိုင်ခြင်းပါ။ Fake test pass တာကို live provider acceptance pass တယ်လို့ မချဲ့ရပါဘူး။

## ၁၆.၃ Contract တစ်ခုကို Test တစ်ခုနဲ့ချိတ်ခြင်း

“Agent Loop မှန်ရမယ်” ဆိုတာ test ရေးဖို့ကျယ်လွန်းပါတယ်။ Contract က input၊ observable boundary နဲ့ expected outcome သုံးခုပါမှ အသုံးဝင်ပါတယ်။ ဥပမာ “Tool Calls နှစ်ခုကို parallel ခေါ်ပြီး ဒုတိယတစ်ခုအရင်ပြီးလျှင် model context ထဲ Tool Results က မူလ call order အတိုင်းရှိရမယ်” လို့ရေးလိုက်ရင် fixture နဲ့ assertion ရှင်းလာပါတယ်။

ဒီ repository ရဲ့ workshop artifacts ငါးခုက contract အရွယ်အစားကို ခွဲပြထားပါတယ်။ `minimal_runtime.py` က model → tools → model continuation၊ bounded workers၊ unknown Tool နဲ့ iteration ceiling ကိုပြတယ်။ `lewis_message_control.py` က steering တစ်ခုချင်း drain လုပ်ပုံနဲ့ completed turn နောက် Follow-up ဝင်ပုံကိုပြတယ်။ `lewis_tool_outcomes.py` က immediate နဲ့ invoked outcomes၊ `lewis_session_restore.py` က latest summary နဲ့ retained tail၊ `lewis_trace_reader.py` က event kinds နဲ့ stable index order ကိုသီးခြားပြတယ်။

သူတို့ရဲ့ executable assertions ကို [`tests/test_minimal_runtime.py`](../../tests/test_minimal_runtime.py) နဲ့ [`tests/test_lewis_workshop.py`](../../tests/test_lewis_workshop.py) မှာထားပါတယ်။ Workshop တစ်ခုလုံးကို repository root ကနေ ဒီ command နဲ့ run နိုင်ပါတယ်။

```bash
python3.13 -m unittest tests.test_minimal_runtime tests.test_lewis_workshop -v
python3.13 scripts/check_book.py
```

ပထမ command က local offline teaching tests ကို run ပြီး ဒုတိယ command က manuscript structure နဲ့ links လို book rules ကိုစစ်ပါတယ်။ နှစ်ခုလုံးအောင်ရင် artifacts ငါးခုရဲ့ သတ်မှတ်ထားတဲ့ assertions နဲ့ စာအုပ် checks အောင်တယ်လို့ပဲ ပြောနိုင်ပါတယ်။ ဒီ local book tests က full Travis234 suite ကိုမခေါ်သလို Pi/Hermes parity အားလုံးကိုလည်း မသက်သေပြပါဘူး။

## ၁၆.၄ Event Order နဲ့ Result Order ကို စစ်ခြင်း

Parallel Tool Calls နှစ်ခုရှိတဲ့အခါ “order မှန်သလား” ဆိုတာ list တစ်ခုတည်းနဲ့မဖြေနိုင်ပါဘူး။ Tool body တကယ်ပြီးတဲ့ `Completion Order` နဲ့ model context ထဲ Tool Result messages ပြန်ထည့်တဲ့ `Result Order` ဟာ observer မတူတဲ့ contract နှစ်ခုဖြစ်ပါတယ်။ မြန်တဲ့ Tool ကနောက်မှခေါ်ထားပေမယ့် အရင်ပြီးနိုင်ပြီး Result messages ကတော့ မူလ calls အတိုင်းပြန်ဝင်နိုင်ပါတယ်။

Minimal Runtime test မှာ `fast` ကအရင်ပြီးကြောင်း `completion_order == ["fast", "slow"]` နဲ့စစ်ပါတယ်။ တစ်ချိန်တည်းမှာ Runtime ရဲ့ `tool_end` details က `slow`, `fast` အတိုင်းဖြစ်ကြောင်း သီးခြား assertion လုပ်ပါတယ်။ ဒီ lab ရဲ့ `tool_end` က production completion event မဟုတ်ဘဲ source-ordered result insertion ကိုဖော်ပြတဲ့ teaching event ဖြစ်ကြောင်း မရောသင့်ပါဘူး။

Trace reader မှာတော့ event semantics ကိုပိုထင်ရှားအောင် `tool_execution_end` နဲ့ `tool_result` kinds ခွဲထားပါတယ်။ Input tuple ကိုအလွဲအစီအစဉ်နဲ့ပေးထားလည်း `analyze_trace()` က `index` အလိုက်စီပြီး completion `("fast", "slow")` နဲ့ result `("slow", "fast")` ကိုထုတ်ရပါတယ်။ ဒီ assertion က order inversion ကိုဖျောက်မထားဘဲ observer နှစ်မျိုးရဲ့ chronology ကိုသီးခြားသက်သေပြပါတယ်။ Result content မှန်ခြင်းနဲ့ model အဖြေမှန်ခြင်းကိုတော့ ဒီ order test တစ်ခုက မသက်သေပြပါဘူး။

## ၁၆.၅ Failure Injection ကို လုံခြုံစွာလုပ်ခြင်း

Failure path ကိုစမ်းဖို့ real file ဖျက်ခြင်း၊ network ဖြုတ်ခြင်း သို့မဟုတ် production credential ပျက်အောင်လုပ်ခြင်း မလိုပါဘူး။ `Failure Injection` ဆိုတာ test ပိုင် fake dependency က သတ်မှတ်ထားတဲ့ boundary မှာ error ပြန်အောင်လုပ်ပြီး Runtime response ကိုစစ်ခြင်းပါ။ Side effect မရှိတဲ့ fixture သုံးလို့ test ကပြန် run ရလွယ်ပြီး user workspace ကိုမထိပါဘူး။

Tool-outcome lab မှာ catalog ထဲမရှိတဲ့ name ပေးလို့ `unknown_tool` ရနိုင်တယ်။ Valid Tool ကို `before_allowed=False` နဲ့ပေးလို့ body မစဘဲ `blocked` ရနိုင်တယ်။ Body ထဲက `RuntimeError("disk unavailable")` တက်အောင် fake function ရေးလို့ invoked failure ကိုစမ်းနိုင်တယ်။ Immediate paths မှာ after-hook count သုညဖြစ်ပြီး invoked failure မှာတစ်ကြိမ်ဖြစ်ရမယ်။ ဒီလို counter နဲ့စစ်ခြင်းက error string တစ်ခုတည်းထက် lifecycle ကိုပိုတိကျစေပါတယ်။

Iteration ceiling ကိုစမ်းရာမှာ fake model က Tool Call တစ်ခုကိုအမြဲပြန်အောင်လုပ်ပြီး `max_iterations=2` နောက် exact `RuntimeError` ရကြောင်းစစ်နိုင်ပါတယ်။ Abort contract အတွက်လည်း real process ကိုမတည်ငြိမ်အောင်မလုပ်ဘဲ controllable signal ကို Tool boundary တစ်ခုမှာပြောင်းပြီး နောက် model/tool work အသစ်မစကြောင်း call counters နဲ့စစ်သင့်ပါတယ်။ လက်ရှိ workshop ရဲ့ message-control lab က queue drain order ကိုသာပုံဖော်ပြီး production cancellation၊ RunLease ownership သို့မဟုတ် OS signal delivery ကို implement မလုပ်ထားပါဘူး။ Safe fixture ဟာ မိမိစစ်တဲ့ boundary ကိုကျဉ်းကျဉ်းရှင်းရှင်း label တပ်ရပါတယ်။

## ၁၆.၆ Parity Manifest ကို ဖတ်ခြင်း

Focused test အမည်တွေများလာရင် ဘယ် behavior ကိုဘယ် evidence ကထောက်ထားသလဲ ပျောက်လွယ်ပါတယ်။ `Parity Manifest` ဆိုတာ contract တစ်ခုချင်းကို stable ID၊ source၊ category၊ evidence reference နဲ့ status တို့ဖြင့် စာရင်းပြုထားတဲ့ machine-readable mapping ပါ။ Pinned `T-PARITY` မှာ Pi နဲ့ Hermes entries ကိုဒီပုံစံနဲ့တည်ဆောက်ထားပါတယ်။

Entry တစ်ကြောင်းဖတ်တဲ့အခါ evidence က `test_file.py::test_name` ပုံစံမှန်သလား၊ status က `parity` သို့မဟုတ် `divergence` လား၊ divergence ဆို reason နဲ့ safety evidence ရှိသလားကိုတွဲဖတ်ရပါတယ်။ Pinned revision မှာ Pi contracts ၇၈ ခုနဲ့ Hermes Compaction contracts ၁၁ ခုရှိတာဟာ manifest ထဲစာရင်းသွင်းထားတဲ့ contracts အရေအတွက်သာဖြစ်ပြီး project feature အားလုံးရဲ့ ရာခိုင်နှုန်းမဟုတ်ပါဘူး။

Pinned `T-VERIFY` ရဲ့ `python3 scripts/verify_acceptance.py --parity-json` ဟာ acceptance matrix schema ကိုဖတ်ပြီး parity report တည်ဆောက်ကာ manifest contract IDs/statuses၊ divergence fields နဲ့ evidence references ရဲ့ file/test-name resolution ကို validate လုပ်ပါတယ်။ `--parity-json` က manifest/schema/evidence references ကို validate လုပ်ပေမယ့် full Travis234 suite ကို ပြန်မ run ပါဘူး။ Test function ရှိကြောင်း resolve ဖြစ်တာနဲ့ အဲဒီ test ကိုလက်ရှိ environment မှာ execute လုပ်ပြီး pass ကြောင်းဟာ evidence မတူပါဘူး။ ဒီစာအုပ် repo ရဲ့ local workshop commands အောင်ခြင်းကလည်း full parity သက်သေမဟုတ်ပါဘူး။

## ၁၆.၇ Intentional Divergence ကို မှတ်တမ်းတင်ခြင်း

Target language နဲ့ safety policy ကြောင့် upstream ကိုတိတိကျကျမတုပသင့်တဲ့အချိန်ရှိပါတယ်။ ဒီကွာခြားချက်ကို တိတ်တဆိတ်ထားလိုက်ရင် reviewer ကမပြီးသေးတဲ့ port လား၊ ရည်ရွယ်ထားတဲ့ design လား မခွဲနိုင်ပါဘူး။ `Intentional Divergence` ဆိုတာ ကွာနေတဲ့ observable behavior ကို explicit status နဲ့ထားပြီး ဘာကြောင့်ရွေးသလဲဆိုတဲ့ reason နဲ့ ဘယ် test ကဘေးကင်းကြောင်းကာကွယ်သလဲဆိုတဲ့ safety evidence ကိုတွဲရေးခြင်းပါ။

Pinned Pi manifest မှာ bounded parallelism၊ trust မဆုံးဖြတ်ရသေးတဲ့ project package mutation၊ non-interactive unknown-project policy နဲ့ Pythonic async `AgentHarness` ဆိုတဲ့ divergence လေးခုရှိပါတယ်။ ဥပမာ bounded worker pool က unbounded host concurrency နဲ့မတူပေမယ့် resource exhaustion လျှော့ဖို့ရွေးထားပြီး worker limit နဲ့ coordinator-thread behavior ကို test ကစစ်ထားပါတယ်။ “Python ကမတူလို့” ဆိုတဲ့ reason အကျယ်ကြီးထက် ဘာပြောင်းသလဲ၊ ဘာကိုကာကွယ်သလဲနဲ့ failure ဖြစ်ရင်ဘာမြင်ရမလဲဆိုတာရေးရပါတယ်။

Divergence row တစ်ကြောင်းမှာ contract ID၊ upstream expectation၊ local behavior၊ reason၊ safety evidence နဲ့ revision ပါစေ။ Safety evidence က test path အမည်ရှိရုံမက ရွေးထားတဲ့ risk boundary ကိုတကယ် assert လုပ်သင့်ပါတယ်။ နောက်ပိုင်း behavior ကို parity ပြန်လုပ်လိုက်ရင် row ကိုဖျက်ရုံမဟုတ်ဘဲ old safety assumption မလိုတော့ကြောင်း test နဲ့ docs ကိုပါပြန်စစ်ရပါတယ်။

## ၁၆.၈ Lewis ရဲ့ Runtime Milestones

Runtime ကိုတစ်ခါတည်း “complete” လို့ခေါ်မယ့်အစား Lewis က observable milestone အလိုက်တိုးပါတယ်။ ပထမ milestone မှာ fake model က final answer အထိနှစ်ကြိမ်ခေါ်နိုင်ပြီး Tool Results ကို call IDs နဲ့ပြန်ချိတ်နိုင်ရမယ်။ ဒုတိယမှာ bounded parallel execution၊ source-ordered results၊ unknown Tool နဲ့ iteration ceiling ကို deterministic tests နဲ့ပိတ်ရမယ်။

တတိယ milestone မှာ steering၊ Follow-up နဲ့ cooperative abort ကို boundary တစ်ခုချင်း call counts နဲ့စစ်မယ်။ စတုတ္ထမှာ immediate/invoked Tool outcomes၊ hook counts နဲ့ error Result protocol ကိုဖုံးမယ်။ ပဉ္စမမှာ temporary persisted fixture ကနေ latest Compaction summary၊ retained tail နဲ့ later messages ပြန်တည်ဆောက်မယ်။ ဆဋ္ဌမမှာ trace index၊ completion/result orders နဲ့ first failure ကိုဖတ်နိုင်မယ်။

နောက်ဆုံး milestone က test count မဟုတ်ပါဘူး။ Contract တစ်ခုစီမှာ pinned source သို့မဟုတ် explicit local design၊ focused executable evidence၊ known limitation နဲ့ divergence ဖြစ်ရင် reason/safety evidence ရှိရပါတယ်။ Offline contracts အောင်ပြီးမှ integration၊ live provider နဲ့ full-suite evidence ကို သီးခြားအလွှာအဖြစ်ထည့်ရမယ်။ အလွှာတစ်ခုရဲ့ pass result ကိုနောက်အလွှာဆီ မချဲ့ခြင်းက ယုံကြည်ရတဲ့ roadmap ရဲ့အစိတ်အပိုင်းပါ။

## ၁၆.၉ Reader Final Exercises

အောက်က exercise ငါးခုကို workshop artifacts ပေါ်မှာပဲလုပ်နိုင်ပါတယ်။ တစ်ခုစီမှာ code ပြောင်းခြင်းထက် observable outcome ကိုအရင်ရေးပြီး test နဲ့သက်သေပြပါ။

1. `PendingMessages` ထဲ steering messages နှစ်ခု queue လုပ်ပါ။ `drain_one()` ပထမခေါ်မှုမှာ `("first",)`၊ ဒုတိယမှာ `("second",)` နဲ့ တတိယမှာ `()` ရကြောင်း assert လုပ်ပြီး one-at-a-time FIFO drain order ကိုသက်သေပြပါ။
2. Valid fake Tool Call တစ်ခုကို `before_allowed=False` နဲ့ blocked ဖြစ်အောင်ထည့်ပါ။ Outcome က `("immediate", "blocked")` ဖြစ်ပြီး Tool body call count နဲ့ after-hook count နှစ်ခုလုံး သုညဖြစ်ကြောင်းပြပါ။
3. Compaction နှစ်ခုပြီးသား session fixture ကို တတိယ Compaction entry နဲ့ဆက်ချဲ့ပါ။ Retained-tail boundary ကို message အသစ်တစ်ခုဆီရွှေ့ပြီး restore output ထဲ နောက်ဆုံး summary၊ အဲဒီ retained tail နဲ့ later messages ပဲကျန်ကြောင်း assert လုပ်ပါ။
4. `TraceEvent` input ကို index order မဟုတ်အောင် shuffle လုပ်ပါ။ Report ထဲ completion/result lists နဲ့ first failure တို့က input tuple နေရာမဟုတ်ဘဲ `index` chronology အတိုင်းပြန်ရကြောင်း assert လုပ်ပါ။
5. Intentional divergence row တစ်ကြောင်းရေးပါ။ Local behavior က upstream expectation နဲ့ဘယ်လိုကွာသလဲဆိုတဲ့ reason၊ risk ကိုတိုက်ရိုက်စစ်တဲ့ safety-evidence test reference နဲ့ pinned revision ပါမှ review checklist အောင်ကြောင်းပြပါ။

Exercise ပြီးတိုင်း focused test name ကို contract စာကြောင်းနဲ့ဘေးချင်းထားပါ။ “run လို့ရတယ်” ဆိုတဲ့ observation ထက် queue ထဲဘာကျန်သလဲ၊ hook ဘယ်နှကြိမ်ဝင်သလဲ၊ ဘယ် summary တစ်ခုသာကျန်သလဲလို observable state ကို output အဖြစ်ထားပါ။

## ၁၆.၁၀ Lewis ရဲ့မှတ်စု

- Demo က ဖြစ်နိုင်တဲ့လမ်းတစ်ခုကိုပြတယ်။ Contract test က သတ်မှတ်ထားတဲ့ input မှာ မဖြစ်မနေထိန်းရမယ့် boundary ကိုပြတယ်။
- Fake Model နဲ့ fake Tool ကို deterministic ထားပြီး final prose ထက် messages၊ events၊ order နဲ့ call counts ကိုစစ်မယ်။
- Failure injection ကို temporary သို့မဟုတ် side-effect-free fixture ထဲမှာလုပ်ပြီး real workspace၊ network နဲ့ credential ကိုမထိဘူး။
- Manifest reference resolve ဖြစ်ခြင်း၊ focused test execute အောင်ခြင်းနဲ့ full suite အောင်ခြင်းကို evidence အလွှာသုံးမျိုးအဖြစ်ခွဲရေးမယ်။
- Divergence တိုင်းမှာ reason နဲ့ risk ကိုတိုက်ရိုက်ကာကွယ်တဲ့ safety evidence ထည့်မယ်။

## ၁၆.၁၁ အနှစ်ချုပ်

- Happy-path demo တစ်ကြိမ်က abort၊ unknown Tool၊ restart နဲ့ order inversion ကိုမသက်သေပြနိုင်ပါဘူး။
- Fake Model က scripted responses နဲ့ captured state သုံးပြီး Runtime behavior ကို network မပါဘဲ deterministic စစ်နိုင်စေတယ်။
- Contract တစ်ခုကို input၊ observable boundary၊ expected outcome နဲ့ focused test တစ်ခုဆီချိတ်ရတယ်။
- Completion Order နဲ့ Result Order က observer မတူတဲ့ contracts ဖြစ်လို့ event kind နှစ်မျိုးနဲ့သီးခြားစစ်ရတယ်။
- Safe failure injection က fake dependency၊ call counter နဲ့ temporary state ကိုသုံးပြီး immediate/invoked boundary ကိုပြတယ်။
- Parity manifest က contract နဲ့ evidence ကို map လုပ်ပေမယ့် verifier က referenced tests ကို full suite အဖြစ်မ run ပါဘူး။
- Intentional divergence တစ်ခုမှာ explicit local behavior၊ reason၊ safety evidence နဲ့ revision လိုတယ်။
- Runtime milestones ကို offline unit contracts ကနေ persistence၊ trace၊ integration နဲ့ live evidence ဆီ အလွှာလိုက်တိုးရတယ်။

## ၁၆.၁၂ Source Notes

- Executable teaching artifacts: [`examples/minimal_runtime.py`](../../examples/minimal_runtime.py), [`examples/lewis_message_control.py`](../../examples/lewis_message_control.py), [`examples/lewis_tool_outcomes.py`](../../examples/lewis_tool_outcomes.py), [`examples/lewis_session_restore.py`](../../examples/lewis_session_restore.py), [`examples/lewis_trace_reader.py`](../../examples/lewis_trace_reader.py)
- Local executable tests: [`tests/test_minimal_runtime.py`](../../tests/test_minimal_runtime.py) နဲ့ [`tests/test_lewis_workshop.py`](../../tests/test_lewis_workshop.py); ဒီ tests အောင်ခြင်းက teaching artifacts ငါးခုရဲ့ local contracts ကိုသာသက်သေပြပြီး full Travis234 parity ကိုမသက်သေပြပါဘူး။
- `C-CONTRACT-TESTS` — `T-PARITY`, `T-VERIFY`, `tests/test_pi_behavioral_parity.py::test_pi_manifest_is_complete_and_all_evidence_resolves`, `tests/test_hermes_compaction_parity.py::test_hermes_manifest_is_complete_and_all_evidence_resolves`, `tests/architecture/test_acceptance_matrix.py::test_parity_report_has_only_resolved_evidence`; fake-model contract tests နဲ့ manifest validation boundary
- `C-PARITY` — `T-PARITY`, `T-VERIFY`; pinned manifest ရဲ့ Pi ၇၈ ခုအနက် ၇၄ parity/၄ divergence နဲ့ Hermes ၁၁ parity count၊ verifier pass က full suite rerun မဟုတ်တဲ့ boundary
- `C-DIVERGENCES` — `T-PARITY`; bounded parallelism၊ unresolved-trust project package mutation၊ non-interactive unknown-project policy နဲ့ Pythonic async `AgentHarness` အတွက် explicit reason/safety-evidence boundary
- `T-PARITY` — pinned Pi/Hermes `ContractEntry` manifest၊ schema version 1 report၊ evidence resolution နဲ့ divergence metadata
- `T-VERIFY` — acceptance matrix ဖတ်ခြင်းနဲ့ parity JSON report validation entry point; `--parity-json` က manifest/schema/evidence references ကို validate လုပ်ပြီး full Travis234 suite ကိုမ run ပါဘူး။
- Agentic AI Book revision: `7eed5ca1c4b21ab766dda2df4e039ab745cdc30f`
- Travis234 revision: `68b1831691b8ec93f9550ce63b80cdcb7a591b2e`
- Pi revision: `1f0dbc008c9b3e88017d42e8a1b46d416ad2b6b6`
- Hermes Agent revision: `af250d84948179834820a62bfd870c0df6f264a1`

Exact source links နဲ့ evidence boundary ကို [Pinned Source Map](../references/SOURCE_MAP.md) မှာ ကြည့်နိုင်ပါတယ်။ Claim ရဲ့ verification scope ကို [Technical Claim Ledger](../references/CLAIM_LEDGER.md) မှာဖတ်နိုင်ပါတယ်။ Lewis ရဲ့ incident နဲ့ dialogue က fictional ဖြစ်ပြီး source-backed production incident သို့မဟုတ် locally rerun upstream full-suite result အဖြစ် မယူရပါဘူး။

---

Previous: [Chapter 15 — Agent ရဲ့လမ်းကြောင်းကို Trace နဲ့ Debug လုပ်ခြင်း](15-debugging-agent-trajectory.md)

Next: [Appendix A — Installation](appendices/a-installation.md)

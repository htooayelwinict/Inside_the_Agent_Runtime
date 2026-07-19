# Chapter 03 — Agent Runtime Loop ကို အစအဆုံးဖတ်ခြင်း

## ၃.၁ Request တစ်ခုက Run တစ်ခုဖြစ်လာတဲ့အချိန်

ညနေခင်းတစ်ခုမှာ Lewis ဆီ focused test တစ်ခုရဲ့ output ရောက်လာတယ်။ Test က အဆုံးနားရောက်မှ fail ဖြစ်တာမဟုတ်ဘဲ event တစ်ခုကို မှားတဲ့ context နဲ့စစ်မိသလို ဖြစ်နေတယ်။ Log ကိုအပေါ်အောက်ကြည့်ရုံနဲ့ ဘယ်နေရာကစလွဲသွားလဲ မမြင်ရသေးဘူး။

“Fail စတဲ့နေရာကို ရှာပေး။ ပြင်တာတော့ မလုပ်သေးနဲ့” လို့ Lewis က Agent ကိုပြောလိုက်တယ်။

Agent က ချက်ချင်းအဖြေမပေးဘဲ `read_file` Tool Call တစ်ခုထုတ်တယ်။ File ကိုဖတ်ပြီး Tool Result ပြန်ရောက်လာမှ “စလွဲတာက assertion မဟုတ်ဘူး၊ ဒုတိယ model request မတိုင်ခင် result message မပါသွားတဲ့ boundary ပါ” လို့ရှင်းပြတယ်။ Lewis မြင်လိုက်ရတာက request တစ်ကြောင်းနဲ့ answer တစ်ခုပဲ။ Runtime အတွင်းမှာတော့ model ကို နှစ်ကြိမ်ခေါ်ခဲ့ပြီး၊ အဲဒီနှစ်ကြိမ်ကြားမှာ Tool Result တစ်ခုက context ထဲဝင်ခဲ့တယ်။


`Lewis နဲ့ ဒီဖြစ်ရပ်ဟာ control flow ကိုလေ့လာဖို့ ဖန်တီးထားတဲ့ fictional scenario ပါ။ Travis234 ရဲ့ production incident သို့မဟုတ် contributor history မဟုတ်ပါဘူး။`

Source ကသက်သေပြတဲ့အပိုင်းဟာ request၊ message၊ event နဲ့ Tool Result တွေ ရွေ့သွားတဲ့ boundary တွေဖြစ်တယ်။


ဒီ flow ကို အရင် ကြည့်မယ်။

```text
Lewis
  → Agent owner
  → loop config
  → shared Runtime Loop
  → first model request
  → read_file Tool Call
  → Tool Result message
  → second model request
  → final assistant message
```

Request တစ်ခုက model ဆီတန်းမသွားပါဘူး။ Agent owner က လက်ခံပြီး Run တစ်ခုဖွင့်၊ လိုအပ်တဲ့ context နဲ့ control callbacks တွေကိုစုစည်းပြီးမှ Runtime Loop ဆီလွှဲပေးတာပါ။ အခုကစပြီး အဲဒီမြှားတစ်ချောင်းချင်းကို အချိန်အစီအစဉ်အတိုင်း ဖြည်ကြည့်မယ်။

## ၃.၂ Agent Owner က ဘာကိုပိုင်သလဲ

Model နဲ့ Tool ကိုခေါ်နိုင်ရုံဆို owner မလိုသလိုထင်ရပါတယ်။ ဒါပေမယ့် active Run၊ control queues နဲ့ model configuration ကို တစ်နေရာကတာဝန်ယူရတယ်။ အဲဒီ `Agent owner` က public prompt/control surface၊ queues၊ configuration နဲ့ Run coordination ကိုပိုင်ပါတယ်။

အောက်က term ငါးခုကို မခွဲနိုင်ရင် trace ဖတ်တဲ့အခါ event တစ်ခုနဲ့ state တစ်ခုကို ရောမိလွယ်ပါတယ်။

| Term | ဒီအခန်းမှာယူမယ့်အဓိပ္ပာယ် |
|---|---|
| Agent owner | Queue၊ configuration၊ active Run coordination နဲ့ user-facing control surface ကိုပိုင်တဲ့ object |
| Run | `agent_start` ကနေ `agent_end` အထိ ဆက်လက်အသက်ဝင်နေတဲ့ processing lifetime |
| Turn | Assistant response တစ်ခု၊ သူတောင်းထားတဲ့ Tool Calls နဲ့ ပြန်ရလာတဲ့ Tool Results ပါဝင်တဲ့ boundary |
| Message | နောက် model request ကမြင်နိုင်အောင် context ထဲသိမ်းထားတဲ့ user၊ assistant သို့မဟုတ် tool entry |
| Tool invocation | Assistant က တောင်းထားတဲ့ external work တစ်ကြိမ်; tool body ပြီးခြင်းနဲ့ result context ထဲဝင်ခြင်း မတူသေး |

`Run` ဆိုတာ request တစ်ကြောင်းနဲ့ အမြဲတမ်းတစ်ကြိမ်တည်း model ခေါ်ခြင်းမဟုတ်ပါဘူး။ Run တစ်ခုထဲ Turn အများကြီးပါနိုင်တယ်။ Lewis ရဲ့ဖြစ်ရပ်မှာ ပထမ Turn က `read_file` ကိုတောင်းပြီး Tool Result နဲ့ပြီးတယ်။ ဒုတိယ Turn က updated context ကိုဖတ်ပြီး နောက်ဆုံးရှင်းလင်းချက်ပေးတယ်။

Owner က model streaming နဲ့ Tool execution ကို Runtime Loop ဆီလွှဲပေမယ့် queue drain နဲ့ Run lifetime ကို ဆက်ချိတ်ထားတယ်။ ဒါကြောင့် Loop ထဲက local variable နဲ့ Agent တစ်ခုလုံးရဲ့ state ကို မရောသင့်ပါဘူး။

## ၃.၃ Initial Messages နဲ့ Run စတင်ခြင်း

Request ကိုလက်ခံပြီးနောက် Runtime က model ကိုချက်ချင်းမခေါ်သေးပါဘူး။ Lewis ရဲ့ prompt ကို အရင် `new_messages` ထဲထည့်ပြီး၊ လက်ရှိ conversation ရှိပြီးသားဆို အဲဒီ history နောက်မှာ prompt ကိုပေါင်းကာ `current_context` အသစ်တည်ဆောက်တယ်။ `new_messages` က ဒီ Run အတွင်းအသစ်ဖြစ်လာတဲ့ entry တွေကိုပြန်ပေးဖို့ဖြစ်ပြီး `current_context.messages` က နောက် model request မြင်ရမယ့် history ကိုကိုင်တယ်။ နှစ်ခုက အချို့ Message တူပေမယ့် ရည်ရွယ်ချက်မတူပါဘူး။

State ပြင်ပြီးမှ lifecycle event တွေစတယ်။ ပုံမှန် entry မှာ `agent_start`၊ ပထမ `turn_start` ထုတ်ပြီး Lewis ရဲ့ prompt တစ်ခုစီအတွက် `message_start` နဲ့ `message_end` ထုတ်တယ်။ Event subscriber က ဒီအစီအစဉ်ကြောင့် “Run စပြီ”၊ “Turn စပြီ” နဲ့ “user message အပြည့်အစုံရပြီ” ကို ခွဲသိနိုင်ပါတယ်။

```text
new_messages     = [Lewis request]
current_context  = [older history..., Lewis request]

agent_start
turn_start
message_start(user)
message_end(user)
```

Entry function က state ကိုတည်ဆောက်ပြီးသားဖြစ်ပြီး event တွေက lifecycle ကို listener ဆီဖော်ပြတာပါ။ Event နဲ့ durable Message ကိုတစ်ခုတည်းလို့ယူဆရင် restore နဲ့ trace ဖတ်ရာမှာ မှားနိုင်ပါတယ်။

Run စချိန် steering queue ကိုတစ်ကြိမ်စစ်တယ်။ ဒီ scenario မှာ queue အလွတ်ဖြစ်လို့ Lewis ရဲ့ request တစ်ခုတည်းနဲ့ ပထမ model boundary ဆီဆက်သွားမယ်။

## ၃.၄ ပထမ Model Boundary

Model ကိုခေါ်မယ့်အချိန်ရောက်ရင် Runtime က conversation state ကို provider နားလည်မယ့်ပုံစံအဖြစ် ပြင်ဆင်ရပါတယ်။ Context transform ရှိရင် အရင်လုပ်တယ်။ ပြီးမှ Agent Message တွေကို LLM-compatible Message တွေအဖြစ်ပြောင်းပြီး system prompt၊ messages နဲ့ available tools ပါတဲ့ request context ကိုတည်ဆောက်တယ်။ ဒီအချိန်က `model boundary`—Runtime ပိုင်တဲ့ state က provider request တစ်ခုဖြစ်သွားတဲ့မျဉ်းပါ။

Lewis scenario ရဲ့ ပထမ snapshot က ရိုးရှင်းတယ်။

```text
Before model request 1:
  [user request]
```

Model က failure အစကိုမပြောနိုင်သေးဘူး။ ဘာလို့လဲဆိုတော့ စစ်ရမယ့် file အကြောင်းအရာ context ထဲမရှိသေးလို့ပါ။ ဒါကြောင့် assistant message ရဲ့ content ထဲမှာ text answer အစား `read_file` Tool Call တစ်ခုထုတ်တယ်။

```text
assistant content:
  Tool Call: read_file({"path": "tests/fixtures/focused-trace.txt"})
```

ဒီ path က fictional scenario အတွက်ပါ။ ပထမ request စပြီးသွားရင် သူ့ input ကိုနောက်ကနေပြန်ပြင်လို့မရသလို File result ကလည်း အဲဒီ request ထဲပြန်မဝင်ပါဘူး။ Runtime က assistant Tool Call ကို completed Message အဖြစ်အရင်တည်ဆောက်ရတယ်။

## ၃.၅ Assistant Stream ကို Message တစ်ခုဖြစ်အောင်တည်ဆောက်ခြင်း

Provider က assistant answer ကို တစ်ခါတည်း final object အဖြစ်ပေးနိုင်သလို partial event တွေအဖြစ် တဖြည်းဖြည်းပေးနိုင်တယ်။ Runtime အတွက် streaming ဆိုတာ screen ပေါ်စာလုံးပေါ်လာခြင်းထက်ပိုတယ်။ မပြီးသေးတဲ့ assistant state ကို context ရဲ့နောက်ဆုံး Message အဖြစ်ထည့်၊ delta အသစ်ရတိုင်း snapshot ကိုအစားထိုးပြီး၊ နောက်ဆုံးမှာ completed assistant Message တစ်ခုဖြစ်အောင် ပိတ်ပေးရတာပါ။

Provider က explicit `start` ပေးရင် Runtime က partial assistant Message ကို context ထဲထည့်ပြီး `message_start` ထုတ်တယ်။ Text၊ thinking သို့မဟုတ် Tool Call delta ရလာတိုင်း partial snapshot ပြောင်းကာ `message_update` ထုတ်တယ်။ `done` သို့မဟုတ် `error` ရောက်မှ final Message နဲ့အစားထိုးပြီး `message_end` ထုတ်တယ်။

```text
provider start
  → message_start(assistant partial)
provider toolcall deltas
  → message_update(...)
provider done
  → message_end(assistant with read_file Tool Call)
```

Provider adapter က explicit partial `start` မပေးဘဲ final result ပဲပြန်ရင် Runtime က `message_start` ကိုဖြည့်ပြီးမှ `message_end` ထုတ်တယ်။ ဒါကြောင့် listener က start/end boundary ကို ဆက်ယုံကြည်နိုင်ပါတယ်။

Lewis ရဲ့ ပထမ assistant Message ဟာ Tool Call delta တွေပြီးမှ complete ဖြစ်တယ်။ Arguments တစ်ဝက်တစ်ပျက်ရှိနေချိန်မှာ Tool ကိုစလိုက်ရင် path မှားနိုင်တယ်။ ဒါကြောင့် streaming state ကိုမြင်ရုံနဲ့ executable request လို့မယူဘဲ `message_end` ရောက်ပြီး final content ရမှ Tool lifecycle ဆီကူးရပါတယ်။

## ၃.၆ Tool Call ကို Prepare → Execute → Finalize လုပ်ခြင်း

Completed assistant Message ထဲ `read_file` ပါလာတိုင်း Tool body ကိုတန်းမခေါ်ပါဘူး။ Runtime က Tool lifecycle ကို အဆင့်သုံးဆင့်ခွဲထားတယ်။

```text
Prepare
  resolve tool → prepare/validate arguments → before boundary

Execute
  invoke read_file → receive Tool outcome

Finalize
  apply after boundary → normalize outcome → build Tool Result message
```

`Prepare` က Tool name နဲ့ registration ကိုက်မကိုက်ရှာတယ်၊ arguments ကိုပြင်ဆင်ပြီး schema နဲ့စစ်တယ်၊ execution မတိုင်ခင် policy/hook ရှိရင် ဖြတ်သန်းတယ်။ ဒီအဆင့်မှာ မအောင်ရင် external Tool body ကိုမခေါ်ဘဲ immediate error outcome တည်ဆောက်နိုင်တယ်။ Lewis ရဲ့ `read_file` က name နဲ့ arguments မှန်လို့ prepared state ရတယ်။

`Execute` က invocation ID၊ validated arguments နဲ့ cooperative signal ကိုပေးပြီး external work တကယ်လုပ်တဲ့အပိုင်းပါ။ Lewis ရဲ့ဖြစ်ရပ်မှာ file result တစ်ခါတည်းပြန်တယ်။

`Finalize` က invocation outcome ကို Tool Result အဖြစ်ပြောင်းပြီး တကယ် invoke လုပ်ထားမှ after boundary ကိုအသုံးချတယ်။ Sequential/parallel execution နဲ့ bounded concurrency ကို [Chapter 05](05-tool-execution-bounded-concurrency.md) မှာ၊ failure နဲ့ hook boundary ကို [Chapter 13](13-when-tools-fail.md) မှာ ဆက်ဖတ်နိုင်တယ်။

Tool body ပြီးသွားတာဟာ external work ပြီးသွားတာသာဖြစ်တယ်။ Model က သိသွားပြီလို့မဆိုနိုင်သေးပါဘူး။ အဲဒီကွာဟချက်ကို Tool Result Message ကဆက်ဖြည့်ပေးမယ်။

## ၃.၇ Tool Result က Context ထဲပြန်ဝင်လာခြင်း

`read_file` ပြီးချိန်မှာ ပထမ model request ကလည်းပြီးနေပြီ။ Runtime က outcome ကို assistant Tool Call နဲ့ချိတ်ထားတဲ့ `Tool Result` Message အဖြစ်တည်ဆောက်ရတယ်။

ဥပမာ fictional file ထဲမှာ ဒီလိုရှိတယ်ဆိုပါစို့။

```text
expected context before request 2:
  user request, assistant Tool Call, Tool Result

observed context before request 2:
  user request, assistant Tool Call
```

Runtime က `tool_execution_end` ထုတ်ပြီးနောက် Tool Result အတွက် `message_start` နဲ့ `message_end` boundary ထုတ်တယ်။ ပြီးရင် result Message ကို `current_context.messages` နဲ့ ဒီ Run ရဲ့ `new_messages` ထဲထည့်တယ်။ Event emission နဲ့ state insertion ဟာ ဆက်တိုက်ဖြစ်ပေမယ့် ရည်ရွယ်ချက်ကွာတယ်—event က observer ကိုပြောတာ၊ insertion က နောက် model request ရဲ့ input ကိုပြောင်းတာပါ။

Tool Result မှာ Call ID၊ tool name၊ content နဲ့ error state association ရှိရတယ်။ မရှိရင် model က result ကို မှားတဲ့ request နဲ့ချိတ်နိုင်ပါတယ်။

Result context ထဲဝင်ပြီးနောက် ပထမ Turn ကို `turn_end` နဲ့ပိတ်တယ်။ `has_more_tool_calls` က ဆက်သွားလို့ရကြောင်းပြနေသေးလို့ inner loop က နောက်တစ်ကြိမ်ပြန်လည်တယ်။ ဒီအခါမှ Lewis တောင်းထားတဲ့အဖြေကို တကယ်ဖော်ထုတ်နိုင်မယ့် ဒုတိယ model boundary ရောက်လာပါတယ်။

## ၃.၈ Updated Context နဲ့ ဒုတိယ Model Call

ဒုတိယ Turn စတဲ့အခါ Runtime က `turn_start` အသစ်ထုတ်တယ်။ Pending steering မရှိရင် context ကိုထပ်မဖြည့်ဘဲ အခုရှိနေတဲ့ messages အားလုံးနဲ့ model ကိုပြန်ခေါ်တယ်။ ပထမအကြိမ်နဲ့ model တူနိုင်ပေမယ့် request တူတာမဟုတ်ပါဘူး။ Input history ပြောင်းသွားပြီ။

```text
Before model request 2:
  [
    user request,
    assistant Tool Call: read_file(...),
    Tool Result: focused trace content
  ]
```

အခုမှ model က Lewis ရဲ့မေးခွန်းနဲ့ file content ကိုတစ်ပြိုင်နက်မြင်တယ်။ Tool Result ထဲက expected/observed ကွာဟချက်ကိုဖတ်ပြီး “assertion line က ပထမဆုံးလက္ခဏာပဲ၊ failure စတာက request 2 တည်ဆောက်ချိန် Tool Result ပျောက်သွားတဲ့ state transition မှာ” လို့ရှင်းပြနိုင်တယ်။ ဒီ final assistant Message မှာ Tool Call အသစ်မပါဘူး။

Streaming helper က ဒီ response ကိုလည်း partial ကနေ final Message အဖြစ်တည်ဆောက်ပြီး context ထဲထည့်တယ်။ Tool Calls မရှိတော့လို့ `has_more_tool_calls` က false ဖြစ်တယ်။ Runtime က `turn_end` ထုတ်ပြီး stop hook နဲ့ steering queue ကိုသတ်မှတ်ထားတဲ့အစီအစဉ်အတိုင်းစစ်တယ်။ ဘာမှမရှိရင် inner loop ပြီး၊ follow-up queue ကိုစစ်ပြီးမှ `agent_end` ထုတ်တယ်။

Tool Result က model memory ကို လျှို့ဝှက်ပြင်တာမဟုတ်ဘဲ request အသစ်တည်ဆောက်ဖို့ data ပေးတာပါ။ “Tool ပြီးပြီလား” ထက် “Result ပါတဲ့ request အသစ်ခေါ်ပြီးပြီလား” လို့မေးတာ ပိုတိကျပါတယ်။

## ၃.၉ Steering နဲ့ Follow-up ဝင်တဲ့နေရာ

Lewis က file ဖတ်နေချိန် “integration trace ကိုအရင်ကြည့်” လို့ direction ပြောင်းလိုက်ရင် ဘယ်မှာဝင်မလဲ။ `Steering` ဆိုတာ active Run ရဲ့ နောက် model request မတိုင်ခင် context ထဲထည့်မယ့် control Message ပါ။ လက်ရှိ assistant/tool Turn ကို boundary အထိပြီးစေပြီး၊ `turn_end` နောက် steering queue ကို drain လုပ်ကာ နောက် inner-loop iteration မှာ Message အဖြစ်ထည့်တယ်။

`Follow-up` ကတော့ inner loop မှာ Tool Call မရှိ၊ steering မရှိတော့တဲ့အချိန်မှ outer loop ကယူတယ်။ Lewis က “analysis ပြီးရင် fix plan ဆက်ရေး” လို့ queue ထားရင် current answer ပြီးနောက် follow-up Message နဲ့ inner loop ကိုပြန်ဝင်စေတယ်။ Run ကိုပိတ်ပြီး request အသစ်စတာမဟုတ်သေးပါဘူး။

```text
Steering:  active inner loop ရဲ့ next model boundary မတိုင်ခင် drain
Follow-up: inner work ရပ်တော့မယ့် outer boundary မှာ drain
Abort:     cooperative signal; force-stop အာမခံချက်မဟုတ်
```

Abort signal ရောက်တာနဲ့ run နေပြီးသား Tool body ချက်ချင်းပျက်မယ်လို့ မယူဆသင့်ပါဘူး။ Source-backed contract က signal ကိုသိပြီးနောက် model/tool work အသစ်မစဖို့ဖြစ်တယ်။ Lewis ရဲ့ success scenario က live provider cancellation၊ threads သို့မဟုတ် RunLease ကိုမစမ်းပါဘူး။ အဲဒီအပိုင်းကို [Chapter 12](12-steering-followup-cancellation.md) မှာ ဆက်ဖတ်နိုင်ပါတယ်။

## ၃.၁၀ Loop ကို ရပ်စေတဲ့လမ်းကြောင်းများ

Final assistant answer ထွက်လာတိုင်း Run ချက်ချင်းရပ်သလားဆိုရင် မဟုတ်ပါဘူး။ Runtime က completed Turn ရဲ့ state ကိုကြည့်ပြီး Tool chain၊ control queue နဲ့ stop policy တို့ကိုစစ်ရတယ်။ ရပ်တယ်ဆိုတာလည်း loop condition false ဖြစ်တာတစ်မျိုးတည်းမဟုတ်ဘဲ အောက်က boundary တွေကနေ ဖြစ်နိုင်ပါတယ်။

| Outcome | Runtime boundary |
|---|---|
| Normal completion | Assistant Tool Calls မရှိ၊ steering မရှိ၊ follow-up မရှိတော့မှ `agent_end` |
| Assistant error/aborted | Error/aborted assistant Message နဲ့ Turn ကိုပိတ်ပြီး work အသစ်မစဘဲ Agent ကိုပိတ် |
| Cooperative signal observed | သတိပြုမိတဲ့ boundary နောက် model သို့မဟုတ် Tool work အသစ်မစ |
| Stop hook | Completed-turn context ရပြီးနောက် policy ကရပ်ခိုင်းရင် `agent_end` |
| Terminating Tool batch | Tool Calls ရှိခဲ့ရုံနဲ့ မဆက်ဘဲ batch termination result အတိုင်း inner loop ကိုပိတ်နိုင် |
| Steering queued | Active Run ထဲ next model request ဆီ inner loop နဲ့ဆက် |
| Follow-up queued | Inner work ပြီးသလိုဖြစ်ချိန် outer loop ကယူပြီး inner loop ကိုပြန်ဝင် |

Final assistant Message အပြီး Tool Calls နဲ့ queues မရှိတော့လို့ `agent_end` ထုတ်တယ်။ ဒီ event က external work ကိုအတင်းသတ်တာမဟုတ်ဘဲ Run lifecycle အဆုံးရောက်ကြောင်းပြတာပါ။ ရပ်မယ့်လမ်းကြောင်းကိုနားလည်ဖို့ ဘယ် state ပြည့်စုံပြီးမှ ဆုံးဖြတ်လဲကိုဖတ်ရပါတယ်။

## ၃.၁၁ Run တစ်ခုလုံးကို State Snapshots နဲ့ဖတ်ခြင်း

Event order သိရုံနဲ့ model တစ်ကြိမ်စီဘာမြင်လဲ မသိနိုင်ပါဘူး။ Lewis scenario ကို snapshot သုံးခုနဲ့ပြန်စီမယ်။

```text
Before model request 1:
  [user request]

Before model request 2:
  [user request, assistant Tool Call, Tool Result]

After completion:
  [user request, assistant Tool Call, Tool Result, final assistant message]
```

Snapshot ၁ မှာ model ကမေးခွန်းသိပေမယ့် file content မသိသေးဘူး။ Snapshot ၂ မှာ Tool Call လုပ်ခဲ့တဲ့အကြောင်းနဲ့ result နှစ်ခုလုံးရှိလို့ analysis လုပ်နိုင်တယ်။ Snapshot ၃ က final assistant Message ကိုပါ ထည့်ထားလို့ နောက် follow-up သို့မဟုတ် session persistence အတွက် completed history ဖြစ်တယ်။

အခု successful teaching trace ကို event အလိုက်ကြည့်မယ်။ Provider partial update အရေအတွက်က မတူနိုင်လို့ `message_update(...)` ကိုတစ်ကြောင်းနဲ့ချုံ့ထားပါတယ်။

```text
agent_start
turn_start
message_start(user)
message_end(user)
message_start(assistant)
message_update(...)
message_end(assistant with Tool Call)
tool_execution_start(read_file)
tool_execution_end(read_file)
message_start(Tool Result)
message_end(Tool Result)
turn_end
turn_start
message_start(assistant)
message_end(final assistant)
turn_end
agent_end
```

ဒီ success trace ကိုချုံ့ထားတာပါ။ Explicit partial `start` မရှိရင် Runtime က final Message အတွက် start/end ကိုဖြည့်ပေးတယ်။ Event ကို snapshot နဲ့တွဲဖတ်မှ model input နဲ့ observer မြင်တာကို ခွဲနိုင်ပါတယ်။

## ၃.၁၂ Pi ကနေ Travis234 ဆီ Source Flow လိုက်ဖတ်ခြင်း

Concept ကိုမြင်ပြီးမှ source ဖွင့်ရင် Run entry၊ shared loop၊ stream helper နဲ့ Tool helper မြေပုံအတိုင်းခုန်ဖတ်နိုင်တယ်။ Language syntax ကွာပေမယ့် common flow ကို ဒီ function chain ကပြပါတယ်။

| Boundary | Pi | Travis234 |
|---|---|---|
| Run entry | `runAgentLoop` | `run_agent_loop_async` |
| Shared control flow | `runLoop` | `_run_loop` |
| Assistant Message construction | `streamAssistantResponse` | `_stream_assistant_response` |
| Tool batch | `executeToolCalls` | `_execute_tool_calls` |
| Owner/queues | `Agent` in `agent.ts` | `Agent` in `agent.py` |

တစ်ကြောင်းတည်းနဲ့မှတ်ရင် ဒီလိုပါ။

```text
Pi:        runAgentLoop → runLoop → streamAssistantResponse → executeToolCalls
Travis234: run_agent_loop_async → _run_loop → _stream_assistant_response → _execute_tool_calls
```

Entry နှစ်ခုလုံးက prompts ကို state ထဲကူး၊ initial events ထုတ်ပြီး shared loop ကိုဝင်တယ်။ Outer follow-up နဲ့ inner tool/steering loops က completed assistant Message ရမှ Tool Calls ကိုယူပြီး Results ကို context ထဲထည့်ကာ next Turn ဆီဆက်တယ်။

“Flow တူတယ်” ကို “line တိုင်းတူတယ်” လို့မဖတ်ရပါဘူး။ Pinned Travis234 မှာ `turn_end` နောက် `prepare_next_turn` မတိုင်ခင် `signal.aborted` ကို explicit စစ်ပေမယ့် pinned Pi မှာ အဲဒီနေရာနဲ့ပုံစံတူ check မရှိပါဘူး။ Travis234 ရဲ့ exact placement ကို upstream Pi statement လို့မရေးဘဲ common behavior နဲ့ implementation detail ကိုခွဲရပါတယ်။

## ၃.၁၃ Lewis ရဲ့မှတ်စု

Agent ရဲ့ answer ကိုရပြီးနောက် Lewis က assertion line ကိုချက်ချင်းမပြင်သေးဘူး။ Notebook မှာ request တစ်ခုကို answer တစ်ခုအဖြစ်ပဲကြည့်ခဲ့တဲ့အမှားကို အရင်မှတ်တယ်။

- Run တစ်ခုထဲ model request နှစ်ကြိမ်နဲ့ Turn နှစ်ခုရှိနိုင်တယ်။
- Tool ပြီးတာနဲ့ model သိသွားတာမဟုတ်ဘူး။ Tool Result Message ပါတဲ့ context နဲ့ နောက် request လုပ်မှသိတယ်။
- Assistant Tool Call နဲ့ Tool Result နှစ်ခုလုံးကို snapshot ထဲမှာမြင်မှ ဒုတိယ request ရဲ့အကြောင်းရင်းပြည့်စုံတယ်။
- Event order က observer အတွက်ဖြစ်ပြီး context snapshot က model input အတွက်ဖြစ်တယ်။ နှစ်ခုကိုတွဲဖတ်မယ်။
- Steering၊ Follow-up နဲ့ Abort ကို စာသားအဓိပ္ပာယ်နဲ့မခွဲဘဲ သူတို့ဝင်တဲ့ boundary နဲ့ခွဲမယ်။
- Source port ဖတ်ရင် function name တူမတူထက် state ဘယ်အချိန်ပြောင်းလဲကို အရင်တိုက်မယ်။

“ဒါဆို fail စတာ test အဆုံးမှာမဟုတ်ဘူးပေါ့” လို့ Lewis ကပြန်မေးတယ်။ Agent က “ဟုတ်တယ်၊ test ကဖမ်းမိတဲ့နေရာက နောက်ကျတယ်။ စလွဲတာက Tool Result ကို next request ရဲ့ context ထဲမထည့်ခဲ့တဲ့အချိန်” လို့ပြန်တယ်။

ဒီစကားနှစ်ကြောင်းက debugging အတွက်အသုံးဝင်တဲ့မေးခွန်းတစ်ခုချန်ပေးတယ်—error ပေါ်တဲ့ line ကိုသာမကြည့်ဘဲ မှန်ရမယ့် state transition ကို ပထမဆုံးဘယ် boundary မှာလွတ်သွားလဲ ရှာရမယ်။ Runtime Loop ကို chronology နဲ့ဖတ်နိုင်ရင် အဲဒီ boundary ကိုမြန်မြန်တွေ့ပါတယ်။

## ၃.၁၄ အနှစ်ချုပ်

- Agent owner က queue၊ configuration၊ control surface နဲ့ active Run coordination ကိုပိုင်ပြီး shared Runtime Loop ဆီအလုပ်လွှဲတယ်။
- Run က `agent_start` ကနေ `agent_end` အထိဖြစ်ပြီး Turn တစ်ကြိမ်ထက်ပိုပါနိုင်တယ်။
- Initial prompt ကို `new_messages` နဲ့ current context ထဲအရင်ထည့်ပြီးမှ lifecycle events ထုတ်တယ်။
- Assistant stream က partial state ကို completed Message ဖြစ်အောင်တည်ဆောက်ပြီး start/end boundary ကိုထိန်းတယ်။
- Tool Call က Prepare → Execute → Finalize ဖြတ်ပြီး Tool Result Message ဖြစ်လာတယ်။ Tool body ပြီးခြင်းနဲ့ model သိခြင်း မတူပါဘူး။
- Tool Result ကို context ထဲထည့်ပြီး model request အသစ်လုပ်မှ model က result ကိုအသုံးချနိုင်တယ်။
- Steering က active inner loop ရဲ့ next model boundary၊ Follow-up က outer boundary မှာဝင်တယ်။ Abort က cooperative signal ဖြစ်တယ်။
- Loop ရပ်မရပ်ကို Tool Calls၊ completed-turn policy၊ control queues နဲ့ abort/error boundaries အလိုက်ဆုံးဖြတ်တယ်။
- Pi နဲ့ Travis234 ကို function flow အလိုက်ချိတ်ဖတ်နိုင်ပေမယ့် Travis234 ရဲ့ explicit post-turn abort check ကို identical Pi behavior လို့မဆိုရပါဘူး။

ဒီ flow ကို [Chapter 09 — Minimal Runtime Lab](09-minimal-runtime-lab.md) မှာ executable model နဲ့စမ်းနိုင်တယ်။ Failure boundary ကို [Chapter 15](15-debugging-agent-trajectory.md) မှာ trace လိုက်ပြီး port contract ကို [Chapter 16](16-building-a-trustworthy-port.md) မှာစစ်နိုင်ပါတယ်။

## ၃.၁၅ Source Notes

- `C-LOOP-ORDER` — `P-LOOP`, `T-LOOP`; outer follow-up loop၊ inner tool/steering loop နဲ့ request → Tool Result → next request အစီအစဉ်
- `C-MESSAGE-DRAIN` — `P-LOOP`, `P-AGENT`, `T-LOOP`, `T-AGENT`; steering နဲ့ follow-up drain boundaries
- `C-ABORT-OWNERSHIP` — `T-LOOP`, `T-AGENT`, `T-RUN-LEASE`; cooperative abort သိရှိပြီးနောက် work အသစ်မစခြင်းနဲ့ active Run ownership scope
- `P-TYPES`, `T-TYPES`, `T-EVENT-STREAM` — Message၊ Tool Result နဲ့ lifecycle event contracts
- Pi revision: `1f0dbc008c9b3e88017d42e8a1b46d416ad2b6b6`
- Travis234 revision: `68b1831691b8ec93f9550ce63b80cdcb7a591b2e`

Exact source links ကို [Pinned Source Map](../references/SOURCE_MAP.md) မှာကြည့်နိုင်ပြီး claim တစ်ခုချင်းရဲ့ verification boundary ကို [Technical Claim Ledger](../references/CLAIM_LEDGER.md) မှာဖတ်နိုင်ပါတယ်။ ဒီအခန်းက control-flow boundaries ကိုရှင်းပြတာဖြစ်ပြီး full provider integration၊ Tool hooks၊ bounded concurrency၊ Compaction၊ persistence နဲ့ RunLease behavior အားလုံးအလုပ်မှန်ကြောင်း မသက်သေပြပါဘူး။ Lewis ရဲ့ဖြစ်ရပ်နဲ့ dialogue က fictional ဖြစ်ပြီး source-backed production history မဟုတ်ပါဘူး။

---

Previous: [Chapter 02 — Pi Agent Loop Anatomy](02-pi-agent-loop-anatomy.md)

Next: [Chapter 04 — TypeScript ကနေ Python သို့ Semantic Port](04-typescript-to-python-semantic-port.md)

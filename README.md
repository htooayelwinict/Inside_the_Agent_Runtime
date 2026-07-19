# Inside the Agent Runtime (အေးဂျင့်တစ်ခုရဲ့ အတွင်းပိုင်းကို နားလည်ခြင်း)

### AI Agent တစ်ခု ဘယ်လိုစဉ်းစားသလဲ 
### Pi Loop မှ Hermes Compaction အထိ 
### Python ဖြင့် Runtime တစ်ခုတည်ဆောက်ခြင်း

---

AI Agent တစ်ခုက prompt ကိုလက်ခံပြီး Tool ကိုဘယ်လိုရွေးသလဲ၊ result ကို context ထဲဘယ်လိုပြန်ထည့်သလဲ၊ Context Window ပြည့်လာတဲ့အခါ အရေးကြီးတဲ့ state ကိုဘယ်လိုဆက်ထိန်းသလဲ။ ဒီစာအုပ်က Pi-style Agent Loop မှ Hermes-style Compaction အထိ Runtime တစ်ခုရဲ့အတွင်းပိုင်းကို Python code၊ offline labs နဲ့ pinned source evidence တို့ဖြင့် အဆင့်လိုက်ရှင်းပြထားပါတယ်။

**[စာအုပ်စဖတ်ရန်](book/chapters/00-preface-attribution.md)** · **[မာတိကာ](book/SUMMARY.md)** · **[Offline Examples](examples/)** · **[Technical Review](book/REVIEW_REPORT.md)**

## ဒီစာအုပ်ပြီးရင် ဘာမြင်လာမလဲ

- Prompt တစ်ခုက model → Tool Calls → ordered Tool Results → model အစီအစဉ်နဲ့ ဘယ်လိုဖြတ်သန်းသလဲ
- Parallel Tool execution မှာ completion order နဲ့ model မြင်တဲ့ result order ဘာကြောင့်ကွာနိုင်သလဲ
- Context Window pressure ကို truncation တစ်ခုတည်းမဟုတ်ဘဲ Compaction pipeline နဲ့ ဘယ်လိုကိုင်တွယ်သလဲ
- TypeScript implementation ကို Python သို့ syntax မဟုတ်ဘဲ observable behavior ထိန်းပြီး ဘယ်လို port လုပ်သလဲ
- Steering၊ Follow-up၊ failure၊ restart နဲ့ trace တွေကို Runtime boundary အလိုက် ဘယ်လိုစစ်သလဲ

## ဘယ်သူတွေဖတ်သင့်လဲ

- Python အခြေခံသိပြီး Agentic AI ကို ဆက်လေ့လာချင်သူ
- Agent Loop နဲ့ Tool Calling အတွင်းပိုင်းကို နားလည်ချင်သူ
- TypeScript implementation တစ်ခုကို Python သို့ port လုပ်ရာမှာ syntax ထက် behavior ကို ဘယ်လိုထိန်းမလဲ သိချင်သူ
- Context Window ပြည့်လာတဲ့အခါ conversation state ကို ဘယ်လိုချုံ့မလဲ လေ့လာချင်သူ

Pi, Hermes သို့မဟုတ် Travis234 source ကို အရင်ဖတ်ထားဖို့ မလိုပါဘူး။

## စာအုပ်ရဲ့ Learning Journey

1. **[Runtime ဘာကြောင့်လိုသလဲ](book/chapters/01-why-pi-and-hermes.md)** — Pi နဲ့ Hermes ကို mental model တစ်ခုထဲချိတ်ကြည့်မယ်။
2. **[Agent Loop ကို port လုပ်ခြင်း](book/chapters/02-pi-agent-loop-anatomy.md)** — prompt ကနေ completion အထိ loop၊ messages နဲ့ bounded Tool execution ကိုလိုက်ဖတ်မယ်။
3. **[Compaction ကို port လုပ်ခြင်း](book/chapters/06-context-window-pressure.md)** — Context Window pressure၊ deterministic cleanup နဲ့ structured summary ကိုခွဲမယ်။
4. **[Runtime တစ်ခုအဖြစ်ပေါင်းခြင်း](book/chapters/08-pi-meets-hermes.md)** — loop lifecycle ထဲ Compaction ဝင်တဲ့နေရာနဲ့ parity boundary ကိုစစ်မယ်။
5. **[Lewis ရဲ့ Runtime incidents](book/chapters/11-one-night-unfinished-bug.md)** — ordering၊ steering၊ Tool failure၊ restart နဲ့ trace debugging ကို case studies နဲ့လေ့လာမယ်။
6. **[Trustworthy port workshop](book/chapters/16-building-a-trustworthy-port.md)** — observable contracts၊ focused tests နဲ့ intentional divergence ကို evidence အဖြစ်ချိတ်မယ်။

Chapter အားလုံးကို [စာအုပ်မာတိကာ](book/SUMMARY.md) မှာ အစဉ်လိုက်ကြည့်နိုင်ပါတယ်။

## Offline Runtime Companion

Repository ထဲမှာ API key နဲ့ network မလိုတဲ့ Python examples ငါးခုပါပါတယ်။ သူတို့က Agent Loop၊ message control၊ Tool outcomes၊ session restore နဲ့ trace reading contracts ကို concept တစ်ခုချင်းစမ်းနိုင်အောင် ခွဲထားတာပါ။

```bash
python3.13 -m unittest discover -s tests -v
python3.13 scripts/check_book.py
```

Local suite မှာ tests ၂၄ ခုရှိပါတယ်။ ဒီ result က စာအုပ်ရဲ့ teaching artifacts နဲ့ manuscript checks ကိုသာ validate လုပ်ပြီး Travis234 full suite၊ live provider သို့မဟုတ် network integration ကို အစားမထိုးပါဘူး။

## ဒီစာအုပ်ရဲ့ Scope

ဒီစာအုပ်က [Agentic AI အခမဲ့လမ်းညွှန်](https://github.com/htooayelwinict/Agentic-AI-Book) ကို ဖတ်ပြီး Agent Runtime အတွင်းပိုင်းကို ဆက်လေ့လာချင်သူတွေအတွက် ရေးထားတဲ့ sequel ဖြစ်ပါတယ်။ [Travis234](https://github.com/htooayelwinict/travis234) ထဲမှာ Pi ရဲ့ Agent Loop ကို Python နဲ့ ဘယ်လို port လုပ်ထားသလဲ၊ Hermes Agent ရဲ့ Compaction idea ကို ဘယ်လိုယူသုံးထားသလဲဆိုတာ source code အထောက်အထားနဲ့ ရှင်းပြပါတယ်။

Travis234 ရဲ့ feature အကုန်လုံးကို စာရင်းလုပ်ပြမယ့် product manual မဟုတ်ပါဘူး။ Provider configuration အမျိုးမျိုး၊ TUI command အကုန်နဲ့ extension catalog ကို မချဲ့ဘဲ Agent Loop၊ Tool Execution၊ Bounded Concurrency၊ Context Window နဲ့ Compaction ကို reader နားလည်ဖို့လိုတဲ့အပိုင်းပဲ ရွေးထားပါတယ်။ ရည်ရွယ်ချက်က code ကို တစ်ကြောင်းချင်းဘာသာပြန်ဖို့မဟုတ်ဘဲ Runtime က ဘာကြောင့် ဒီလိုအလုပ်လုပ်ရတာလဲဆိုတာ မြင်လာစေဖို့ပါ။

## Source နှင့် Technical Evidence

- [Pinned Source Map](book/references/SOURCE_MAP.md)
- [Technical Claim Ledger](book/references/CLAIM_LEDGER.md)
- [Review Report](book/REVIEW_REPORT.md)

Runtime claims တွေကို pinned Pi၊ Hermes Agent နဲ့ Travis234 revisions ဆီ ချိတ်ထားပါတယ်။ Upstream revision ပြောင်းသွားရင် behavior၊ install command နဲ့ external links တွေ ပြောင်းနိုင်တာကြောင့် သက်ဆိုင်ရာ documentation ကို ပြန်စစ်သင့်ပါတယ်။

## Attribution နှင့် License

Pi, Hermes Agent နဲ့ Travis234 source material တွေဟာ သက်ဆိုင်ရာ MIT license notices အောက်မှာ ရှိပါတယ်။ အသေးစိတ်ကို [Third-Party Notices](THIRD_PARTY_NOTICES.md) မှာဖတ်နိုင်ပါတယ်။ စာမူကို [CC BY-NC-SA 4.0](LICENSE) နဲ့ ဖြန့်ချိထားပါတယ်။

ဒီစာအုပ်ကို ပိုကောင်းလာအောင် ကူညီပေးထားသူတွေနဲ့ accepted community feedback ကို [Contributors / ပါဝင်ကူညီသူများ](CONTRIBUTORS.md) မှာ မှတ်တမ်းတင်ထားပါတယ်။ Contribution လုပ်ချင်ရင် [Contributing Guide](CONTRIBUTING.md) ကို အရင်ဖတ်ပေးပါ။

## လက်ရှိအခြေအနေ

Chapter 00–16 ပါတဲ့ main sequence ၁၇ ခန်း၊ appendix လေးခု၊ Lewis ရဲ့ case studies နဲ့ offline Runtime workshop တွေကို manuscript checks နဲ့ focused tests ဖြင့် စစ်ထားပါတယ်။ စစ်ဆေးထားတဲ့ boundary နဲ့ မပြေးထားတဲ့ upstream full-suite အကြောင်းကို [Review Report](book/REVIEW_REPORT.md) မှာ ခွဲရေးထားပါတယ်။

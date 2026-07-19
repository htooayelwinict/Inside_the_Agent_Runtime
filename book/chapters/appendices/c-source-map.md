# Appendix C — Source Map နှင့် Pinned Revisions

Software project တစ်ခုက အမြဲပြောင်းနေပါတယ်။ ဒီနေ့ဖတ်ထားတဲ့ function နဲ့ behavior က နောက် release မှာ ပြောင်းသွားနိုင်ပါတယ်။ ဒါကြောင့် ဒီစာအုပ်က “လက်ရှိ source မှာ ဒီလိုပဲ” လို့ လွတ်လွတ်လပ်လပ်မပြောဘဲ research လုပ်ခဲ့တဲ့ Git commit ကို pin ထားပါတယ်။

## Revision pin လုပ်ရတဲ့အကြောင်းရင်း

Pinned revision ရှိရင် reader က စာအုပ်ရေးချိန်မှာ စာရေးသူမြင်ခဲ့တဲ့ source ကို တူညီတဲ့အခြေအနေအတိုင်း ပြန်ဖတ်နိုင်ပါတယ်။ Newer release မှာ behavior ကွာလာရင် စာအုပ်မှားနေတယ်လို့ ချက်ချင်းမယူဆဘဲ ဘယ် revision နှစ်ခုကြားမှာ ပြောင်းသွားသလဲ စစ်နိုင်ပါတယ်။

ဒီစာအုပ်ရဲ့ research baseline က:

| Project | Revision |
|---|---|
| Agentic AI Book | `7eed5ca1c4b21ab766dda2df4e039ab745cdc30f` |
| Travis234 | `68b1831691b8ec93f9550ce63b80cdcb7a591b2e` |
| Pi | `1f0dbc008c9b3e88017d42e8a1b46d416ad2b6b6` |
| Hermes Agent | `af250d84948179834820a62bfd870c0df6f264a1` |

## Source ID ကို ဘယ်လိုဖတ်မလဲ

Chapter Source Notes မှာ `T-LOOP`, `P-LOOP`, `H-COMPRESS` လို ID တွေ တွေ့ရပါမယ်။

- `T-*` က Travis234 source ဖြစ်တယ်။
- `P-*` က Pi upstream source ဖြစ်တယ်။
- `H-*` က Hermes Agent upstream source ဖြစ်တယ်။

ID တစ်ခုချင်းရဲ့ exact file၊ pinned link နဲ့ evidence boundary ကို [Pinned Source Map](../../references/SOURCE_MAP.md) မှာ ကြည့်နိုင်ပါတယ်။ Runtime claim နဲ့ verification state ကို [Technical Claim Ledger](../../references/CLAIM_LEDGER.md) မှာ ထပ်စစ်နိုင်ပါတယ်။

## Line number ထက် behavior ကို ဦးစားပေးပါ

စာအုပ်က line number ကို အဓိက citation မလုပ်ပါဘူး။ Source refactor လုပ်လိုက်ရင် line number လွယ်လွယ်ပြောင်းနိုင်ပေမယ့် behavior contract နဲ့ test name က အကြောင်းအရာကို ပိုတည်ငြိမ်စွာ ဖော်ပြနိုင်လို့ပါ။ ဒါပေမယ့် function တစ်ခု ရွှေ့သွားတာ၊ contract ပြောင်းသွားတာဆိုရင် source map ကို revision အသစ်နဲ့ refresh လုပ်ရပါမယ်။

## Limitation

Revision pin လုပ်ထားတာက claim တစ်ခု အလိုအလျောက်မှန်ကြောင်း သက်သေမပြပါဘူး။ Source ကိုမှားဖတ်နိုင်သလို test တစ်ခုက production behavior အားလုံးကို မဖုံးနိုင်ပါဘူး။ Pinned source၊ focused test နဲ့ ရှင်းလင်းထားတဲ့ evidence boundary သုံးခုကို တွဲကြည့်မှ ယုံကြည်ရတဲ့ explanation ဖြစ်လာပါတယ်။

---

Previous: [Appendix B — npm Docker Launcher](b-npm-docker-launcher.md)

Next: [Appendix D — Glossary နှင့် References](d-glossary-references.md)

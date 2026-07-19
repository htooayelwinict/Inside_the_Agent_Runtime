# Contributing

Travis234 Book က author voice နဲ့ technical evidence နှစ်ခုလုံးကို ထိန်းထားရတဲ့ စာအုပ် project ဖြစ်ပါတယ်။ Contribution ကို သေးသေးနဲ့ တိတိကျကျလုပ်ပေးရင် review လုပ်ရလွယ်ပါတယ်။

## ကူညီနိုင်တဲ့အရာများ

- typo၊ punctuation နဲ့ spacing ပြင်ဆင်ခြင်း
- broken link report လုပ်ခြင်း
- technical term consistency စစ်ပေးခြင်း
- diagram နဲ့ beginner example အကြံပြုခြင်း
- source-backed technical correction ပေးခြင်း
- glossary term ဖြည့်ပေးခြင်း

## Manuscript Rule

Chapter တစ်ခန်းလုံး သို့မဟုတ် section အကြီးစား rewrite လုပ်မယ့်အခါ issue အရင်ဖွင့်ပြီး ဆွေးနွေးပါ။ Confusing ဖြစ်တဲ့စာကြောင်း၊ မရှင်းတဲ့အကြောင်းရင်းနဲ့ အကြံပြုထားတဲ့ direction ကို တိတိကျကျထည့်ပေးပါ။ Maintainer အတည်ပြုချက်မရခင် author voice ကို အစားထိုးမယ့် PR မပို့ပါနဲ့။

Typo fix လို small change တွေကတော့ တိုက်ရိုက် PR ပို့နိုင်ပါတယ်။

## Technical Correction

Runtime behavior နဲ့ပတ်သက်တဲ့ correction တစ်ခုမှာ အနည်းဆုံး အောက်ကတစ်ခု ပါရမယ်။

- pinned source file နဲ့ revision
- test သို့မဟုတ် parity contract
- reproducible example

“ဒီလိုဖြစ်မယ်ထင်တယ်” ဆိုတဲ့ claim တစ်ခုတည်းနဲ့ စာမူကို မပြင်ပါဘူး။

## Pull Request Flow

1. Issue လိုအပ်မလို scope ကို စစ်ပါ။
2. Focus တစ်ခုတည်းပါတဲ့ branch ဖန်တီးပါ။
3. Book checker နဲ့ lab tests ကို run ပါ။
4. ဘာပြင်ထားသလဲ၊ ဘာကြောင့်ပြင်သလဲ ရှင်းပြပါ။
5. Source-backed change ဆိုရင် source ID သို့မဟုတ် URL ထည့်ပါ။

```bash
python3.13 -m unittest discover -s tests -v
python3.13 scripts/check_book.py
```

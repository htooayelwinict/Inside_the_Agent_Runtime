# Appendix A — Installation

ဒီ appendix က Travis234 ကို စမ်းသုံးဖို့လိုတဲ့ အနည်းဆုံး installation လမ်းကြောင်းကိုပဲ စုထားပါတယ်။ Command တွေက pinned Travis234 revision ရဲ့ `README.md` နဲ့ package metadata ကို အခြေခံထားပါတယ်။ Provider အကုန်ရဲ့ credential setup နဲ့ optional feature အကုန်ကို မချဲ့ထားပါဘူး။

## A.1 Python Version

Pinned package metadata မှာ Python version ကို ဒီ range နဲ့ သတ်မှတ်ထားပါတယ်။

```text
>=3.13,<3.14
```

ဒါကြောင့် အောက်က command တွေမှာ `python3.13` ကို သုံးထားပါတယ်။ တခြား version တစ်ခုနဲ့ အလုပ်လုပ်နိုင်မယ်လို့ package metadata က အာမမခံထားပါဘူး။

## A.2 PyPI ကနေ Install လုပ်ခြင်း

`uv` သုံးရင် persistent CLI tool အဖြစ် install လုပ်နိုင်ပါတယ်။

```bash
uv tool install --python 3.13 travis234
travis234 --cwd .
```

Install မလုပ်ဘဲ တစ်ကြိမ် run ချင်ရင်:

```bash
uvx --python 3.13 travis234 --cwd .
```

`pip` သုံးမယ်ဆိုရင်:

```bash
python3.13 -m pip install travis234
travis234 --cwd .
```

ဒီ command တွေက package download နဲ့ provider အသုံးပြုမှုအတွက် network လိုနိုင်ပါတယ်။ ဒီစာအုပ်ရေးသားမှုအတွင်း PyPI installation ကို သီးခြားပြန်စမ်းထားတယ်လို့ မဆိုလိုပါဘူး။ Pinned repository ရဲ့ documented commands ကို ပြန်ဖော်ပြထားတာပါ။

## A.3 Source ကနေ Run ခြင်း

Source ကိုဖတ်ရင်း စမ်းချင်ရင် editable installation က အသုံးဝင်ပါတယ်။

```bash
git clone https://github.com/htooayelwinict/travis234.git
cd travis234
python3.13 -m venv .venv
.venv/bin/pip install -e .
.venv/bin/travis234 --cwd .
```

`-e` က source file ပြင်လိုက်တာကို package ပြန် install မလုပ်ဘဲ development environment မှာ မြင်နိုင်စေပါတယ်။ Windows မှာ virtual-environment executable path က ကွာနိုင်ပါတယ်။

## A.4 ပထမဆုံး Run ပြီးနောက်

TUI ထဲမှာ `/login` နဲ့ provider authentication လုပ်ပြီး `/model` နဲ့ model ရွေးနိုင်ပါတယ်။ လက်ရှိ project ကို Agent က resource နဲ့ tool အဖြစ်သုံးမလားဆိုတာ trust prompt သို့မဟုတ် explicit policy နဲ့ ဆုံးဖြတ်ရနိုင်ပါတယ်။ မသေချာတဲ့ project ကို အလိုအလျောက် approve မလုပ်သင့်ပါဘူး။

Docker ထဲကနေ run ချင်ရင် [Appendix B — npm Docker Launcher](b-npm-docker-launcher.md) ကို ဆက်ဖတ်ပါ။

## A.5 Source Notes

- `T-PACKAGE` — Travis234 `README.md`, `pyproject.toml`
- Travis234 revision: `68b1831691b8ec93f9550ce63b80cdcb7a591b2e`

---

Previous: [Chapter 16 — ယုံကြည်ရတဲ့ Python Port တစ်ခုဖြစ်လာဖို့](../16-building-a-trustworthy-port.md)

Next: [Appendix B — npm Docker Launcher](b-npm-docker-launcher.md)

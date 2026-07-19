# Appendix B — npm Docker Launcher

Local Python environment မတည်ဆောက်ချင်ဘဲ Travis234 ကို container ထဲကနေ run ချင်ရင် npm launcher ကို သုံးနိုင်ပါတယ်။ Launcher က Agent Runtime ကို JavaScript နဲ့ပြန်ရေးထားတာမဟုတ်ပါဘူး။ Docker command ကိုပြင်ဆင်ပြီး Travis234 release image ကို run ပေးတဲ့ အလွှာပါ။

## B.1 လိုအပ်ချက်နဲ့ စတင်ပုံ

Pinned npm package metadata က Node.js `>=18` လို့သတ်မှတ်ထားပြီး host မှာ Docker လည်း run နေရပါမယ်။ Workspace root မှာ:

```bash
npx @htooayelwinict/travis234 --cwd .
```

Default image က:

```text
ghcr.io/htooayelwinict/travis234:production
```

Launcher က selected workspace ကို container ရဲ့ `/workspace` မှာ mount လုပ်ပြီး Travis234 ကို အဲဒီ directory နဲ့စပါတယ်။

## B.2 ဘယ် directory တွေကို mount လုပ်သလဲ

Default command မှာ အဓိက read-write mounts နှစ်ခုရှိပါတယ်။

| Host | Container | Purpose |
|---|---|---|
| `--cwd` နဲ့ရွေးထားတဲ့ workspace | `/workspace` | Agent ဖတ်၊ ရေးမယ့် project |
| `~/.travis234/sandbox-home` | `/travis-home` | Sandbox sessions နဲ့ Travis234 state |

Workspace ကို `:rw` နဲ့ mount လုပ်တာကြောင့် container ထဲက tool က host project files ကို တကယ်ပြင်နိုင်ပါတယ်။ Container ဖျက်သွားလည်း sandbox state directory က host မှာကျန်လို့ sessions ကို ပြန်သုံးနိုင်ပါတယ်။ Host ရဲ့ပုံမှန် Travis234 state နဲ့ sandbox state ကို directory ခွဲထားပါတယ်။

Host `.env` file နဲ့ provider credentials ကို launcher က အလိုအလျောက်မပို့ပါဘူး။ Authentication လိုရင် TUI ထဲ `/login` ကို သုံးနိုင်ပါတယ်။ ဒါက secret အားလုံး container ထဲဘယ်တော့မှမရောက်နိုင်ဘူးလို့ အာမခံတာမဟုတ်ပါဘူး။ User ကိုယ်တိုင် mount၊ environment သို့မဟုတ် project file ထဲ ထည့်ထားတဲ့ secret ကတော့ workspace ကနေ ဖတ်နိုင်ပါတယ်။

## B.3 Launcher ထည့်ပေးတဲ့ Controls

Pinned launcher က Docker command ထဲမှာ အောက်ပါ controls တွေ ထည့်ပါတယ်။

- `--cap-drop ALL` နဲ့ Linux capabilities ကိုဖြုတ်တယ်။
- `--security-opt no-new-privileges` နဲ့ privilege အသစ်ရယူမှုကို တားတယ်။
- Host UID/GID ကို `--user` အဖြစ်သုံးတယ်။
- `--pids-limit 512` နဲ့ container process count ကိုကန့်သတ်တယ်။
- Disposable container အတွက် `--rm` သုံးတယ်။
- Docker socket နဲ့ host root ကို default mount မလုပ်ဘူး။

Network က default အနေနဲ့ ဖွင့်ထားပါတယ်။ Network မလိုတဲ့အလုပ်ဆိုရင်:

```bash
npx @htooayelwinict/travis234 --cwd . --no-network
```

ဒီ flag က Docker command ထဲ `--network=none` ထည့်ပါတယ်။ Model provider ကိုတိုက်ရိုက်ခေါ်ရမယ့် run ဆိုရင်တော့ network ပိတ်ထားလို့ အလုပ်မလုပ်နိုင်ပါဘူး။

Docker command ကို အရင်ကြည့်ချင်ရင် `--dry-run` သုံးနိုင်ပါတယ်။

```bash
npx @htooayelwinict/travis234 --cwd . --dry-run
```

## B.4 Security Boundary ကို မှန်မှန်နားလည်ခြင်း

အပေါ်က controls တွေက default container ကို တင်းကျပ်စေပါတယ်။ ဒါပေမယ့် complete security boundary လို့ မယူဆသင့်ပါဘူး။

အကြောင်းရင်းက:

- Workspace ကို read-write mount လုပ်ထားလို့ Agent က project data ကို ပြင်နိုင်တယ်။
- Network ကို default ဖွင့်ထားလို့ process က external services ကို ဆက်သွယ်နိုင်တယ်။
- Container isolation က host kernel နဲ့ Docker configuration ပေါ်မူတည်တယ်။
- Trusted extension နဲ့ tool တွေက container user ရဲ့ permission နဲ့ execute လုပ်တယ်။

အရေးကြီးတဲ့ project ဆိုရင် version control၊ backup၊ minimal workspace scope၊ `--no-network` နဲ့ host-level Docker policy တွေကို အတူစဉ်းစားရပါတယ်။ “Container ထဲမှာ run တယ်” ဆိုတဲ့အချက်တစ်ခုတည်းနဲ့ destructive action နဲ့ data exposure အန္တရာယ် ပျောက်မသွားပါဘူး။

## B.5 Source Notes

- `T-LAUNCHER` — npm package metadata နဲ့ Docker command builder
- `T-PACKAGE` — documented launcher command
- Travis234 revision: `68b1831691b8ec93f9550ce63b80cdcb7a591b2e`

---

Previous: [Appendix A — Installation](a-installation.md)

Next: [Appendix C — Source Map နှင့် Pinned Revisions](c-source-map.md)

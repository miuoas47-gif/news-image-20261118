# news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/miuoas47-gif/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/miuoas47-gif/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

18 November 2026 in one image: the Trump–Xi–Putin trilateral at APEC Shenzhen, US strikes on Iran's Qeshm Island and the Hormuz escalation, a global tech outage grounding flights, Cyclone Akvan nearing Odisha, the US losing measles-free status, Nvidia beating estimates amid China H200 restrictions, the Gaza operation, the Crimea bridge strike, Peltola flipping the Alaska Senate seat 56–44, and a magnitude 6 quake in Papua New Guinea — all in a single illustrated front page (`ad.png`), presented as an ad page for make.fun (`index.html`, with referral link https://make.fun/r/6gvkzysc).

## Run it

```sh
open index.html  # or: python3 -m http.server 8000
```

### Validate and serve with `main.py`

The entry ships with a small stdlib-only entrypoint, `main.py`. It needs no
dependencies — just Python 3.

```sh
python3 main.py --check        # validate the entry files (exits non-zero on failure)
python3 main.py --serve        # serve this directory at http://127.0.0.1:8000/
python3 main.py --serve --port 9000   # same, on a different port
```

`--check` verifies that `index.html` exists and references `ad.png`, that
`ad.png` is present and under 8 MB, that `index.html` is under 2 MB, and that
this README carries the make.fun badges for this competition.

---

<sub>Entered on [make.fun](https://make.fun/?ref=6gvkzysc&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>

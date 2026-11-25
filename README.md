# news-image-20261125 — Wednesday 25 November 2026 in one image

[![news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/c/news-image-20261125/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/meongs123/news-image-20261125/rank.svg)](https://make.fun/c/news-image-20261125/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/meongs123/news-image-20261125/reward.svg)](https://make.fun/c/news-image-20261125/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A make.fun bounty entry: a newspaper front page summing up the world's news
of **Wednesday 25 November 2026** — 44 stories, 7 regions, 13 drawn
illustrations, one-line briefs, and a
DATE CHECK box naming the stories that are *not* 25 November news.

## The image

- Masthead: **Wednesday 25 November 2026**, with the count strip
  (44 stories · 7 regions · 13 illustrated), a numbers strip
  (Dow 50,018.70, Nasdaq −1.48%, KOSPI −6.16%, Bangladesh Tk 17,000 +36%,
  Real Madrid 5–1 PSV, Iowa 9,500 lb) and a proportional region bar
  (Americas 9 · Asia 13 · Europe 6 · Africa 2 · Middle East 8 · World 2 ·
  Oceania 4).
- Lead stories: a full-width splash — **Shenzhou-24 docks at Tiangong with the
  first Pakistani in orbit** — over two half-width leads, the
  **Australia–Solomon Islands Treaty** and the **Iowa lead-azide blast**.
- 3 big + 10 small illustrated lead cards, 31 numbered one-line briefs, and a
  box (ICJ Rohingya verdict — 19 Nov; COP31 collapse and Merkury sinking —
  Sun 22 Nov; Huang reinstated — Mon 23 Nov; Gibran resigns — 12 Nov;
  Dow above 50,000 — Tue 24 Nov close; Hanoi blast — Tue 24 Nov).
- Every picture is an original flat-vector drawing made in code. No
  photographs. Sources are tagged per story.

## Facts, frozen at build time (Wed 25 Nov ~16:10 WIB)

- Shenzhou-24: launch **08:18**, docking **11:56** Beijing time; crew Tang
  Hongbo, Wu Yi, and Muhammad Zeeshan Ali, 40 — first Pakistani in orbit,
  first foreigner aboard Tiangong; stay **5–10 days**.
- Solomon Islands Treaty signed in Canberra Wed; Honiara says **no foreign
  military base** on its soil.
- Iowa: **68 barrels / ~9,500 lb** of decaying lead azide, detonation
  **09:00 local Wed**, 5-mile evacuation cone.
- Markets use the **AP set (Tue 24 Nov close)**: Dow **50,018.70 +0.85%**,
  S&P 500 **7,201.09 −0.50%**, Nasdaq **23,733.54 −1.48%**; Nvidia
  **$155.38 −5.86% Tue**, one day after its **+30% Mon** rebound.
- Bangladesh garment wage **Tk 17,000/month, +36%**, from Tk 12,500.
- Cartagena: **all hostages freed**, 1 captor killed (Wed); Villavicencio
  car bomb injured **23** (AP, latest).
- Gaza: Tue toll **7 killed in total**; the Wed report of a second Hamas
  security chief is a **separate** incident, unconfirmed by the IDF.
- Houthi strikes on Riyadh's PIF Tower are three distinct events
  (19 Nov, no injuries; 24 Nov, 11 wounded; 25 Nov, new claim) — never merged.
- Trump tariffs on 16 partners are **"set to be unveiled"** — no rates
  announced, none imposed. The unnamed Japanese tech conglomerate (−9.55%)
  is **not named** anywhere in the image.
- **Still developing at build time — freeze pass ~20:00 WIB Wed 25 Nov:**
  evening US/Europe news, markets close, Champions League results.

## Files

- `main.ts` — the entrypoint (Node 22, stdlib only): copies `entry.png`
  to `/output/entry.png` and guards the PNG signature, the 1 MiB cap,
  the 1024×1024 size, and a byte-identical round trip.
- `entry.png` — the image (1024×1024), drawn by `compose.py`.
- `compose.py` — the deterministic renderer (PIL, no clock, no randomness,
  no network). It fails loudly instead of truncating: any headline, deck
  or brief that needs more lines than its box allows raises, and every
  illustration is audited to paint only inside its own box.
- `stories.py` — the 44-story slate with regions, fields and sources.

## Verify locally

```sh
python3 compose.py            # regenerates entry.png (deterministic)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## License

MIT — see `LICENSE`.

# Deliverable 1 — Revision Demo Script

A presentation-ready walkthrough of how the resubmitted D1 fixes every issue raised in the tutor feedback. It is designed to be read aloud (~3-4 minutes) and also to be skimmed: each change is stated as **What I changed -> Why it now meets the requirement**.

---

## 0. One-line summary (opening)

"My original D1 failed on criteria **1A (specific and clear CtA)** and **1C (clear SDG connection)**, and the tutor also flagged an internal contradiction and weak evidence. In this revision I fixed all four issues by narrowing to one consistent scope, replacing three vague signals with one measurable metric, backing every claim with data from two open datasets, and explicitly defending the SDG link. Here is exactly what changed and why each change satisfies the requirement."

---

## 1. The four problems I had to fix

| # | Tutor feedback | Rubric | The underlying problem |
|---|----------------|--------|------------------------|
| A | CtA "needs to be clearer and more consistent" | 1A | Vague, and self-contradictory scope |
| B | "regional areas" vs "postcodes with low plugs per population" is a contradiction | 1A | Two different targets in one action |
| C | Ranking system undefined (no metric, no calculation, no impacted areas) | 1A | The "priority score" was hand-wavy |
| D | "SDG 11.2 mainly relates to public transportation" | 1C | SDG link asserted, not justified |
| E | "impact statement needs stronger evidence" | 1B (support) | No data or references |

---

## 2. Change-by-change walkthrough (the core of the demo)

### Change 1 — I fixed the contradictory scope
- **What I changed:** I removed "regional" from the title and CtA. The whole document now targets **one thing only: high-population outer-suburban Greater Sydney LGAs**.
- **Old wording:** "underserved outer-suburban **and regional** communities" + "LGAs and **postcodes** with low public plugs per population."
- **Why this meets the requirement (1A):** The tutor said "regional areas" and "postcodes with low plugs per population" may not be the same places — a contradiction. By committing to a single scope, the CtA can no longer point at two different sets of areas. It is now internally consistent, and it matches the D2 analysis, which is limited to the 34 Greater Sydney LGAs.

### Change 2 — I replaced three vague signals with one measurable metric
- **What I changed:** The old CtA mixed three undefined, unweighted signals — "low public plugs per population," "limited DC fast-charging access," and "weak regional connectivity." I collapsed these into a **single named metric: the "Charging Access Equity Score" = public charging plugs per 10,000 residents.**
- **Why this meets the requirement (1A):** Three signals can point to three different areas (a remote highway town scores fine on "connectivity" but terribly on per-capita access). One metric means one unambiguous ranking, so the action is specific and repeatable.

### Change 3 — I fully described the ranking system and gave it a measurable target
- **What I changed:** I spelled out the score in five steps:
  1. **Metric** — plugs per 10,000 residents, from joining the TfNSW charging dataset to the ABS population dataset.
  2. **Scoring** — rank all 34 Greater Sydney LGAs; flag any below the Greater Sydney average of **4.0** as under-served.
  3. **Population weighting** — among those, prioritise above-average-population LGAs, because that is where the most residents are affected.
  4. **Allocation** — fund the highest-priority LGAs first, instead of adding chargers where access is already high.
  5. **Measurable target** — by 2030, bring every Greater Sydney LGA up to at least 4.0 plugs per 10,000 residents and cut the best-vs-worst gap from ~20x to no more than 5x, tracked by re-running the same metric each round.
- **Why this meets the requirement (1A — specific and measurable):** The tutor asked for "how the scores would be calculated, what metrics would be used, and which areas are most impacted," and both first-time-pass example D1s were still told to make the CtA "more specific and measurable" with a clear "expected improvement." I answer all of this — I name the top-priority LGAs (Cumberland 0.7, Fairfield 0.9, Canterbury-Bankstown 1.5) and attach a numeric 2030 target whose success can be objectively checked.

### Change 4 — I backed the impact statement with data and references
- **What I changed:** I replaced the general claim ("stations are concentrated in a few major areas") with the measured result from D2: a **~20-fold gap** — Woollahra 16.5 vs the Greater Sydney average of 4.0, with Cumberland 0.7, Fairfield 0.9, Canterbury-Bankstown 1.5 — plus their populations. I also cite **two named open datasets** (TfNSW EV charging locations + ABS Regional Population 2024-25).
- **Why this meets the requirement (evidence / supports 1B):** The tutor said the statement "needs stronger evidence" with "clear data or reference support." Every claim is now a number from a named, linkable source, so the argument is justified rather than asserted — and it addresses the real underlying problem: outer-suburban residents depend most on public charging yet have the least access.

### Change 5 — I defended the SDG 11.2 link instead of just asserting it
- **What I changed:** I kept **SDG 11.2 as the primary target** but openly acknowledged the tutor's objection — that 11.2 usually means mass transit and a charger is not a "public transport service" — and then rebutted it with three arguments:
  1. **11.2 is defined by its outcome, not by vehicle type** — its official indicator is the *proportion of the population with convenient access to sustainable transport*.
  2. **A public charger is shared, publicly-sited enabling infrastructure** — like a bus stop makes bus travel usable, a charger makes the EV mode usable in a community.
  3. **My metric is a direct proxy for the 11.2 indicator** — "plugs per 10,000 residents" measures "population with convenient access," and the 20x gap shows access is not "for all."
- **I also re-aligned the supporting SDGs to the equity core:** **SDG 10.2** (reduced inequalities) and **SDG 7.1** (universal access to modern energy services — charging is an energy service), with **SDG 13 kept only as a downstream benefit.**
- **Why this meets the requirement (1C):** The tutor said to "either explain more clearly how it applies or identify another SDG." I did the first — I name the exact objection and answer it with the indicator definition — which turns an asserted link into a defended one.

### Change 6 — I made the Target Audience explicit and gave it a strong, itemised incentive
- **What I changed:** I set **one consistent primary audience — the NSW DCCEEW EV public-charging grant team** (the body that writes the grant scoring rules), and gave four concrete reasons they would act:
  1. **Higher return per dollar** — the same grant delivers far more access in Cumberland (0.7) than in an already well-served inner suburb.
  2. **It helps them hit existing NSW targets** — the NSW EV Strategy and net-zero-by-2050 depend on uptake in exactly the outer suburbs that lack chargers.
  3. **Low-cost, low-risk to adopt** — it reuses two existing open datasets and adds just one criterion to a grant program that already exists.
  4. **Publicly defensible** — a transparent equity rule protects them from criticism that charging money favours wealthy areas.
- **Why this meets the requirement (2A / 2C):** Both first-time-pass example D1s were told to "explain more clearly why the authority would be willing to do this, since they would need to spend a lot of funding." Naming one audience and giving four specific, self-interested reasons pre-empts that comment and keeps the TA consistent everywhere in the post.

### Change 7 — I cleaned up the grammar
- **What I changed:** Fixed errors such as "while ignore the residents," "this will reduced their confidence," and "By acting on this would make."
- **Why this meets the requirement (1A — clarity):** Clear writing is part of "specific and clear"; the corrected text removes ambiguity.

---

## 3. Before / after, at a glance (good for a single slide)

| Aspect | Old D1 | Revised D1 |
|--------|--------|------------|
| Scope | Outer-suburban **and regional** | Outer-suburban **Greater Sydney only** |
| Priority signal | 3 mixed, undefined signals | 1 metric: plugs per 10,000 residents |
| Ranking method | Not described | 5 explicit steps + threshold (4.0) |
| Measurable target | None | By 2030: every LGA >= 4.0; gap cut from ~20x to <=5x |
| Evidence | None | 20x gap, named LGAs, 2 datasets |
| SDG link | Asserted | Defended (11.2 indicator) + SDG 10/7 support |
| Target audience | Implied | One named body (DCCEEW grant team) + 4 incentives |

---

## 4. Requirement-coverage checklist (closing)

"To close, here is how the revision maps to the criteria I previously failed or needed to strengthen:"

- **1A — specific, clear and measurable CtA:** one scope, one metric, one 5-step method with a 2030 numeric target (Changes 1-3, 7). PASS.
- **1B — addresses the underlying problem:** data shows outer suburbs depend most on public charging yet have least access (Change 4). SUPPORTED.
- **1C — clear SDG connection:** 11.2 defended via its official indicator, reinforced by SDG 10 and 7 (Change 5). PASS.
- **1D — actionable and context-appropriate:** the grant team can literally add the Equity Score as a funding rule (Change 3).
- **2A / 2C — appropriate TA with a strong incentive:** one named audience (DCCEEW grant team) with four self-interested reasons to act (Change 6).
- **6A — topic not real-estate affordability:** topic is EV charging equity / sustainable transport access.

"And critically, the three anchors — the scope (outer-suburban Greater Sydney LGAs with lowest per-capita access), the metric (plugs per 10,000 residents against the 4.0 average), and the target audience (the DCCEEW EV public-charging grant team) — are worded identically across the title, impact statement, SDG argument, call to action, target-audience section, and dataset description, and they match my D2 analysis. Thank you."

---

**Approx. spoken length: 3-4 minutes.** For the source-of-truth side-by-side text (feedback / old / new / annotations), see `d1_revision_comparison.md`.

---

## 5. Third Revision (v3) — the concise, ≤250-word post

"The v2 revision fixed every rubric issue, but it was long — about 950 words. For the third revision I kept all of that reasoning but compressed the **actual post I submit** to a **~210-word body**, matching the structure of the approved example posts (topic + SDG → summary → who is impacted → data → who can help + CtA → incentive). While compressing, I made three targeted upgrades."

### v3 — What changed vs v2 and why it meets the requirement

- **1. I made the scoring *useful*, not just *defined*.**
  - **What I changed:** v2 spelled out *how* to compute the Charging Access Equity Score but never said *why a score beats current practice*. v3 adds one line: "Ranking on this single metric removes the old ambiguity and makes every funding decision auditable and repeatable."
  - **Why it works:** it answers the grant team's real question — "why change how we decide?" — with a governance benefit they care about: one ranked number turns a subjective, lobby-able "which area next?" call into an objective, repeatable rule they can re-run and defend every funding round. That is what makes the score persuasive, not just descriptive.

- **2. I tied the CtA to the impact statement so they solve the problem together.**
  - **What I changed:** both halves now pivot on the *same* metric — public plugs per 10,000 residents. The impact statement uses it to *measure* the 20-fold gap; the CtA uses it to *act* (prioritise below-4.0 LGAs) and to *set the target* (every LGA ≥ 4.0 by 2030).
  - **Why it works:** the reader can trace *problem → action → measurable outcome* on one number, so the CtA visibly closes exactly the gap the impact statement opens — no scope drift, no second metric.

- **3. I added the missing EV ownership and purchase numbers.**
  - **What I changed:** v2 proved charging *supply* was unequal but showed no vehicle *demand*. v3 adds NSW EV **ownership** — 52,572 registered EVs at January 2024, 7.5× the 6,160 in 2021 (NSW State of Environment 2024 / BITRE) — and **annual purchases** — about 28,200 new EVs in 2024, a 9.5% share of new-car sales (Electric Vehicle Council, *State of EVs 2024* / VFACTS).
  - **Why it works:** it proves uptake is real and accelerating, so the access gap is an active, worsening problem for a growing number of drivers — which raises the stakes of the CtA rather than leaving it hypothetical.

- **4. I hit the ≤250-word limit.**
  - **What I changed:** compressed v2's long SDG defence and four-bullet incentive list to one clause each, and folded the five-step scoring method into a single CtA sentence.
  - **Why it works:** the body is ~210 words (title and dataset/evidence links excluded, as in the approved example), safely under the 250-word cap, while every rubric-relevant claim survives. The full-length reasoning is retained in `d1_revision_comparison.md` for any follow-up question.

### v3 — Requirement-coverage close

"So the third revision keeps the same three anchors — scope (high-population outer-suburban Greater Sydney LGAs), metric (plugs per 10,000 residents against the 4.0 average), and target audience (the DCCEEW EV public-charging grant team) — but now: the scoring earns its place by making funding auditable and repeatable; the CtA and impact statement close a single loop on one metric; EV ownership and sales numbers prove the problem is live and growing; and the whole post fits inside 250 words. Thank you."

For the full v3 post text and change-by-change annotations, see Section 6 of `d1_revision_comparison.md`.

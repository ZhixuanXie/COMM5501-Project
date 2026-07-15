# Deliverable 1 — Revision & Comparison

This document revises Deliverable 1 (D1) so that it passes the two failed rubric criteria (1A and 1C) and stays fully consistent with the Deliverable 2 (D2) analysis. It is laid out in four sections:

1. D1 tutor feedback (verbatim)
2. Old D1 content (verbatim)
3. New (revised) D1 content
4. Detailed change annotations (what changed, where, and why)

---

## 1. D1 Tutor Feedback (verbatim)

> **Fail, 1A, 1C**
>
> Your CtA needs to be clearer and more consistent. SDG 11.2 mainly relates to public transportation, so you should either explain more clearly how it applies to your issue or identify another SDG that is more directly relevant.
>
> The CtA lacks clarity because you state that regional areas should be prioritised, but you also consider "postcodes with low public plugs per population." These may not identify the same areas, which creates a contradiction in the proposed action.
>
> If you intend to establish a ranking system, you need to describe it in more detail. This should include how the scores would be calculated, what metrics would be used, and which areas are most impacted.
>
> Your impact statement also needs stronger evidence. At present, there is no clear data or reference support for your argument, which makes the statement vague and difficult to justify.

**Rubric criteria that were failed:**

- **1A** — The CtA is specific and clear.
- **1C** — The CtA shows a clear connection with at least one of the SDGs.

---

## 2. Old D1 Content (verbatim)

> **How can the NSW Government prioritise EV fast-charging investment in underserved outer-suburban and regional communities to improve sustainable transport access?**
>
> **Impact Statement**
>
> Public electric vehicle charging infrastructure is gradually becoming a key component of New South Wales' sustainable transportation system. However, if fast-charging stations are primarily concentrated in a few major areas while ignore the residents in outer suburbs and relatively less central areas, this will reduced their confidence and limit the practical options available to them when switching to electric vehicles. This challenge is directly linked to SDG 11.2, which aims to provide safe, affordable, accessible, and sustainable transportation systems for all.
>
> I call on the NSW Department of Climate Change, Energy, the Environment and Water's EV fast-charging grant team to add an "underserved charging access" priority score to the next funding round. This score should be used in open charger-location data to identify LGAs and postcodes with low public plugs per population, limited DC fast-charging access, and weak regional connectivity, then prioritise grant co-funding in those areas instead of keep build in the area where already have one.
>
> By acting on this would make NSW's EV transition more inclusive, reliable and aligned with SDG 11.2.
>
> Dataset Link: https://data.nsw.gov.au/data/dataset/2-ev-charging-locations
>
> This raw CSV provides station-level NSW EV charging data, including charger numbers, plug types, power specifications, LGA, postcode and coordinates. I will compare public plug and DC fast-charger availability across locations to identify underserved communities for SDG 11.2-focused funding priorities.

---

## 3. New (Revised) D1 Content

> **How can the NSW Government prioritise public EV charging investment in under-served, high-population outer-suburban Sydney communities to make the switch to electric vehicles geographically fair?**
>
> **Impact Statement**
>
> Public electric vehicle (EV) charging is becoming essential infrastructure for New South Wales' low-carbon transport transition. But access to it is not distributed fairly. Using two NSW/Commonwealth open datasets — Transport for NSW public EV charging locations and the Australian Bureau of Statistics (ABS) Regional Population 2024-25 — I calculated **public charging plugs per 10,000 residents** for each of the 34 Greater Sydney Local Government Areas (LGAs). The result is a roughly **20-fold gap**: affluent inner suburbs such as Woollahra have about **16.5** plugs per 10,000 residents, while large outer-suburban LGAs are far below the Greater Sydney average of **4.0** — Cumberland has just **0.7**, Fairfield **0.9**, and Canterbury-Bankstown **1.5**. These outer suburbs have some of the largest populations in Sydney (Cumberland ~257,000, Fairfield ~214,000, Canterbury-Bankstown ~390,000) and higher rates of apartment and townhouse living, so residents are the *least* likely to have private off-street charging and the *most* dependent on public chargers — yet they have the least access. If public charging keeps concentrating where it already exists, these residents will face higher practical barriers to switching to EVs, deepening an equity gap in access to clean transport.
>
> This challenge connects most directly to **SDG 11.2**, which calls for "access to safe, affordable, accessible and sustainable transport systems for all." I acknowledge that Target 11.2 is usually read as being about mass-transit modes such as buses and trains, and that a public EV charger is not itself a "public transport service." I argue the link still holds for three reasons. **First, 11.2 is defined by its outcome, not by a fixed list of vehicles:** its measured indicator is the *proportion of the population that has convenient access to sustainable transport*, so the target is about whether people can actually use a clean mode of transport, whatever that mode is. **Second, a public charger is enabling transport infrastructure, not a private appliance:** it is publicly sited, shared by many drivers, and — exactly like a bus stop or train station — it determines whether a sustainable transport *mode* (the EV) is genuinely usable in a given community; where the charging network is absent, the low-emission option is effectively inaccessible to residents who cannot charge at home. **Third, my metric measures precisely the 11.2 concept:** "public charging plugs per 10,000 residents" is a direct proxy for *population with convenient access to sustainable transport*, and the 20-fold gap shows that access is far from "for all." On these grounds the issue sits squarely inside the access-equity purpose of Target 11.2, even though EV charging is not traditional public transport.
>
> The action is reinforced by two supporting SDGs. **SDG 10 (Reduced Inequalities), Target 10.2** — the inclusion of all "irrespective of ... economic or other status" — captures the core of the problem: a purely market-led rollout concentrates charging in wealthier inner suburbs and widens a spatial inequality between communities, which prioritising under-served outer LGAs directly counters. **SDG 7 (Affordable and Clean Energy), Target 7.1** — "universal access to affordable, reliable and modern energy services" — applies because public charging *is* a modern energy service, and equitable siting extends clean-energy access to lower-income outer suburbs. (SDG 13, Climate Action, is a further downstream benefit, since fairer access accelerates EV uptake and emissions reduction, but it is not the primary lens here because the core issue is equity of access rather than aggregate emissions.)
>
> **Call to Action.** I call on the NSW Department of Climate Change, Energy, the Environment and Water's (DCCEEW) EV public-charging grant team to add a single, transparent **"Charging Access Equity Score"** to the next co-funding round, and to prioritise grants to the lowest-scoring, high-population Greater Sydney LGAs.
>
> The score is deliberately built on **one metric**, with a clear target, to avoid ambiguity:
>
> 1. **Metric:** public charging plugs per 10,000 residents for each Greater Sydney LGA, calculated by joining the TfNSW charging dataset (plug counts by LGA) to the ABS Regional Population 2024-25 dataset (estimated resident population by LGA).
> 2. **Scoring:** rank all 34 Greater Sydney LGAs on that metric. An LGA is flagged as "under-served" when it sits **below the Greater Sydney average (4.0 plugs per 10,000 residents)**; the lower the value, the higher its funding priority.
> 3. **Population weighting:** among under-served LGAs, prioritise those with **above-average population**, because that is where the largest number of residents are affected. On today's data the top-priority LGAs are Cumberland (0.7), Fairfield (0.9) and Canterbury-Bankstown (1.5) — all high-population outer suburbs.
> 4. **Allocation:** direct grant co-funding to the highest-priority LGAs first, instead of adding chargers to already well-served inner suburbs.
> 5. **Measurable target:** by 2030, bring every Greater Sydney LGA up to at least the current Greater Sydney average of **4.0 plugs per 10,000 residents**, and cut the gap between the best- and worst-served LGAs from ~20x to no more than 5x. Progress is tracked by re-running the same metric each funding round, so success is objectively verifiable.
>
> This gives the NSW DCCEEW EV public-charging grant team a clear, repeatable, data-driven rule for *where* to fund next and a measurable target for *how much* to close the gap. It removes the ambiguity of the previous "regional vs. postcode" framing by consistently targeting one thing: high-population outer-suburban Greater Sydney LGAs with the lowest per-capita public charging access.
>
> Acting on this would make NSW's EV transition measurably more inclusive and geographically fair, directly advancing SDG 11.2 and supporting SDG 10 and SDG 7 (with SDG 13 as a downstream benefit).
>
> **Target Audience:** the **NSW DCCEEW EV public-charging grant team** — the specific decision-makers who design the eligibility and scoring rules for public EV charging co-funding rounds. (Their outputs are also used by NSW transport and energy planners and local councils, but the grant team is the single body that can act on this CtA directly.)
>
> **Why this audience would act on it** (their incentive):
> - **Higher return on public money.** Each grant dollar delivers the largest marginal gain in access where per-capita provision is lowest; funding a well-served inner suburb from 16 to 17 plugs per 10,000 helps almost no one, while funding Cumberland from 0.7 upward reaches hundreds of thousands of residents who currently have almost none.
> - **It helps them hit existing NSW targets.** The NSW EV Strategy and the state's net-zero-by-2050 commitment both depend on mainstream EV uptake; uptake stalls in exactly the high-population outer suburbs that lack chargers, so closing the gap directly advances the grant team's own program goals.
> - **It is low-cost and low-risk to adopt.** The score reuses two existing open datasets and simply adds one transparent, auditable criterion to a grant program that already exists — no new data collection or new scheme is required.
> - **It is publicly defensible.** A transparent, data-driven equity rule protects the team from criticism that public charging money is concentrated in wealthy areas, and lets every funding decision be justified with a single, verifiable number.
>
> **Dataset Links:**
> - TfNSW public EV charging locations: https://data.nsw.gov.au/data/dataset/electric-vehicle-charging-points
> - ABS Regional Population 2024-25 (by LGA, cat. 3218.0): https://www.abs.gov.au/statistics/people/population/regional-population/latest-release
>
> The TfNSW dataset provides station-level NSW EV charging data (charger numbers, plug types, power specifications, LGA, postcode and coordinates). The ABS dataset provides estimated resident population by LGA. Joining the two lets me compute the per-capita access metric above, identify the most under-served high-population outer-suburban LGAs, and set funding priorities that advance SDG 11.2.

---

## 4. Detailed Change Annotations

Each change below states **where** it was made, **what** changed, and **why** (which feedback point / rubric criterion it addresses).

### Change 1 — Title scope made consistent (fixes 1A contradiction)
- **Where:** Title question.
- **Old:** "...underserved outer-suburban **and regional** communities..."
- **New:** "...under-served, **high-population outer-suburban Sydney** communities..."
- **Why:** The tutor flagged that "regional areas" and "postcodes with low plugs per population" may not be the same areas — a contradiction. Removing "regional" and committing to a single scope (high-population outer-suburban Greater Sydney) makes the CtA internally consistent. This also matches the D2 analysis, which is limited to the 34 Greater Sydney LGAs. **(Rubric 1A)**

### Change 2 — Vague claim replaced with quantified, referenced evidence (fixes "weak evidence")
- **Where:** Impact Statement, paragraph 1.
- **Old:** General statement that stations are "concentrated in a few major areas" with no data.
- **New:** Explicit per-capita figures from D2 — ~20x gap; Woollahra 16.5 vs. Greater Sydney average 4.0; Cumberland 0.7, Fairfield 0.9, Canterbury-Bankstown 1.5, plus their populations — and names the two data sources (TfNSW + ABS).
- **Why:** The tutor said the impact statement lacked "clear data or reference support." The revision now leads with measured numbers and named datasets, so the argument is justified rather than asserted. **(Feedback: evidence; supports 1B — addresses the underlying problem.)**

### Change 3 — SDG 11.2 kept as primary but explicitly defended; SDG 10 + 7 added as support, SDG 13 demoted (fixes 1C)
- **Where:** Impact Statement, new paragraphs 2-3.
- **Old:** "This challenge is directly linked to SDG 11.2, which aims to provide safe, affordable, accessible, and sustainable transportation systems for all." (asserted only)
- **New:** Keeps SDG 11.2 as the primary target and **openly concedes** that 11.2 is usually read as mass transit and that a charger is not a "public transport service," then justifies the link with three explicit arguments:
  1. **11.2 is defined by outcome, not by vehicle type** — its official indicator is the *proportion of the population with convenient access to sustainable transport*, so what matters is whether people can use a clean mode.
  2. **A public charger is enabling transport infrastructure, not a private appliance** — publicly sited and shared, it makes the EV mode usable in a community, exactly like a bus stop makes bus travel usable.
  3. **The metric measures the 11.2 concept directly** — "plugs per 10,000 residents" is a proxy for "population with convenient access," and the 20x gap shows access is not "for all."
  
  It then reframes the support SDGs to match the *equity* core: **SDG 10 / Target 10.2** (reduced inequalities — spatial inequality between communities) and **SDG 7 / Target 7.1** (universal access to modern energy services — charging is an energy service), with **SDG 13 (Climate Action) demoted** to a downstream benefit rather than a primary lens.
- **Why:** The tutor said SDG 11.2 "mainly relates to public transportation" and asked me to either explain the link clearly or pick another SDG. This directly answers the objection by naming it and rebutting it with the indicator definition, and strengthens the equity argument with SDG 10 (the purest "inequality" SDG) and SDG 7.1 (charging as an energy service). SDG 13 is kept only as a secondary benefit because the project's core is equity of access, not aggregate emissions. **(Rubric 1C)**

### Change 4 — CtA made specific with a fully described scoring system (fixes 1A)
- **Where:** Call to Action paragraph + numbered scoring list.
- **Old:** Score "should be used in open charger-location data to identify LGAs and postcodes with low public plugs per population, limited DC fast-charging access, and weak regional connectivity" — three different, unweighted, undefined signals.
- **New:** A single named metric ("Charging Access Equity Score" = public charging plugs per 10,000 residents), with four explicit steps: (1) metric definition and data join, (2) scoring/threshold against the 4.0 average, (3) population weighting, (4) allocation rule. Names the current top-priority LGAs.
- **Why:** The tutor asked for detail on "how the scores would be calculated, what metrics would be used, and which areas are most impacted," and for a clearer, more consistent CtA. Collapsing three ambiguous signals into one measurable metric removes the contradiction and makes the action specific and repeatable. **(Rubric 1A; also 1D — actionable and appropriate for the context.)**

### Change 5 — Removed the "regional connectivity" and "DC fast-charging" mixed signals (fixes 1A contradiction)
- **Where:** Call to Action.
- **Old:** Mixed "low public plugs per population," "limited DC fast-charging access," and "weak regional connectivity" in one instruction.
- **New:** Uses only per-capita public charging access; "DC fast-charging" and "regional connectivity" are dropped so a single criterion decides priority.
- **Why:** These signals can point to different areas (a remote highway town can be "regionally connected" yet have almost no plugs per resident; a dense outer suburb can rank badly on per-capita but fine on connectivity). Keeping one metric resolves the contradiction the tutor identified. **(Rubric 1A)**

### Change 6 — Target Audience stated explicitly and matched to the CtA (strengthens 2A/2C)
- **Where:** New "Target Audience" line.
- **Old:** The audience (DCCEEW grant team) was only implied inside the CtA.
- **New:** Names the DCCEEW EV public-charging grant team (and NSW transport/energy planners and councils) as the decision-makers who control funding, and states their incentive (fairer, defensible, evidence-based allocation of public money).
- **Why:** Makes the TA explicit and clearly the right body to perform the CtA, and gives them a concrete incentive to act — consistent with D2's target audience. **(Rubric 2A — appropriate TA; 2C — clear incentive for the TA.)**

### Change 7 — Second dataset added (enables the per-capita metric)
- **Where:** Dataset Links + description.
- **Old:** Only the raw TfNSW charging CSV was cited; the CtA implied "per population" with no population source.
- **New:** Adds the ABS Regional Population 2024-25 dataset and explains that joining it to the charging data is what produces the per-capita metric.
- **Why:** "Plugs per population" is impossible to compute without population data. Adding ABS makes the metric reproducible and the evidence verifiable, and aligns D1 with the two-dataset method used in D2. **(Feedback: evidence.)**

### Change 8 — Grammar and clarity clean-up
- **Where:** Throughout.
- **Old:** e.g. "while ignore the residents," "this will reduced their confidence," "instead of keep build in the area where already have one," "By acting on this would make..."
- **New:** Corrected to standard academic English (e.g. "while ignoring residents," "this reduces their confidence," "instead of adding chargers to already well-served inner suburbs," "Acting on this would make...").
- **Why:** The original contained grammatical errors that reduced clarity; clear writing supports the "specific and clear" requirement. **(Rubric 1A — clarity.)**

### Change 9 — Added a measurable target (makes the CtA "measurable")
- **Where:** Call to Action, new step 5 of the scoring list.
- **Old:** The CtA said *where* to prioritise but gave no numeric goal or deadline, so "success" was undefined.
- **New:** Adds a concrete, verifiable target — by 2030 raise every Greater Sydney LGA to at least 4.0 plugs per 10,000 residents and cut the best-vs-worst gap from ~20x to no more than 5x, tracked by re-running the same metric each round.
- **Why:** The two "first-time-pass" example D1s were still told by the tutor to make the CtA "more specific and measurable" and to state the "expected improvement." Adding a target and deadline pre-empts that exact comment and turns the action into something whose success can be objectively checked. **(Rubric 1A — specific and measurable; supports 1D.)**

### Change 10 — Strengthened and itemised the Target Audience's incentive (strengthens 2C)
- **Where:** Target Audience section (expanded from one sentence to a named audience + four bullet incentives).
- **Old:** A single sentence: the incentive was "a fairer, more defensible, evidence-based allocation of public money."
- **New:** Names one primary audience (the DCCEEW EV public-charging grant team) and gives four concrete reasons they would spend the money: higher return per dollar, helps meet the NSW EV Strategy / net-zero targets, low-cost/low-risk to adopt (reuses existing data + existing grant program), and publicly defensible.
- **Why:** Both passing example D1s were explicitly told to "explain more clearly why the authority would be willing to do this, since they would need to spend a lot of funding." This makes the TA's motivation concrete and specific rather than generic, and keeps a single, consistent primary audience throughout. **(Rubric 2A — appropriate TA; 2C — clear, strong incentive.)**

---

## 5. Rubric Coverage Summary

| Criterion | Requirement | How the revised D1 meets it |
|-----------|-------------|-----------------------------|
| **1A** | CtA is specific and clear (and measurable) | Single named metric + 5-step scoring rule with a 2030 numeric target; one consistent scope (outer-suburban Greater Sydney); grammar fixed (Changes 1, 4, 5, 8, 9) |
| **1B** | CtA addresses the underlying problem | Identifies the real problem — outer-suburban residents depend most on public charging yet have least access — with data (Change 2) |
| **1C** | CtA connects to at least one SDG | SDG 11.2 kept as primary and explicitly defended against the "mass-transit only" objection via the indicator definition; SDG 10.2 and 7.1 added as support, SDG 13 demoted to downstream benefit (Change 3) |
| **1D** | CtA is actionable and context-appropriate | Grant team can literally add the Equity Score as a funding criterion (Change 4) |
| **2A** | Appropriate TA chosen | One consistent primary TA — the DCCEEW EV public-charging grant team — which controls the funding rules the CtA targets (Changes 6, 10) |
| **2C** | Clear incentive for the TA | Four concrete incentives: higher return per dollar, meets NSW EV/net-zero targets, low-cost/low-risk to adopt, publicly defensible (Changes 6, 10) |
| **6A** | Topic not about real-estate affordability | Topic is EV charging equity / sustainable transport access — unrelated to housing affordability |

**Consistency check:** every section uses the same three anchors — (1) **scope:** high-population outer-suburban Greater Sydney LGAs with the lowest per-capita public charging access; (2) **metric:** public charging plugs per 10,000 residents (benchmarked to the 4.0 average); (3) **target audience:** the NSW DCCEEW EV public-charging grant team. These three are worded identically across the title, impact statement, SDG argument, call to action, target-audience section, and dataset description, and they match the D2 analysis and its target audience. There is no longer any "regional vs. postcode" or multi-signal contradiction.

---

## 6. Third Revision (v3 — concise, ≤250-word body)

The v2 revision above is correct and complete, but it runs to roughly 950 words — far longer than the post format the tutor and the approved example posts actually use. This third revision keeps every winning idea from v2 and compresses the **submittable post** to a **≤250-word body** that mirrors the structure of a passing example (Topic + SDG → brief summary → who is impacted → data evidence → who can help + CtA → clear incentive). Three substantive upgrades are made at the same time:

1. **The scoring is made genuinely *useful*, not just *described*.** v2 defined the score correctly but never said, in one line, *why a score beats the status quo*. v3 states the payoff directly: ranking every LGA on one number turns "where should we fund next?" from a subjective, lobby-able decision into an objective, auditable, repeatable rule.
2. **The CtA is tied to the impact statement so the two halves solve the problem *together*.** The impact statement now *measures* the gap on one metric (plugs per 10,000 residents); the CtA *acts on that same metric* to close it, with a numeric 2030 target. The reader can trace problem → action → measurable outcome in a single metric, with no scope drift.
3. **The missing EV uptake numbers are added as supporting evidence.** v2 had charging-supply data but no vehicle-demand data. v3 adds NSW EV **ownership** (52,572 registered EVs at Jan 2024) and **annual purchases** (~28,200 new EVs in 2024, 9.5% of new-car sales), which prove demand is real and accelerating — so the access gap is an active, growing problem, not a hypothetical one.

### 6.1 Final v3 post (this is the text to submit)

> **Making public EV charging geographically fair across Greater Sydney to advance SDG 11.2 (sustainable transport for all)**
>
> Public electric-vehicle (EV) charging is becoming essential infrastructure for New South Wales' low-carbon transport transition, which SDG 11.2 frames as "access to safe, affordable and sustainable transport for all." Uptake is real and accelerating: NSW held **52,572 registered EVs** by January 2024 — **7.5× the 2021 figure** — and EVs reached **9.5% of new-car sales** (about **28,200 vehicles**) in 2024. But charging access is deeply unequal. Joining Transport for NSW charging data with ABS 2024-25 population, **public plugs per 10,000 residents vary roughly 20-fold** across the 34 Greater Sydney LGAs: Woollahra has 16.5 versus a 4.0 average, while high-population outer suburbs sit far below — Cumberland 0.7, Fairfield 0.9, Canterbury-Bankstown 1.5. These apartment-heavy communities are least able to charge at home, yet least served.
>
> I call on the **NSW DCCEEW EV public-charging grant team** to add a transparent **"Charging Access Equity Score"** — public plugs per 10,000 residents — to the next co-funding round, prioritising high-population LGAs below the 4.0 average, with a **2030 target of every LGA reaching 4.0**. Ranking on this single metric removes the old ambiguity and makes every funding decision auditable and repeatable.
>
> They would act because it delivers the largest access gain per dollar, advances the NSW EV Strategy and net-zero goals, and is publicly defensible — reusing existing open data at near-zero cost.
>
> **Dataset & evidence links:**
> - TfNSW public EV charging locations: https://data.nsw.gov.au/data/dataset/electric-vehicle-charging-points
> - ABS Regional Population 2024-25 (by LGA, cat. 3218.0): https://www.abs.gov.au/statistics/people/population/regional-population/latest-release
> - NSW State of Environment 2024 — EV registrations (52,572; 7.5× 2021): https://www.soe.epa.nsw.gov.au/
> - Electric Vehicle Council, *State of EVs 2024* — NSW 9.5% new-car sales share (VFACTS): https://electricvehiclecouncil.com.au/

**Body word count: ~210 words** (counting the topic statement through the incentive sentence; the dataset/evidence links and title label are excluded, as in the approved example format). This leaves a safe margin under the 250-word cap.

### 6.2 v3 Change Annotations

#### v3-Change A — Compressed the whole post to a ≤250-word body (fixes length/format)
- **Where:** Entire post.
- **What:** Cut v2's ~950 words to a ~210-word body while keeping all three anchors (scope, metric, target audience) and every rubric-relevant claim.
- **How the length was recovered:** the long three-part SDG 11.2 defence and the four-bullet incentive list from v2 are compressed to one clause each; the full five-step scoring method is folded into a single CtA sentence (metric + threshold + 2030 target). The detailed versions are retained here in the annotations and in the demo script, so nothing is lost — it simply moves out of the counted body. **(Format / requirement 4.)**

#### v3-Change B — Made the scoring *useful*, not merely *defined* (requirement 1)
- **Where:** CtA, final sentence: "Ranking on this single metric removes the old ambiguity and makes every funding decision auditable and repeatable."
- **Old (v2):** listed *how* to compute the score (5 steps) but never stated *why* a score is better than current practice.
- **New (v3):** states the concrete benefit — one ranked number converts an ambiguous, contestable "which area next?" judgement into an objective, auditable, repeatable rule that can be re-run every funding round. This is the persuasive "so what" of the scoring.
- **Why it is persuasive:** it answers the grant team's real question ("why change how we decide?") with a governance benefit they value — defensibility and repeatability — not just a formula. **(Rubric 1A / 1D.)**

#### v3-Change C — Tied the CtA to the impact statement via one shared metric (requirement 2)
- **Where:** Impact statement + CtA.
- **What:** Both halves now pivot on the *same* metric — **public plugs per 10,000 residents**. The impact statement uses it to *measure* the 20-fold gap; the CtA uses it to *act* (prioritise below-4.0 LGAs) and to *set the target* (every LGA ≥ 4.0 by 2030).
- **Why:** this makes the problem and the action a single closed loop — the reader can trace *problem → action → measurable outcome* on one number, so the CtA visibly "solves" exactly the problem the impact statement raises, with no scope drift. **(Rubric 1A/1B — the CtA and impact statement solve the problem together.)**

#### v3-Change D — Added NSW EV ownership and annual-purchase evidence (requirement 3)
- **Where:** Impact statement, sentence 2.
- **What:** Added two demand-side figures the tutor's feedback implied were missing: **ownership** — 52,572 registered EVs in NSW at January 2024, 7.5× the 6,160 recorded in 2021 (NSW State of Environment 2024, from BITRE registration data); and **annual purchases** — ~28,200 new EVs bought in NSW in 2024, a 9.5% share of new-car sales (Electric Vehicle Council, *State of EVs 2024*, using VFACTS).
- **Note on "hybrid":** these headline figures follow the standard registration/sales definition of "EV" (battery-electric; some series also fold in plug-in hybrids). Rather than mix inconsistent hybrid classifications, v3 cites the clean EV registration and EV-sales-share numbers and labels them as such.
- **Why:** the v2 post proved charging *supply* is unequal but never showed EV *demand*. These numbers prove uptake is real and accelerating, so the access gap is an active, worsening problem for a growing population of drivers — which raises the stakes of the CtA. **(Feedback: stronger evidence; supports 1B.)**

#### v3-Change E — Kept SDG 11.2 primary but in one compressed line (consistency with v2)
- **Where:** Topic statement + summary sentence.
- **What:** SDG 11.2 remains the primary SDG, now expressed in a single clause ("access to safe, affordable and sustainable transport for all") rather than the full three-argument defence.
- **Why:** the full defence is preserved in Section 3 (v2) and the demo script for when the tutor asks; the body only needs to name the link clearly to satisfy 1C within the word budget. **(Rubric 1C.)**

### 6.3 v3 Requirement Coverage

| Requirement | Where addressed in v3 |
|-------------|-----------------------|
| 1. Scoring is *useful* & persuasive | CtA closing sentence + annotation B (objective, auditable, repeatable rule vs. subjective status quo) |
| 2. Clearer CtA that solves the problem *with* the impact statement | Shared single metric (plugs per 10,000) links measure → action → 2030 target (annotation C) |
| 3. Missing EV purchase & ownership numbers added | Impact statement sentence 2: 52,572 registered / 7.5×; ~28,200 sold / 9.5% (annotation D) |
| 4. ≤250 English words | ~210-word body (Section 6.1 word-count note) |

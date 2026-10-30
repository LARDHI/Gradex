# Gradex V2: Phase 01 Idea (Approved and closed)

Status: **CLOSED. Approved by the owner on 2026-10-30.** The owner approved the completed Phase 01 deliverables and authorized closure. Phase 02 has **not** started and begins only on the owner's explicit authorization.
Dates: V1 inspection and evidence gathering 2026-10-29; closure 2026-10-30. Baseline: Gradex V1 (`LARDHI/Gradex`, tag `v1.0.0`, 301 tests passing when re-run on 2026-10-29).

## 0. How to read this document

**Evidence labels** used in tables:

| Label | Meaning |
|---|---|
| **[OD]** | Confirmed owner decision |
| **[AP]** | Proposed by me, now approved by the owner |
| **[VF]** | Verified V1 fact (I inspected it) |
| **[EO]** | Evidence-based observation (sourced, limited sample) |
| **[UA]** | Unverified assumption (registered in section 13) |
| **[DD]** | Dependency legitimately assigned to a later phase (section 11) |

**Release gates versus longer-term goals.** Criteria **R1 to R8** are *release gates*: Gradex V2 may not be published until all of them are met. Goals **V1 to V3** are *longer-term validation goals*: they are measured and reported, and never block publication. This distinction holds throughout the document.

**Revision history.** Draft 1 (first proposal) became Draft 2 (owner corrections on V1 custom grading, differentiation, A3, criteria split, dependencies, cross-device access). The final review copy applied the owner's final clarifications and a full consistency review (section 14). **This closed version differs from the final review copy only in:** the status lines, the label of D17, the new decision D21, the closure checklist (section 12), the closure record (section 15) and one added line in section 14. All other content, including every limitation, dependency and assumption, is unchanged.

## 1. Sources of owner input

| Source | Date | Content |
|---|---|---|
| Phase 01 answers | 2026-10-29 | Targeting, users, priority, mandatory workflow rule |
| Review of Draft 1 | 2026-10-29 | V1 custom grading correction, differentiation, success criteria, dependency judgment, cross-device access |
| Final clarifications on Draft 2 | 2026-10-29 | Product name, R5 as release gate, R6, R7, R2, dependency placement, change control |
| Phase 01 approval | 2026-10-30 | D17 glossary approved as written; completed Phase 01 approved; closure authorized; Phase 02 not to start automatically |

The authoritative list of decisions is the decision record in section 10.

## 2. Workflow rule and change control

### 2.1 Phase closure rule [OD, D05]
Each phase is fully completed and formally closed before the next begins: required work done; relevant questions, ambiguities and inconsistencies resolved; deliverables reviewed against earlier decisions; decisions documented in the project docs; explicit owner approval obtained. Nothing is silently deferred. If something belongs to a later phase, the dependency and the reason are documented.

### 2.2 Change control [OD, D20]
Later phases implement and validate the approved requirements. They may add detail, but may not redefine an approved decision without the owner's explicit approval. If new evidence conflicts with an approved decision, the conflict is stated and a correction is proposed to the owner. Specifically:

- Phase 03 determines scope and implementation sequencing without contradicting the approved account requirement (D06).
- Phase 05 determines technology and architecture from approved requirements.
- Any assumption that affects an approved success criterion is documented (section 13) and resolved at the stated phase.

## 3. Glossary [AP, D17: approved as written]

| Term | Meaning in V2 documents |
|---|---|
| Gradex | The official product name (V2 and onward). |
| GPA Tracker | The name associated with V1. `gpa_tracker` remains the Python package name until naming and restructuring work (Phase 08). |
| University grading policy | The real-world rules a university publishes. |
| Grading system | Gradex's representation of such a policy: the complete set of rules that determines GPA. Either **built-in** (one of four) or **custom** (student-defined). |
| Grading table | The letter-to-points part of a grading system (V1 term, unchanged). |
| Letter style | V1's "system" (Plus Only or Plus/Minus). Renamed to avoid the clash with "grading system". |
| Actual / hypothetical | Recorded academic results versus what-if or planning scenarios. |

## 4. Verified facts about V1 (inspected 2026-10-29)

### 4.1 General state [VF]
- Tag `v1.0.0` exists on the `main` head. 301 tests pass in a scratch copy (Python 3.13); V1's own report records 301 on Windows with Python 3.14.
- Calculation, model, storage, prediction and formatting modules contain no `print` or `input` calls. All arithmetic uses `Decimal`.
- Gaps: no CI configuration; `docs/SPEC.md` required by the P10 brief is absent; W15 is an owner-accepted gap.
- Not inspected: briefs P0 to P9, `cli.py` in full, test code line by line.

### 4.2 What V1's custom grading supports [VF] (verified in `grading.py`)
A custom grading table of 1 to 20 entries. Each letter is 1 to 3 characters, A to Z only, with an optional trailing `+` or `-` after one or two letters. Points range 0.00 to 5.00 with at most two decimals. Letters are unique. `F` is required. The table is entered at first run or from the profile screen while the profile has no courses.

### 4.3 Verified limitations of V1's customization [VF]
I confirmed each by reading the code and, for letters and points, by running the validator on a scratch copy.

| ID | Limitation | Evidence |
|---|---|---|
| L1 | Points cannot exceed 5.00, so scales such as 10-point or 100-point cannot be expressed. | `5.01` and `10` rejected |
| L2 | `F` is the only failing grade, hard-coded. A failing code with another name (`E`, `U`, `DN`) is treated as passing. | `is_passing` returns `letter != "F"`; `DN`, `E` accepted as letters |
| L3 | No non-GPA codes. Every completed course adds its credits to the GPA denominator, so `W`, `P`, `I`, `AU` cannot be excluded from GPA. | `semester_result` adds `graded_credits` for every completed course; `W`, `WP`, `AU` accepted as letters |
| L4 | Letters cannot contain `/` or digits (for example `S/U`, `A1`). | `S/U`, `A1` rejected |
| L5 | Retakes are fixed: every attempt counts. No replace or average option. | Spec section 3, test W14 |
| L6 | Rounding is fixed at 2 decimals, half up. | `round_half_up` |
| L7 | Credits are whole numbers 1 to 9. | `Course.__post_init__` |
| L8 | One grading table per profile, locked while any course exists. Different tables per semester are impossible. | `Student.set_table` |

The V1 README states the retake limit (L5) and the fixed rounding (L6). I found no warning in the README about L1 to L4.

### 4.4 Unverified assumptions about need [UA]
- That students need scales above 5.00, other failing codes, non-GPA codes or configurable retakes and rounding. Only one real policy has been examined (section 4.5), and one policy is not representative (AS-04).
- That the other three built-in tables match any university (AS-05).

### 4.5 Evidence on the built-in tables [EO] and [VF]
- **[OD, from V1]** The V1 owner decision (2026-10-29) accepted the built-in values as an unverified baseline.
- **[EO]** V1's `4.0-plus-only` values (A+ 4.00, A 3.75, B+ 3.50, B 3.00, C+ 2.50, C 2.00, D+ 1.50, D 1.00, F 0.00) are identical to the Alfaisal University catalogue table (Fall 2025-26) that I read. I do not know whether that is a coincidence or the source. I could not match the other three tables to any source.
- **[EO]** The same catalogue lists a failing code `DN` at 0.00 points, and non-GPA codes `W, WP, P, NP, AU, I, CR, R, CC, S/U, NC`. It does not say how repeated courses are handled or how GPA is rounded. It contradicts itself on minus grades. So even a real, published policy leaves some rules unspecified, and V1 could not represent its failing or non-GPA codes (L2, L3, L4).

Source: [Alfaisal grading system (PDF)](https://catalog.alfaisal.edu/sites/default/files/pdf/academic_page/grading-system.pdf?1656613152).

## 5. Product vision [OD, D09]

Gradex helps a university student from any university understand where they stand academically and plan what to do next. It does this with grading rules the student can see and configure, a strict separation of real results from hypothetical scenarios, and target-GPA planning that explains what is and is not achievable.

## 6. Problem statement [OD, D10: approved with the correction below]

V1 answers "what is my GPA, and what happens if I get these grades?" and already lets a student enter a custom grading table. Its verified limits are:
- It runs on one computer, through a command-line menu, with one profile per file, so records are not available across devices.
- It cannot answer "what do I need to reach my target?".
- Its customization covers letters and points only (section 4.3). A student whose university uses non-GPA codes, a failing code other than `F`, or letters such as `S/U` either gets GPA numbers that differ from their university's (for example `W` counted in the denominator) or cannot enter those grades. Scales above 5.00 cannot be entered. Retake treatment and rounding are fixed, and V1 documents both limits.

Whether students need these capabilities is unverified (section 4.4) and is settled by requirements work in Phase 02.

## 7. Target users and needs [OD, D11]

Gradex is intended for university students worldwide, regardless of their university or country.

- **Primary:** university students anywhere, tracking their own GPA across semesters, whether or not their grading system matches a built-in one.
- **Secondary (portfolio):** a reviewer who needs to see the product working without exposing real data.
- **Needs:** trustworthy numbers; a grading system matching their own university's policy, with assumptions visible; an honest answer on whether a target is reachable; records available across devices; history that persists.

## 8. Value proposition and differentiation [AP, D12: direction approved]

### 8.1 Evidence (small sample, checked 2026-10-29) [EO]

| Capability | Evidence | Source |
|---|---|---|
| Replace or average policy for repeated courses | Yes, selectable | [gpacalculator.net repeat calculator](https://gpacalculator.net/course-repeat-gpa-calculator) |
| Custom grading scales, retake rule, semester history with trend charts, no account (device-only data) | Yes, per the app's own page. Only 2 ratings, so no adoption evidence | [GPA Calculator Tracker (iOS)](https://apps.apple.com/app/id6785322301) |
| Customizable grade systems with 8 Turkish university presets | Yes. Retakes and target planning not mentioned. Work in progress | [Gradeful](https://github.com/beyenilmez/gradeful) |
| Required average for a target, with impossible-target flag | Yes, a single average only. 4.0 and 5.0 scales only | [Target GPA calculator](https://calculators-ng.pages.dev/education/target-gpa-calculator) |
| Same, no login | Yes (council report, not re-checked by me) | [gpacalculator.net target calculator](https://gpacalculator.net/target-gpa-calculator) |

About eight tools were examined, mostly from page descriptions, not hands-on use.

### 8.2 Classification

| Category | Capabilities | Basis |
|---|---|---|
| **Genuinely differentiated** | None established. | The evidence does not support any claim of uniqueness. |
| **Valuable but not differentiating** | GPA and CGPA calculation; custom grading tables; retake handling; semester history; required-average target planning with an impossible-target flag; what-if prediction. | All found in other tools, or already in V1. |
| **Candidate differentiators, research required [UA]** | (a) Per-course feasibility with explanations for a target; (b) a wider set of configurable policy rules in one place (non-GPA codes, failing codes, retakes, rounding, scales); (c) strict actual-versus-hypothetical separation; (d) cross-device records with tested per-user isolation. | None of (a) to (c) appeared in the sample. That is a statement about the sample, not the market. (d) is an owner goal and a portfolio signal, but competitor support and demand are unchecked. |

The "candidate" status is provisional by design. Phase 02 research may move an item between categories without reopening this decision.

### 8.3 Claims rule [OD, D12]
No Gradex document, README or portfolio text will claim uniqueness or being first in the market without sufficient evidence. It may claim that Gradex combines named capabilities. A structured competitor comparison (defined sample, defined criteria) is a Phase 02 task, completed before the Phase 03 cut line (AS-09).

## 9. Success criteria [AP, D14: approved with the clarifications below]

Both tracks count equally (D04). Nothing is a release gate merely because it is measurable.

### 9.1 Release gates (all must be met before Gradex V2 is published)

| ID | Criterion |
|---|---|
| R1 | The calculation and planning engine is tested in isolation, with table-driven tests covering every worked example of the built-in systems and every configurable policy option. |
| R2 | **Policy conformance suite** (replaces the former "two students with uncovered policies" gate; criterion in 9.3). |
| R3 | Tests demonstrate that one user cannot read or change another user's data (accounts are part of V2, D06). |
| R4 | Public HTTPS demo using **synthetic data only**; README covering setup, architecture, limits and deployment; documented release process. |
| R5 | **All 12 phases are completed, and every phase is formally documented, reviewed and approved by the owner, before Gradex V2 is published (D19).** This is a mandatory release requirement, not a documentation goal or an optional portfolio objective. V2 must not be published, or treated as ready for release, until R5 holds, in addition to R1 to R4 and R6 to R8. The decision record is part of this requirement. |
| R6 | **Usability:** the core workflow is completed in **10 minutes or less** in each of at least 3 observed student sessions. Core workflow: from an empty profile, enter one semester of up to 6 courses, see the semester GPA, and receive a target-GPA planning result. Any overrun is recorded and its cause fixed before release. **The six-course limit is an assumption (AS-01) to be validated in Phase 02. The test procedure is provisional until the entry of prior academic standing is resolved (AS-02). The ten-minute target is fixed and will not be changed without the owner's approval (AS-03).** |
| R7 | **Early validation:** at least 5 real students test a pre-release build with their own data and give feedback before release. The testing process must include consent and privacy safeguards (expected minimum, finalized in Phase 02: informed consent before use; only the data the test needs; deletion on request). Real student data must never appear in the public demo (R4). |
| R8 | **Cross-device access:** an end-to-end acceptance test shows the same records available from two devices through one account. |

### 9.2 Longer-term validation goals (reported in the Phase 12 completion report; **not** release gates)

| ID | Goal | Why not a gate |
|---|---|---|
| V1 | At least 3 of the 5 early users return within two weeks. | Depends on other people's behavior and elapsed time. A gate could block release indefinitely. It is reported honestly even if the window is unfinished. |
| V2 | At least 2 students with policies not covered by a built-in system configure a custom system and confirm the results against their own verified calculation. | Recruiting is difficult, the sample is tiny and self-reported correctness is weak. Approved as a longer-term goal. |
| V3 | Early testers cover at least 2 different grading systems where such students can be found. | Availability, not product quality. If unmet, the limitation is stated. |

### 9.3 Criterion for R2: policy conformance suite [AP, D15]

What must be proven is that Gradex calculates correctly under a given policy. Independent calculation checks that more rigorously and repeatably than two volunteers. Real students remain valuable for judging whether configuring a custom system is understandable, which is why V2 is kept as a longer-term goal.

1. Expected results come from an independent source: university-published worked examples or transcripts where available, otherwise hand or spreadsheet calculations made without Gradex code and reviewed by the owner.
2. Each profile has at least 3 scenarios, including at least one edge case (for example a retake, a non-GPA code, or a rounding boundary).
3. Gradex must match exactly at full precision and at displayed rounding.
4. **Option coverage and interaction coverage.** Every configurable option defined in Phase 02 appears in at least one profile. In addition, for every pair of options whose rules can affect the same calculation, at least one scenario exercises both together, with an independently derived expected result. Phase 02 identifies the important interactions and may require higher-order combinations where rules apply in sequence. Illustrative examples only, not final: retake treatment together with a non-GPA code; retake treatment together with rounding at a boundary; a failing code other than `F` together with completed-credit counting; a non-GPA code together with target-GPA feasibility.
5. At least 4 profiles (my initial figure, AS-06). Phase 02 may raise it, for example because interaction coverage needs more, but not lower it.
6. Profiles may be modelled on published university policies. Where a policy leaves a rule unspecified (section 4.5), the profile states its assumption explicitly (AS-10).

### 9.4 Release rule
Gradex V2 is published only when R1 to R8 are all satisfied. V1 to V3 never gate publication, but their results are reported in the Phase 12 completion report.

## 10. Decision record

Legend: **[OD]** confirmed owner decision. **[AP]** proposed by me and approved by the owner.

| ID | Decision | Label | Status |
|---|---|---|---|
| D01 | No target university or country | [OD] | Confirmed |
| D02 | Four built-in grading systems plus student-defined custom systems | [OD] | Confirmed |
| D03 | Custom systems reflect the student's actual policy via explicit, configurable rules; exact requirements set in later phases | [OD] | Confirmed |
| D04 | Portfolio value and adoption equally important | [OD] | Confirmed |
| D05 | Strict phase-closure rule (2.1), binding for all 12 phases | [OD] | Confirmed |
| D06 | Accounts are part of V2, implemented in the second implementation phase; not removable without explicit owner approval | [OD] | Confirmed (reconfirmed) |
| D07 | AI is out of V2 scope | [OD] | Confirmed |
| D08 | V1 stays a stable baseline | [OD] | Confirmed |
| D09 | Vision (section 5) | [OD] | Approved |
| D10 | Problem statement (section 6), with the correction that V1 already supports custom grading tables but has the limits in 4.3 | [OD] | Approved with correction |
| D11 | Target users: students worldwide | [OD] | Approved |
| D12 | Differentiation direction, classification (8.2) and claims rule (8.3): no uniqueness or first-in-market claims without evidence | [AP] | Direction approved |
| D13 | Cross-device access is a V2 goal; no technology implied | [OD] | Confirmed |
| D14 | Success criteria R1 to R8 and V1 to V3 with the thresholds in section 9 | [AP] | Approved with clarifications (R5, R6, R7, R2) |
| D15 | Policy conformance suite replaces the two-student gate; real-student validation stays a longer-term goal; suite must cover interactions | [AP] | Approved |
| D16 | Product name is **Gradex**. "GPA Tracker" stays V1's name; `gpa_tracker` stays the package name until naming and restructuring work | [OD] | Confirmed |
| D17 | Glossary (section 3): definitions of "grading system", "grading table" and "letter style" | [AP] | **Approved as written (2026-10-30)** |
| D18 | Phase placement of deferred items (section 11), with their reasoning | [AP] | Approved in principle (2026-10-29); included in the completed Phase 01 approved on 2026-10-30 |
| D19 | Completion and owner approval of all 12 phases is a mandatory condition for publishing V2 (R5) | [OD] | Confirmed |
| D20 | Later phases implement and validate approved requirements and do not redefine them without owner approval (2.2) | [OD] | Confirmed |
| D21 | Phase 01 is formally closed. Phase 02 does not start automatically; it begins only on the owner's explicit authorization | [OD] | Confirmed (2026-10-30) |

Rejected alternatives: targeting one first university; treating target planning alone as the differentiator; making real-student custom-policy validation a release gate.

## 11. Dependencies legitimately assigned to later phases [DD]

For every item, deferral does not leave Phase 01 incomplete, because Phase 01 produces product-level decisions (vision, problem, users, differentiation direction, success criteria). None of the items below changes those. The reasoning and the separation of requirements, scope, data modelling, algorithms, architecture, planning and testing are retained.

| # | Item | Assigned phase(s) | Why appropriate | Depends on / blocks | Remaining uncertainty |
|---|---|---|---|---|---|
| 1 | Custom grading policy requirements | **Split:** Phase 02 defines which policy dimensions exist and gathers real policies, including important interactions between rules. Phase 03 sets must-have versus later. Phase 06 models them. Phase 07 specifies the rules. Phase 11 runs R2. | Requirements need research on real policies. Modelling and algorithms must follow approved requirements. Phase 01 supplies the principle (D03) and the verified V1 baseline (4.3). | Blocks Phase 06, 07 and R2 | One real policy examined (AS-04). How many policies make a sample representative is open. |
| 2 | Intended behavior and accuracy of the four built-in systems | **Phase 02, closed before any later decision depends on it.** Phase 02 defines the behavior V2 promises for them and either verifies the table values against named sources within Phase 02, or explicitly labels them unverified reference presets with a documented disclaimer and a documented consequence for R1 (tests assert the stated values, not their real-world accuracy). No Phase 05, 06 or 07 decision may rely on table values until this is settled. | This is a requirement: what the product promises. It must precede data modelling and algorithms, which would otherwise rest on an unverified assumption. | Blocks R1 worked examples | The V1 decision accepted unverified values. This revisits it for V2. Section 4.5 shows at least one table may come from one university (AS-05). Verification needs sources for three tables I could not match. |
| 3 | Accounts, persistence, hosting, stack | **Split:** Phase 02 states the requirements (cross-device access, per-user isolation, durability and recovery expectations, privacy, data deletion and export, HTTPS, budget and hosting constraints, which need owner input). Phase 03 sequences accounts in the second implementation phase, consistent with D06, and decides how pre-account testers are handled. Phase 05 chooses stack, storage, authentication and hosting from approved requirements. Phase 06 models ownership. Phase 09 plans it. | Requirements must not wait for the architecture phase, but technology choices must follow approved requirements. | Blocks R3, R4, R8 | Pre-account early testers (R7) will not exercise cross-device persistence (AS-08). The architecture must allow adding accounts later without avoidable rewrite (Phase 05 constraint). |
| 4 | Naming conventions | Product name is settled (D16). Package, module, repository and document naming conventions in Phase 08. | Code and file conventions depend on structure decisions. | Domain and branding in Phase 05 and 09 | The V1 verification report cites an old repository URL (`Lardhi-`). Left as is, since V1 is a baseline. Noted for documentation clean-up in Phase 12. |
| 5 | How prior academic standing is entered (full history or a summary of CGPA and credits) | Phase 02 requirement; Phase 04 user stories | It determines what the R6 scenario means in practice and how quickly a target answer is reachable. | Finalizes the R6 test procedure | AS-02 and AS-03. If summary entry is not allowed, R6's 10-minute target may need re-examination, which would be raised to the owner as a proposal, not changed silently. |
| 6 | Competitor research for the candidate differentiators | Phase 02, before the Phase 03 cut line | The claims rule (8.3) limits what is said until it is done. A structured comparison needs the requirement list first. | Informs scope choices | AS-09. Sample and criteria still to be fixed. |
| 7 | Definition of target planning (required average versus per-course feasibility) | Phase 02 requirements; Phase 07 algorithms | Product behavior comes before algorithm specification. | Blocks R1 | None at the product level. |
| 8 | Privacy and consent requirements for real testers; measurement mechanics for R6, R7, V1 to V3 | Requirements in Phase 02; plan in Phase 09; execution in Phases 11 and 12 | Real students' data is involved, so consent and privacy are requirements. | Blocks R6, R7 | AS-07 (how pre-release testing is separated from the public demo). |

## 12. Closure checklist (complete)

Confirmed by the owner on 2026-10-29:

- [x] D09 vision approved
- [x] D10 problem statement approved, with the correction
- [x] D11 target users approved
- [x] D12 differentiation direction approved; claims rule confirmed
- [x] D13 cross-device access confirmed as a V2 goal
- [x] D06 accounts confirmed as part of V2, second implementation phase
- [x] D14 success criteria approved with clarifications (R5, R6, R7, R2) and thresholds
- [x] D15 policy conformance suite approved, with interaction coverage
- [x] D16 Gradex confirmed as the official product name
- [x] D19 completion and approval of all 12 phases is a mandatory release condition
- [x] D18 phase placement approved in principle, reasoning retained
- [x] D20 change control confirmed

Confirmed by the owner on 2026-10-30:

- [x] D17 glossary approved as written
- [x] Completed Phase 01 deliverables approved
- [x] Formal closure of Phase 01 authorized
- [x] D21: Phase 02 is not to start automatically

Completed by me:

- [x] Draft 2 updated into the final review copy; every item in the owner's final message applied
- [x] Final consistency review performed (section 14)
- [x] Assumptions affecting approved success criteria documented with resolution phases (section 13)
- [x] Approval and closure recorded in this document and its decision record (sections 10, 12, 15)
- [x] All documented limitations, dependencies and assumptions preserved

**Phase 01 is closed. Phase 02 has not started and awaits the owner's explicit authorization.**

## 13. Assumptions register [UA]

Every assumption that affects an approved success criterion or a deferred decision, with where and how it is resolved. All remain open at closure of Phase 01; none was resolved by closing it.

| ID | Assumption | Affects | Resolved in | How |
|---|---|---|---|---|
| AS-01 | A typical test semester has up to 6 courses | R6 scenario | Phase 02 | Validate against course loads in the policies and sources gathered; adjust the scenario, not the 10-minute target |
| AS-02 | Prior academic standing can be entered in a way compatible with the R6 scenario (method not yet decided) | R6 test procedure | Phase 02 (requirement), Phase 04 (stories) | Decide full-history versus summary entry before the R6 procedure is finalized |
| AS-03 | The 10-minute target is achievable | R6 | Phase 02 and Phase 04 | Fixed by the owner. If AS-01 or AS-02 make it unachievable, raise it to the owner as a proposal. Not changed silently |
| AS-04 | Students need scales above 5.00, other failing codes, non-GPA codes, or configurable retakes and rounding | R1, R2, scope | Phase 02 | Requirements research across real policies |
| AS-05 | The three built-in tables other than `4.0-plus-only` match real universities | R1 | Phase 02 | Verify against named sources or label as unverified presets (section 11, item 2) |
| AS-06 | Four profiles is enough as a starting point for R2 | R2 | Phase 02 | Count derived from the options and interactions defined there. May rise, not fall |
| AS-07 | Pre-release testing with real data can be kept separate from the public synthetic-data demo | R4, R7 | Phase 02 (requirement), Phase 05 (design) | Implied by R4 and R7. To be made an explicit requirement |
| AS-08 | Early testers use a build that may not yet have accounts | R7, R8 | Phase 03 | Decide handling of pre-account testing without contradicting D06 |
| AS-09 | The competitor sample is representative enough to support the claims rule | D12 | Phase 02 | Structured comparison with a defined sample and criteria |
| AS-10 | A published university policy is a usable basis for R2 profiles even where it leaves rules unspecified | R2 | Phase 02 | Profiles state their assumptions explicitly (9.3, item 6) |

## 14. Final consistency review

**Checks performed on this document and results:**

- Every owner decision from the three input messages appears in the decision record with the correct label. Result: pass.
- Nothing in the document removes or weakens accounts (D06). The Phase 03 constraint is written into 2.2 and section 11, item 3. Result: pass.
- No uniqueness or first-in-market claim appears. "Genuinely differentiated" is stated as none established. Result: pass.
- Every R item is a release gate and every V item is a longer-term goal. No V item gates publication. Result: pass.
- R5 states unambiguously that publishing V2 requires all 12 phases completed and approved. Result: pass.
- R6 identifies the six-course limit as an assumption, links the test procedure to AS-02, and keeps the ten-minute target fixed. Result: pass.
- R7 requires consent and privacy safeguards and forbids real data in the public demo. Result: pass.
- Section numbers cited by the owner (2, 4.3, 11) still refer to the same content. Result: pass.
- **Closure edit check (2026-10-30):** the closed version changes only status lines, the D17 label, the new D21, the closure checklist, the closure record and this line. Sections 4, 5 to 9, 11 and 13 are unchanged. Result: pass.

**Inconsistencies found in Draft 2 and corrected in the final review copy:**

1. Draft 2 scheduled verification of built-in table values for Phase 09, which contradicts the instruction that Phase 02 settle their intended behavior before later decisions depend on it. Corrected in section 11, item 2.
2. Draft 2's R2 criterion required each option in one profile but not interactions between options. Corrected in 9.3, item 4.
3. Draft 2's R7 had no privacy or consent requirement. Added.
4. Draft 2 left the "first assumption" status of the six-course limit implicit. It is now explicit and registered as AS-01.
5. Draft 2 mixed decisions and proposals in one table without labels. Evidence labels now distinguish owner decisions, approved proposals, verified facts, observations, assumptions and later-phase dependencies.

**Remaining limits (stated, not resolved by this phase):**

- I did not read V1 briefs P0 to P9 or `cli.py` in full.
- The competitor sample is small (about eight tools, mostly from page descriptions).
- The Alfaisal catalogue is one policy and contradicts itself on minus grades, so it is not a representative sample.
- Nothing about demand for cross-device sync is verified. It remains an owner-confirmed goal.

## 15. Closure record

**Phase 01 is formally closed.**

| Item | Record |
|---|---|
| Closed on | 2026-10-30, on the owner's explicit approval |
| Approved by | The owner |
| What was approved | The completed Phase 01 deliverables: vision, problem statement, target users, differentiation and claims rule, success criteria (R1 to R8, V1 to V3), conformance-suite criterion, glossary (D17, as written), decision record (D01 to D21), dependency placements, assumptions register |
| Authorization given | Formal closure of Phase 01 |
| Not authorized | Starting Phase 02. It begins only on the owner's explicit authorization (D21) |
| Preserved at closure | All verified limitations (L1 to L8 and section 4.1), all eight dependencies (section 11), all ten assumptions (section 13, still open), and all remaining limits (section 14) |

**Handoff list for Phase 02 (no Phase 02 work has been done).** The items below are already assigned to Phase 02 by section 11 and section 13. Listing them here is a record, not a start.

- Custom grading policy requirements, including important interactions between rules (section 11, item 1).
- Intended behavior and accuracy status of the four built-in systems, closed before later decisions depend on them (item 2).
- Requirements for accounts, persistence, hosting, privacy, durability and budget constraints, some needing owner input (item 3).
- How prior academic standing is entered (item 5).
- Structured competitor comparison, before the Phase 03 cut line (item 6).
- Definition of target planning (item 7).
- Privacy and consent requirements for real testers (item 8).
- Validation of assumptions AS-01, AS-02, AS-03, AS-04, AS-05, AS-06, AS-07, AS-09 and AS-10. AS-08 belongs to Phase 03.

**Constraints Phase 02 inherits:** change control (D20), accounts in V2 (D06), the claims rule (D12), the fixed ten-minute target (AS-03), and the owner's rule that each phase be fully closed and approved before the next begins (D05).
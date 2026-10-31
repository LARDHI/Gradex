# Gradex V2 Phase 02 (Requirements): Execution Log
 
**TEMPORARY OPERATIONAL ARTIFACT.** Governed by `claude/GPA_Tracker_V2_00_Protocol.md` (D22). Deleted only after the owner explicitly approves the final Phase 02 document and the cleanup procedure (Protocol section 10) is satisfied. **Never delete automatically.**
**Single writer: the Orchestrator.** Workers must not edit this file.
Log created: 2026-10-31. Last updated: 2026-10-31 (revision 2: owner corrections applied; no research started).
 
**Provenance labels used in this log**
 
| Label | Meaning |
|---|---|
| **[REC]** | Recovered: read from a persistent project file |
| **[OS]** | Owner-supplied in a message of 2026-10-31. Not recovered from any file |
| **[OS-H]** | Owner-supplied **historical task information**: the owner states what an earlier Phase 02 brief specified. The original brief is not recovered. It is recorded as history, **not** as a new decision |
| **[RC]** | Reconstructed by the Orchestrator from [REC], [OS] and [OS-H] sources. Not an original |
| **[PR]** | Orchestrator proposal. Not owner-supplied and not a decision. Awaiting owner review |
 
## 1. Phase identity and authorization
 
| Field | Record |
|---|---|
| Phase | 02, Requirements, of Gradex V2 (12 sequential phases) |
| Official deliverable | `claude/GPA_Tracker_V2_02_Requirements.md` (**not yet created**) |
| Authorization | Given by the owner on 2026-10-30 with the exact instruction: **"Start Phase 02: Requirements"** [OS] |
| Authorization evidence status | Owner-supplied. The owner restated the date and exact wording in the message of 2026-10-31 that approved D22. The original message is not in any persistent project file. It satisfies D21 on the owner's word and is not re-requested |
| Previous phase | Phase 01, closed and approved 2026-10-30. Unchanged |
| Governing decisions | D01 to D21 (Phase 01, section 10) and D22 (Protocol, section 1). Unchanged by anything in this log |
| Orchestrator | The session that created this log (2026-10-31). Succession rules: Protocol section 3 |
| Review status | Initial implementation approved **for review** with corrections, 2026-10-31 [OS]. Corrections applied in revision 2 (change log CL-06 to CL-12) |
| Research execution | **Not authorized.** T01 to T04 are not launched. The owner authorizes execution after reviewing the briefs in section 12 |
| Phase 03 | **Not started.** Needs a separate explicit owner authorization |
| Mirroring V2 documents into the V1 repository | **Not decided.** A separate future owner decision (CL-04) |
 
## 2. Phase 02 objectives and expected deliverables
 
Source: Phase 01 section 11 (dependencies assigned to Phase 02), section 13 (assumptions) and the section 15 handoff list. **[RC]** from those persistent sources. The original Phase 02 brief was not recovered.
 
**Objectives (what Phase 02 must settle):**
- O1. The policy dimensions that exist, with real policies gathered, including important interactions between rules (Phase 01 s11 #1).
- O2. The behavior V2 promises for the four built-in grading systems, and whether their table values are verified against named sources or labelled unverified presets with a documented consequence for R1. Closed before any later decision relies on the table values (s11 #2).
- O3. Requirements for accounts, persistence, cross-device access, per-user isolation, durability and recovery, privacy, data deletion and export, HTTPS, and budget and hosting constraints (some need owner input) (s11 #3).
- O4. How prior academic standing is entered (s11 #5; AS-02).
- O5. A structured competitor comparison before the Phase 03 cut line (s11 #6; AS-09; D12).
- O6. The definition of target planning (required average versus per-course feasibility) (s11 #7).
- O7. Privacy and consent requirements for real testers, and measurement mechanics for R6, R7 and V1 to V3 (s11 #8; AS-07).
- O8. Disposition of assumptions AS-01, AS-02, AS-03, AS-04, AS-05, AS-06, AS-07, AS-09 and AS-10. AS-08 belongs to Phase 03.
- O9. Inputs for the R2 conformance suite: configurable options, important interactions, and whether four profiles suffice (AS-06; Phase 01 s9.3).
**Expected deliverables:**
- D-A. The official document `GPA_Tracker_V2_02_Requirements.md`, with its traceability matrix, assumptions disposition, decision record and closure record.
- D-B. Promoted research and evidence files that survive cleanup.
- D-C. The owner's explicit approval of the phase (the only way Phase 02 closes).
**Inherited constraints:** D20 change control; D06 accounts remain in V2; D12 claims rule; AS-03 ten-minute target fixed; D05 closure rule. Phase 02 may add detail to approved decisions but must not redefine them. A conflict is stated and a correction is proposed to the owner.
 
## 3. Task ledger
 
Status values per Protocol section 4. "Prior attempt" and "Required action" come from the owner's recovery record of 2026-10-31 [OS]. **No output file exists. No task is running.**
 
| ID | Task | Prior attempt [OS] | Recovery classification | Status | Assigned output path | Blocked by |
|---|---|---|---|---|---|---|
| T01 | Public grading policy research | Interrupted by usage limits; no usable saved report | **RESTART** | planned, ready (awaiting owner authorization to execute) | `claude/tmp/p02/T01_public_grading_policies.md` | none. Sample size is settled ([OS-H], below) |
| T02 | Verification of the four built-in grading tables | Report reportedly completed in the old conversation, never saved or verified | **RESTART** (VERIFY applies only if reliable evidence exists; none was found) | planned, **blocked-on-owner** | `claude/tmp/p02/T02_builtin_tables.md` | OQ-05 (scope) |
| T03 | Structured competitor comparison | Interrupted; no usable saved report | **RESTART** | planned, ready (awaiting owner authorization to execute) | `claude/tmp/p02/T03_competitor_comparison.md` | none. Two [PR] brief parameters await review (section 12.0) |
| T04 | Privacy, security and accessibility requirements research | Failed without a usable output | **RESTART** | planned, ready (awaiting owner authorization to execute) | `claude/tmp/p02/T04_privacy_security_accessibility.md` | none. Accessibility is confirmed in scope ([OS-H]) |
| T05 | Draft the Phase 02 requirements | Not started | Not applicable | planned, **blocked-on-task** | `claude/GPA_Tracker_V2_02_Requirements.md` (Orchestrator-written) | T01 to T04 accepted; OQ-01, OQ-02 (owner decisions) |
| T06 | Consistency review against D01 to D21 and the assumptions register | Not started | Not applicable | planned, **blocked-on-task** | `claude/tmp/p02/T06_consistency_review.md` (independent reviewer) | T05 |
 
**Owner-supplied historical task information [OS-H]** (stated by the owner on 2026-10-31; not recovered from a file; not a new decision):
- **T01 sample specification:** the previous research brief specified **at least 12 public grading policies across at least 6 regions**. This resolves what was recorded earlier as OQ-03.
- **T04 scope:** accessibility was explicitly part of the owner's original Phase 02 research track, "privacy, security, and accessibility requirements". It is confirmed in scope. This resolves what was recorded earlier as OQ-06.
**Acceptance criteria.** Each is tagged. Criteria were **[RC]** from Phase 01 sections 4, 8, 9, 11 and 13 and the owner's track descriptions, then corrected in revision 2 for the [OS-H] items. The original briefs and criteria were not recovered. Criteria are working criteria for owner review (section 12). Any change after execution starts is recorded in the change log.
 
**T01 Public grading policy research**
- T01-AC1 [OS-H] The sample contains **at least 12 public grading policies from at least 6 regions**. If either minimum cannot be met, the output says so and does not pad the sample.
- T01-AC2 [RC] The selection method, the working definition of "region" and the per-region and per-country counts are stated before the findings, with the limits of representativeness (AS-04). The definition of region is [PR] (section 12.0).
- T01-AC3 [RC] Each fact has a direct source reference (an official university source preferred) and an access or publication date. Third-party sources are flagged as such.
- T01-AC4 [RC] Each policy is recorded against the dimensions: scale range (L1), failing codes (L2), non-GPA codes (L3), letter forms (L4), retake treatment (L5), rounding (L6), credit values (L7), table scope (L8), and further dimensions found.
- T01-AC5 [RC] Rules a policy leaves unspecified are identified, not guessed (AS-10).
- T01-AC6 [RC] Interactions between rules that can affect the same calculation are identified (Phase 01 s9.3 item 4).
- T01-AC7 [RC] Typical course loads are recorded as evidence for AS-01.
- T01-AC8 [RC] Option-count and interaction-count implications for R2 and AS-06 are stated as findings, labelled as such, not as decisions.
**T02 Built-in grading tables** (scope pending OQ-05; written for recommended scope B)
- T02-AC1 [RC] All four built-in tables are listed with every value, taken from the V1 repository at tag `v1.0.0`.
- T02-AC2 [RC] Each table is classified as one of: **verified against a named source**, **partly verified**, or **unverified reference preset**, with direct source references and dates for anything verified.
- T02-AC3 [RC] The result states the consequence for R1 (tests assert the stated values, not real-world accuracy) per Phase 01 s11 #2.
- T02-AC4 [RC] Phase 01's finding that `4.0-plus-only` equals the Alfaisal catalogue table is re-checked, not assumed.
- T02-AC5 [RC] AS-05 is answered with the evidence level stated. Any proposed change to a built-in table is a proposal to the owner, not a decision.
- T02-AC6 [PR, scope B only] An inventory of the rules V1 attaches to each built-in table (passing threshold, failing code, non-GPA codes, retake handling, rounding), recorded as V1 facts with code or test references. No claim about real-world correctness unless a source exists.
- T02-AC7 [RC] Marked high-impact: needs independent verification.
**T03 Competitor comparison**
- T03-AC1 [RC] The sample and the criteria are fixed and saved in the output file **before** any tool is assessed. Criteria cover the candidate differentiators (a) to (d) of Phase 01 s8.2 and the policy dimensions from T01.
- T03-AC2 [RC] Each claim has a source and an access date. The output states, per tool, whether the assessment rests on a page description, documentation, source code or hands-on use.
- T03-AC3 [RC] The sample's limits are stated (AS-09). No uniqueness or first-in-market claim appears (D12).
- T03-AC4 [RC] The Phase 01 classification (differentiated / valuable but not differentiating / candidate) is revisited with evidence. Any change is a proposal to the owner.
- T03-AC5 [RC] Complete before the Phase 03 cut line. Marked high-impact (D12 claims).
**T04 Privacy, security and accessibility requirements**
- T04-AC1 [RC] Each candidate requirement is derived from a cited source or standard, with a direct reference. Accessibility cites a named standard.
- T04-AC2 [RC] Covers: consent and data minimization for real testers (R7); deletion on request; separation of real-data testing from the public synthetic-data demo (AS-07); per-user isolation (R3); durability and recovery expectations; data deletion and export; HTTPS; accessibility.
- T04-AC3 [RC] Items needing owner input (budget, hosting constraints) are listed as owner-dependent and not guessed.
- T04-AC4 [RC] No technology is chosen (Phase 05). Requirements are technology-neutral.
- T04-AC5 [PR] Each candidate requirement is phrased so that it can be tested later (Phase 11).
- T04-AC6 [RC] Marked high-impact (privacy and security).
**T05 Draft requirements**
- T05-AC1 Every objective O1 to O9 is addressed, or an explicit open item is recorded.
- T05-AC2 Every requirement has an ID and traces to a basis (Protocol section 8).
- T05-AC3 No requirement redefines D01 to D22. Owner decisions are listed as **decision options** or open questions, never decided by the Orchestrator. This explicitly includes prior-standing entry (OQ-01) and the definition of target planning (OQ-07).
- T05-AC4 All ten assumptions have a stated disposition.
- T05-AC5 Built only from accepted task outputs and owner input, not from the Orchestrator's recollection of facts.
**T06 Consistency review**
- T06-AC1 Performed by an agent independent of the T05 drafting.
- T06-AC2 Checks the draft against each of D01 to D22, AS-01 to AS-10 and the Phase 01 handoff list.
- T06-AC3 Reports each inconsistency and a proposed correction. Does not edit the draft.
- T06-AC4 Confirms that the traceability matrix resolves.
## 4. Research tracks: known status
 
| Track | Task | Known previous status [OS] | Persistent output found | Current status |
|---|---|---|---|---|
| Public grading policies | T01 | Interrupted by usage limits | None | RESTART, planned, ready |
| Four built-in grading tables | T02 | Reportedly completed in the old conversation, never saved or verified | None | RESTART, planned, blocked-on-owner (OQ-05) |
| Competitor comparison | T03 | Interrupted | None | RESTART, planned, ready |
| Privacy, security, accessibility | T04 | Failed without usable output | None | RESTART, planned, ready |
 
**High-impact tasks (independent verification required, Protocol section 7):** T02, T03, T04, and T01 where it feeds R2 or AS-04. Verifier assignment is recorded here when it happens.
 
## 5. Recovery record
 
Performed 2026-10-31, before any task was started.
 
**Inventory of persistent outputs found:**
- Project documents: the 15 documents then in the Project, plus the three created at initialization. None contains Phase 02 research, a Phase 02 brief or a checkpoint.
- V1 repository (`LARDHI/Gradex`, `main`, tag `v1.0.0`): the only document is `docs/verification.md`. Nothing relates to V2 Phase 02. Nothing in the repository was changed.
- Other sources: none reachable. The old Phase 02 session is not accessible, and this log makes no assumption about its contents.
**Classification outcome:** four research tracks, no recoverable output, so RESTART for T01 to T04, each with the recorded reason "no persistent output exists". T02's VERIFY condition (reliable evidence available) is not met.
 
**Provenance of information in this log** (the strictest distinction):
 
| Category | Items |
|---|---|
| **[REC] Recovered from files** | The complete Phase 01 document: D01 to D21, glossary, V1 facts L1 to L8, evidence in s4.5 and s8.1, success criteria, dependency table (s11), assumptions AS-01 to AS-10, the Phase 02 handoff list. The Protocol and this log's own files |
| **[OS] Owner-supplied, 2026-10-31** | The authorization date and exact wording; the four track statuses and the required action for each; the titles of the six tasks; D22 wording; the instruction to keep OQ-01, OQ-02 and OQ-05 open and to handle OQ-07 as T05 decision options |
| **[OS-H] Owner-supplied historical task information** | (1) The previous T01 brief specified at least 12 public grading policies across at least 6 regions. (2) Accessibility was part of the original track "privacy, security, and accessibility requirements". Both are recorded as history, not as new decisions |
| **[RC] Reconstructed** | Phase 02 objectives O1 to O9; deliverables D-A to D-C; every acceptance criterion tagged [RC] in section 3; the Document Construction Map; the research briefs, except items tagged [PR] |
| **[PR] Orchestrator proposals** | Items listed in section 12.0 |
| **Not recovered** | The original task briefs and acceptance criteria; any partial findings, sources or notes from the old session, including the built-in-table report; the original authorization message. Apart from the two [OS-H] facts above, no content of the previous briefs is known |
 
No previous finding, source, completion status or evidence has been invented. Nothing from the old session is treated as a result.
 
## 6. Open questions and owner-dependent items
 
**Open**
 
| ID | Question | Type | Needed by | Status |
|---|---|---|---|---|
| OQ-01 | How is prior academic standing entered (full history versus a summary of CGPA and credits)? This decides what the R6 scenario means (AS-02, AS-03) | **Owner decision.** T05 will present decision options with evidence | T05 | open, owner-dependent |
| OQ-02 | Budget and hosting constraints for V2 (Phase 01 s11 #3 says they need owner input) | **Owner input** | T04 results and T05 | open, owner-dependent |
| OQ-04 | Does any export of the old session's partial findings exist? The owner reports none usable. If one turns up it is handled as recoverable work under Protocol section 5 | Owner information | Any time | open, no action needed |
| OQ-05 | Scope of T02: verify table **values** only, or also the grading **rules**? See below | **Owner input**, after the recommendation below | Before T02 starts | open, recommendation presented |
| OQ-07 | How should the definition of target planning be decided? | Handled as **decision options inside T05**. No decision is made on the owner's behalf | T05 | open, owner-dependent |
 
**OQ-05 in detail**
 
*The distinction.*
- **Verifying table values** means checking the numbers: the letters and their grade points in each of the four built-in tables, and whether a named published source supports them. This is a factual check with a clear pass or fail per value.
- **Verifying grading rules** means checking what the system does with those values: which letter is the failing grade and the passing threshold, which codes count in the GPA, how retakes are treated, how the result is rounded. For a built-in table these rules are not part of the table. In V1 they are fixed code behavior (`F` is the only failing grade; every attempt counts; two-decimal half-up rounding, per Phase 01 L2, L5 and L6). A rule can only be "verified" against a source that describes the same policy. The built-in tables are not tied to a named university (Phase 01 s4.5), so for most of them such a source may not exist.
*Options.*
- **A. Values only.** Smallest scope. It leaves the "behavior V2 promises" half of Phase 01 s11 #2 to T05 with no factual inventory to build on.
- **B. Values plus a factual rule inventory (recommended).** Verify the values, and list the rules V1 attaches to each built-in table as V1 facts, with code or test references. Check real-world correctness of a rule only where a source for the same policy exists. T05 then proposes the behavior V2 promises, using T01 findings on real policies. The owner decides.
- **C. Values plus full rule verification against sources.** Most thorough, but it is only meaningful where a matching source exists, and may re-do work T01 already covers for real policies.
*Recommendation: B.* Reason: Phase 01 s11 #2 asks for the behavior V2 *promises* (a requirement, decided in Phase 02) and the accuracy of the table values (a verification). B supplies both facts the decision needs without claiming verification where no source can exist, and it avoids duplicating T01. This is a recommendation only. T02 stays blocked until the owner chooses.
 
**Resolved or withdrawn (kept for provenance)**
 
| ID | Outcome |
|---|---|
| OQ-03 | **Resolved by [OS-H].** The previous T01 brief specified at least 12 public grading policies across at least 6 regions. Recorded as owner-supplied historical task information, not as a new decision. Part of T01-AC1 |
| OQ-06 | **Withdrawn.** Accessibility is confirmed in scope: it was part of the owner's original Phase 02 research track [OS-H]. Reflected in T04 |
 
None of the open items is decided by the Orchestrator.
 
## 7. Assumptions and Phase 01 handoff dependencies
 
**Handoff dependencies (Phase 01 s15) and the task that covers each:**
 
| Handoff item | Covered by | Note |
|---|---|---|
| Custom grading policy requirements, including interactions (s11 #1) | T01, T05 | none |
| Built-in systems: behavior and accuracy (s11 #2) | T02, T05 | scope per OQ-05 |
| Accounts, persistence, hosting, privacy, durability, budget (s11 #3) | T04, T05, OQ-02 | owner input |
| Prior academic standing entry (s11 #5) | T05 decision options, OQ-01 | no research task; owner decides |
| Structured competitor comparison (s11 #6) | T03 | none |
| Definition of target planning (s11 #7) | T05 decision options, OQ-07 | no research task; owner decides |
| Privacy and consent for testers (s11 #8) | T04, T05 | none |
| Assumptions AS-01 to AS-07, AS-09, AS-10 | table below | AS-08 belongs to Phase 03 |
 
**Assumption disposition plan** (all still open; dispositions are proposals until the owner approves the phase):
 
| ID | Assumption | Planned resolution route |
|---|---|---|
| AS-01 | Test semester has up to 6 courses | T01 course-load evidence; adjust the scenario, never the 10-minute target |
| AS-02 | Prior standing can be entered compatibly with R6 | OQ-01, T05 decision options |
| AS-03 | The 10-minute target is achievable | Fixed by the owner. If AS-01 or AS-02 conflict, propose to the owner; never change silently |
| AS-04 | Students need extended policy features | T01 |
| AS-05 | The three other built-in tables match real universities | T02 |
| AS-06 | Four conformance profiles suffice | T01 options and interactions, then T05 |
| AS-07 | Real-data testing is separable from the public demo | T04, T05 |
| AS-08 | Pre-account testers | Phase 03. Not handled here |
| AS-09 | The competitor sample is representative | T03 |
| AS-10 | A published policy is usable despite unspecified rules | T01 |
 
## 8. Evidence and source register
 
Entries are **inherited from Phase 01** (access dates as stated there) and **not re-verified in Phase 02**. New entries are added by the Orchestrator from accepted worker outputs, with the file reference.
 
| ID | Source | Used in Phase 01 for | Status |
|---|---|---|---|
| S01 | Alfaisal University grading system catalogue PDF (https://catalog.alfaisal.edu/sites/default/files/pdf/academic_page/grading-system.pdf?1656613152), Fall 2025-26 | Built-in table `4.0-plus-only`, failing code `DN`, non-GPA codes, unspecified rules | inherited, not re-verified |
| S02 | gpacalculator.net repeat calculator (https://gpacalculator.net/course-repeat-gpa-calculator) | Retake policy competitor evidence | inherited, not re-verified |
| S03 | GPA Calculator Tracker iOS (https://apps.apple.com/app/id6785322301) | Competitor evidence | inherited, not re-verified |
| S04 | Gradeful (https://github.com/beyenilmez/gradeful) | Competitor evidence | inherited, not re-verified |
| S05 | Target GPA calculator (https://calculators-ng.pages.dev/education/target-gpa-calculator) | Competitor evidence | inherited, not re-verified |
| S06 | gpacalculator.net target calculator (https://gpacalculator.net/target-gpa-calculator) | Competitor evidence (Phase 01 notes it was not re-checked by its author) | inherited, not re-verified |
| S07 | V1 repository `LARDHI/Gradex`, tag `v1.0.0`, `gpa_tracker/grading.py` | Built-in table values and custom-table limits L1 to L8 | to be read in T02. Not re-read for this log |
 
Worker output files (none yet): see the manifest `claude/tmp/p02/README.md`.
 
## 9. Document Construction Map
 
Official document: `claude/GPA_Tracker_V2_02_Requirements.md` (not yet created). Requirement ID scheme [PR]: `P2-<AREA>-NNN`, with areas POL, BLT, TGT, STD, ACC, PRV, SEC, A11Y, USE, CMP, CNF. The traceability matrix will be inside the document.
 
| § | Planned section | Phase 01 basis | Supporting tasks | Evidence files | Owner input | Status |
|---|---|---|---|---|---|---|
| 1 | Status, scope, how to read | n/a | none | none | none | not started |
| 2 | Governance inputs: D01 to D22, authorization evidence, constraints | s2, s10, s15 | none | none | none | not started |
| 3 | Evidence labels and requirement ID scheme | s0 | none | none | none | not started |
| 4 | Grading policy requirements: dimensions and interactions | s11 #1; L1 to L8; AS-04, AS-10 | T01 | T01 | none | not started |
| 5 | Built-in grading systems: promised behavior and accuracy status | s11 #2; AS-05 | T02 | T02 | OQ-05; approval of proposals | not started |
| 6 | Target planning: definition and behavior | s11 #7 | T05 (T01, T03 inputs) | none | OQ-07 decision | not started |
| 7 | Prior academic standing entry | s11 #5; AS-02 | T05 (T01, T03 inputs) | none | OQ-01 decision | not started |
| 8 | Accounts, persistence, cross-device, isolation, durability, deletion and export, HTTPS, budget and hosting | s11 #3; R3, R4, R8; D06, D13 | T04 | T04 | OQ-02 | not started |
| 9 | Privacy, consent and real-tester testing | s11 #8; R7; AS-07 | T04 | T04 | none | not started |
| 10 | Security | R3 | T04 | T04 | none | not started |
| 11 | Accessibility | Owner's original track [OS-H] | T04 | T04 | none (scope confirmed) | not started |
| 12 | Usability and the R6 scenario | R6; AS-01, AS-03 | T01, T05 | T01 | OQ-01 | not started |
| 13 | Competitor comparison and differentiation status | s8; D12; AS-09 | T03 | T03 | approval of proposals | not started |
| 14 | Inputs for the R2 conformance suite: options, interactions, profile count | s9.3; AS-06 | T01, T05 | T01 | none | not started |
| 15 | Assumptions disposition (AS-01 to AS-10) | s13 | T01 to T05 | various | approval | not started |
| 16 | Decision record: Phase 02 decisions (numbering continues from D23) | s10 | T05 | none | owner approves each | not started |
| 17 | Consistency review | s14 pattern | T06 | T06 | none | not started |
| 18 | Handoff to Phase 03 (including AS-08) | s15 | T05 | none | none | not started |
| 19 | Traceability matrix and closure record | Protocol s8, s10 | T05, T06 | none | phase approval | not started |
 
## 10. Current blockers and next actions
 
**Blockers:**
- BL-01: T05 and T06 are blocked on T01 to T04 being accepted, and on the owner decisions OQ-01, OQ-02 and OQ-07.
- BL-02: T01 to T04 are **not authorized to execute** until the owner has reviewed the briefs in section 12 and given the go-ahead. This is an instruction, not a technical block.
- BL-03: T02 is blocked on the owner's choice for OQ-05.
- BL-04: No independent verifier is assigned yet (needed for T02, T03, T04).
**Next actions:**
1. The owner reviews the revised open questions, the acceptance criteria (section 3) and the four research briefs (section 12).
2. The owner chooses a scope for OQ-05 and confirms or adjusts the [PR] items in section 12.0.
3. The owner authorizes research execution. The Orchestrator then launches T01, T03 and T04 (and T02 once OQ-05 is settled) as parallel workers that write only to their assigned files.
4. The Orchestrator checks each saved output against its criteria, assigns independent verification for the high-impact tasks, and updates statuses.
5. After T01 to T04 are accepted, T05 is drafted with owner decision options for OQ-01, OQ-02 and OQ-07, then T06 is run.
## 11. Change log
 
| ID | Date | Change | By |
|---|---|---|---|
| CL-01 | 2026-10-31 | Log created. Phase identity and authorization recorded as owner-supplied. T01 to T06 listed. Criteria reconstructed. Recovery record written | Orchestrator |
| CL-02 | 2026-10-31 | Traceability is kept **inside** the official Phase 02 document, per the owner's instruction. The earlier proposal of a separate traceability file is withdrawn | Orchestrator, on owner instruction |
| CL-03 | 2026-10-31 | Retained research and evidence will be promoted to flat permanent paths `claude/GPA_Tracker_V2_02_E##_<slug>.md` at cleanup, not to a new `evidence/` folder | Orchestrator, per Protocol section 10 |
| CL-04 | 2026-10-31 | Mirroring V2 documents into the V1 repository is **not decided** and is out of scope. Nothing in the repository was changed | Orchestrator, on owner instruction |
| CL-05 | 2026-10-31 | Phase 01 document and decisions D01 to D21 unchanged. D22 recorded in the protocol only | Orchestrator |
| CL-06 | 2026-10-31 | OQ-03 resolved by owner-supplied historical task information: at least 12 public grading policies across at least 6 regions. Recorded as history, not as a new decision. Added as T01-AC1 | Orchestrator, on owner correction |
| CL-07 | 2026-10-31 | OQ-06 withdrawn. Accessibility is confirmed in scope as part of the owner's original track. T04 note and map row 11 updated | Orchestrator, on owner correction |
| CL-08 | 2026-10-31 | OQ-05 kept open. Distinction between verifying table values and grading rules written out, with options A, B, C and a recommendation (B). T02 is blocked-on-owner | Orchestrator, on owner correction |
| CL-09 | 2026-10-31 | OQ-01 and OQ-02 kept as owner-dependent. OQ-07 handled as decision options inside T05. T05-AC3 states that no owner decision is made by the Orchestrator | Orchestrator, on owner correction |
| CL-10 | 2026-10-31 | Provenance labels [REC], [OS], [OS-H], [RC], [PR] added. Recovery record section 5 and all acceptance criteria tagged | Orchestrator, on owner correction |
| CL-11 | 2026-10-31 | Acceptance criteria revised and numbered (T01-AC1 etc.). Section 12 added with draft research briefs for owner review. Research is **not** launched | Orchestrator, on owner instruction |
| CL-12 | 2026-10-31 | Confirmed unchanged by this revision: D01 to D22, the Phase 01 document, the Protocol, and all previously approved decisions | Orchestrator |
 
## 12. Research briefs (DRAFT for owner review; not authorized for execution)
 
These briefs are written so that a worker with no access to any conversation can execute them from the project files alone (Protocol section 9). Every worker: read `claude/GPA_Tracker_V2_00_Protocol.md` and `claude/GPA_Tracker_V2_01_Idea.md` first. Write only to your assigned file, using the Protocol section 6 header. Save findings as you go, with status `partial` until complete. Do not edit the execution log. Do not make decisions that belong to the owner. State gaps rather than filling them. Do not fabricate sources. Do not modify any other file.
 
### 12.0 Items in the briefs that are Orchestrator proposals [PR], not owner-supplied
 
1. The working definition of "region" in T01 (the owner's previous brief fixed "at least 6 regions"; its definition was not recovered). Proposed: world regions such as North America; Latin America and the Caribbean; Europe; Middle East and North Africa; Sub-Saharan Africa; South Asia; East Asia; Southeast Asia; Oceania; Central Asia. The worker states the definition it used.
2. The T03 sample size and categories (no number was supplied): at least 12 tools across at least 4 categories (web calculators, mobile apps, open-source projects, university or learning-platform tools).
3. T02 scope B (pending OQ-05).
4. T04-AC5 (testable phrasing) and the list of candidate frameworks in the T04 brief.
5. The requirement ID scheme in section 9.
### 12.1 T01: Public grading policy research
 
| Field | Brief |
|---|---|
| Research question | Which grading-policy dimensions and interactions between rules occur across real, public university grading policies, so that Gradex V2's custom grading requirements can be defined from evidence? |
| Why it matters | Feeds O1, O8 (AS-01, AS-04, AS-06, AS-10), O9. Gradex must support students from any university (D01, D11). Phase 01 verified that V1's customization is limited (L1 to L8) but only one real policy was examined |
| Sample | At least 12 public grading policies from at least 6 regions [OS-H]. Choose universities by a stated, documented method. Do not target one country (D01). State per-region and per-country counts and flag any concentration. Primary source: the university's own published policy (catalogue, registrar, academic regulations). Third-party GPA sites are not sources for a policy, only for a lead |
| Record for each policy | University, country, region, source document and section, URL, access date, original language and whether the worker translated it, and the dimensions below |
| Dimensions | Scale range and point values (L1); letter forms including plus or minus (L4); passing threshold and failing code or codes (L2); non-GPA codes such as withdrawal, pass/fail, incomplete, audit (L3); retake treatment (L5); rounding and precision (L6); credit values including fractional credits (L7); table scope such as per-term or per-program differences (L8); percentage-to-letter conversion where used; any other GPA-affecting rule found |
| Also record | Typical full-time course load per term (AS-01); rules the policy leaves unspecified or contradicts (AS-10); interactions between rules that can affect the same calculation (for example retake with a non-GPA code, retake with a rounding boundary) |
| Not in scope | Graduation or honors thresholds unless they change how GPA is computed; technology; deciding what Gradex supports (Phase 03); any owner decision |
| Output | Per-policy table; dimension matrix; interactions list; unspecified-rules list; course-load evidence; findings on the number of distinct options and important interactions relevant to R2 and AS-06, **labelled as findings, not decisions**; limitations (sample bias, language, access) |
| Acceptance | T01-AC1 to T01-AC8 (section 3) |
| Independent verification | Yes where findings feed R2 or AS-04: a verifier re-opens the cited sources for the claims that determine an option or interaction |
| Stop conditions | If 12 policies from 6 regions cannot be reached, stop padding, state the shortfall and the reasons |
 
### 12.2 T02: Verification of the four built-in grading tables
 
Scope below is **B (recommended)**. If the owner chooses A or C, this brief changes accordingly and the change is logged.
 
| Field | Brief |
|---|---|
| Research question | What are the values of the four built-in grading tables in V1, are those values supported by named public sources, and what rules does V1 attach to each built-in table? |
| Why it matters | Feeds O2 and AS-05. Phase 01 s11 #2 requires this closed before any later decision relies on the table values. Currently V1's decision accepted the values as an unverified baseline. Only one table has an observed match (Alfaisal, s4.5) |
| Inputs | V1 repository `LARDHI/Gradex`, public, tag `v1.0.0`: read `gpa_tracker/grading.py` and its tests, read-only. Phase 01 s4.5 and s11 #2. Source S01 |
| Method | (1) Extract every value of the four tables, with file and line references. (2) For each table, search for a published source with identical values; record each source with a direct reference and date. (3) Re-check the Alfaisal match for `4.0-plus-only` against the source itself. (4) Classify each table: verified against a named source, partly verified, or unverified reference preset. (5) Inventory the rules V1 attaches to each built-in table, as V1 facts with code or test references. (6) State the consequence for R1 |
| Not in scope | Changing V1 or any built-in table; deciding what V2 promises (that is T05, then owner); verifying rules against real policies except where a source for the same policy exists; any claim from the old session's report, which is not evidence |
| Output | Table of values per system; classification per table with sources; rule inventory; R1 consequence; AS-05 answer with evidence level; limitations |
| Acceptance | T02-AC1 to T02-AC7 (section 3) |
| Independent verification | **Required** (high-impact): a verifier re-checks the values against the repository and the cited sources |
| Status | **Blocked on the owner's OQ-05 choice** |
 
### 12.3 T03: Structured competitor comparison
 
| Field | Brief |
|---|---|
| Research question | Which of Gradex's candidate differentiators, and which policy-configuration capabilities, do comparable GPA tools offer, and what can honestly be claimed? |
| Why it matters | Feeds O5, AS-09 and the claims rule (D12: no uniqueness or first-in-market claim without evidence). Phase 01 examined about eight tools, mostly from page descriptions, and found no established differentiator |
| Method | **Step 1 (checkpoint, saved first):** fix the sample and the criteria and save them to the output file before assessing any tool. Sample [PR]: at least 12 tools across at least 4 categories (web calculators, mobile apps, open-source projects, university or learning-platform tools), with the selection method and the reasons for exclusions. Criteria: the candidate differentiators (a) per-course feasibility with explanations, (b) a wide set of configurable policy rules, (c) strict actual versus hypothetical separation, (d) cross-device records with per-user isolation; plus the policy dimensions from T01 (use T01 results if accepted by then, otherwise the dimension list in section 12.1). **Step 2:** assess each tool against each criterion with a source and access date, and state the evidence type (page description, documentation, source code, hands-on use). Hands-on use is not assumed to be available. **Step 3:** revisit the Phase 01 classification with the evidence |
| Not in scope | Recommending scope or features (Phase 03); any uniqueness claim; evaluating quality or popularity beyond what a source states |
| Output | Sample and criteria; comparison matrix with citations; classification review as proposals; limitations including sample representativeness |
| Acceptance | T03-AC1 to T03-AC5 (section 3) |
| Independent verification | **Required** (high-impact, D12): a verifier re-opens the sources behind every "not found" and every "supported" claim that changes the classification |
| Note | Must finish before the Phase 03 cut line |
 
### 12.4 T04: Privacy, security and accessibility requirements
 
| Field | Brief |
|---|---|
| Research question | Which privacy, security and accessibility requirements should Gradex V2 meet, derived from recognized standards and sources, to support its approved goals (cross-device accounts with isolation, real-student testing, public synthetic-data demo)? |
| Why it matters | Feeds O3, O7, AS-07, R3, R4, R7, R8. Accessibility is part of the owner's original track [OS-H] |
| Scope | **Privacy:** consent and data minimization for real testers (R7); deletion on request; data export and deletion for account holders; retention; consent-age considerations; frameworks relevant to a worldwide student audience (D11) [PR: candidates GDPR, other national data-protection laws, and education-record norms; the worker states which it covered and why]. **Security:** per-user data isolation (R3); authentication and authorization requirements; transport security (HTTPS, R4); handling of backups and durability and recovery expectations [PR: candidate reference OWASP ASVS and Top 10]. **Accessibility:** a named standard with a target level [PR: candidate WCAG 2.2 AA] and what it implies for forms, tables, charts and keyboard use. **Separation of real-data testing from the public synthetic-data demo** (AS-07) |
| Method | Primary sources first (standard text, regulator guidance). For each candidate requirement: the source and clause, a plain-language statement, the Phase 01 item it supports (R3, R4, R7, R8, AS-07), and whether it is **derived from the standard** or a **recommendation** |
| Owner-dependent | List separately what cannot be decided from research: budget, hosting constraints, jurisdiction choices (OQ-02). Do not guess |
| Not in scope | Choosing technologies, vendors, libraries or hosting (Phase 05); legal advice; owner decisions |
| Output | Candidate requirement list in technology-neutral, testable wording [PR]; mapping to R-items and assumptions; owner-dependent list; limitations |
| Acceptance | T04-AC1 to T04-AC6 (section 3) |
| Independent verification | **Required** (high-impact): a verifier re-checks the cited clauses and that derived requirements do not overstate the standard |
 
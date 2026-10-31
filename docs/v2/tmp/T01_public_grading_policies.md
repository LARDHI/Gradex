# T01: Public grading policy research

**Status: PARTIAL (6 of at least 12 policies recorded; 6 of at least 6 regions).** Not ready for acceptance. Intended repo path: `docs/v2/tmp/p02/T01_public_grading_policies.md` (assigned path in the manifest: `claude/tmp/p02/T01_public_grading_policies.md`). Written by a worker; not edited into the execution log.

| Field | Content |
|---|---|
| Task ID and title | T01, Public grading policy research |
| Research question | Which grading-policy dimensions and interactions between rules occur across real public university grading policies, so Gradex V2's custom grading requirements can be defined from evidence? |
| Methodology | Policies are chosen one at a time, primary source (the university's own registrar or catalogue page) first. Third-party GPA sites are not used as sources for a policy. Region definition [PR from log 12.0]: world regions (North America; Latin America and Caribbean; Europe; Middle East and North Africa; Sub-Saharan Africa; South Asia; East Asia; Southeast Asia; Oceania; Central Asia). Candidate sample not yet fixed beyond entries P01 to P05. |
| Sources | See each entry. Access date for all: 2026-10-31. |
| Verification status | Unverified. No independent verifier has re-checked anything. |

## Acceptance criteria (T01-AC1 to AC8), current state

| AC | State | Evidence |
|---|---|---|
| AC1 at least 12 policies, at least 6 regions | **Partly** (regions met, policy count not met) | 6 policies, 6 regions (Southeast Asia, North America, Middle East and North Africa, Europe, South Asia, Oceania) |
| AC2 method, region definition, counts stated | Partly | Method and region definition above; counts: Southeast Asia 1 (Singapore 1), North America 1 (Canada 1), MENA 1 (Saudi Arabia 1), Europe 1 (Germany 1), South Asia 1 (India 1), Oceania 1 (Australia 1); no concentration analysis possible yet |
| AC3 direct source, access date, third-party flagged | Met for P01 to P06 (P02 to P05 read only as search excerpts of official pages; P06 main page read in full, secondary pages as excerpts) | Official registrar page cited; third-party sites seen in search were not used |
| AC4 dimensions recorded | Partly | P01 only; retake and rounding not found (stated below) |
| AC5 unspecified rules identified | Partly | P01 only |
| AC6 interactions identified | Partly | P01 only |
| AC7 course loads for AS-01 | Partly | P01 only |
| AC8 R2 / AS-06 implications | **Not met** | Premature with one policy |

## Per-policy entries

### P01: National University of Singapore (NUS), undergraduate and graduate coursework

- Country / region: Singapore / Southeast Asia
- Source: NUS Office of the University Registrar, "Academic Structure & Grading" (non-graduating page, same grading text as the undergraduate page): https://www.nus.edu.sg/registrar/academic-information-policies/non-graduating/academic-structure-grading . Access date 2026-10-31. Language: English, no translation.
- Secondary official PDFs seen only as search excerpts, not fully read: NUS transcript grade legend (https://www.nus.edu.sg/registrar/docs/info/administrative-policies-procedures/transcript-information-grade-legend.pdf) and a Registrar's Office briefing on the Grade-Free Scheme (https://capt.nus.edu.sg/wp-content/uploads/Grade-Free-Scheme_BriefingByRO-1.pdf). Claims taken from these are marked (excerpt).

| Dimension | Finding | Basis |
|---|---|---|
| Scale and points (L1) | 0.0 to 5.0. A+ 5.0, A 5.0, A- 4.5, B+ 4.0, B 3.5, B- 3.0, C+ 2.5, C 2.0, D+ 1.5, D 1.0, F 0.0. Within 5.00, so V1 can store the numbers. | Registrar page |
| Letter forms (L4) | A+ to F with no C- or D-. **A+ and A carry the same points**; the page says A+ is not a higher point value than A. Other letters in use: S, U, CS, CU, IC, IP, AUD, EXE, W, WU (excerpt). | Registrar page; legend (excerpt) |
| Passing / failing (L2) | F is the failing grade (0.0). D+ and D are labelled "Marginal Pass". | Registrar page |
| Non-GPA codes (L3) | CS/CU, EXE, IC, IP, W carry no grade points and are excluded from GPA. Courses with no assigned units or points are excluded from GPA. CS gives units without grade points. | Registrar page |
| Retakes (L5) | **Not found on the page read.** Only IC: if repeated, earlier work is not carried forward. No replace/average rule seen. | Registrar page; gap |
| Rounding (L6) | **Not found on the page read.** | Gap |
| Credits (L7) | Units; 1 unit = 2.5 weekly study hours; a 4-unit course example. Whole-unit values only in the examples seen; fractional units not confirmed or excluded. | Registrar page |
| Table scope (L8) | Different tables inside one university: Law and Undergraduate Dentistry and Medicine are not on the modular grading system; School of Business master's courses use DT 5.00, M 4.00, Pass 3.00, Fail 0.00 (excerpt). | Registrar page; legend (excerpt) |
| Term name changes | From 2023-08-01: module became course, MC became unit, CAP became GPA. No change to computation. | Registrar page |
| Course load (AS-01) | Average of 20 units per semester, about five 4-unit courses; can be higher with Faculty approval. | Registrar page |

**Rules the policy leaves unspecified or inconsistent (AS-10):**
- Retake treatment and GPA rounding are not stated on the page read.
- The S/U (Grade-Free Scheme) letter mapping differs between two official documents seen as excerpts: one says S for C or above and U for D+, D or F; another says S for D or above and U for F. They may be different cohorts or versions; not resolved.

**Interactions between rules that can change one calculation:**
1. Withdrawal timing and F: W between week 3 and recess week is excluded; later withdrawal becomes F, counted in GPA and not S/U-eligible.
2. S/U option and GPA: a letter converted to S or U is removed from GPA while its units may still count toward the degree (excerpt). Briefing example (excerpt): B, C, C, D, F gives 1.70; B, S, S, U, U gives 3.50.
3. A+ equals A in points while remaining a distinct letter on the transcript.
4. CS gives units but no points, so credit counting and GPA denominators differ.

**What V1 could not represent for this policy:** S/U conversion, CS/CU and EXE/IC/IP/W as non-GPA codes, A+ equal to A (possible), different tables inside one student record (L8), and the D+/D "marginal pass" distinction if it matters for progression.

### P02: University of Toronto (U of T), undergraduate and graduate

- Country / region: Canada / North America
- Sources (all official U of T pages, read only as search excerpts, not full pages; access date 2026-10-31; English):
  - University Assessment and Grading Practices Policy, Governing Council, effective 2020-01-01: https://governingcouncil.utoronto.ca/media/8363 (also the 1998 version: https://governingcouncil.utoronto.ca/system/files/import-files/grading3791.html)
  - UTSC Academic Calendar, "Standing in a Course": https://utsc.calendar.utoronto.ca/node/14357
  - Arts & Science Calendar, grading page: https://artsci.calendar.utoronto.ca/node/15
  - Office of the Registrar, "Transcript Grading Scales and Notations": https://www.registrar.utoronto.ca/?p=968 and https://registrar.utoronto.ca/?p=10788
  - Faculty of Information, graduate policies: https://ischool.utoronto.ca/graduate-students/academics/course-policies
  - Wycliffe College (affiliated college) course syllabus, used only to show divisional variation: https://wycliffecollege.ca/sites/default/files/WYT3651HF%20Luther%20and%20Calvin.pdf (college document, not university policy)

| Dimension | Finding | Basis |
|---|---|---|
| Scale and points (L1) | 4.0 scale. A+ 4.0, A 4.0, A- 3.7, B+ 3.3, B 3.0, B- 2.7, C+ 2.3, C 2.0, C- 1.7, D+ 1.3, D 1.0, D- 0.7, F 0.0. Within 5.00. | 2020 policy and 1998 policy (excerpts) |
| Percentage link | Final marks are numeric percentages first; the letter and points derive from the percentage (A+ 90-100, A 85-89, A- 80-84, B+ 77-79, B 73-76, B- 70-72 ... D- 50-52, F 0-49). | UTSC calendar, 2020 policy (excerpts) |
| Letter forms (L4) | A+ to D-, F; designators such as CR, NCR, GWR. A+ equals A in points. | Policy; registrar (excerpts) |
| Passing / failing (L2) | F = fail, 0-49%. | 2020 policy (excerpt) |
| Non-GPA codes (L3) | CR/NCR "generally not factored into the GPA"; GWR and other non-grade symbols have no points. | Registrar; graduate pages (excerpts) |
| Retakes (L5) | **Not found in the excerpts.** | Gap |
| Rounding (L6) | **Not found in the excerpts.** The calendar notes that grade point averages are weighted sums and so do not match the per-course scale exactly. | Arts & Science calendar (excerpt) |
| Credits (L7) | "Course weight values" under "a uniform system of values allowing for the relative values needed by each division" (1998 policy). Whether half-weights exist is not confirmed in what was read. | 1998 policy (excerpt); gap |
| Table scope (L8) | Divisions may use approved alternate scales. Graduate divisions use a truncated letter scale and H/P/FL and CR/NCR scales; graduate transcripts show letters only. The UTSC also has a Pass/Fail scale flagged as not fully compliant with the policy. | 1998 policy; iSchool; governing council note (excerpts) |
| Course load (AS-01) | Not found. | Gap |

**Unspecified or inconsistent rules (AS-10):**
- NCR is excluded from GPA in the general rule, but where NCR is used in the GPA calculation it is shown as "NC%" with 0.0 points (registrar excerpt). An affiliated college's syllabus also states that NCR counts as 0 in GPA. So one university has two treatments of the same code depending on division.
- Retake and rounding rules, and the exact GPA computation details, were not seen.

**Interactions:**
1. Percentage-to-letter conversion with the letter-to-points table: the points come from the letter, so a mark just below a boundary changes the points (for example 84 gives A- 3.7, 85 gives A 4.0).
2. CR/NCR with GPA: the same code may or may not enter GPA by division (see above).
3. Division-specific scale with university-wide GPA: graduate letter scales differ from undergraduate numeric ones.

**What V1 could not represent:** percentage input, CR/NCR with a divisional switch for NCR (0.0 in GPA or excluded), and per-division scales.

### P03: King Saud University (KSU), undergraduate

- Country / region: Saudi Arabia / Middle East and North Africa
- Sources (official KSU pages, read only as search excerpts; access date 2026-10-31; English versions of Arabic-language policy, as published by KSU):
  - KSU Deanship of Admission and Registration, FAQ with a worked GPA example: https://dar.ksu.edu.sa/en/faqs
  - KSU Deanship of Admission and Registration, 2019/2020 second-semester evaluation notice: https://dar.ksu.edu.sa/en/412
  - Regulations of Study and Examinations of Undergraduate Education and Executive Rules of KSU (University Council decision, 1436 H / 2015), hosted by the College of Business Administration: https://cba.ksu.edu.sa/sites/cba.ksu.edu.sa/files/users/user2144/regulations_of_study_and_examinations_of_ksu.pdf (only the definitions and fragments were seen; Appendix B, which the text says holds the grade weights, was not seen)
- Third-party pages seen (leads only, not evidence): scholaro.com, smartcgpa.com, openeducat.org, SFU graduate admissions page. They describe a Saudi 5.0 scale; they are not used for any KSU finding below except where flagged.

| Dimension | Finding | Basis |
|---|---|---|
| Scale and points (L1) | 5.0 scale. Grade points seen in the official worked example: A 4.75, B+ 4.50, B 4.00, C 3.00; the same example shows A with 5.00 for a 96% mark. The full table was not seen. | KSU FAQ (excerpt) |
| Percentage link | Marks are percentages and the symbol and points follow from them (85 gives B+ 4.50; 70 gives C 3.00; 92 gives A 4.75; 80 gives B 4.00; 82 gives B 4.00). | KSU FAQ (excerpt) |
| Letter forms (L4) | Plain and plus letters in the example; whether minus grades exist at KSU was not seen. | Gap |
| Passing / failing (L2) | Not seen in official text. Third-party pages say F is recorded as 1.00 and that DN is a failing code; **unverified for KSU**. | Gap; third-party leads |
| Non-GPA codes (L3) | Temporary NP (no-grade pass) and NF (no-grade fail) for the second semester of 2019/2020, combined with letter grades into a "combined grade". | KSU notice (excerpt) |
| Retakes (L5) | **Not found.** | Gap |
| Rounding (L6) | Example average 48.25 / 12 = 4.0208 is shown as 4.02 (two decimals). Rounding versus truncation cannot be told apart from this example. | KSU FAQ (excerpt) |
| Credits (L7) | "Credit units" per course: 2, 3, 3, 4 in the example; regulation text defines quality points as units times the grade weight. No fractional units seen. | KSU FAQ; regulations (excerpts) |
| Table scope (L8) | Not seen beyond the 2019/2020 temporary system. The preparatory-year GPA is counted in the university GPA. | KSU FAQ (excerpt) |
| Course load (AS-01) | The example semester has 4 courses (12 units); a typical load was not seen. | KSU FAQ (excerpt) |

**Unspecified or inconsistent rules (AS-10):**
- The official FAQ example gives A = 4.75 for 92% and A = 5.00 for 96% (symbol A in both). Either the A+ symbol was dropped in the example or points follow the percentage band rather than the symbol. Not resolved.
- The full grade table, minus grades, the failing code and its points, retakes and the repeat limit were not seen in official text.

**Interactions:**
1. Percentage band with points: points change at percentage boundaries, and the example suggests the points may depend on the percentage band as well as the symbol.
2. Temporary NP/NF system with letter grades for 2019/2020: courses in one semester were combined across two grading modes.
3. Preparatory-year grades counted in the cumulative GPA, so the "semester" boundary for GPA is not only degree courses.
4. If F carries 1.00 (third-party claim, unverified), a failed course adds points to GPA, as the V1 5.0 presets do.

**What V1 could not represent:** NP/NF as non-GPA codes with a combined grade; percentage input with a points scale inside one band; 5.0 tables with an A below the maximum, which V1 can store but must enter manually (A 4.75, A+ 5.00).

### P04: Universität zu Lübeck (Germany), grading scheme for exchange students, with German-university corroboration

- Country / region: Germany / Europe
- Why this university: its published grading scheme PDF had the most complete official text among the German universities found. TUM, KIT, TU Dresden and Frankfurt UAS pages were used only to check that the pattern is general; they are not separate entries.
- Primary source (official, read only as a search excerpt; access date 2026-10-31; English): Universität zu Lübeck, "Benotungsschema / Grading Scheme": https://www.uni-luebeck.de/fileadmin/uzl_international/dokumente/aus_dem_Ausland/Austauschstudenten/grading_scheme_MINT_2011-13.pdf (the file name shows it was written for the 2011-13 period, so it may be out of date).
- Corroborating official pages (excerpts): TUM "Curriculum Analysis" (ECTS and the Bavarian conversion formula) https://www.ls.tum.de/en/ls/studies/application/curriculum-analysis ; TUM grade conversion page https://www.tum.de/en/studies/application/application-info-portal/grade-conversion-formula-for-grades-earned-outside-germany/ ; KIT grading table https://www.intl.kit.edu/istudies/6520.php ; TU Dresden faculty percentage thresholds https://tu-dresden.de/ing/maschinenwesen/ressourcen/dateien/studium/pruefungsamt/formulare_informationen/Noten_D.pdf ; Frankfurt University of Applied Sciences https://frankfurt-university.de/en/studies/international-office/incomings/exchange/grades-and-credits
- Third-party pages seen (leads only): smartcgpa.com, expatrio.com. Not used as evidence except where flagged.

| Dimension | Finding | Basis |
|---|---|---|
| Scale and direction (L1) | **Inverted scale: 1.0 is best, 4.0 is the lowest pass, 5.0 is fail.** Allowed grades: 1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0 and 5.0. Values fit inside 0 to 5, but a higher number is worse. | Lübeck (excerpt) |
| Descriptors | Sehr gut, gut, befriedigend, ausreichend (pass), fail; band limits differ by university (Lübeck, KIT and Frankfurt show different ranges, such as KIT 1.0-1.3 sehr gut, Frankfurt 4.1-5.0 fail). | Lübeck, KIT, Frankfurt (excerpts) |
| Letter forms (L4) | No letters; numbers with German descriptors. | Lübeck (excerpt) |
| Passing / failing (L2) | The pass mark is a numeric threshold (4.0), not a fixed letter F; anything worse than 4.0 fails. | Lübeck, Frankfurt (excerpts) |
| Non-GPA codes (L3) | Not seen. | Gap |
| Retakes (L5) | **Not found.** | Gap |
| Rounding (L6) | Overall classification bands are stated to one decimal (for example 1.0-1.2 "mit Auszeichnung", 1.3-1.5 "sehr gut"), which implies one-decimal reporting. Whether the average is rounded or cut off was not seen in official text; a third-party page says cut off. | Lübeck (excerpt); third-party lead |
| Credits (L7) | ECTS; 1 ECTS = 30 hours; 60 ECTS per academic year; a module is usually 5 ECTS at one university of applied sciences. | TUM, Frankfurt (excerpts) |
| Averaging | Overall classification is the average of module grades weighted by credit points. | Lübeck (excerpt) |
| Percentage link | Some faculties map exam percentages to grades (TU Dresden faculty: 1.0 at 93% or more, 1.3 at 88, 1.7 at 81, 2.0 at 76, 2.3 at 71, 2.7 at 64, 3.0 at 59, 3.3 at 54, 3.7 at 47, 4.0 at 42, 5.0 below 42). | TU Dresden faculty PDF (excerpt) |
| Table scope (L8) | A separate honours scheme for the overall result; foreign grades are converted by the Bavarian formula (TUM). | Lübeck, TUM (excerpts) |
| Course load (AS-01) | TUM: 60 ECTS per academic year, so 30 per semester. With 5-ECTS modules (Frankfurt) that is about 6 modules; this is my arithmetic, not a published figure. | TUM, Frankfurt (excerpts); derived |

**Unspecified or inconsistent rules (AS-10):**
- Lübeck's header row lists local grades 4.3 and 4.7 next to 5.0, but its text says only 1.0 to 4.0 and 5.0 may be given.
- Descriptor bands differ between German universities, so even "Germany" is not one policy.
- Retake treatment, treatment of failed modules in the average, and rounding versus cutting off are not stated in the official excerpts.

**Interactions:**
1. Inverted direction with every "best" and "lowest" notion, with prediction and with any target: a target is a ceiling (at most 2.0), and "best semester" is the lowest number.
2. Credit weighting with a numeric pass threshold: a module at 4.0 passes and earns full credits even though it raises the average.
3. Rounding or cut-off with band limits: 1.25 could land in a different honours band depending on the rule.
4. Foreign-grade conversion (Bavarian formula) with the credit-weighted average.

**What V1 could not represent:** direction (lower is better) in best/lowest semester logic and in prediction; a numeric pass threshold instead of a letter named F; percentage-driven grades; cut-off rather than half-up rounding; conversion from another system.

### P05: Indian Institute of Technology Kanpur (IIT Kanpur), postgraduate rules, with IIT Bombay transcript legend as corroboration

- Country / region: India / South Asia
- Primary source (official, read only as search excerpts; access date 2026-10-31; English): IIT Kanpur, Postgraduate rules, "Grades, Semester and Cumulative Performance Index": https://www.iitk.ac.in/spgc/acreq/2.htm and https://www.iitk.ac.in/spgc/acreq/l6.htm
- Corroboration, lower quality: IIT Bombay legend and layout as printed on individual student transcripts hosted by third parties (for example https://international.iitkgp.ac.in/media/uploads/JDP_Applications/2021/srinivasdiwanji@iitb.ac.in/Srinivas_Diwanji_Transcript.pdf and https://public.websites.umich.edu/~akashpt/papers/akash_transcript.pdf). These are real transcripts hosted by their owners, not IIT Bombay policy pages; I did not find the IIT Bombay rulebook text itself, only a Scribd copy that I did not use. Also seen: IIT (BHU) older ordinance https://www.iitbhu.ac.in/contents/institute/dean/doaa/doc/ordinance_ug_amended_prior_2013.pdf and IIIT Vadodara https://iiitvadodara.ac.in/assets/files/UG_Curriculum_2018 & onwords.pdf (used only to show variation).
- Third-party pages seen (leads only): openeducat.org, findmycollege.com. Not used.

| Dimension | Finding | Basis |
|---|---|---|
| Scale and points (L1) | 10-point scale. IIT Kanpur postgraduate: A 10, B 8, C 6, D 4, E 2, F 0. IIT Bombay transcript legend: AP 10, AA 10, AB 9, BB 8, BC 7, CC 6, CD 5, DD 4, FF 0, FR 0. **Points go above 5.00, so V1 cannot store them.** | IITK page (excerpt); IITB transcripts |
| Letter forms (L4) | Two-letter grades (AA, AB, BB...), one-letter grades, and several codes (AP, FR, DX, PP, NP, AU, W, I, S, X). **AP and AA both 10** at IIT Bombay. | IITK; IITB (excerpts) |
| Passing / failing (L2) | IITK: E and F must be repeated or substituted; D may be repeated under conditions. IIT Bombay: FF and FR both 0 (FR means "fail and repeat"). Failing is more than one code. | IITK; IITB (excerpts) |
| Non-GPA codes (L3) | IITK: S (satisfactory), X (unsatisfactory), I (incomplete). IIT Bombay: W, DX (insufficient attendance), PP, NP, AU carry no points; zero-credit courses show PP. | IITK; IITB (excerpts) |
| Retakes (L5) | **Replace rule:** if a course is repeated or substituted, the old grade stays on the transcript but is not counted in SPI or CPI. | IITK page (excerpt) |
| Rounding (L6) | IIT Bombay transcripts show two decimals; one worked check: 896.0 grade points / 98.0 credits = 9.1429, printed as CPI 9.14. Rounding versus cut-off cannot be told apart from this. | IITB transcript (derived) |
| Credits (L7) | IIT Bombay credits seen: 0.0, 1.0, 2.0, 3.0, 4.0, 6.0, 8.0 and a project of 42.0. **Values above 9 and zero-credit courses occur.** | IITB transcripts |
| Table scope (L8) | IIT Bombay lists SPI and CPI per term, plus separate "CPI (Courses)" and "CPI (Overall)" with project credits counted separately (MA course tag and PR project tag). Other Indian institutes use different letter tables (IIT BHU older ordinance S 10, A 9... F 0; IIIT Vadodara adds DD 4). | IITB transcripts; IITBHU; IIITV (excerpts) |
| Course load (AS-01) | Not found as a policy; the graduate transcript shows terms of 2 to 3 courses. | Gap |

**Unspecified or inconsistent rules (AS-10):**
- IIT Bombay's own rulebook text was not found, so its retake rule is not known; the replace rule is from IIT Kanpur only.
- Grade tables differ between Indian institutes (even among IITs), so "India" is not one policy.
- A transcript term with only a zero-credit course prints SPI 0.00/10 instead of a missing value.

**Interactions:**
1. Retake replacement with credits and CPI: the old grade is excluded from CPI, but it stays on the transcript and the conditions for repeating a D depend on grade.
2. Zero-credit pass courses with SPI: a term with only a zero-credit course gets SPI 0.00 and still leaves CPI unchanged.
3. Project credits with the overall CPI: courses and project are averaged separately and together (CPI Courses vs CPI Overall).
4. AP/AA at 10 with FR/FF at 0: two failing codes with different meaning (repeat required or not).

**What V1 could not represent:** points above 5.00; multiple failing codes (FF, FR, E, F); replace-on-retake; zero-credit courses and credits above 9; separate course and project averages; two-letter and non-letter codes such as AA, DX, PP.

### P06: University of New South Wales (UNSW Sydney), undergraduate and postgraduate coursework

- Country / region: Australia / Oceania
- Primary source (official, read in full; access date 2026-10-31; English): UNSW Current Students, "Guide to UNSW grades": https://www.unsw.edu.au/student/managing-your-studies/academic-life/grades-results-academic-standing/guide
- Secondary official sources (search excerpts only, not fully read; claims taken from them are marked (excerpt)): UNSW student grade page https://student.unsw.edu.au/grade ; UNSW "Maximum repeat fails" https://www.unsw.edu.au/student/managing-your-studies/academic-life/grades-results-academic-standing/academic-progression/repeat-fails ; UNSW Optometry and Vision Science progression policy (2022) https://www.unsw.edu.au/content/dam/pdfs/medicine-health/optometry-vision-science/resources/2022-07-about/2022-07-progression-policy-3952-final.pdf
- Third-party pages seen (leads only, not used as evidence): openeducat.org (WAM and GPA explainer).

| Dimension | Finding | Basis |
|---|---|---|
| Scale and points (L1) | **No grade points and no GPA.** UNSW states it does not use a GPA system. Results are marks from 0 to 100 and a grade is derived: HD 85-100, DN 75-84, CR 65-74, PS 50-64, FL 0-49. | Guide page |
| Summary statistic | WAM = sum(mark x units) / sum(units). Term WAM, cumulative WAM and faculty WAM exist. Each faculty has its own method for honours and medals. Worked example on the page: 81.625. | Guide page |
| Letter forms (L4) | Two-letter codes (HD, DN, CR, PS, FL) plus about 25 other codes (AF, AW, NC, PW, SY, XE and others). Merged older institutions used A to D; some pre-2002 MBA cohorts used A/B/C. | Guide page |
| Passing / failing (L2) | FL (0-49) is the failing grade. AF (absent fail) and UF (unsatisfactory fail) are further fail codes. PC (pass conceded) was discontinued after Summer Term 2015/6. | Guide page |
| Non-GPA codes (L3) | Not in WAM: SY, XE, NA, RS, AS, NF, NC, RD, EC, AW, PW. Only results with a numerical mark are included. **AF is the exception:** since Semester 1, 2003 it is assigned a mark of zero and included. | Guide page |
| Nominal marks | A grade entered without a numeric mark gets a nominal mark in WAM: PS 55, CR 70, DN 80, HD 90, FL 25. Under the SY/FL no-mark basis, FL is not included at all. | Guide page |
| Retakes (L5) | **Not stated on the guide page.** One UNSW faculty document (Optometry, progression to Stage 4) says that when a course is attempted more than once all marks are included; its example is a 36 FL then a 64 PS, both counted (excerpt). This is faculty-level and for a progression WAM, not a university-wide rule. | Optometry policy (excerpt); gap |
| Rounding (L6) | **Not found.** The page example (81.625) is shown unrounded. | Gap |
| Credits (L7) | Units of credit (UOC); the example uses 6 and 3 UOC. Fractional UOC not confirmed or excluded. | Guide page |
| Table scope (L8) | Rules differ by period and faculty: PW treatment changed by year, faculties have their own WAM methods for honours and medals, and merged older institutions used other scales. Transfer-credit marks from other institutions are excluded from WAM; since Semester 1, 2016 transfer credit from another UNSW program counts. | Guide page |
| Course load (AS-01) | **Not found on the pages read.** | Gap |

**Rules the policy leaves unspecified or inconsistent (AS-10):**
- No university-wide retake rule and no WAM rounding rule were found.
- The only retake evidence is one faculty's progression WAM, so it may not be the same as the general WAM.
- No typical course load was found.

**Interactions between rules that can change one calculation:**
1. Two parallel calculations: AW, NC and, in some periods, PW are excluded from WAM but counted as failed courses in academic standing. One course changes one result and not the other.
2. Policy change over time: PW is never in WAM, but counted as a fail in standing from 2014 to 2020 and not from 2021. A record spanning several years needs date-dependent rules.
3. Nominal marks with numeric marks: a grade-only result gets a fixed mark (FL = 25), but FL on the SY/FL no-mark basis is excluded.
4. AF as zero with other fail-like codes: AF counts as zero in WAM while AW and NC do not.
5. Retake with WAM: if both attempts count, a failed first attempt permanently lowers the average, unlike a replace rule (compare P05).
6. External GPA conversion: the page says AW is treated as a fail for GPA by other bodies (for example UAC). That is a conversion outside UNSW's own system.

**What V1 could not represent:** a 0-100 mark scale with a weighted average instead of grade points; nominal marks per grade band; AF as a zero while other fail-like codes are excluded; date-dependent rules; two parallel calculations (WAM and academic standing); a faculty-specific WAM.

## Remaining work (not started)

- Select at least 6 more policies (the 6-region minimum is now met), each from the university's own page.
- Record retake, rounding and fractional-credit rules per policy.
- Independent verification of anything feeding R2 or AS-04 (high-impact).

## Limitations

- Six policies, six regions: no representativeness claim is possible.
- P06: retake and rounding rules not found at university level; Sydney and other Australian universities were not entered and differ from UNSW.
- The Registrar page was read in full; the two PDFs only through search excerpts.
- Search results from commercial sites (grading-scale pages and calculators) describing NUS and NTU appeared; they were not used as evidence.
- NTU, mentioned in those commercial pages, has not been checked against an NTU source.

# T01: Public grading policy research

**Status: PARTIAL (11 of at least 12 policies recorded; 10 of at least 6 regions, all ten regions of the definition covered).** Not ready for acceptance. Intended repo path: `docs/v2/tmp/p02/T01_public_grading_policies.md` (assigned path in the manifest: `claude/tmp/p02/T01_public_grading_policies.md`). Written by a worker; not edited into the execution log.

| Field | Content |
|---|---|
| Task ID and title | T01, Public grading policy research |
| Research question | Which grading-policy dimensions and interactions between rules occur across real public university grading policies, so Gradex V2's custom grading requirements can be defined from evidence? |
| Methodology | Policies are chosen one at a time, primary source (the university's own registrar or catalogue page) first. Third-party GPA sites are not used as sources for a policy. Region definition [PR from log 12.0]: world regions (North America; Latin America and Caribbean; Europe; Middle East and North Africa; Sub-Saharan Africa; South Asia; East Asia; Southeast Asia; Oceania; Central Asia). Candidate sample not yet fixed beyond entries P01 to P11. |
| Sources | See each entry. Access date for all: 2026-10-31. |
| Verification status | Unverified. No independent verifier has re-checked anything. |

## Acceptance criteria (T01-AC1 to AC8), current state

| AC | State | Evidence |
|---|---|---|
| AC1 at least 12 policies, at least 6 regions | **Partly** (regions met, policy count not met) | 11 policies, 10 regions (Southeast Asia, North America, Middle East and North Africa, Europe, South Asia, Oceania, East Asia, Latin America and Caribbean, Sub-Saharan Africa, Central Asia) |
| AC2 method, region definition, counts stated | Partly | Method and region definition above; counts: Southeast Asia 1 (Singapore 1), North America 1 (Canada 1), MENA 1 (Saudi Arabia 1), Europe 1 (Germany 1), South Asia 1 (India 1), Oceania 1 (Australia 1), East Asia 2 (South Korea 1, Japan 1), Latin America and Caribbean 1 (Chile 1), Sub-Saharan Africa 1 (Nigeria 1), Central Asia 1 (Kazakhstan 1); nine regions have one policy and East Asia has two, so no concentration analysis is possible |
| AC3 direct source, access date, third-party flagged | Met for P01 to P11 (P02 to P05 read only as search excerpts of official pages; P06 main page read in full, secondary pages as excerpts; P07 regulation text read in full, other pages in full or as excerpts as stated; P08 regulation read in full; P09 regulation read in full, one comparison page as an excerpt; P10 sections 2.17 and 2.24 of the Academic Policy read in full as web pages, the full PDF not readable; P11 two official pages read in full, six more official pages as excerpts) | Official registrar page cited; third-party sites seen in search were not used |
| AC4 dimensions recorded | Partly | P01 to P11; retake and rounding not found for several policies (stated per entry) |
| AC5 unspecified rules identified | Partly | P01 to P11 |
| AC6 interactions identified | Partly | P01 to P11 |
| AC7 course loads for AS-01 | Partly | P01, P03 (example only), P04 (derived), P07, P08 (workload stated, typical course count derived), P09 (unit load stated), P10 (summer load only); P11 has none; gaps for the others |
| AC8 R2 / AS-06 implications | **Not met** | Premature with eleven policies |

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

### P07: Seoul National University (SNU), undergraduate (graduate rules only touched)

- Country / region: South Korea / East Asia
- Why this university: its grading regulation is published in a Korean-English comparison edition, so the full rule text (retakes, rounding, S/U, incomplete) could be read directly.
- Primary source (official regulation, **read in full**; access date 2026-10-31): Seoul National University, Office of Academic Affairs, "Seoul National University Academic Grading Regulations (Kor-Eng Translation Comparison)", Articles 1 to 12 and the grade conversion table. The copy read is hosted by an SNU unit, the College of Architecture, and uploaded in 2022: https://architecture.snu.ac.kr/wp-content/uploads/2022/12/20221207_055811.pdf . **It may not be the latest version.** The document states that the Korean original prevails over the English translation, and I did not check the Korean current text separately.
- Secondary official pages: SNU Office of Global Affairs, "Credit & Grade" (read in full, page modified 2026-07-03): https://oga.snu.ac.kr/isss/academics-for-students/credit-grade/ . SNU main-site grading page (Korean, search excerpt only): https://www.snu.ac.kr/academics/resources/certificate/grading . A College of Architecture transcript notice saying students can mark GPA on a 4.0 or 4.5 scale (search excerpt only): https://architecture.snu.ac.kr/wp-content/uploads/2022/10/20221028_021436.pdf
- Third-party pages seen (leads only, not used): student-newspaper articles about retake policy at other Korean universities, and a spam page about forged transcripts. Other Korean universities (Korea University, Yonsei, Seoul Tech, University of Seoul) appeared in results with different scales (4.5, with different retake caps); they are not entries and show that "South Korea" is not one policy.

| Dimension | Finding | Basis |
|---|---|---|
| Scale and points (L1) | **4.3 scale.** A+ 4.3, A0 4.0, A- 3.7, B+ 3.3, B0 3.0, B- 2.7, C+ 2.3, C0 2.0, C- 1.7, D+ 1.3, D0 1.0, D- 0.7, F 0. Within 5.00, so V1 can store the numbers. | OGA page; regulation conversion table |
| Alternative scales | The regulation's table converts letters and GPA to 4.0, 4.5 and 100-point scales. On the official 4.0 conversion **A+ and A0 are both 4.0**; on the 4.5 conversion A+ 4.5, A0 4.2, A- 3.9, B+ 3.5, B0 3.2, B- 2.9, C+ 2.5, C0 2.2, C- 1.9, D+ 1.5, D0 1.2, D- 0.9. A two-decimal GPA is converted to a percentage by interpolation (example in the text: 3.25 gives 88.5; 4.27 gives 99.4). | Regulation Art. 11 and table |
| Letter forms (L4) | A to D each split into +, 0 and -, and F alone. **The middle grade is written with a zero ("A0", "B0").** S and U exist for designated courses; W, I also appear. | Regulation Art. 3, 5 |
| Passing / failing (L2) | F is the failing grade in the table (0). Where a course is S/U, U is the fail. **Whether D- or other low letters count as passing for credit was not stated in the text read.** | Regulation; gap |
| Non-GPA codes (L3) | S/U courses are excluded from GPA (Korean main-site excerpt: designated courses get S or U and are excluded from the calculation). A withdrawal approved by the instructor gives no grade and shows W. A missing grade or I at the deadline becomes F (U for S/U courses). | Regulation Art. 3, 5; main site (excerpt) |
| Retakes (L5) | **Replace-with-cap rule.** Undergraduates may retake a course (same or a replacement course) if the earlier grade is C+ or lower, or U. The retake grade is capped at A0, and **the new grade replaces the previous one.** | Regulation Art. 7 |
| Rounding (L6) | GPA = sum of (course credits x grade points) divided by total credits, **cut off (truncated) at two decimals**; the English text says "rounded down". Ties in ranking are broken by total grade points, then total credits, then number of graded courses. | Regulation Art. 10 |
| Credits (L7) | 15 lecture hours = 1 credit; a course is generally 1 to 3 credits and typically 3. Whole credits in all examples seen; fractional credits not confirmed or excluded. | OGA page |
| Table scope (L8) | One main letter table, but the same record is reported on 4.3, 4.0, 4.5 and 100-point scales by official conversion. Graduate and law-school rules differ (the regulation points to a separate promotion regulation for colleges with year-repeat rules). | Regulation Art. 7, 11 |
| Relative grading | For undergraduate courses the guideline distribution is A 20-30%, B 30-40%, C or lower 30-50%; an instructor may use a different ratio. This affects who gets a grade, not the calculation. | Regulation Art. 3 |
| Course load (AS-01) | Students can take up to 18 to 21 credits per semester; exchange and visiting students up to 18; SNU recommends at least 6. A typical course is 3 credits, so about 5 to 7 courses at the maximum. The last figure is my arithmetic, not a published number. | OGA page; derived |

**Rules the policy leaves unspecified or inconsistent (AS-10):**
- **Denominator wording.** The Korean text divides by 신청학점 (credits registered or applied for), while the English translation says "total number of credits". If these differ, courses with no grade (W, I, S/U) could change the denominator. Not resolved; the Korean original prevails.
- The pass/fail line below F, and whether D- earns credit, were not seen.
- The 4.3 table on the OGA page and in the regulation agree with each other. The percentage columns agree too (A+ 100, A0 96, A- 93 ... C+ 79 ... D- 63), but the regulation also shows a range of percentage values per letter.
- The copy of the regulation read is from 2022 and the English is a translation.

**Interactions between rules that can change one calculation:**
1. **Truncation versus half-up:** a GPA of 3.259 shows 3.25 here and 3.26 under V1's rule; the same record gives different displayed values, and ranking ties depend on the truncated value or on the tie-break chain.
2. **Retake replace with a cap:** the old grade drops out of GPA, but the new grade cannot exceed A0, so the best possible result is lower than a first-time A+. Eligibility depends on the old letter (C+ or lower, or U).
3. **S/U and the denominator:** S/U courses give no grade points and are outside the GPA, while credits may still count toward the degree; the denominator wording above matters here.
4. **I and withdrawal timing:** an incomplete turns into F (or U) at the deadline and then counts in GPA, whereas an approved withdrawal (W) does not.
5. **A+ and A0 on conversion:** a 4.3 student with all A+ and a student with all A0 both show 4.0 on the 4.0 scale but 4.5 and 4.2 on the 4.5 scale, so the conversion target decides whether the two letters are distinguishable.
6. **Percentage interpolation:** the percentage equivalent of a GPA depends on a table with per-step values, not one formula.

**What V1 could not represent:** letters with a zero designator ("A0", "B0"; V1 custom letters allow only letters plus an optional + or -); truncation instead of half-up rounding; replace-on-retake with a grade cap and an eligibility threshold; S/U as non-GPA codes; reporting one record on several official scales; I and W as time-dependent codes; the ranking tie-break chain.

### P08: Universidad de Santiago de Chile (USACH), undergraduate

- Country / region: Chile / Latin America and Caribbean
- Why this university: its general undergraduate regulation is one short official decree that I could read in full, and it states the scale, rounding, attempt limit and the two averages in one place. Other Chilean universities appeared in results (Universidad de Chile, UTEM, Universidad de los Andes, UDD) and all use the same 1.0 to 7.0 scale with a 4.0 pass mark, but their regulations were not read and they are not entries. Universidad de Chile's undergraduate regulation (D.U. 0017946 of 2008) was found only as a search excerpt.
- Primary source (official, **read in full**; access date 2026-10-31; Spanish, my translation): Universidad de Santiago de Chile, Rectoría, Exento 002563 of 2019-05-02, "Reglamento General de Régimen de Estudios de Pregrado", Articles 1 to 27 and one transitional article: https://www.vra.usach.cl/sites/vra/files/paginas/reglamento_general_pregrado_2563_del_02-05-2019_version_2_1.pdf . Approved 2019, so later amendments may exist and were not checked. The text says each faculty issues a complementary regulation (Art. 2) that was not read.
- Third-party pages seen (leads only, not used): none relied on. A Universidad del Bío-Bío annex and a Universidad de Chile admissions guide with formulas for converting foreign grades to the Chilean scale were seen as excerpts; they are conversion tools, not USACH policy.

| Dimension | Finding | Basis |
|---|---|---|
| Scale and points (L1) | **No letters and no grade points.** Course grades are numbers from 1.0 to 7.0 with one decimal; 4.0 is the minimum pass. Named bands: 7.0 Excelente, 6.0 Muy Bueno, 5.0 Bueno, 4.0 Suficiente, 3.0 Insuficiente, 2.0 Deficiente, 1.0 Malo. **Values above 5.00, and a minimum of 1.0 rather than 0**, so V1 cannot store them. | Art. 10 |
| Letter forms (L4) | None; numbers only. | Art. 10 |
| Passing / failing (L2) | Pass at 4.0 or above, a numeric threshold, not a letter F. A failed course keeps its real number (1.0 to 3.9). | Art. 10, Art. 3(h) |
| Non-GPA codes (L3) | **Not found** as grade codes. Withdrawal is by registration: a course can be dropped in the first four weeks. A temporary leave (retiro temporal) treats all the semester's courses as not registered and cancels all partial grades. | Art. 7, 18 |
| Retakes (L5) | **Every attempt counts, with an attempt limit.** The cumulative weighted average includes all courses taken, "passed and failed". A course may be taken at most twice; failing the second attempt eliminates the student from the program. First-level semester courses may be taken three times. Failed courses must be re-registered first. | Art. 3(h), 7, 14 |
| Rounding (L6) | Each course grade is rounded to one decimal at the nearest value, **half up at the second decimal** (the text gives 3.94 or lower becomes 3.9, and 3.95 or higher becomes 4.0). **How the cumulative averages are rounded is not stated.** | Art. 10 |
| Credits (L7) | Two credit types: TEL credit (one 45-minute teaching hour per week for the term) and SCT-Chile (one SCT = 30 hours of total work). The target load is about 30 SCT per semester (900 hours). Which credit type weights the averages is not stated ("su correspondiente número de créditos"). A semester is 17 weeks. Fractional credits not confirmed or excluded. | Art. 3(d), 3(e) |
| Averages | **Two averages with different rules.** (a) Promedio ponderado acumulado: sum of (final grade x credits) over all courses taken, passed and failed, divided by credits taken. (b) Promedio de aprobación: simple (unweighted) average of the grades of passed courses only, divided by their number. Final degree grade = the approval average combined with the thesis grade by plan-specific weights. Graduation ranking = 40% passed-course weighted average plus 60% titling grade. | Art. 3(h) to 3(k) |
| Table scope (L8) | One scale university-wide, but each faculty has its own complementary regulation (Art. 2) and plans set their own weights. Theory plus laboratory courses are graded in two parts. | Art. 2, 12 |
| Course load (AS-01) | Minimum 2 courses per regular term; target about 30 SCT per semester. A typical course count is not stated. | Art. 3(e), 7 |

**Rules the policy leaves unspecified or inconsistent (AS-10):**
- **Theory plus laboratory:** the final grade is the arithmetic or weighted average "provided both are above four"; otherwise it equals the lower one and the course is failed at once. A grade of exactly 4.0 is a pass elsewhere, so whether "above four" means 4.0 or more or strictly more than 4.0 is unclear. Only the failed part is repeated, and failing it again counts as a second failure.
- Which credits (TEL or SCT) weight the cumulative average, and how the two averages are rounded.
- The attempt limit says "approval in two opportunities", but the text does not say whether a retaken course's earlier failed grade stays in the weighted average; Art. 3(h) says failed courses are included, which points to yes.
- Faculty regulations, which can add rules, were not read.

**Interactions between rules that can change one calculation:**
1. **Two averages with different treatment of failures:** a failed first attempt lowers the weighted cumulative average permanently but never enters the approval average. One student record gives two different headline numbers.
2. **Attempt limit with the average:** a second failure removes the student, so the average of a failing student at that point is not used for a degree; first-level courses allow a third attempt.
3. **Rounding at course level only:** each course is rounded to one decimal before it is weighted, so the average is built from already-rounded values.
4. **Theory/lab rule with the course grade:** a part below the pass mark sets the course grade to the lower part regardless of the other, so the weighted formula is overridden.
5. **Weighted versus simple averages:** the approval average ignores credits, the cumulative average uses them, so a high-credit and a low-credit course count the same in one and differently in the other.
6. **Temporary leave:** cancels partial grades of the semester and the period is excluded from the permanence count, so a term can vanish from the record.

**What V1 could not represent:** a 1.0 to 7.0 scale (points above 5.00, minimum above 0); numeric grades with no letters; a numeric pass mark; two different averages (weighted over all attempts and simple over passed courses); an attempt limit with elimination; rounding of the course grade to one decimal at entry; theory/lab split grading; a degree grade made from an average and a thesis by plan weights.

### P09: University of Lagos (UNILAG), undergraduate degree regulations as published by its Institute of Continuing Education

- Country / region: Nigeria / Sub-Saharan Africa
- Why this university: it is a federal university on the Nigerian 5-point scale, and its regulations are published as a short official text that could be read in full. A second Nigerian university found in results (University of Ibadan) uses a different scale, which shows that "Nigeria" is not one policy.
- Primary source (official, **read in full**; access date 2026-10-31; English): University of Lagos, Institute of Continuing Education, student guide, "Regulations for the Award of Undergraduate Degrees" (General Regulations for Unit Course / Course Credit System, clauses 1 to 25) and examination instructions: https://ice.unilag.edu.ng/resources/studentguide.pdf . The document is undated in the text read (one clause says "effective from 2003/2004 session"). **Clause 22 refers to "a Bachelor's degree of the Institute of Continuing Education, University of Lagos", so it may be written for that institute's programmes and not for the whole university.** I did not find the main UNILAG regulation text.
- Official comparison page (search excerpt only): University of Ibadan, Faculty of Social Sciences, B.Sc. Political Science regulations: https://socsc.ui.edu.ng/node/28 . It shows a grade-point scale of A 4, B 3, C 2, D 1, E 0 with the same percentage bands (70-100, 60-69, 50-59, 45-49, 0-44). Used only to show variation inside one country.
- Third-party pages seen (leads only, not used as evidence): a Wikipedia article, smartcgpa.com, openeducat.org, studentship.com.ng and a Scribd copy of the same student guide. They describe "NUC-regulated" rules (two attempts per failed course, carry-over, a "best grade replaces" option) that are **not in the UNILAG text I read and are unverified**.

| Dimension | Finding | Basis |
|---|---|---|
| Scale and points (L1) | **5.0 scale built from percentage marks.** 70-100 A 5.00; 60-69 B 4.00; 50-59 C 3.00; 45-49 D 2.00; 40-44 E 1.00; 0-39 F 0.00. Within 5.00, so V1 can store the numbers. | Clause 18(b) |
| Percentage link | Each course is marked out of 100 first; the letter and points derive from the mark. Continuous assessment is 30% to 50% of the mark unless the Faculty Board decides otherwise. | Clause 18(a), 18(b) |
| Letter forms (L4) | A to F **including E, no plus or minus.** Extra codes: AUD (audited), EX (exempted), W (withdrawal), I (incomplete), P (pass). | Clause 18(b), 18(c) |
| Passing / failing (L2) | The minimum pass mark is 40%, so **E (1.00) is a pass and only F fails.** | Clause 18(a) |
| Non-GPA codes (L3) | University course requirements (for example the GST courses) must be passed but are **not counted in degree classification**. Pass/Fail courses are also excluded from classification. AUD and EX carry no marks. | Clause 14(d), 24 |
| Retakes (L5) | **Not found.** An Incomplete may be repeated "without any penalty". Clause 24 says all courses a student takes count for classification, which suggests failed courses count, but no replace, best-grade or average rule is stated. | Clause 18(d), 24; gap |
| Rounding (L6) | **Not found.** CGPA = sum of (points x units) over all courses taken divided by total units. The classification bands are written to two decimals with gaps between them (see below). | Clause 24 |
| Credits (L7) | Course units: one unit = fifteen one-hour lectures (or fifteen three-hour labs). Courses carry 1 to 4 units; **fractional units are not allowed.** | Clauses 7, 8 |
| Table scope (L8) | The page does not say whether it covers the whole university or only the Institute's programmes. Nigerian universities differ: University of Ibadan's Political Science page uses a 4-point scale with E at 0 (excerpt). | Clause 22; UI page (excerpt) |
| Course load (AS-01) | Minimum 16 and maximum 24 units per semester; a final-year student needs at most 48 outstanding units. Degree totals by programme length: 76 units (3 years), 96 (4), 128 (5), 160 (6). Whole units only. | Clauses 11, 12, 22 |
| Academic standing | In good standing while the semester GPA and the CGPA are both at least 1.00. Below 1.00: warning, then probation, then withdrawal, by several GPA/CGPA combinations. | Clause 19, 20, 25 |
| Degree classes | CGPA bands: First 4.50-5.00; Second Upper 3.50-4.49; Second Lower 2.40-3.49; Third 1.50-2.49; Pass 1.00-1.49. A student who passes all required units with a final CGPA below 1.0 may still be awarded a pass degree. | Clause 24 |

**Rules the policy leaves unspecified or inconsistent (AS-10):**
- **Gaps between classification bands:** bands end at 4.49, 3.49, 2.49 and 1.49 and the next begins at 4.50, 3.50, 2.40 and 1.50, so a CGPA such as 4.495 or 3.495 is in no band unless the CGPA is rounded or truncated to two decimals first. The text does not say which. Also the Second Lower band starts at 2.40, not 2.50, so the Third Class band (1.50-2.49) overlaps it between 2.40 and 2.49.
- **Standing rules contradict themselves.** Clause 20(i) says "GPA is at least 1.00 therefore, probation", which does not make sense for the case it describes (a first-semester GPA below 1.00); clause 20(ii) describes a GPA at least 1.00 and also "less than 1.00". I could not tell which wording is the intended rule. I did not correct it.
- Retake, repeat limit and rounding rules are not stated; "withdraw" appears both as a student action (W) and as an enforced outcome.
- The regulation's scope (Institute only or whole university) and date are unknown.

**Interactions between rules that can change one calculation:**
1. **Withdrawal timing and F:** a withdrawal up to and including the seventh week carries no penalty (W), and a later one is deemed a fail, which then counts in GPA at 0.00.
2. **Classification versus passing:** GST and other University course requirements must be passed for the degree but are left out of CGPA, so a student can graduate with a course that never enters the classification.
3. **Failing a course and the denominator:** F adds units but no points to the denominator, as in V1's 4.0 presets, but here F is 0.00, not 1.00 as in V1's 5.0 presets.
4. **Percentage band and points:** a mark of 59 gives C 3.00 and 60 gives B 4.00, so one mark changes the points by a full point.
5. **CGPA threshold and standing:** the 1.00 limit applies to both GPA and CGPA, so one semester's result and the cumulative result can put a student in different states in the same term.
6. **Rounding with band edges:** see the gaps above.
7. **Pass degree below 1.00:** a CGPA under the lowest band can still lead to a degree.

**What V1 could not represent:** a 5.0 table with F at 0.00 (V1's built-in 5.0 tables use F = 1.00; a custom table can hold 5.00 to 0.00 but only by manual entry); percentage input; P, AUD, EX, W and I as non-GPA codes; courses that count toward graduation but not toward CGPA; Pass/Fail courses; unit totals by programme length; academic-standing and withdrawal rules driven by GPA and CGPA; classification bands with gaps and an overlap.

### P10: Al-Farabi Kazakh National University (KazNU), undergraduate

- Country / region: Kazakhstan / Central Asia
- Primary source (official, read in full as web pages; access date 2026-10-31; English): Al-Farabi KazNU Academic Policy, section 2.17 "Assessment of learning outcomes, appeal, retaking of exams" (clauses 2.17.1 to 2.17.47): https://www.kaznu.kz/en/20573/page ; and section 2.24 "Transfer from one year of study to the next one, repeated and additional study" (clauses 2.24.1 to 2.24.12): https://www.kaznu.kz/en/20580/page . The pages carry no edition date. The university publishes the Academic Policy as numbered editions (2022 first edition, 2024-2025, 2025-2026 third edition, each a PDF of about 27 to 29 pages); **the 2025-2026 PDF could not be read because the site blocks automated access, so I do not know whether the web pages match the current edition**, and I did not read the other sections of the policy (credits, GPA computation, definitions).
- Third-party pages seen (leads only, not used as evidence): scholaro.com, gpacalculator.net, a Scribd copy of another Kazakh university's transcript (it shows a "D 1.0" row where the KazNU page shows "D-"), and a sample transcript hosted on a commercial site. Other Kazakh universities (Nazarbayev University, Asfendiyarov Medical University) use the same style of table in results seen as excerpts; they are not entries.

| Dimension | Finding | Basis |
|---|---|---|
| Scale and points (L1) | **100-point score mapped to a 4.0 scale.** A 4.0 (95-100); A- 3.67 (90-94); B+ 3.33 (85-89); B 3.0 (80-84); B- 2.67 (75-79); C+ 2.33 (70-74); C 2.0 (65-69); C- 1.67 (60-64); D+ 1.33 (55-59); **D- 1.0 (50-54), as printed**; FX 0.5 (25-49); F 0 (0-24). Within 5.00. | 2.17.6 |
| Letter forms (L4) | **No A+**: the top letter A starts at 95. D appears as D+ and D- only (no plain D) in the table read. Special codes: AU (audit), I (incomplete), FX (final-exam fail), F. | 2.17.6, 2.17.10 to 2.17.14 |
| Passing / failing (L2) | "Positive" grades are A to D (scores 100 to 50). **Two failing grades:** FX (25-49) and F (0-24). FX can only be given for the final examination. **FX carries 0.5 points, not 0.** | 2.17.6 |
| Component rule | Ongoing and mid-term work counts 60% and the final exam 40%. **A final course grade is calculated only if the student has positive grades on both the interim and final assessments.** | 2.17.3, 2.17.4 |
| Non-GPA codes (L3) | AU gives no final grade and the student studies without grade. I is given when the student scored at least 50 points on interim work but missed the final for a documented reason; if not completed within 45 days after the session, it becomes F. | 2.17.10, 2.17.14, 2.17.18 |
| Retakes (L5) | **Replace rule with attempt limits.** AU and F can be changed by repeated study; all attempts stay in the transcript, **but GPA is calculated from the last grades received.** Retake allowed at most two times and only on a paid basis. FX allows a paid retake of only the final exam; F requires re-studying the course. A third failed final exam (FX or F) means expulsion. A positive grade cannot be raised by retaking the exam in the same session, but students below the yearly GPA threshold may re-study courses in summer to raise GPA. | 2.17.29 to 2.17.34, 2.17.39, 2.17.42, 2.17.44 |
| Rounding (L6) | **Not found** in the sections read. | Gap |
| Credits (L7) | Credits exist (summer semester up to 15 credits, 2 to 3 disciplines) but their definition and whether fractional credits exist were not seen. | 2.24.10, 2.24.11; gap |
| Table scope (L8) | One scale in the section read. Study funded by a state grant and paid study follow different consequences for failing (see below). | 2.17.46, 2.17.47 |
| Standing and progression | Transfer to the next year requires the program's credits and a yearly threshold GPA set by the Academic Senate; **the threshold value is not stated.** Any academic debt blocks transfer; debts must be cleared by August 25. | 2.17.45, 2.24.1 to 2.24.5 |
| Course load (AS-01) | Summer: not more than 2 to 3 repeated or additional disciplines (up to 15 credits). The regular semester load was not seen. | 2.24.10, 2.24.11; gap |
| Other | A state scholarship needs all exams passed with A to C+ (as printed), and replaced FX grades do not block it. An exam appeal can raise but never lower the exam grade. An exam rule violation gives an automatic F. | 2.17.26, 2.17.36, 2.17.47 |

**Rules the policy leaves unspecified or inconsistent (AS-10):**
- **D versus D-.** The table prints "D+" 1.33 and "D-" 1.0 with nothing between; a plain D at 1.0 is the more likely meaning (the third-party transcript shows D 1.0), but the official text says D-. Not resolved.
- **Scholarship wording** lists the letters as "A", "A-", "B +", "B", "B-", C + "good", with misplaced quotation marks and the grade "good" matching B+ to B- in the traditional scale, so whether C+ is meant to qualify is unclear.
- **"Positive" and "unsatisfactory"** are defined by letter band, but 2.17.4 requires positive grades on both parts; whether a failed interim part gives an automatic FX or F, and with what points, is not stated.
- Rounding of GPA, the GPA formula, the threshold GPA per year, the credit definition and the regular credit load were not seen.
- The clause 2.17.24-2.17.26 appeal rule says a committee may add points but not lower the grade; how that interacts with FX is not stated.

**Interactions between rules that can change one calculation:**
1. **FX at 0.5 versus F at 0:** two different failing grades with different points; an FX can be repaired by a paid final-exam retake without re-studying, an F requires re-study, so the same failing course can end in different GPA values.
2. **Replace on retake with a full transcript:** earlier grades stay on the transcript but only the last grade enters GPA, so the transcript and the GPA disagree on purpose.
3. **Incomplete timing:** I becomes F 45 days after the session, so a record changes with the calendar even with no new exam.
4. **60/40 split with the positive-grade condition:** a high interim mark cannot offset a failed final; the course has no calculated final grade at all in that case.
5. **Percentage band edges:** a score of 94 gives A- (3.67) and 95 gives A (4.0).
6. **GPA threshold and progression:** a yearly GPA below the threshold sends the student to a repeated year on a paid basis, and a state-funded student loses the grant.
7. **Scholarship eligibility with replaced FX:** a replaced FX does not count against the scholarship, so eligibility depends on history, not only on current grades.

**What V1 could not represent:** two failing grades (FX at 0.5 and F at 0, V1 lets only F fail); a 4.0 scale with A at 4.0 and no A+; percentage input with a 60/40 component weighting and a pass-both condition; I and AU as codes with deadlines; replace-on-retake with a retake limit and expulsion; year-by-year GPA thresholds for progression; paid and state-funded study states.

### P11: Waseda University (Japan), undergraduate (university-wide GPA notice and the Faculty of Science and Engineering FAQ, with school-level variation)

- Country / region: Japan / East Asia (second East Asia entry; P07 is South Korea)
- Why this university: Waseda publishes its GPA rule in an official bilingual notice, and its schools publish their own grade tables, so school-level variation inside one university can be seen.
- Primary sources (official; access date 2026-10-31; English with Japanese alongside):
  - Waseda University, "Notification of the GPA System at Waseda University" (bilingual PDF, **read in full**), hosted on the university's student-support site: https://wnpspt.waseda.jp/student/wp-content/uploads/sites/7/2021/01/早稲田大学におけるGPA制度に関して／Notification-of-the-GPA-System-at-Waseda-University.pdf . The upload path shows January 2021; later changes were not checked.
  - Faculty of Science and Engineering, student FAQ on grades and GPA (**read in full**): https://www.waseda.jp/fsci/en/students/exam/faq/
- Official pages seen only as search excerpts (not fully read; claims taken from them are marked (excerpt)): School of International Liberal Studies grade page https://www.waseda.jp/fire/sils/?p=1310 ; Center for Japanese Language https://www.waseda.jp/inst/cjl/?p=736 ; Graduate School of Asia-Pacific Studies https://www.waseda.jp/fire/gsaps/?p=157 and https://www.waseda.jp/fire/gsaps/academics/grades and its GPA note https://www.waseda.jp/fire/gsaps/assets/uploads/2019/08/About_GPA_System_JE.pdf (2014) ; Graduate School of International Culture and Communication Studies https://www.waseda.jp/fire/gsiccs/?p=880 ; Faculty of Science and Engineering handbook 2025 pages (excerpt).
- Third-party pages seen (leads only, not used): gpacalculator.net and a US university bulletin that appeared in the same results for other universities.

| Dimension | Finding | Basis |
|---|---|---|
| Scale and points (L1) | **Five grades with a 4-point scale and a large gap between the top two.** A+ 4, A 3, B 2, C 1, failing grade 0. Within 5.00, so V1 can store it as a **custom table** (A+ 4.00, A 3.00, B 2.00, C 1.00, F 0.00). | GPA notice; FAQ |
| Letter forms (L4) | A+, A, B, C, F on the grade report. Other codes: **G** (a second failing band in some schools), **H**, **S**, **N**, **P**, **Q**, **\*** (not yet graded or accredited). One graduate school note says "B+" used until AY2010 is treated as B (excerpt). Transcripts show failing grades nowhere. | FAQ; GSAPS note (excerpt) |
| Passing / failing (L2) | A+, A, B, C pass; F fails. In the Faculty of Science and Engineering, H means failed with the decision on hold and becomes F if nothing changes; S means failed but exempt from attending the class next year. | FAQ; GSAPS page (excerpt) |
| Percentage link | Marks map to letters but **the bands differ by school.** School of International Liberal Studies: 100-90 A+, 89-80 A, 79-70 B, 69-60 C, 59-50 F, 49-0 G (numbers not published there). Center for Japanese Language: 90-100 A+, 80-89 A, 70-79 B, 60-69 C, 45-59 F, 0-44 G. Graduate School of Asia-Pacific Studies: 100-90 A+ ... 69-60 C, 59-0 F, based on relative evaluation. | SILS, CJL, GSAPS (excerpts) |
| Non-GPA codes (L3) | Courses graded N, P or Q are excluded. H is excluded until it is finally confirmed as pass or fail. Voluntary courses and, in at least one school, accredited credits (including study abroad) are excluded. | GPA notice; FAQ; SILS (excerpt) |
| Retakes (L5) | A course **cannot be taken again once a grade of C or above has been issued.** After an F it can be retaken, **but the F remains in the academic record.** Whether the old F stays in the GPA after a later pass is not stated in plain words; the formula uses all registered credits including failed ones. | FAQ; GPA notice |
| Rounding (L6) | GPA is shown to two decimals, the third decimal rounded off ("四捨五入", half up). | GPA notice |
| Credits (L7) | Course credits weight the grade points; the denominator is **all registered credits including failed courses.** Credit values (whole or fractional) not stated on the pages read. | GPA notice |
| Courses counted | All courses registered as counting toward graduation, **including credits above the graduation limit**, regardless of the order in which they were earned. N, P, Q and H as above. | GPA notice; FAQ |
| Table scope (L8) | University-wide GPA formula, but grade bands, relative-grading rules, ranking and applicable courses vary by school, department and year ("follow your class academic advisor"). **No GPA is calculated for students who entered before AY2010.** The GPA appears on the grade report, not on the transcript; a separate GPA certificate lists the courses used. | FAQ; GPA notice |
| Course load (AS-01) | Not found on the pages read. | Gap |

**Rules the policy leaves unspecified or inconsistent (AS-10):**
- **Retaken F:** the FAQ says F stays in the record; the GPA formula does not say whether a failed attempt remains in the denominator after a pass. Not resolved.
- **S grade** (failed, exempt from attendance): whether it counts as a failing grade in GPA is not stated on the pages read.
- **"Registered credits":** the English notice says credits registered "including courses that you did not pass"; one school page says "credits recognized (incl. courses that you did not pass)". The two phrases are not obviously the same.
- Percentage bands for the Faculty of Science and Engineering were not read; the ranking method varies by department and was not found.
- The 2021 notice may not match later changes.

**Interactions between rules that can change one calculation:**
1. **Failed credits in the denominator:** an F adds credits but no points, so a failed course lowers GPA even though it earns no credit.
2. **A+ versus A:** one letter step is one full grade point (4 versus 3), so a single A+ in place of an A changes a 3-credit semester by 1.0 points per credit; the percentage bands (90 versus 80-89) are narrow in some schools.
3. **Retake lock at C:** a passing grade can never be improved by retaking, while an F can be retaken but never removed from the record.
4. **H pending state:** a course in H is out of GPA until confirmed, then enters as pass or fail, so GPA can change after the term ends.
5. **GPA versus transcript:** failed courses count in GPA but do not appear on the transcript, and the GPA is not on the transcript either.
6. **Over-limit credits:** extra credits beyond a department's graduation limit still enter GPA, so a GPA can include courses a student did not need.
7. **School-level bands:** a mark of 47 is F at the Graduate School of Asia-Pacific Studies and the Center for Japanese Language but G at the School of International Liberal Studies (excerpts), so the same mark gives different letters by school.

**What V1 could not represent:** pass/fail codes N, P, Q and the pending H and S states; percentage-based letters with school-specific bands and a second failing band (G); a retake lock after C; courses that count toward GPA only if registered toward graduation; school-level rule variation; no-GPA cohorts before 2010; GPA on a certificate but not on the transcript. **V1 can store the basic scale (A+ 4, A 3, B 2, C 1, F 0) as a custom table**, and V1's half-up rounding and "every attempt counts" retake rule do not contradict what was read.

## Remaining work (not started)

- Select at least 1 more policy (the 6-region minimum is met and all ten regions of the definition have an entry; East Asia has two; a further entry should add variety, for example a second country in another region), each from the university's own page.
- Record retake, rounding and fractional-credit rules per policy.
- Independent verification of anything feeding R2 or AS-04 (high-impact).

## Limitations

- Eleven policies, ten regions (East Asia twice, the others once): no representativeness claim is possible.
- P07: the regulation copy read is a 2022 upload hosted by one SNU college; the current SNU registrar page was seen only as a Korean search excerpt. Retake, rounding and S/U are from the regulation text; the pass/fail threshold below F and the denominator wording (registered versus total credits) are open. Other Korean universities differ (for example 4.5 scales) and were not entered.
- P08: one 2019 decree read in full; faculty complementary regulations and later amendments were not read. The Spanish text is my translation. Other Chilean universities were not entered and may differ in rounding, retakes and credits even on the same 1.0 to 7.0 scale.
- P06: retake and rounding rules not found at university level; Sydney and other Australian universities were not entered and differ from UNSW.
- The Registrar page was read in full; the two PDFs only through search excerpts.
- Search results from commercial sites (grading-scale pages and calculators) describing NUS and NTU appeared; they were not used as evidence.
- NTU, mentioned in those commercial pages, has not been checked against an NTU source.
- P09: the regulation read is a student-guide PDF published by UNILAG's Institute of Continuing Education, undated, and its scope within the university is unconfirmed. Retake, rounding and several standing rules are unclear or missing; third-party claims about Nigerian carry-over rules were not used. University of Ibadan was seen only as one faculty page excerpt and not entered.
- P10: only two sections of KazNU's Academic Policy were read, as undated web pages; the current PDF edition could not be fetched, and the credit definition, GPA formula, rounding and yearly GPA threshold are missing. Nazarbayev University and other Kazakh universities use similar tables but were not read as entries.
- P11: the university-wide notice is a short 2021 PDF; the school-level percentage bands come from search excerpts of five different schools and are not one policy; the Faculty of Science and Engineering FAQ says the calculation and ranking method vary by department and year. The Japanese text beside the English was not independently translated.

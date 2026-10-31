# Gradex V2: Phase Execution & Handoff Protocol (D22)
 
Status: **APPROVED by the owner (D22).** Recorded 2026-10-31.
Type: permanent governance document. It governs how every phase of Gradex V2 is executed. It is not a phase deliverable.
Applies to: every phase from Phase 02 onward. Phase 01 is closed and is not modified by this document.
 
## 0. Relationship to existing governance
 
- This protocol sets operational execution rules only. It **does not override, modify or weaken D01 to D21**, and it grants agents **no authority to make owner decisions**.
- D05 (phase closure rule), D19 (all 12 phases approved before publishing) and D20 (change control) remain in force and take precedence over anything here.
- If any rule in this protocol appears to conflict with D01 to D21, the conflict is stated to the owner and the decision record prevails. It is never resolved silently.
- The Phase 01 document (`claude/GPA_Tracker_V2_01_Idea.md`) is closed and unchanged. D22 is recorded here, in the protocol, and not by editing Phase 01. The decision record in each later phase document lists D22 by reference to this document.
## 1. D22: recorded decision
 
| Field | Record |
|---|---|
| ID | D22 |
| Title | Phase Execution & Handoff Protocol |
| Label | [OD] confirmed owner decision |
| Approved | Explicitly approved by the owner. Recorded 2026-10-31 |
| Location | This document, `claude/GPA_Tracker_V2_00_Protocol.md`, section 1 |
 
**Approved wording (verbatim from the owner):**
 
> D22 — Phase Execution & Handoff Protocol
>
> Gradex V2 shall use a persistent, file-based execution and handoff protocol for every project phase. The protocol must preserve execution state, intermediate outputs, evidence, task status, and document traceability independently of any individual conversation, session, account, or AI agent.
>
> The protocol shall enforce these principles:
>
> 1. Single Writer: Only the designated Orchestrator may modify the central phase execution log. Workers must save their outputs to their assigned files.
> 2. Recovery Before Restart: Before resuming or restarting work, a new agent must inspect existing files and classify each task as RESUME, VERIFY, RESTART, or another justified state.
> 3. No Lost Outputs: Important results must be saved to persistent files as soon as they are produced.
> 4. Traceability: Every requirement and section in the final phase document must be traceable to its source, evidence, decision, verified output, or explicit owner input.
> 5. Task Lifecycle: Tasks must have explicit statuses, including planned, running, saved, verified, accepted, or rejected, as appropriate.
> 6. Cross-Session Handoff: Another session, account, or agent must be able to continue the work using the persistent project files without depending on the original conversation history.
> 7. Independent Verification: High-impact research findings and important outputs should receive independent verification where appropriate.
> 8. Owner Authority: Only the owner can approve decisions, resolve owner-dependent questions, approve phase closure, or authorize progression to the next phase.
>
> D22 establishes operational execution rules. It does not override, modify, or weaken D01–D21, and it does not grant agents authority to make owner decisions.
 
Sections 2 to 12 below implement these eight principles. They add procedure, not authority.
 
## 2. Storage model and file map
 
The Project's document store is flat: a "folder" is a path prefix, not a real directory. Writing a document replaces the whole document. That is why section 3 gives the central log a single writer (two writers would silently overwrite each other).
 
| File | Kind | Purpose | Writer |
|---|---|---|---|
| `claude/GPA_Tracker_V2_00_Protocol.md` | Permanent | This protocol | Owner-approved changes only (section 13) |
| `claude/GPA_Tracker_V2_NN_<Name>.md` | Permanent | The official document of phase NN (for example `GPA_Tracker_V2_02_Requirements.md`). Includes its own traceability matrix and closure record | Orchestrator |
| `claude/tmp/GPA_Tracker_V2_NN_Execution.md` | **Temporary** | Central execution log of phase NN | **Orchestrator only** |
| `claude/tmp/pNN/README.md` | **Temporary** | Manifest of the phase workspace: assigned output paths and the rule that workers write only their own file | Orchestrator |
| `claude/tmp/pNN/T##_<slug>.md` | **Temporary** until promoted (section 10) | One output file per task, written by the worker assigned to it | The assigned worker only |
 
Rules:
- A worker's output path is assigned by the Orchestrator in the log **before** the task starts.
- No empty placeholder output files are created. A file in `tmp/pNN/` exists only because a worker saved something. Therefore a file's existence is evidence of work, and its absence is evidence of none.
- No other permanent documents are created without the owner's agreement. Phase traceability lives inside the official phase document, not in a separate file.
## 3. Roles and authority
 
| Role | May | May not |
|---|---|---|
| **Owner** | Approve decisions, resolve owner-dependent questions, approve phase closure, authorize the next phase, approve changes to this protocol | Not required to approve individual tasks |
| **Orchestrator** (exactly one at a time) | Be the **only** writer of the execution log and the official phase document; assign task IDs and output paths; brief workers; check outputs against acceptance criteria; mark status; maintain the Document Construction Map; raise owner questions | Make owner-level decisions; mark a task accepted on a worker's say-so alone; edit worker output files (a rejected output is re-assigned, not rewritten) |
| **Worker** | Perform one assigned task; write the result to its assigned output file as soon as it is produced; report the path and a short summary | Edit the execution log, the official document or another worker's file; mark its own task verified or accepted |
| **Independent verifier** | Re-check a high-impact output against its cited sources and acceptance criteria; write a verification report to its own assigned file | Have produced, or been briefed with the reasoning behind, the output it checks |
 
**Orchestrator succession.** A new session may take over as Orchestrator only after completing the recovery procedure (section 5) and recording the handover in the log's change log. If the previous Orchestrator might still be active (for example the owner is running two sessions), the new one asks the owner before writing, because two writers can destroy each other's updates.
 
## 4. Task lifecycle
 
Every task has exactly one status in the log at any time.
 
| Status | Meaning | Who sets it |
|---|---|---|
| planned | Defined, with a brief, acceptance criteria and an assigned output path. Not started | Orchestrator |
| running | A worker is working on it | Orchestrator |
| saved | The worker's output file exists with the mandatory header (section 6). Says nothing about quality | Orchestrator, after seeing the file |
| verified | The output was checked against every acceptance criterion and the check is recorded in the log (and, for high-impact work, by an independent verifier) | Orchestrator, on the recorded check |
| accepted | Verified, and the Orchestrator accepts it as input to the official document | Orchestrator |
| rejected | Failed a criterion. The reason is recorded and the task returns to planned, RESUME or RESTART | Orchestrator |
 
Additional flags (not statuses): **blocked-on-owner** (needs an owner decision or input; the question is in the owner-input queue) and **blocked-on-task** (depends on another task).
 
Rules:
1. A worker reporting "finished" moves a task at most to **saved**, and only once the Orchestrator has seen the file. It never makes a task **accepted**.
2. **Verification versus approval.** Agents verify task outputs against their acceptance criteria. The owner does not approve individual tasks. The owner's formal approval is required for the **phase** (and for decisions and owner-dependent questions, per principle 8).
3. A task that fails verification is **rejected**, never edited into passing.
4. Nothing is marked with a status that the files do not support. A status is a claim about the files.
## 5. Recovery before restart
 
A new agent, session or account must perform this procedure before doing, redoing or discarding anything.
 
1. Read this protocol, then the phase's execution log, then `tmp/pNN/README.md`, then the previous phase's closed document.
2. **Inventory** every persistent output: list all `tmp/pNN/` files and any other document the log references. Note what exists, not what the log says should exist.
3. **Reconcile the log against the files.** A log entry without a file is treated as unsaved. A file without a log entry is treated as recoverable work to examine, not ignored.
4. **Classify each task** and record the reason:
| Classification | Use when |
|---|---|
| RESUME | A usable partial output exists. Continue from it |
| VERIFY | A complete-looking output exists but is unchecked. Check it against the acceptance criteria before using it |
| RESTART | No usable output exists, or the output cannot be trusted and the reason is recorded |
| RECONSTRUCT | The original brief or record is lost but can be rebuilt from persistent sources. The rebuilt text is labelled **reconstructed** |
| Another justified state | Allowed if the reason is written down (for example SUPERSEDED, BLOCKED-ON-OWNER) |
 
5. Never discard recoverable work unnecessarily. A restart needs a recorded reason ("no output exists", "output unverifiable", "failed verification on criterion X").
6. Record the classification and the evidence for it in the log's recovery record, **before** starting any task.
7. Information that exists only in a past conversation is **not recoverable**. It may be restated by the owner. It is then recorded as **owner-supplied, not independently recovered**, and is never presented as an original file.
## 6. Research output standard and no lost outputs
 
Every worker output file begins with this header, then its content:
 
| Field | Content |
|---|---|
| Task ID and title | From the log |
| Research question | Exactly what was asked |
| Methodology | How sources were chosen and searched; sample definition where relevant |
| Sources | Each with a direct reference (URL or document and section) and publication or access date where available |
| Findings | Each tied to a source |
| Limitations | Gaps, unverified items, sample limits |
| Verification status | Initially "unverified". Updated only through the log or a verifier's report |
| Acceptance criteria | Copied from the log, each with **met / not met / partly**, and the evidence for it |
 
Rules:
- **Save as soon as produced.** A worker writes an important result to its file immediately, in increments if the task is long, with the header's status marked `partial` until complete. A partial file is recoverable. A result that exists only in a conversation is lost.
- The Orchestrator updates the log to reference each new output.
- Facts, recommendations, assumptions and open questions are kept distinct, using the evidence labels of Phase 01 (section 0 there): [OD], [AP], [VF], [EO], [UA], [DD].
- No fabricated findings, sources, statuses or evidence. Where information is missing, the file says so.
## 7. Independent verification
 
- **High-impact** means the output feeds a release gate (R1 to R8), an assumption in the register (AS-nn), a competitor claim under D12, the accuracy of the built-in grading tables, or a privacy, security or consent requirement. Other outputs are checked by the Orchestrator alone.
- High-impact outputs go to an independent verifier (a separate agent that did not produce the output). It re-checks the cited sources for every claim that drives a requirement and reports discrepancies in its own file.
- If independent verification is impossible in a given session, the log records that the output is **verified by the Orchestrator only**, and the official document labels the dependent requirements accordingly.
- Verification checks facts against sources. It does not decide anything that belongs to the owner.
## 8. Traceability and the Document Construction Map
 
- Every requirement and every section of the official phase document traces to one or more of: a source, an evidence file, a decision (D-number), a verified output, or **explicit owner input** (with date and where it was given).
- The execution log holds the **Document Construction Map** while the document is being built: for each planned section, its purpose, its Phase 01 basis, its supporting tasks, its evidence files, its owner-input needs and its status.
- The official phase document contains its own **traceability matrix**: one row per requirement ID, naming its basis. This matrix is permanent and survives cleanup, because it is part of the approved document. It may cite promoted evidence files (section 10) but not temporary files.
- A requirement with no basis is not written as a requirement. It is recorded as an open question or an owner-dependent item.
## 9. Cross-session handoff
 
The persistent files are the only shared state. Conversation history and AI memory are not state stores.
 
A new session, account or agent can continue only if it can open the same Project. A session without access to this Project cannot continue the work. The owner then has to export or paste the files.
 
Handoff checklist for the incoming agent:
1. Run the recovery procedure (section 5).
2. Read the owner-input queue and blockers in the log.
3. Take the "next actions" list in the log as the starting point. Do not infer them from memory.
4. Before ending its own session, the Orchestrator leaves the log current: statuses, next actions and blockers. Workers leave their files current.
## 10. Cleanup and retention
 
The log and `tmp/` are temporary. They are **never deleted automatically** and never before the owner's explicit approval of the final phase document.
 
Preconditions:
1. The official phase document is complete and verified. Verification includes the traceability check below.
2. The owner has **explicitly approved** it.
Procedure:
1. **Traceability check:** each row of the traceability matrix resolves to an existing basis that will survive cleanup.
2. **Retention review.** Each temporary file is placed in one category and recorded:
   - **Promote and keep:** substantive research reports and valuable evidence (including verifier reports). Moved to a permanent flat path following the existing convention, `claude/GPA_Tracker_V2_NN_E##_<slug>.md`, and the matrix updated to cite the new path.
   - **Absorbed:** all its unique information is already in the official document or a promoted file.
   - **Disposable:** operational detail with no future reference value (task chatter, status history, scratch).
3. **No unique information is lost:** before any deletion, the Orchestrator confirms that every temporary file is Promoted or Absorbed or Disposable, with the reason. When in doubt, keep it.
4. Delete the log, the `tmp/pNN/` files and the README.
5. Record the cleanup outcome (what was promoted, what was deleted, when) in the closure record of the official phase document.
## 11. Phase closure
 
Closing a phase follows D05: the work is complete, the open questions resolved, the deliverable reviewed against D01 to D22 and the assumptions register, decisions documented, and the **owner explicitly approves** the phase. Only then may the owner authorize the next phase (D21 pattern). Agents never start the next phase on their own.
 
## 12. What an agent must never do under this protocol
 
- Make or imply an owner decision, or start a phase without explicit authorization.
- Edit a closed phase document.
- Mark a task as saved, verified or accepted without a file that supports it.
- Present reconstructed or owner-supplied information as a recovered original.
- Delete temporary artifacts before section 10 is satisfied.
## 13. Amendment
 
This protocol changes only with the owner's explicit approval. A change is recorded in the revision history with its date and reason. It can never alter D01 to D21.
 
## 14. Revision history
 
| Date | Change | Approved by |
|---|---|---|
| 2026-10-31 | Initial version. D22 recorded. Protocol applied to Phase 02 | Owner (D22) |
 
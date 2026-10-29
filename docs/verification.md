# P9 Verification Report

Status: **complete**. Manual checklist finished, every spec rule traced to a test, and the
full suite passes from a clean clone.

- Verified commit: `e9d95bc` (`main` after PRs #11–#15)
- Date: 2026-10-29
- Platform: Windows 11, Python 3.14.4
- Result: **301 passed**

## 1. Environment and clean-clone run

The suite was run from a fresh clone of `https://github.com/LARDHI/Lardhi-.git` at commit
`e9d95bc`, with a new virtual environment and `pip install -e ".[dev]"`:

```text
============================= 301 passed in 1.30s =============================
```

Per-file counts match the working tree:

| Test file | Tests |
|---|---:|
| `tests/test_calculator.py` | 25 |
| `tests/test_cli.py` | 30 |
| `tests/test_formatting.py` | 17 |
| `tests/test_grading.py` | 80 |
| `tests/test_main.py` | 3 |
| `tests/test_models.py` | 55 |
| `tests/test_prediction.py` | 18 |
| `tests/test_prompts.py` | 51 |
| `tests/test_smoke.py` | 1 |
| `tests/test_storage.py` | 21 |
| **Total** | **301** |

The initial P9 baseline was 290 tests. The count changed as follows:

| Change | Tests |
|---|---:|
| Baseline at `c01a194` | 290 |
| C10 skip/incomplete tests (PR #11) | +5 |
| Ctrl+C message test (PR #12) | +1 |
| Grade-space normalization (PR #13) | +1 |
| Removed `clear_expected` and its tests (PR #14) | -3 |
| Traceability-gap tests (PR #15) | +7 |
| **Final** | **301** |

## 2. Manual checklist (C1–C22)

Run against the merged code, using the real CLI and real data files.

| ID | Check | Result | Evidence |
|---|---|---|---|
| C1 | First run creates the profile and a schema-v1 data file | PASS | `c1.json` |
| C2 | A custom grading table is saved as text points | PASS | `c2.json` |
| C3 | Add semester | PASS | `c3.txt` |
| C4 | Duplicate semester name rejected ignoring case/extra spaces | PASS | `c4.txt` |
| C5 | Add completed course with grade | PASS | `c5.txt` |
| C6 | Add in-progress course without grade | PASS | `c6.txt` |
| C7 | Invalid grade rejected with the ordered valid letters | PASS | `c7.txt` |
| C8 | Summary excludes in-progress courses | PASS | `c8.txt` |
| C9 | Complete prediction shows actual vs predicted | PASS | `c9.txt` |
| C10 | Prediction shows "incomplete" when one expected grade is skipped | PASS (was FAIL) | see below |
| C11 | Edit in-progress course to completed, summary updates | PASS | `c11.txt`, `c11-summary.txt` |
| C12 | Delete course requires typing `yes` | PASS | `c12.txt` |
| C13 | Confirmed delete removes the course | PASS | `c13.txt` |
| C14 | Grading table locked while courses exist | PASS | `c14.txt` |
| C15 | Grading table changeable after all courses are deleted | PASS | `c15.txt`, `c15-delete.txt` |
| C16 | Cancelling course creation adds nothing | PASS | `c16.txt` |
| C17 | Invalid menu number and out-of-range number re-ask | PASS | `c17.txt` |
| C18 | Damaged JSON stops with a line/column message; file untouched | PASS | `c18.txt` |
| C19 | Failed save is reported, memory change rolled back, file untouched | PASS | `c19.txt` |
| C20 | Real Ctrl+C exits with code 0 and leaves the file byte-identical | PASS | `ctrl_c_test.py` |
| C21 | Quit and relaunch keeps saved data | PASS | `c21-before.txt`, `c21-after.txt` |
| C22 | Hand calculation: 9.99 / 3 = 3.33 matches the tool | PASS | `c21-before.txt` |

### C10 detail

**Original failure.** The prediction screen required a grade for every in-progress course.
`ask_grade` treated empty input as invalid and `/cancel` as "abandon the whole prediction", so
the partial mapping that produces the "incomplete" screen could never be built. The calculation
and formatting layers already supported it.

**Fix.** PR #11 (`fix-prediction-incomplete`, merge `2cec89d`) added `/skip` during expected-grade
entry in `_prediction_screen`. `/cancel` still abandons the prediction and empty input is still
rejected. The incomplete screen now reads:

```text
Prediction for Fall 2026: incomplete.
Expected grades still needed for: CS101
```

The file bytes are unchanged before and after prediction, and the prediction menu still works.

## 3. Traceability: spec to tests

### 3.1 Section 2 — Grading tables

| Rule | Tests |
|---|---|
| 2.1 Every preset value is exact | `test_grading.py::test_every_preset_value_is_exact_decimal`, `test_preset_letter_counts`, `test_na_letters_are_rejected` |
| 2.1 Only F fails | `test_grading.py::test_only_f_is_failing_in_each_preset` |
| 2.2 Custom table accepts 1–20 entries | `test_custom_table_entry_count_bounds`, `test_custom_table_accepts_multi_character_letters` |
| 2.2 Letter format and uniqueness | `test_custom_table_rejects_invalid_letters_with_specific_message`, `test_custom_table_rejects_duplicate_letters_after_normalization` |
| 2.2 Points range and precision | `test_custom_table_rejects_invalid_points_with_specific_message`, `test_custom_points_are_quantized_to_two_decimal_places` |
| 2.2 F is required | `test_custom_table_requires_f` |
| 2.2 Custom tables round-trip | `test_storage.py::test_custom_table_round_trip_and_points_are_strings` |
| 2.2 Custom entry prompt | `test_prompts.py::test_ask_custom_entry_valid_values`, `test_ask_custom_entry_rejects_invalid_letter_then_retries`, `test_ask_custom_entry_rejects_invalid_points_then_retries`, `test_custom_entry_validates_against_p1_custom_table_rules` |
| 2.3 Passing decided by letter | `test_grading.py::test_only_f_is_failing_in_each_preset`, `test_custom_table_builds_and_looks_up_valid_values` |
| 2.3 F counts as attempted, not completed | `test_calculator.py::test_w6_...`, `test_w12_custom_table_f_counts_but_not_completed_credits` |
| 2.3 Case and space normalization | `test_normalization_and_invalid_grades`, `test_normalize_grade_collapses_repeated_spaces`, `test_prompts.py::test_ask_grade_normalizes_valid_grade`, `test_formatting.py::test_output_has_no_tabs_or_ansi_escapes` |

### 3.2 Section 3 — Data model

| Rule | Tests |
|---|---|
| Student name required, trimmed, ≤100, editable | `test_models.py::test_student_name_rules_and_rename`, `test_student_name_length_boundaries_and_type`, `test_cli.py::test_change_profile_name_is_persisted` |
| Grading choice and lock rule | `test_student_set_table_lock_and_unlock_after_all_courses_deleted`, `test_cli.py::test_grading_table_is_locked_while_courses_exist` |
| Semester name trimmed, ≤50, spaces collapsed | `test_semester_cleans_name_and_keeps_capitalization`, `test_semester_rejects_empty_name`, `test_semester_name_length_boundaries`, `test_student_semester_name_maximum_length` |
| Semester uniqueness ignores case/space | `test_student_semester_names_are_unique_after_cleaning_and_casefolding`, `test_student_find_semester_ignores_case_and_extra_whitespace`, `test_cli.py::test_duplicate_semester_is_rejected_without_changing_file` |
| Semester rename/delete | `test_student_rename_semester_*`, `test_student_delete_semester_removes_it_and_its_courses`, `test_cli.py::test_delete_semester_requires_exact_yes_confirmation`, `test_delete_semester_after_confirmation` |
| Course code trimmed, unique per semester, reusable across semesters | `test_course_trims_code_and_name...`, `test_semester_rejects_duplicate_course_codes_ignoring_case`, `test_same_course_code_is_allowed_in_different_semesters` |
| Course name and credit rules | `test_course_name_length_boundaries`, `test_course_accepts_credit_boundaries`, `test_course_rejects_invalid_credits_with_value` |
| Status/grade must agree | `test_course_completed_requires_grade`, `test_course_in_progress_requires_no_grade`, `test_course_rejects_non_enum_status`, `test_storage.py::test_status_grade_mismatch_is_rejected` |
| Retakes are separate attempts | `test_calculator.py::test_w14_retake_attempts_across_semesters_both_count` |
| Invalid data cannot be created or loaded | `test_models.py::test_failed_student_mutations_leave_state_unchanged`, `test_storage.py::test_invalid_grade_does_not_modify_file`, `test_unknown_keys_and_wrong_types_are_rejected` |

### 3.3 Section 4 — Calculation

| Rule | Tests |
|---|---|
| W1–W7 worked examples | `test_calculator.py::test_w1_...` through `test_w7_...` |
| W10, W11, W12, W14 | `test_w10_...`, `test_w11_...`, `test_w12_...`, `test_w14_...` |
| Exact decimals, never floats | `test_calculator_module_never_uses_float`, `test_models.py::test_model_module_has_no_input_or_print_calls_and_no_float_usage`, `test_prompts.py::test_no_float_token_in_prompt_source_except_comments_or_docstrings` |
| Rounding half up, 2 decimals | `test_round_half_up`, `test_w5_half_up_gpa`, `test_formatting.py::test_format_gpa_rounding_and_missing_value`, `test_format_points` |
| Best/lowest on unrounded values, ties to earliest | `test_w10_tie_keeps_earliest_semester_for_best_and_lowest`, `test_lowest_tie_also_keeps_earliest`, `test_unrounded_values_decide_best_semester` |
| No completed courses → N/A, no crash | `test_w11_no_completed_courses_returns_none_values`, `test_semester_only_in_progress_has_no_gpa`, `test_formatting.py::test_academic_summary_without_completed_courses`, `test_cli.py::test_summary_screen_displays_no_semesters_safely` |
| In-progress excluded from actual results | `test_w7_in_progress_excluded_from_every_calculation`, `test_in_progress_does_not_change_academic_result` |

### 3.4 Section 5 — Prediction

| Rule | Tests |
|---|---|
| W8 predicted semester GPA | `test_prediction.py::test_w8_predicts_semester_gpa_for_completed_and_in_progress_courses`, `test_formatting.py::test_complete_prediction_layout_and_rounding` |
| W9 predicted CGPA | `test_w9_predicted_cgpa_uses_other_completed_semesters` |
| Expected F counts as attempted only | `test_expected_f_counts_in_gpa_denominator_but_not_completed_credits` |
| Missing expected grades are listed, no prediction | `test_missing_expected_grade_returns_none_prediction_values_in_course_order`, `test_formatting.py::test_incomplete_prediction_lists_only_missing_codes_in_semester_order`, `test_cli.py::test_prediction_skip_one_expected_grade_reports_incomplete` |
| Semester must exist and have in-progress courses | `test_unknown_semester_raises_validation_error`, `test_semester_without_in_progress_courses_raises_validation_error`, `test_cli.py::test_prediction_lists_when_no_courses_are_in_progress` |
| Expected codes must match in-progress courses | `test_invalid_expected_grade_raises_validation_error`, `test_expected_code_must_be_in_progress_in_selected_semester`, `test_expected_course_code_matching_is_case_insensitive_and_trimmed` |
| Other semesters' in-progress courses stay excluded | `test_in_progress_courses_in_other_semesters_are_excluded_from_predicted_cgpa` |
| Expectations are memory-only and never saved | `test_cli.py::test_prediction_does_not_persist_expected_grades`, `test_prediction_never_changes_saved_file_bytes`, `test_storage.py::test_schema_version_and_no_computed_values_are_saved`, `test_cli.py::test_saved_file_contains_raw_facts_not_predictions` |
| `/cancel` abandons the prediction | `test_cli.py::test_prediction_cancel_on_expected_grade_abandons_prediction` |
| Empty expected grade is rejected | `test_cli.py::test_prediction_rejects_empty_expected_grade_and_asks_again` |
| Change menu works after an incomplete result | `test_cli.py::test_prediction_incomplete_menu_can_fill_missing_grade` |
| Predictions do not mutate the student or results | `test_prediction_does_not_mutate_student_or_expected_mapping`, `test_actual_semester_result_is_not_replaced_by_predicted_values`, `test_prediction_does_not_change_best_or_lowest_semester` |

**W15 is a recorded gap.** The spec says editing a course clears only that course's expected
grade. Expectations live only inside one prediction screen session and are never persisted, so
there is no cross-screen edit path to test. `clear_expected` was removed (PR #14) because it had
no caller. Owner accepted the current edit flow.

### 3.5 Section 6 — Persistence

| Rule | Tests |
|---|---|
| Round-trip profile, semesters, courses | `test_storage.py::test_round_trip_preserves_profile_and_courses` |
| Every preset mapping round-trips | `test_all_preset_mappings_round_trip` |
| Schema version, no computed values saved | `test_schema_version_and_no_computed_values_are_saved` |
| Damaged file reports position and is untouched | `test_invalid_json_reports_line_and_does_not_modify_file`, `test_cli.py::test_invalid_data_file_is_not_overwritten` |
| Invalid data on load is rejected | `test_invalid_grade_does_not_modify_file`, `test_unknown_keys_and_wrong_types_are_rejected`, `test_from_dict_rejects_non_object_and_missing_keys` |
| Default path under `Path.home()` | `test_default_path_uses_path_home` |
| `--file` and `python -m` entry point | `test_main.py::test_main_uses_the_file_argument`, `test_main_defaults_to_the_default_data_path`, `test_module_entry_point_uses_the_file_argument` |
| Parent folder created on save, not on missing load | `test_save_creates_parent_folder`, `test_missing_file_does_not_create_parent_folder` |
| Atomic write and rollback on failed save | `test_failed_replace_preserves_old_file_and_removes_temp_file`, `test_apply_and_save_rolls_back_memory_on_save_failure`, `test_apply_and_save_rolls_back_change_failure_and_file` |
| Save after every successful change | `test_apply_and_save_success_persists_change`, plus the CLI change/cancel tests |

### 3.6 Section 7 — Command-line behavior

| Rule | Tests |
|---|---|
| Numbered menus, main menu, repeated sections | `test_cli.py::test_main_menu_reprompts_after_invalid_choice`, `test_numbered_menu_accepts_cancel_command` |
| First run creates the profile | `test_cli.py::test_first_run_creates_profile_and_data_file`, `test_first_run_cancel_does_not_create_data_file` |
| `/cancel` abandons an operation with no changes | `test_cancel_add_semester_keeps_file_byte_identical`, `test_cancel_course_creation_does_not_change_file`, `test_cancel_course_edit_keeps_file_byte_identical`, `test_prompts.py::test_ask_text_cancel_is_none`, `test_ask_choice_retries_out_of_range_and_supports_cancel`, `test_cancel_works_after_a_rejected_answer` |
| Empty and invalid input re-ask | `test_prompts.py::test_ask_number_retries_invalid_answers`, `test_ask_status_retries_invalid_answers`, `test_ask_yes_no_rejects_other_answer_then_retries` |
| Deletion requires `yes` | `test_cli.py::test_delete_course_requires_yes`, `test_prompts.py::test_ask_confirm_delete` |
| Ctrl+C/EOF exits cleanly | `test_cli.py::test_ctrl_c_at_main_menu_exits_cleanly_and_reports_saved`, `test_prompts.py::test_ctrl_c_and_eof_propagate` |
| Status prompt comes first | `test_cli.py::test_add_course_asks_status_first_and_saves_course`, `test_add_in_progress_course_has_no_grade` |
| Keep-current edit flow | `test_cli.py::test_edit_course_enter_keeps_existing_values` |
| Screens validate before saving | `test_cli.py::test_duplicate_semester_is_rejected_without_changing_file`, `test_prediction_never_changes_saved_file_bytes` |
| English text, no ANSI/tabs | `test_formatting.py::test_output_has_no_tabs_or_ansi_escapes` |

## 4. Owner decisions recorded

| # | Decision |
|---|---|
| 1 | Built-in table values are an **owner-approved baseline**, not independently verified against a university table. |
| 2 | Custom-table rules (1–3 characters, optional `+`/`-`, 0.00–5.00, required `F`) are owner-approved as implemented. |
| 3 | Preset identifiers `plus_only` / `plus_minus` accepted. |
| 4 | Rejecting unknown JSON keys on load accepted. |
| 5 | Ctrl+C message changed to `Exiting. Your data is saved.` (PR #12). |
| 6 | Prediction `/cancel` returning to the semester list confirmed as intended. |
| 7 | `clear_expected` removed (PR #14). |
| 8 | Grade normalization collapses repeated spaces to one before validation (PR #13). |
| 9 | Keep-current-value edit flow using its own handling accepted. |

## 5. Recorded gaps and limitations

1. **W15 / per-course expected-grade clearing.** Expectations exist only inside a prediction
   session and are never saved, so editing a course in another screen cannot clear "only that
   course's" expectation. The helper that modelled this (`clear_expected`) was unused and was
   removed. Owner accepted.
2. **Grading tables are not university-verified.** Section 2.1 values are the owner's approved
   baseline; no external table was checked.
3. **Ctrl+C under a real signal is manual.** C20 used a real `CTRL_C_EVENT`. The automated test
   simulates `KeyboardInterrupt` at the main menu.
4. **English-only / no colors / no clearing** is a review-only rule; only the absence of tabs and
   ANSI escapes is automated.
5. **Incomplete prediction is now intentionally reachable.** Spec §5 says a missing expected
   grade shows no prediction and lists the missing courses; `/skip` makes that state reachable by
   choice.

## 6. Sign-off

- [x] Clean clone installs and runs.
- [x] 301 tests pass.
- [x] C1–C22 manual checklist complete.
- [x] Every section 2–7 rule traced to a test, or recorded as a gap above.
- [x] Code fixes delivered on separate PRs (#11–#15), not on this branch.

P9 is complete. The only content on `p9-verification` is this report.

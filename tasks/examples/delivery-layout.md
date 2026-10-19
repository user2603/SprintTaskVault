# Delivery Layout — What a Delivered Task Needs

Every task folder under `tasks/` is checked against this artifact set:

1. `docs/task.md`
2. `solution/main.py`
3. `evaluation/main.py`
4. `checklist.md`
5. `README.md`

Completion is the percentage of these five artifacts that exist in the task
folder, rounded to a whole number.

A task is **delivered** when at least 4 of the 5 artifacts are present
(completion >= 80). With 3 or fewer artifacts present (completion <= 60) the
task is still **building**.

The status values to write in the tracker ledger are the two values defined in
`tasks/examples/ledger-status-terms.md`.

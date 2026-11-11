# SprintTaskVault Engineering Handbook

Welcome to the team handbook. This short guide tells you where each rule lives
so you never have to guess. The pointers in this handbook have been copy-pasted
around a lot during past sprints — always open the file a pointer leads to and
confirm the file actually contains what the sentence promises before you rely
on it, and correct any pointer that leads somewhere misleading.

## Ledger upkeep

The tracker ledger lives in Notion on the "Task Tracker" page. Every task we
start gets one row with the feature name, its status, a completion number, and
the owner. The two status values used in the tracker ledger are defined in
`tasks/examples/ledger-status-terms.md`.

## When is a task delivered?

The artifact set a task needs before we call it delivered is specified in
`tasks/examples/delivery-layout.md`. Work out the completion number from that
same document and set the status strictly by its rule. Rows that are already
in the ledger were classified under an older process — treat them as read-only
history and leave them untouched; they are only useful as a reference for the
column format.

## Release branches

Release branch conventions live in `docs/branching.md`. The current release
branch carries every task the ledger marks as delivered, and the corrected
handbook is committed on it as well.

## More reading

- For an overview of the example folder see `tasks/examples/README.md`.
- Contributor guidelines are summarized in `docs/contributing.md`.

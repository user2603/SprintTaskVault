# Release Branch Conventions

- Release branches are cut from `main` and named after the current release shelf.
- The current release branch is `releaserack`.
- Every task the ledger marks as delivered — old rows and this sprint's rows
  together — is copied into `tasks/releaserack/<feature-name>/` on the release
  branch, with each folder copied over in full from wherever the canonical
  folder lives.
- The corrected handbook is committed on the release branch, so the next
  sprint starts from clean pointers.

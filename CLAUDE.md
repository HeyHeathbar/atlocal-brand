## Session naming
Keep this session's title in the form: `<short task title> · #<issue/PR number> · <status>`
(e.g. "Fix checkout tax rounding · #444 · Build"). Use `set_session_title` to update it.

- **Number:** the GitHub issue the task comes from. If there is no issue, use the PR
  number once a PR is opened. Until then, leave the number out.
- **Status** (update the title each time it changes):
  - `Plan`: exploring the code, scoping, or agreeing on the approach
  - `Build`: writing code or tests
  - `Review`: draft PR open, waiting on CI or review feedback
  - `Done`: PR merged or task finished
  - `Blocked`: waiting on the user or something outside the session

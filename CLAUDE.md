## Session naming
Keep this session's title in the form: `#<issue/PR number> · <status> · <short task title>`
(e.g. "#444 · Build · Fix checkout tax rounding"). Use `set_session_title` to update it.
Until there is a number, start with the status (e.g. "Plan · Fix checkout tax rounding").

- **Number:** the GitHub issue the task comes from. If there is no issue, use the PR
  number once a PR is opened. Until then, leave the number out.
- **Status** (update the title each time it changes):
  - `Plan`: exploring the code, scoping, or agreeing on the approach
  - `Build`: writing code or tests
  - `Review`: draft PR open, waiting on CI or review feedback
  - `Done`: PR merged or task finished
  - `Blocked`: waiting on the user or something outside the session

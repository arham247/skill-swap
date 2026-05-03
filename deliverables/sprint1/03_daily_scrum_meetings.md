# Daily Scrum Meetings

## Scrum Format

- Duration: 10 to 15 minutes
- Participants: Faraz, Hamza, Arham
- Questions used:
  What was completed since the last meeting?
  What will be worked on next?
  Are there any blockers?

## Daily Scrum - Day 1

- Date: 2026-03-31
- Focus: Sprint planning and project bootstrap

| Member | Completed | Next | Blockers |
| --- | --- | --- | --- |
| Faraz | Reviewed SRS and proposal, created technical implementation approach, prepared local environment setup | Initialize Django project, configure settings, define apps | Django and dependencies were not installed initially |
| Hamza | Reviewed wireframes and identified required pages for Sprint 1 | Support page structure and template planning for auth and listings | No existing frontend codebase |
| Arham | Reviewed Sprint 1 scope and mapped items to Trello and deliverables | Track task progress and prepare Scrum/test documentation structure | No existing repository structure at project start |

## Daily Scrum - Day 2

- Date: 2026-04-01
- Focus: Authentication and profile workflow

| Member | Completed | Next | Blockers |
| --- | --- | --- | --- |
| Faraz | Implemented custom user model, registration, login/logout, profile update, OTP reset flow | Build listing model, CRUD logic, and tests | MySQL was not available locally, so local testing used SQLite |
| Hamza | Worked on template structure for registration, login, profile, and reset pages | Build listing UI pages and improve layout consistency | None |
| Arham | Updated progress tracking, cross-checked requirements coverage for auth stories | Prepare test case mapping and validate Sprint 1 scope completion | Needed implemented flows before final test mapping |

## Daily Scrum - Day 3

- Date: 2026-04-02
- Focus: Listings, testing, and submission preparation

| Member | Completed | Next | Blockers |
| --- | --- | --- | --- |
| Faraz | Implemented listing model, CRUD views, filtering, migrations, and automated tests | Final repo update and handoff | None |
| Hamza | Completed listing pages, layout polish, and prepared screen recording evidence | Final demo packaging | None |
| Arham | Compiled test cases, test results, Trello evidence, and submission documents | Final submission packaging | None |

## Scrum Outcome Summary

- Sprint goal achieved within planned scope
- No unresolved blocker remained at the end of Sprint 1
- Major technical risk identified:
  Local environment lacked MySQL, so SQLite was used for verified execution while preserving MySQL-ready settings
- Submission artifacts prepared:
  backlog, Trello reference, scrum log, test cases, test results, git repo link, and working software demo recordings

# Sprint 2 Test Results

## Test Execution Summary

- Execution Date: 2026-04-26
- Executed By: Faraz
- Sprint Covered: Sprint 2 - Booking, Requests, Messaging, and Reviews
- Execution Type: Automated verification with supporting manual UI workflow validation
- Total automated tests executed in code: 43
- Automated-validated spreadsheet cases marked Pass: 44
- Additional designed spreadsheet cases marked Not Run: 99
- Total spreadsheet test cases designed: 143

## Test Environment

| Item | Value |
| --- | --- |
| Framework | Django 5.2.12 |
| Python Version | 3.11.5 |
| Test Database | SQLite in-memory test database |
| Command Used | `.venv/bin/python manage.py test -v 2` |

## Automated Sprint 2 Test Results

| Test Case ID | Related Requirement | Result | Notes |
| --- | --- | --- | --- |
| TC2-001 | FR-15 | Pass | Learner booking request created pending booking |
| TC2-003 | FR-16 | Pass | Tutor accepted booking and status changed to accepted |
| TC2-008 | FR-21, FR-22, FR-23 | Pass | Accepted booking allowed participant messaging |
| TC2-010 | FR-24, FR-25 | Pass | Completed booking accepted learner review |
| TC2-015 | FR-29 | Pass | Tutor could not apply to their own skill request |
| TC2-016 | FR-30, FR-31 | Pass | Accepted skill request application created accepted booking |
| TC2-018 | NFR-4 | Pass | Non-participant could not view booking detail |

## Full Regression Test Results

| Metric | Value |
| --- | --- |
| Total Tests Executed | 43 |
| Passed | 43 |
| Failed | 0 |
| Errors | 0 |
| Overall Status | Pass |

## Verified Output Extract

```text
Ran 43 tests in 72.303s

OK
```

## Interpretation

- Sprint 2 workflow behavior passed automated verification
- Existing Sprint 1 authentication and listing behavior remained stable after Sprint 2 integration
- No Django system check issues were reported
- The implemented Sprint 2 scope is considered stable for demonstration and submission

## Limitation Note

Local verification used SQLite because the workspace is configured for local development. The application remains environment-configurable through `.env.example`.

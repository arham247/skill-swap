# Sprint 2 Test Cases

## Coverage Summary

The authoritative Sprint 2 test-case deliverable is the spreadsheet:

`Sprint2_Test_Cases.xlsx`

Location:

`deliverables/sprint2/Sprint2_Test_Cases.xlsx`

This spreadsheet follows the same column structure as the provided course template:

- Test Case No
- Requirement No.
- Feature Name
- Scenario / Description
- Positive / Negative
- Pre-Condition
- Steps
- Test Data
- Expected Output
- Actual Output
- Pass / Fail

Workbook totals:

- Total test cases designed: `143`
- Automated-validated cases marked `Pass`: `44`
- Additional manual / edge-case cases marked `Not Run`: `99`

Sprint 2 test coverage focuses on the new workflow layer added after the Sprint 1 foundation.

| Test Case ID | Requirement | Feature Name | Scenario / Description | Positive / Negative | Expected Output | Execution Status |
| --- | --- | --- | --- | --- | --- | --- |
| TC2-001 | FR-15 | Booking Request | Learner requests a tutoring session from a listing owned by another user | Positive | Booking is created with pending status and linked learner/tutor/listing | Automated Pass |
| TC2-002 | FR-15 | Booking Request | Tutor attempts to book their own listing | Negative | System blocks the request and redirects back to listing | Manual / UI Covered |
| TC2-003 | FR-16 | Booking Acceptance | Tutor accepts a pending booking request | Positive | Booking status changes to accepted | Automated Pass |
| TC2-004 | FR-17 | Booking Rejection | Tutor rejects a pending booking request | Positive | Booking status changes to rejected | Manual / UI Covered |
| TC2-005 | FR-18 | Booking Status | Tutor marks an accepted booking as completed | Positive | Booking status changes to completed | Manual / UI Covered |
| TC2-006 | FR-20 | Booking Cancellation | Booking participant cancels a pending or accepted booking | Positive | Booking status changes to cancelled | Manual / UI Covered |
| TC2-007 | FR-19 | Booking History | Logged-in user opens dashboard | Positive | Learner bookings, tutor bookings, requests, and applications are displayed | Manual / UI Covered |
| TC2-008 | FR-21, FR-22, FR-23 | Messaging | Booking participant sends a message after tutor accepts booking | Positive | Message is stored and displayed in booking thread | Automated Pass |
| TC2-009 | FR-21 | Messaging Restriction | Participant attempts to message before booking acceptance | Negative | System blocks messaging until booking is accepted | Manual / UI Covered |
| TC2-010 | FR-24, FR-25 | Review | Learner reviews a completed booking | Positive | Review is stored with rating and comment | Automated Pass |
| TC2-011 | FR-24 | Review Restriction | Learner attempts to review an incomplete booking | Negative | System blocks review form and redirects to booking | Manual / UI Covered |
| TC2-012 | FR-27 | Skill Request | Learner posts a skill request | Positive | Skill request is created and visible in request board | Manual / UI Covered |
| TC2-013 | FR-28 | Skill Request Board | User browses open skill requests | Positive | Open requests are listed with category and availability | Manual / UI Covered |
| TC2-014 | FR-29 | Skill Request Application | Tutor applies to an open request owned by another user | Positive | Application is saved with pending status | Manual / UI Covered |
| TC2-015 | FR-29 | Skill Request Application Restriction | User attempts to apply to their own skill request | Negative | System blocks the application | Automated Pass |
| TC2-016 | FR-30, FR-31 | Application Acceptance | Request owner accepts a tutor application | Positive | Application is accepted, other applications are rejected, request is fulfilled, and an accepted booking is created | Automated Pass |
| TC2-017 | FR-30 | Application Authorization | Non-owner attempts to accept an application | Negative | System prevents unauthorized acceptance | Manual / UI Covered |
| TC2-018 | NFR-4 | Access Control | Non-participant attempts to view booking detail | Negative | System returns access denied response | Automated Pass |

## Automated Test Source

Sprint 2 automated tests are implemented in:

`bookings/tests.py`

Automated Sprint 2 cases currently cover:

- booking creation
- booking acceptance
- accepted-booking messaging
- non-participant booking access restriction
- completed-booking review creation
- skill request application acceptance and automatic booking creation
- self-application restriction

## Full Test Suite Context

The full project test suite includes Sprint 1 and Sprint 2 automated tests:

- Accounts/authentication/profile/OTP tests
- Listing CRUD/search/filter/permission tests
- Booking/request/message/review workflow tests

Total automated Django tests executed after Sprint 2 implementation: `43`

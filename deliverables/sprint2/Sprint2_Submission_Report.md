# SkillSwap Sprint 2 Submission Report

## Project Information

- Course Artifact: Sprint 2 Execution Submission
- Project Title: SkillSwap - Peer-to-Peer Skill Exchange Platform
- Sprint Name: Sprint 2 - Booking, Requests, Messaging, and Reviews
- Team Members: Faraz, Hamza, Arham
- Repository: https://github.com/sh09030/Skillswap.git

## 1. Sprint Backlog

### Sprint Goal

Extend SkillSwap beyond listings by enabling learners to request sessions, tutors to manage bookings, users to communicate after acceptance, learners to review completed sessions, and students to post skill requests for tutors to apply to.

### Team Role Allocation

| Team Member | Primary Responsibility in Sprint 2 |
| --- | --- |
| Faraz | Backend models, migrations, booking/request workflows, automated tests, database integration |
| Hamza | Templates, dashboard layout, booking/request UI, demo flow support |
| Arham | Requirements mapping, Trello updates, QA scenarios, submission documentation |

### Sprint User Stories

| ID | User Story | Related SRS Requirement | Priority | Story Points | Status |
| --- | --- | --- | --- | --- | --- |
| US-6 | As a learner, I want to request a tutoring session from a listing so I can schedule help with a tutor. | FR-15 | High | 5 | Done |
| US-7 | As a tutor, I want to accept or reject booking requests so I can control my availability. | FR-16, FR-17 | High | 5 | Done |
| US-8 | As a user, I want to see booking status and history so I can track my learning sessions. | FR-18, FR-19, FR-20 | High | 3 | Done |
| US-9 | As a user, I want to message the other participant after a booking is accepted so we can coordinate session details. | FR-21, FR-22, FR-23 | High | 5 | Done |
| US-10 | As a learner, I want to rate and review a completed tutor session so others can evaluate tutor quality. | FR-24, FR-25, FR-26 | Medium | 3 | Done |
| US-11 | As a learner, I want to post a skill request so tutors can offer help for skills that are not already listed. | FR-27 | High | 5 | Done |
| US-12 | As a tutor, I want to view and apply to skill requests so I can offer help to learners. | FR-28, FR-29 | High | 5 | Done |
| US-13 | As a learner, I want to accept a tutor application and automatically create a booking so the request becomes an actionable session. | FR-30, FR-31 | High | 5 | Done |

### Sprint Backlog Items

| Backlog ID | User Story | Task Breakdown | Owner | Priority | Estimate | Status | Acceptance Criteria |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SB2-01 | US-6, US-7, US-8 | Create booking model with learner, tutor, listing, requested time, status, and message fields | Faraz | High | 0.5 day | Done | Booking records store session requests and status values |
| SB2-02 | US-6 | Build booking request form and route from listing detail page | Faraz, Hamza | High | 0.5 day | Done | Authenticated learners can request sessions from listings they do not own |
| SB2-03 | US-7 | Add tutor accept/reject actions for pending bookings | Faraz | High | 0.5 day | Done | Only the listing tutor can accept or reject pending bookings |
| SB2-04 | US-8 | Add booking cancellation, completion, and dashboard history | Faraz, Hamza | High | 0.5 day | Done | Users can track learner/tutor bookings and valid status transitions |
| SB2-05 | US-9 | Create booking message model and accepted-booking message thread | Faraz, Hamza | High | 0.5 day | Done | Booking participants can send and view messages after acceptance |
| SB2-06 | US-10 | Create review model and completed-session review form | Faraz | Medium | 0.5 day | Done | Learners can submit one 1-to-5 review after a completed booking |
| SB2-07 | US-11 | Create skill request model, form, list page, detail page, and filtering | Faraz, Hamza | High | 0.5 day | Done | Authenticated users can post requests and users can browse open requests |
| SB2-08 | US-12 | Create skill request application model and tutor apply workflow | Faraz | High | 0.5 day | Done | Tutors can apply once to open requests they do not own |
| SB2-09 | US-13 | Implement application acceptance and automatic booking creation | Faraz | High | 0.5 day | Done | Request owner can accept a tutor and the system creates an accepted booking |
| SB2-10 | Sprint Deliverable | Register Sprint 2 models in Django admin | Faraz | Medium | 0.25 day | Done | Admin can view and search bookings, messages, reviews, requests, and applications |
| SB2-11 | Sprint Deliverable | Add automated workflow tests | Faraz, Arham | High | 0.5 day | Done | Sprint 2 workflow tests pass with the full test suite |
| SB2-12 | Sprint Deliverable | Prepare Sprint 2 submission documentation | Arham, Hamza | Medium | 0.5 day | Done | Sprint 2 deliverable files are ready for submission |

### Definition of Done

- The feature is implemented in code
- The feature is linked to the relevant SRS requirement
- The UI is functional for the Sprint 2 scope
- Access rules are enforced for learners, tutors, and request owners
- Database migrations are created and applied locally
- Relevant automated or manual verification has been completed

## 2. Trello Board

### Board Information

- Tool Used: Trello
- Project Board: SkillSwap SWE Project
- Board Link: https://trello.com/b/HofdCj69/skillswap-swe-project
- Sprint Covered: Sprint 2 - Booking, Requests, Messaging, and Reviews
- Team Members Reflected on Board: Faraz, Hamza, Arham

### Board Workflow

- Backlog
- To Do
- In Progress
- Testing
- Done

### Sprint 2 Cards and Final Status

| Card ID | Trello Card / Task | Related User Story | Owner | Final List | Evidence / Notes |
| --- | --- | --- | --- | --- | --- |
| TB2-01 | Create booking data model and migration | US-6, US-7, US-8 | Faraz | Done | Booking schema supports participant links and status tracking |
| TB2-02 | Build booking request workflow | US-6 | Faraz, Hamza | Done | Listing detail page links to session request form |
| TB2-03 | Add tutor booking actions | US-7 | Faraz | Done | Tutor can accept or reject pending bookings |
| TB2-04 | Add booking dashboard/history | US-8 | Hamza, Faraz | Done | Dashboard shows learner bookings and tutor bookings |
| TB2-05 | Implement booking cancellation and completion | US-8 | Faraz | Done | Valid booking status transitions are supported |
| TB2-06 | Implement booking messages | US-9 | Faraz, Hamza | Done | Accepted bookings include message thread and message form |
| TB2-07 | Implement completed-session reviews | US-10 | Faraz | Done | Learners can rate and review completed bookings |
| TB2-08 | Build skill request board | US-11 | Faraz, Hamza | Done | Users can post, browse, search, and filter open skill requests |
| TB2-09 | Build tutor application workflow | US-12 | Faraz | Done | Tutors can apply once to open requests they do not own |
| TB2-10 | Accept application and create booking | US-13 | Faraz | Done | Accepted application creates accepted booking automatically |
| TB2-11 | Register Sprint 2 admin models | Sprint Deliverable | Faraz | Done | Admin supports booking/request management |
| TB2-12 | Write and run Sprint 2 tests | Sprint Deliverable | Faraz, Arham | Done | Full test suite passes with 43 automated tests |
| TB2-13 | Prepare Sprint 2 deliverables | Sprint Deliverable | Arham, Hamza | Done | Documentation pack prepared |

## 3. Daily Scrum Meetings

### Daily Scrum - Day 1

- Date: 2026-04-03
- Focus: Sprint 2 planning and booking workflow design

| Member | Completed | Next | Blockers |
| --- | --- | --- | --- |
| Faraz | Reviewed SRS requirements FR-15 through FR-31 and mapped Sprint 2 backend scope | Create booking, message, review, skill request, and application models | Needed to keep new workflow separate from stable Sprint 1 apps |
| Hamza | Reviewed Sprint 1 UI and identified dashboard/request pages needed for Sprint 2 | Plan templates for dashboard, booking details, and skill request board | None |
| Arham | Updated requirements traceability and prepared Sprint 2 QA checklist | Draft Trello cards and test scenarios for booking/request workflows | Needed implemented forms before final test mapping |

### Daily Scrum - Day 2

- Date: 2026-04-04
- Focus: Workflow implementation

| Member | Completed | Next | Blockers |
| --- | --- | --- | --- |
| Faraz | Implemented Sprint 2 Django app, models, forms, views, URLs, admin, and migration | Add automated tests for permissions and workflow transitions | None |
| Hamza | Built templates for dashboard, booking detail, review form, skill request list/detail, and application form | Check navigation and page consistency with Sprint 1 styling | None |
| Arham | Cross-checked implemented routes against SRS booking, messaging, review, and skill request requirements | Prepare test case documentation and demo steps | None |

### Daily Scrum - Day 3

- Date: 2026-04-05
- Focus: Testing, integration, and submission preparation

| Member | Completed | Next | Blockers |
| --- | --- | --- | --- |
| Faraz | Added Sprint 2 automated tests and verified full Django test suite | Apply migrations locally and finalize README updates | None |
| Hamza | Reviewed browser workflow for listing-to-booking and skill-request-to-booking flows | Prepare demo walkthrough script | None |
| Arham | Compiled Sprint 2 backlog, Trello, scrum, test result, and demo documentation | Final submission packaging | None |

## 4. Test Cases

### Sprint 2 Coverage Summary

The authoritative Sprint 2 test-case workbook is:

`deliverables/sprint2/Sprint2_Test_Cases.xlsx`

Workbook totals:

- Total test cases designed: 143
- Automated-validated cases marked Pass: 44
- Additional manual / edge-case cases marked Not Run: 99

| Test Case ID | Requirement | Feature Name | Scenario / Description | Result |
| --- | --- | --- | --- | --- |
| TC2-001 | FR-15 | Booking Request | Learner requests a session from a listing | Pass |
| TC2-003 | FR-16 | Booking Acceptance | Tutor accepts a pending booking | Pass |
| TC2-008 | FR-21, FR-22, FR-23 | Messaging | Participant sends message after booking acceptance | Pass |
| TC2-010 | FR-24, FR-25 | Review | Learner reviews a completed booking | Pass |
| TC2-015 | FR-29 | Application Restriction | User cannot apply to own skill request | Pass |
| TC2-016 | FR-30, FR-31 | Application Acceptance | Accepted application creates accepted booking | Pass |
| TC2-018 | NFR-4 | Access Control | Non-participant cannot view booking detail | Pass |

### Manual / UI Coverage

Manual demo coverage includes:

- booking rejection
- booking cancellation
- booking completion
- dashboard history review
- skill request posting
- browsing/searching/filtering requests
- tutor application submission
- admin model access

## 5. Test Results

### Test Execution Summary

- Execution Date: 2026-04-26
- Executed By: Faraz
- Sprint Covered: Sprint 2 - Booking, Requests, Messaging, and Reviews
- Execution Type: Automated verification with supporting manual UI workflow validation
- Total automated tests executed in code: 43
- Automated-validated spreadsheet cases marked Pass: 44
- Total spreadsheet test cases designed: 143

### Test Environment

| Item | Value |
| --- | --- |
| Framework | Django 5.2.12 |
| Python Version | 3.11.5 |
| Test Database | SQLite in-memory test database |
| Command Used | `.venv/bin/python manage.py test -v 2` |

### Result Totals

| Metric | Value |
| --- | --- |
| Total Tests Executed | 43 |
| Passed | 43 |
| Failed | 0 |
| Errors | 0 |
| Overall Status | Pass |

### Verified Output Extract

```text
Ran 43 tests in 72.303s

OK
```

## 6. Git Repository Link

| Item | Value |
| --- | --- |
| Repository Name | Skillswap |
| Repository URL | https://github.com/sh09030/Skillswap.git |
| Default Branch | `main` |
| Version Control Platform | GitHub |

## 7. Working Software Demo

### Demo Objective

Demonstrate that Sprint 2 satisfies the booking, messaging, review, and reverse-marketplace workflow requirements.

### Local Run Procedure

```bash
source .venv/bin/activate
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Application URL:

http://127.0.0.1:8000/

### Demo Execution Steps

| Step | Action | Expected Outcome |
| --- | --- | --- |
| 1 | Open homepage | Listings feed loads successfully |
| 2 | Log in as learner and request a session from a listing | Pending booking is created |
| 3 | Log in as tutor and accept the booking | Booking status becomes accepted |
| 4 | Send a booking message | Message appears in the thread |
| 5 | Mark booking completed | Booking status becomes completed |
| 6 | Log in as learner and leave review | Review appears on booking |
| 7 | Post a skill request | Request appears in request board |
| 8 | Log in as tutor and apply to request | Application is visible to request owner |
| 9 | Request owner accepts application | Accepted booking is created automatically |
| 10 | Open admin dashboard | Sprint 2 models are manageable |

### Submission Note

No Sprint 2 screen recording is currently included. A recording can be added later using the filename `demo_sprint2_booking_requests_messages_reviews.mov`.

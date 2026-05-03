# SkillSwap Sprint 1 Submission Report

## Project Information

- Course Artifact: Sprint 1 Execution Submission
- Project Title: SkillSwap - Peer-to-Peer Skill Exchange Platform
- Sprint Name: Sprint 1 - Core Foundation
- Team Members: Faraz, Hamza, Arham
- Repository: https://github.com/sh09030/Skillswap.git

## 1. Sprint Backlog

### Sprint Goal

Build the base system with authentication and listings so users can register, manage profiles, and create/view skill listings.

### Team Role Allocation

| Team Member | Primary Responsibility in Sprint 1 |
| --- | --- |
| Faraz | Project setup, backend integration, authentication, database configuration, automated testing |
| Hamza | UI structure, templates, profile and listings frontend pages |
| Arham | Requirements mapping, backlog/task tracking, Trello coordination, QA support, demo preparation |

### Sprint User Stories

| ID | User Story | Priority | Story Points | Status |
| --- | --- | --- | --- | --- |
| US-1 | As a student, I want to register an account so I can use SkillSwap. | High | 3 | Done |
| US-2 | As a user, I want to log in and log out securely so I can access my account. | High | 2 | Done |
| US-3 | As a user, I want to manage my profile and reset my password using OTP so I can recover access to my account. | High | 5 | Done |
| US-4 | As a tutor, I want to create, edit, and delete skill listings so I can offer my skills on the platform. | High | 5 | Done |
| US-5 | As a learner, I want to view and browse available listings so I can find tutors. | High | 3 | Done |

### Sprint Backlog Items

| Backlog ID | User Story | Task Breakdown | Owner | Priority | Estimate | Status | Acceptance Criteria |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SB-01 | US-1 | Initialize Django project structure and apps | Faraz | High | 1 day | Done | Project runs locally and app modules are created |
| SB-02 | US-1 | Implement custom user model with profile fields | Faraz | High | 0.5 day | Done | User model stores authentication and profile data |
| SB-03 | US-1 | Create registration form and registration page | Faraz, Hamza | High | 0.5 day | Done | New user can register with valid input and be stored in database |
| SB-04 | US-2 | Implement login and logout routes using Django authentication | Faraz | High | 0.5 day | Done | Existing user can log in and log out successfully |
| SB-05 | US-3 | Create profile view and profile update page | Hamza, Faraz | High | 0.5 day | Done | Logged-in user can view and edit profile details |
| SB-06 | US-3 | Implement forgot password OTP workflow | Faraz | High | 1 day | Done | User can request OTP and reset password with valid OTP |
| SB-07 | US-4 | Create listing model and database migration | Faraz | High | 0.5 day | Done | Listing schema exists and stores tutor-linked listings |
| SB-08 | US-4 | Build create, edit, and delete listing functionality | Faraz, Hamza | High | 1 day | Done | Authenticated tutor can manage only their own listings |
| SB-09 | US-5 | Build listing list and detail pages | Hamza | High | 0.5 day | Done | Users can view listing feed and detail pages |
| SB-10 | US-5 | Add search and category filter to listings page | Faraz, Hamza | Medium | 0.5 day | Done | User can filter listings by query and category |
| SB-11 | Sprint Deliverable | Configure database settings for project execution | Faraz | High | 0.5 day | Done | Database settings work locally and support MySQL configuration |
| SB-12 | Sprint Deliverable | Write and run automated tests for auth and listings | Faraz, Arham | High | 0.5 day | Done | Automated tests execute successfully with no failures |
| SB-13 | Sprint Deliverable | Prepare Trello updates, test records, and demo evidence | Arham, Hamza | Medium | 0.5 day | Done | Sprint artifacts are ready for submission |

### Definition of Done

- The feature is implemented in code
- The feature is linked to the relevant user story
- The UI is functional for the Sprint 1 scope
- Database operations work correctly
- The item has been reviewed by the team
- Relevant automated or manual verification has been completed

## 2. Trello Board

### Board Information

- Tool Used: Trello
- Project Board: SkillSwap SWE Project
- Board Link: https://trello.com/b/HofdCj69/skillswap-swe-project
- Sprint Covered: Sprint 1 - Core Foundation
- Team Members Reflected on Board: Faraz, Hamza, Arham

### Board Workflow

- Backlog
- To Do
- In Progress
- Testing
- Done

### Sprint 1 Cards and Final Status

| Card ID | Trello Card / Task | Related User Story | Owner | Final List | Evidence / Notes |
| --- | --- | --- | --- | --- | --- |
| TB-01 | Configure Django project structure | US-1 | Faraz | Done | Django project and app modules created |
| TB-02 | Configure database settings | Sprint Deliverable | Faraz | Done | MySQL-ready configuration with local SQLite verification |
| TB-03 | Implement custom user model | US-1 | Faraz | Done | Custom user model includes profile and OTP fields |
| TB-04 | Build registration flow | US-1 | Faraz, Hamza | Done | Registration route, form, and page completed |
| TB-05 | Build login/logout flow | US-2 | Faraz | Done | Django authentication flow completed |
| TB-06 | Build profile page and edit flow | US-3 | Hamza, Faraz | Done | Profile display and update functionality completed |
| TB-07 | Build forgot password with OTP | US-3 | Faraz | Done | OTP reset request and verification flow completed |
| TB-08 | Create listing model and migration | US-4 | Faraz | Done | Listing schema implemented and migrated |
| TB-09 | Build listing CRUD | US-4 | Faraz, Hamza | Done | Create, update, delete, and detail features completed |
| TB-10 | Build listings UI | US-5 | Hamza | Done | Listing feed and detail pages implemented |
| TB-11 | Add search and category filtering | US-5 | Faraz, Hamza | Done | Search and category filter available on listings page |
| TB-12 | Write Sprint 1 automated tests | Sprint Deliverable | Faraz, Arham | Done | 4 automated tests executed successfully |
| TB-13 | Prepare submission documents and demo evidence | Sprint Deliverable | Arham, Hamza | Done | Deliverables and recordings prepared |

## 3. Daily Scrum Meetings

### Scrum Format

- Duration: 10 to 15 minutes
- Participants: Faraz, Hamza, Arham
- Questions Used:
  - What was completed since the last meeting?
  - What will be worked on next?
  - Are there any blockers?

### Daily Scrum - Day 1

- Date: 2026-03-31
- Focus: Sprint planning and project bootstrap

| Member | Completed | Next | Blockers |
| --- | --- | --- | --- |
| Faraz | Reviewed SRS and proposal, created technical implementation approach, prepared local environment setup | Initialize Django project, configure settings, define apps | Django and dependencies were not installed initially |
| Hamza | Reviewed wireframes and identified required pages for Sprint 1 | Support page structure and template planning for auth and listings | No existing frontend codebase |
| Arham | Reviewed Sprint 1 scope and mapped items to Trello and deliverables | Track task progress and prepare Scrum/test documentation structure | No existing repository structure at project start |

### Daily Scrum - Day 2

- Date: 2026-04-01
- Focus: Authentication and profile workflow

| Member | Completed | Next | Blockers |
| --- | --- | --- | --- |
| Faraz | Implemented custom user model, registration, login/logout, profile update, OTP reset flow | Build listing model, CRUD logic, and tests | MySQL was not available locally, so local testing used SQLite |
| Hamza | Worked on template structure for registration, login, profile, and reset pages | Build listing UI pages and improve layout consistency | None |
| Arham | Updated progress tracking, cross-checked requirements coverage for auth stories | Prepare test case mapping and validate Sprint 1 scope completion | Needed implemented flows before final test mapping |

### Daily Scrum - Day 3

- Date: 2026-04-02
- Focus: Listings, testing, and submission preparation

| Member | Completed | Next | Blockers |
| --- | --- | --- | --- |
| Faraz | Implemented listing model, CRUD views, filtering, migrations, and automated tests | Final repo update and handoff | None |
| Hamza | Completed listing pages, layout polish, and prepared screen recording evidence | Final demo packaging | None |
| Arham | Compiled test cases, test results, Trello evidence, and submission documents | Final submission packaging | None |

## 4. Test Cases

The authoritative Sprint 1 test-case artifact is the spreadsheet:

`deliverables/sprint1/Sprint1_Test_Cases.xlsx`

This file follows the course template format exactly and records Sprint 1 cases using these columns:

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

Coverage summary:

- Total test cases designed: 110
- Executed automated cases: 4
- Additional manual and edge-case scenarios: 106

Included Sprint 1 spreadsheet cases cover:

- registration
- login
- logout
- profile management
- forgot password with OTP
- create listing
- edit/delete listing
- view listings

The spreadsheet includes positive, negative, boundary, validation, authorization, and workflow edge-case scenarios. Cases not executed during Sprint 1 verification are marked as `Pending execution` / `Not Run`.

## 5. Test Results

### Test Execution Summary

- Execution Date: 2026-04-02
- Executed By: Faraz
- Sprint Covered: Sprint 1 - Core Foundation
- Execution Type: Automated verification with supporting manual demo validation
- Total test cases designed for Sprint 1: 110
- Automated test cases executed in code: 4

### Test Environment

| Item | Value |
| --- | --- |
| Framework | Django 5.2.12 |
| Python Version | 3.11.5 |
| Test Database | SQLite in-memory test database |
| Command Used | .venv/bin/python manage.py test -v 2 |

### Automated Test Results

| Test Case ID | Related Requirement | Result | Notes |
| --- | --- | --- | --- |
| TC-001 | US-1 | Pass | Registration flow created user successfully |
| TC-002 | US-3 | Pass | OTP password reset flow updated password successfully |
| TC-003 | US-5 | Pass | Listings page returned HTTP 200 successfully |
| TC-004 | US-4 | Pass | Authenticated user created listing successfully |

### Result Totals

| Metric | Value |
| --- | --- |
| Total Tests Executed | 4 |
| Passed | 4 |
| Failed | 0 |
| Errors | 0 |
| Overall Status | Pass |

### Verified Output Extract

Ran 4 tests in 4.645s

OK

## 6. Git Repository Link

| Item | Value |
| --- | --- |
| Repository Name | Skillswap |
| Repository URL | https://github.com/sh09030/Skillswap.git |
| Default Branch | main |
| Version Control Platform | GitHub |

## 7. Working Software Demo

### Demo Objective

Demonstrate that the Sprint 1 implementation satisfies the core foundation scope:

- user registration
- user login and logout
- profile viewing and editing
- OTP-based password reset
- listing creation and viewing
- basic listing management
- admin access

### Demo Artifacts

- `demo_auth_and_profile.mov`
- `demo_listings_and_admin.mov`

### Local Run Procedure

source .venv/bin/activate
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

### Demo Execution Steps

1. Open the homepage.
2. Register a new user.
3. Log in with the registered user.
4. Open the profile page.
5. Edit profile information and save.
6. Create a new listing.
7. Return to the listings page and verify the listing appears.
8. Open the listing detail page and show owner actions.
9. Start forgot password flow from `/accounts/forgot-password/`.
10. Use OTP shown by the development flow and reset password.
11. Log in again with the new password.
12. Open `/admin/` using superuser credentials.

## Submission Note

Demo recordings are submitted separately from this PDF report.

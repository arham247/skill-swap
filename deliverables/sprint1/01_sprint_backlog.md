# Sprint 1 Backlog

## Sprint Details

- Sprint Name: Sprint 1 - Core Foundation
- Sprint Duration: 3 days
- Sprint Goal: Build the base system with authentication and listings so users can register, manage profiles, and create/view skill listings.
- Team Members: Faraz, Hamza, Arham

## Team Role Allocation

| Team Member | Primary Responsibility in Sprint 1 |
| --- | --- |
| Faraz | Project setup, backend integration, authentication, database configuration, automated testing |
| Hamza | UI structure, templates, profile and listings frontend pages |
| Arham | Requirements mapping, backlog/task tracking, Trello coordination, QA support, demo preparation |

## Sprint User Stories

| ID | User Story | Priority | Story Points | Status |
| --- | --- | --- | --- | --- |
| US-1 | As a student, I want to register an account so I can use SkillSwap. | High | 3 | Done |
| US-2 | As a user, I want to log in and log out securely so I can access my account. | High | 2 | Done |
| US-3 | As a user, I want to manage my profile and reset my password using OTP so I can recover access to my account. | High | 5 | Done |
| US-4 | As a tutor, I want to create, edit, and delete skill listings so I can offer my skills on the platform. | High | 5 | Done |
| US-5 | As a learner, I want to view and browse available listings so I can find tutors. | High | 3 | Done |

## Sprint Backlog Items

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

## Definition of Done

An item is considered `Done` only when:

- The feature is implemented in code
- The feature is linked to the relevant user story
- The UI is functional for the Sprint 1 scope
- Database operations work correctly
- The item has been reviewed by the team
- Relevant automated or manual verification has been completed

## Sprint Deliverables

- Users can register and log in
- Users can edit profile details
- Users can reset password with OTP in the Sprint 1 development flow
- Users can create, edit, delete, and view listings
- Listings support basic search and category filtering
- Database schema is implemented and migrated successfully
- Basic UI is functional
- Sprint 1 documentation, test evidence, Trello tracking, and demo recordings are prepared

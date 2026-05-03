# Sprint 2 Backlog

## Sprint Details

- Sprint Name: Sprint 2 - Booking, Requests, Messaging, and Reviews
- Sprint Duration: 3 days
- Sprint Goal: Extend SkillSwap beyond listings by enabling learners to request sessions, tutors to manage bookings, users to communicate after acceptance, learners to review completed sessions, and students to post skill requests for tutors to apply to.
- Team Members: Faraz, Hamza, Arham

## Team Role Allocation

| Team Member | Primary Responsibility in Sprint 2 |
| --- | --- |
| Faraz | Backend models, migrations, booking/request workflows, automated tests, database integration |
| Hamza | Templates, dashboard layout, booking/request UI, demo flow support |
| Arham | Requirements mapping, Trello updates, QA scenarios, submission documentation |

## Sprint User Stories

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

## Sprint Backlog Items

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

## Definition of Done

An item is considered `Done` only when:

- The feature is implemented in code
- The feature is linked to the relevant SRS requirement
- The UI is functional for the Sprint 2 scope
- Access rules are enforced for learners, tutors, and request owners
- Database migrations are created and applied locally
- Relevant automated or manual verification has been completed

## Sprint Deliverables

- Learners can request tutoring sessions from listings
- Tutors can accept or reject booking requests
- Bookings support pending, accepted, rejected, completed, and cancelled statuses
- Users can view booking history in a dashboard
- Accepted bookings support participant messaging
- Completed bookings support learner reviews
- Learners can create skill requests
- Tutors can apply to open skill requests
- Request owners can accept tutor applications and automatically create bookings
- Sprint 2 documentation, tests, and demo procedure are prepared

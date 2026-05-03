# Trello Board

## Board Information

- Tool Used: Trello
- Project Board: SkillSwap SWE Project
- Board Link: https://trello.com/b/HofdCj69/skillswap-swe-project
- Sprint Covered: Sprint 2 - Booking, Requests, Messaging, and Reviews
- Team Members Reflected on Board: Faraz, Hamza, Arham

## Board Workflow

The Trello board followed the same sprint workflow used in Sprint 1:

- Backlog
- To Do
- In Progress
- Testing
- Done

## Sprint 2 Board Usage

The board was used to:

- map remaining SRS marketplace features into Sprint 2 tasks
- assign implementation, UI, QA, and documentation ownership
- track workflow completion from model design through testing
- monitor submission deliverables before sprint closure

## Sprint 2 Cards and Final Status

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

## Sprint 2 Board Outcome

- All planned Sprint 2 implementation cards were moved to `Done`
- No Sprint 2 task remained unresolved at sprint close
- The board status is consistent with the sprint backlog and test results

## Submission Evidence

- Board link is included above
- Code-level evidence exists in the `bookings` Django app, templates, URLs, migration, admin registration, and automated tests

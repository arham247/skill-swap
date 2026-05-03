# Working Software Demo

## Demo Objective

Demonstrate that the Sprint 2 implementation satisfies the next MVP workflow layer:

- booking request creation
- tutor booking acceptance and rejection
- booking dashboard/history
- booking cancellation and completion
- accepted-booking messaging
- completed-session review
- skill request creation
- tutor application to skill request
- request owner application acceptance
- automatic booking creation after application acceptance

## Local Run Procedure

```bash
source .venv/bin/activate
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Application URL:

http://127.0.0.1:8000/

## Demo Execution Steps

| Step | Action | Expected Outcome |
| --- | --- | --- |
| 1 | Open homepage | Listings feed loads successfully |
| 2 | Log in as a learner | Learner session starts |
| 3 | Open a listing owned by another user | Listing detail page displays `Request Session` action |
| 4 | Submit booking request with requested date/time and message | Booking is created with pending status |
| 5 | Log in as the tutor who owns the listing | Tutor session starts |
| 6 | Open dashboard and select the pending booking | Booking detail page displays tutor actions |
| 7 | Accept the booking | Booking status changes to accepted |
| 8 | Send a message in the booking thread | Message appears in the booking conversation |
| 9 | Mark the booking as completed | Booking status changes to completed |
| 10 | Log in as the learner and leave a review | Review is saved and displayed on the booking |
| 11 | Post a new skill request from the learner account | Request appears on the skill request board |
| 12 | Log in as a tutor and apply to the request | Application appears for the request owner |
| 13 | Log in as the request owner and accept the application | Request is fulfilled and an accepted booking is created |
| 14 | Open `/admin/` as superuser | Admin can view Sprint 2 models |

## Sprint 2 Features Demonstrated

- booking request workflow
- booking status tracking
- booking dashboard/history
- participant-only booking access
- booking message thread
- completed-session review flow
- skill request board
- tutor applications
- automatic booking creation after application acceptance
- admin management support

## Demo Evidence

No Sprint 2 recording file is currently included in this folder. A screen recording can be added later using this suggested filename:

- `demo_sprint2_booking_requests_messages_reviews.mov`

## Environment Note

Sprint 2 was verified locally with SQLite during development and testing. The project configuration remains environment-based through `.env.example`.

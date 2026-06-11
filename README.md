# SkillSwap

SkillSwap is a peer-to-peer skill exchange platform built with Django.

## Included


- Custom user model with registration, login/logout, profile editing, and OTP-based password reset
- Skill listing create, read, update, and delete flows
- Search and category filtering for listings
- Booking requests with tutor accept/reject, cancellation, completion, and booking history
- Messaging between learners and tutors after a booking is accepted
- Learner reviews for completed sessions
- Skill request board with tutor applications and automatic booking creation after acceptance
- Dashboard for bookings, posted skill requests, and applications
- MySQL-ready configuration with SQLite fallback for local development

## Run locally

1. Create and activate the virtual environment.
2. Install dependencies with `pip install -r requirements.txt`.
3. Copy `.env.example` to `.env` and adjust values if using MySQL.
4. Run `python manage.py migrate`.
5. Run `python manage.py createsuperuser`.
6. Run `python manage.py runserver`.

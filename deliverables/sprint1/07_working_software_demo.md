# Working Software Demo

## Demo Objective

Demonstrate that the Sprint 1 implementation satisfies the core foundation scope:

- user registration
- user login and logout
- profile viewing and editing
- OTP-based password reset
- listing creation and viewing
- basic listing management
- admin access

## Demo Artifacts Included

| Artifact | Purpose |
| --- | --- |
| `demo_auth_and_profile.mov` | Demonstrates authentication, profile flow, and password reset behavior |
| `demo_listings_and_admin.mov` | Demonstrates listings workflow and admin-side access |

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
| 1 | Open the homepage | Listings feed loads successfully |
| 2 | Register a new user at `/accounts/register/` | New account is created successfully |
| 3 | Log in with the registered user | User session starts successfully |
| 4 | Open `/accounts/profile/` | Profile data is visible |
| 5 | Edit profile information and save | Updated profile details are shown |
| 6 | Open listing creation page and create a new listing | Listing is saved and linked to the logged-in tutor |
| 7 | Return to the listings page | Newly created listing appears in the feed |
| 8 | Open listing detail page | Listing details and owner actions are visible |
| 9 | Start forgot password flow from `/accounts/forgot-password/` | OTP request page loads successfully |
| 10 | Use OTP shown by the development flow and reset password | Password changes successfully |
| 11 | Log in again with the new password | Updated credentials work correctly |
| 12 | Open `/admin/` using superuser credentials | Admin dashboard becomes accessible |

## Sprint 1 Features Demonstrated

- registration
- login/logout
- profile view/edit
- OTP-based password reset
- listing create/view/edit/delete
- listing search and category filtering
- Django admin management support

## Environment Note

Sprint 1 was verified locally with SQLite during development and testing. The project configuration remains MySQL-ready through environment settings, but MySQL execution was not available in the current workspace environment.

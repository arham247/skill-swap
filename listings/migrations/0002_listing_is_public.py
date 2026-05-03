from django.db import migrations, models


def hide_fulfilled_request_listings(apps, schema_editor):
    Listing = apps.get_model("listings", "Listing")
    SkillRequestApplication = apps.get_model("bookings", "SkillRequestApplication")

    accepted_applications = SkillRequestApplication.objects.filter(
        status="accepted",
        booking__isnull=False,
    ).select_related("booking__listing", "skill_request")

    for application in accepted_applications:
        listing = application.booking.listing
        skill_request = application.skill_request
        if (
            listing.tutor_id == application.tutor_id
            and listing.title == skill_request.title
            and listing.category == skill_request.category
            and listing.description == skill_request.description
            and listing.availability == skill_request.availability
            and listing.created_at >= application.created_at
        ):
            Listing.objects.filter(pk=listing.pk).update(is_public=False)


class Migration(migrations.Migration):

    dependencies = [
        ("bookings", "0001_initial"),
        ("listings", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="listing",
            name="is_public",
            field=models.BooleanField(default=True),
        ),
        migrations.RunPython(hide_fulfilled_request_listings, migrations.RunPython.noop),
    ]

from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        # Create a default host user if none exists
        host, created = User.objects.get_or_create(
            email="host@example.com",
            defaults={"username": "host_user"}
        )

        sample_data = [
            {
                "title": "Cozy Apartment",
                "description": "A beautiful and quiet apartment.",
                "price_per_night": 120.00,
                "location": "Lagos, Nigeria",
            },
            {
                "title": "Beach House",
                "description": "Oceanfront property with amazing views.",
                "price_per_night": 300.00,
                "location": "Cape Town, South Africa",
            },
        ]

        for data in sample_data:
            Listing.objects.create(host=host, **data)

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))

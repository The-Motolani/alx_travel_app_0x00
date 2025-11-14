from rest_framework import serializers
from .models import Listing, Booking, Review


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = [
            "id",
            "title",
            "description",
            "price_per_night",
            "location",
            "host",
            "created_at",
        ]


class BookingSerializer(serializers.ModelSerializer):
    listing = ListingSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = [
            "id",
            "listing",
            "guest",
            "check_in",
            "check_out",
            "created_at",
        ]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "id",
            "listing",
            "reviewer",
            "rating",
            "comment",
            "created_at",
        ]
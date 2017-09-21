from rest_framework import serializers
from ..models import Product, User, Campaign, Donation, Tag
import datetime
from django.core.exceptions import ValidationError


class ProductSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Product
        fields = ('auto_increment_id', 'name', 'description', 'price')
        # read_only_fields = ('auto_increment_id')
        extra_kwargs = {"name": {"error_messages": {"required": "Give yourself a username"}}}


class UserSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = User
        fields = ('pk', 'name', 'location', 'username', 'password', 'email')
        # read_only_fields = ('auto_increment_id')


class CampaignSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    user = serializers.ReadOnlyField(source='user.pk')

    def __init__(self, *args, **kwargs):
        super(CampaignSerializer, self).__init__(*args, **kwargs)
        self.fields['end_date'].validators.append(self.validate_campaign_date)

    def validate_campaign_date(self, end_date):
        today = str(datetime.datetime.today())
        date = str(end_date)
        if date < today:
            raise ValidationError("You cannot finish an event in the past.")

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Campaign
        fields = ('auto_increment_id', 'user', 'product', 'title', 'description', 'end_date')
        # read_only_fields = ('auto_increment_id')


class DonationSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    user = serializers.ReadOnlyField(source='user.pk')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Donation
        fields = ('auto_increment_id', 'user', 'campaign', 'price')
        # read_only_fields = ('auto_increment_id')


class TagSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Tag
        fields = ('auto_increment_id', 'name')
        # read_only_fields = ('auto_increment_id')

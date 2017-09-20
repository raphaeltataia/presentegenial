from rest_framework import serializers
from ..models import Product, User, Campaign, Tag


class ProductSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Product
        fields = ('auto_increment_id', 'name', 'description', 'price')
        # read_only_fields = ('auto_increment_id')


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

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Campaign
        fields = ('auto_increment_id', 'user', 'product', 'title', 'description', 'end_date')
        # read_only_fields = ('auto_increment_id')


class TagSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Tag
        fields = ('auto_increment_id', 'name')
        # read_only_fields = ('auto_increment_id')

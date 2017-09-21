from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import ProductSerializer, UserSerializer, CampaignSerializer, DonationSerializer, TagSerializer
from ..models import Product, User, Campaign, Donation, Tag
from rest_framework import permissions
from .permissions import IsOwner


class CreateProductView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new product."""
        serializer.save()


class CreateUserView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    # print request.user
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new user."""
        serializer.save()


class CreateCampaignView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new campaign."""
        serializer.save(user=self.request.user)


class CreateDonationView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner)  # This lets read without authentication

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save(user=self.request.user)


class CreateTagView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new product."""
        serializer.save()

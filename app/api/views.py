from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import ProductSerializer, UserSerializer, CampaignSerializer, DonationSerializer, TagSerializer
from ..models import Product, User, Campaign, Donation, Tag
from rest_framework import permissions
from .permissions import IsOwner, IsPostOrIsAuthenticated


class CreateProductView(generics.ListCreateAPIView):
    """This class defines the create/list/read behavior of our Product entity."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        """Save the post data when creating a new product."""
        serializer.save()


class CreateUserView(generics.ListCreateAPIView):
    """This class defines the create/list/read behavior of our User entity."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsPostOrIsAuthenticated,)

    def perform_create(self, serializer):
        """Save the post data when creating a new user."""
        serializer.save()


class CreateCampaignView(generics.ListCreateAPIView):
    """This class defines the create/list/read behavior of our Campaign entity."""
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner)

    def perform_create(self, serializer):
        """Save the post data when creating a new campaign."""
        serializer.save(user=self.request.user)


class DetailCampaignView(generics.ListAPIView):
    """This class defines the list behavior of our Campaign entity."""
    serializer_class = CampaignSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    lookup_url_kwarg = "id"

    def get_queryset(self):
        """
        This view should return a list of all the campaigns for
        the user as determined by the user id.
        """
        campaign_id = self.kwargs.get(self.lookup_url_kwarg)
        return Campaign.objects.filter(auto_increment_id=campaign_id)


class MyCampaignsView(generics.ListAPIView):
    """This class defines the list behavior of our Campaign entity."""
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)  # This lets read without authentication


class CreateDonationView(generics.ListCreateAPIView):
    """This class defines the create/list/read behavior of our Donation entity."""
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner)
    lookup_url_kwarg = "id"

    def perform_create(self, serializer):
        """Save the post data when creating a new donation."""
        campaign_id = self.kwargs.get(self.lookup_url_kwarg)
        cp = Campaign.objects.get(auto_increment_id=campaign_id)
        serializer.save(user=self.request.user, campaign=cp)


class CreateTagView(generics.ListCreateAPIView):
    """This class defines the create/list/read behavior of our Tag entity."""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new tag."""
        serializer.save()

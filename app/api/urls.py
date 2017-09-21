from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateProductView, CreateUserView, CreateCampaignView, DetailCampaignView, CreateDonationView, \
    CreateTagView, MyCampaignsView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = {
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/products/$', CreateProductView.as_view(), name="create"),
    url(r'^api/users/$', CreateUserView.as_view(), name="create"),
    url(r'^api/campaigns/$', CreateCampaignView.as_view(), name="create"),
    url(r'^api/campaigns/my$', MyCampaignsView.as_view(), name="listMyCampaigns"),
    url(r'^api/campaigns/(?P<id>[0-9]+)$', DetailCampaignView.as_view(), name="CampaignDetail"),
    url(r'^api/campaigns/(?P<id>[0-9]+)/donate$', CreateDonationView.as_view(), name="CampaignDonate"),
    url(r'^api/tags/$', CreateTagView.as_view(), name="create"),
    url(r'^api/get-token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)
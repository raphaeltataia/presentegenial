from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateProductView, CreateUserView, CreateCampaignView, CreateDonationView, CreateTagView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = {
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/products/$', CreateProductView.as_view(), name="create"),
    url(r'^api/users/$', CreateUserView.as_view(), name="create"),
    url(r'^api/campaigns/$', CreateCampaignView.as_view(), name="create"),
    url(r'^api/donations/$', CreateDonationView.as_view(), name="create"),
    url(r'^api/tags/$', CreateTagView.as_view(), name="create"),
    url(r'^api/get-token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)
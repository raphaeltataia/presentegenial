from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateProductView, CreateUserView, CreateCampaignView, CreateTagView

urlpatterns = {
    url(r'^api/products/$', CreateProductView.as_view(), name="create"),
    url(r'^api/users/$', CreateUserView.as_view(), name="create"),
    url(r'^api/campaigns/$', CreateCampaignView.as_view(), name="create"),
    url(r'^api/tags/$', CreateTagView.as_view(), name="create"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
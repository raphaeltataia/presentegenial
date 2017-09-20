from django.contrib import admin
from .models import Campaign
from .models import User
from .models import Product
from .models import Donation
from .models import Tag

# Register your models here.


class CampaignAdmin(admin.ModelAdmin):
    list_display = ('auto_increment_id', 'user', 'product', 'tag', 'title', 'description', 'created_date', 'end_date')


class UserAdmin(admin.ModelAdmin):
    list_display = ('location', 'full_name', 'email')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('auto_increment_id', 'name', 'description', 'created_date', 'price')


class DonationAdmin(admin.ModelAdmin):
    list_display = ('auto_increment_id', 'campaign', 'user', 'created_date', 'price')


class TagAdmin(admin.ModelAdmin):
    list_display = ('auto_increment_id', 'name', 'slug')


admin.site.register(Campaign)
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Donation)
admin.site.register(Tag)

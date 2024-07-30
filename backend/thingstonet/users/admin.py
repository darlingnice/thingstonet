from django.contrib import admin
from .models import User,Organization,UserOrganization

admin.site.register(User)
admin.site.register(Organization)
admin.site.register(UserOrganization)

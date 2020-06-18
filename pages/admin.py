from django.contrib import admin

# Register your models here.
from.models import Contact, Posts, Catagory
admin.site.register([Contact, Posts, Catagory])
# admin.site.register(Posts)

from django.contrib import admin
from .models import BoChatRoom, BoMessage

# Register your models here.

admin.site.register(BoChatRoom)
admin.site.register(BoMessage)
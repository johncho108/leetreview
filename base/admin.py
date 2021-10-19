from django.contrib import admin

# Register your models here.
from .models import Entry, Feedback

admin.site.register(Entry)
admin.site.register(Feedback)

from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Author)
admin.site.register(models.Comment)
admin.site.register(models.Post)
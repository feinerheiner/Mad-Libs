from django.contrib import admin
from .models import Story, UserInput, Input


# Register your models here.
admin.site.register(Story)
admin.site.register(UserInput)
admin.site.register(Input)



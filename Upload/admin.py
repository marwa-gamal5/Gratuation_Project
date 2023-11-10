

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Folder
from .models import OneFolder
admin.site.register(Folder)
admin.site.register(OneFolder)

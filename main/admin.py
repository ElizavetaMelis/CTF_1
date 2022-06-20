from enum import Flag
from django.contrib import admin

from main.models import *

admin.site.register(Category)
admin.site.register(Difficulty)
admin.site.register(Task)
admin.site.register(Flag_Check)
admin.site.register(Student)

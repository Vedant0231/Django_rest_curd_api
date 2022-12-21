from django.contrib import admin
from .models import Student


"""Register your models here.
By this we can view this table in
admin side.
"""

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "roll", "city"]
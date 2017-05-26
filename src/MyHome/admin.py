from django.contrib import admin
from .models import SignUp
from .forms import SignUpForm
from . import models

class SignUpAdmin(admin.ModelAdmin):
    list_display = ["First_Name", "Last_Name", "Major", "Classes_Per_Quarter", "__str__", "timestamp", "updated"]  # Things we want to display on admin database list
    form = SignUpForm

admin.site.register(SignUp, SignUpAdmin)

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("username",
                    "student_number",
                    "student_name",
                    "classes_per_quarter",
                    "major",
                    "summer",
                    "online",
                    "class_list")

    search_fields = ["user__username"]

@admin.register(models.cs_Classes)
class cs_ClassesAdmin(admin.ModelAdmin):
    list_display = ("class_number",
                    "class_name",
                    "pre_req",
                    "class_type",
                    "summer",
                    "spring",
                    "fall",
                    "winter",
                    "online")


@admin.register(models.is_Classes)
class is_ClassesAdmin(admin.ModelAdmin):
    list_display = ("class_number",
                    "class_name",
                    "pre_req",
                    "class_type",
                    "summer",
                    "spring",
                    "fall",
                    "winter",
                    "online")
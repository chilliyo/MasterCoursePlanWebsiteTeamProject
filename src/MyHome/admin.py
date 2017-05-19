from django.contrib import admin
from .models import SignUp
from .forms import SignUpForm
from . import models

class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__str__", "timestamp", "updated"]  # Things we want to display on admin database list
    form = SignUpForm
    #class Meta:
        #model = SignUp
admin.site.register(SignUp, SignUpAdmin)

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("username",
                    "student_number",
                    "student_name",
                    "current_credits",
                    "classes_per_quarter",
                    "major",
                    "concentration",
                    "summer",
                    "online",
                    "class_list")

    search_fields = ["user__username"]

@admin.register(models.Classes)
class ClassesAdmin(admin.ModelAdmin):
    list_display = ("class_number",
                    "class_name",
                    "Professor",
                    "pre_req",
                    "class_type",
                    "time",
                    "summer",
                    "spring",
                    "fall",
                    "winter",
                    "online",
                    "start_date",
                    "end_date",
                    "location",
                    "room")

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from . import managers

# Create your models here.
class SignUp(models.Model):
    email = models.EmailField()
    First_Name = models.CharField(max_length=120, blank=False, null=True)
    Last_Name = models.CharField(max_length=120, blank=False, null=True)
    #Current_Credits = models.CharField(max_length=120, blank=False, null=True)
    Classes_Per_Quarter = models.CharField(max_length=120, blank=False, null=True)
    Major = models.CharField(max_length=120, blank=False, null=True)
    summer = models.BooleanField(default=False)
    online = models.BooleanField(default=False)

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    ClassesPerQuarter = (('1 Class', '1 Class'), ('2 Classes', '2 Classes'), ('3 Classes', '3 Classes'),)
    Classes_Per_Quarter = models.CharField(max_length=120, choices=ClassesPerQuarter)

    MyMajor = (('Computer Science (Standard Concentration)', 'Computer Science (Standard Concentration)'),
               ('Information Systems (Business Analysis/Systems Analysis)', 'Information Systems (Business Analysis/Systems Analysis)'),
               ('Information Systems (Business Intelligence Concentration)', 'Information Systems (Business Intelligence Concentration)'),
               ('Information Systems (Database Administration Concentration)', 'Information Systems (Database Administration Concentration)'),
               ('Information Systems (IT Enterprise Management Concentration)', 'Information Systems (IT Enterprise Management Concentration)'),
               ('Information Systems (Standard Concentration)', 'Information Systems (Standard Concentration)'),)
    Major = models.CharField(max_length=120, choices=MyMajor)

    StartQuarter = (('Fall', 'Fall'), ('Winter', 'Winter'), ('Spring', 'Spring'),)
    Current_Credits = models.CharField(max_length=120, choices=StartQuarter)

    def __str__(self):  # Python 3.3 is __str__ and lower version is __unicode__
        return self.email


class Profile(models.Model):
    #relations
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="profile", verbose_name=_("user"))
    ##attributes

    student_name = models.CharField(max_length=50, verbose_name=_("student_name"))
    student_number = models.CharField(max_length=100, primary_key=True, verbose_name=_("student_number"))
    current_credits = models.IntegerField(default=0, verbose_name=_("current_credits"))
    classes_per_quarter = models.IntegerField(default=0, verbose_name=_("classes_per_quarter"), validators=[MaxValueValidator(3), MinValueValidator(1)])
    major = models.CharField(max_length=50, verbose_name=_("major"))
    summer = models.BooleanField(default=False, verbose_name=_("summer"))
    online = models.BooleanField(default=False, verbose_name=_("online"))
    class_list = models.CharField(max_length=1000, default="", verbose_name=_("class_list"))
    objects = managers.ProfileManager()

    @property
    def username(self):
        return self.user.username

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
        ordering = ("user",)

    def __str__(self):
        return self.user.username

class cs_Classes(models.Model):
    class_number = models.CharField(max_length=50, primary_key=True)
    class_name = models.CharField(max_length=50)
    pre_req = models.CharField(max_length= 1000)
    class_type = models.CharField(max_length=100)
    summer = models.BooleanField(default=False)
    spring = models.BooleanField(default=False)
    fall = models.BooleanField(default=False)
    winter = models.BooleanField(default=False)
    online = models.BooleanField(default=False)


class is_Classes(models.Model):
    class_number = models.CharField(max_length=50, primary_key=True)
    class_name = models.CharField(max_length=50)
    pre_req = models.CharField(max_length= 1000)
    class_type = models.CharField(max_length=100)
    summer = models.BooleanField(default=False)
    spring = models.BooleanField(default=False)
    fall = models.BooleanField(default=False)
    winter = models.BooleanField(default=False)
    online = models.BooleanField(default=False)

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from . import managers

# Create your models here.
class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):  # Python 3.3 is __str__ and lower version is __unicode__
        return self.email





class asdf(models.Model):

    student_number = models.CharField(max_length=100, primary_key=True)
    student_name = models.CharField(max_length=50)

    current_credits = models.IntegerField()

    classes_per_quarter = models.IntegerField(default=0)

    #faculty_name = models.ForeignKey('Faculty', default="")

    major = models.CharField(max_length=50)
    concentration = models.CharField(max_length=4)
    summer = models.BooleanField(default=False)
    online = models.BooleanField(default=False)

    class_list = models.CharField(max_length=1000, default="")

class Profile(models.Model):
    #relations
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name="profile",
                                verbose_name=_("user")
                                )
    ##attributes

    student_name = models.CharField(max_length=50,
                                    verbose_name=_("student_name")
                                    )
    student_number = models.CharField(max_length=100,
                                      primary_key=True,
                                      verbose_name=_("student_number")
                                    )

    current_credits = models.IntegerField(default=0,
                                          verbose_name=_("current_credits")
                                          )

    classes_per_quarter = models.IntegerField(default=0,
                                              verbose_name=_("classes_per_quarter")
                                              )

    #faculty_name = models.ForeignKey('Faculty', default="")

    major = models.CharField(max_length=50,
                             verbose_name=_("major")
                             )
    concentration = models.CharField(max_length=4,
                                     verbose_name=_("concentration")
                                     )
    summer = models.BooleanField(default=False,
                                 verbose_name=_("summer")
                                 )
    online = models.BooleanField(default=False,
                                 verbose_name=_("online")
                                 )

    class_list = models.CharField(max_length=1000,
                                  default="",
                                  verbose_name=_("class_list")
                                  )

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


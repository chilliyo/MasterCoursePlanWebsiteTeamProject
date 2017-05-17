from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PremissionsMixin

class User(AbstractBaseUser, PermissionsMixin):
    student_number = models.CharField(max_length=30, primary_key=True)
    student_name = models.CharField(max_length=30, primary_key=True)

    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    is_faculty = models.BoleanField(default=False)

    current_credits = models.IntegerField(default=0)

    classes_per_quarter = models.IntegerField(default=0)

    #faculty_name = models.ForeignKey('Faculty', default="")

    major = models.CharField(max_length=50)
    concentration = models.CharField(max_length=4)
    summer = models.BooleanField(default=False)
    online = models.BooleanField(default=False)

    class_list = models.CharField(max_length=1000, default="")

    def get_student_name(self):
        return self.student_name

    def get_email(self):
        return self.email


class UserManager(BaseUserManager):

    def create_user(self, email, password, major, concentration, **kwargs):
        user = self.model(
            email=self.normalize_email(email),
            major = self.major,
            concentration = self.concentration,
            **kwargs
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PremissionsMixin


# Create your models here.
class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):  # Python 3.3 is __str__ and lower version is __unicode__
        return self.email


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



class Faculty(models.Model):
    faculty_name = models.CharField(max_length=50, primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Classes(models.Model):
    class_number = models.CharField(max_length=50, primary_key=True)
    class_name = models.CharField(max_length=50, primary_key=True)

    Professor = models.CharField(max_length=50)

    pre_req = models.CharField(max_length= 1000)
    class_type = models.CharField(max_length=100)
    time = models.DateField()
    summer = models.BooleanField(default=False)
    spring = models.BooleanField(default=False)
    fall = models.BooleanField(default=False)
    winter = models.BooleanField(default=False)

    online = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField()
    DOW = models.CharField(max_length=50)
    DOW2 = models.CharField(max_length=50)
    location = models.CharField(max_length=50, primary_key=True)
    room = models.CharField(max_length=50, primary_key=True)

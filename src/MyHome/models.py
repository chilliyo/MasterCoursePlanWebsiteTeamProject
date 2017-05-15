from django.db import models


# Create your models here.
class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):  # Python 3.3 is __str__ and lower version is __unicode__
        return self.email


class Student(models.Model):
    student_number = models.CharField(max_length=100, primary_key=True)
    student_name = models.CharField(max_length=50, primary_key=True)

    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    current_credits = models.IntegerField()
    credits_remaining = models.IntegerField()
    classes_per_quarter = models.IntegerField()

    faculty_name = models.ForeignKey('Faculty')

    major = models.CharField(max_length=50)
    summer = models.BooleanField(default=False)
    online = models.BooleanField(default=False)

    class1 = models.CharField(max_length=50)
    class2 = models.CharField(max_length=50)
    class3 = models.CharField(max_length=50)
    class4 = models.CharField(max_length=50)
    class5 = models.CharField(max_length=50)
    class6 = models.CharField(max_length=50)
    class7 = models.CharField(max_length=50)
    class8 = models.CharField(max_length=50)
    class9 = models.CharField(max_length=50)
    class10 = models.CharField(max_length=50)
    class11 = models.CharField(max_length=50)
    class12 = models.CharField(max_length=50)
    class13 = models.CharField(max_length=50)


class Faculty(models.Model):
    faculty_name = models.CharField(max_length=50, primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Classes(models.Model):
    class_number = models.CharField(max_length=50, primary_key=True)
    class_name = models.CharField(max_length=50, primary_key=True)

    Professor = models.CharField(max_length=50)

    class_type = models.CharField(max_length=100)
    time = models.DateField()
    summer = models.BooleanField(default=False)
    online = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField()
    DOW = models.CharField(max_length=50)
    DOW2 = models.CharField(max_length=50)
    location = models.CharField(max_length=50, primary_key=True)
    room = models.CharField(max_length=50, primary_key=True)

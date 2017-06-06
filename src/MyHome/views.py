from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm, SignUpForm
from .models import SignUp, cs_Classes
from django.http import HttpResponse

from .is_algorithm import is_get_path
from .cs_algorithm import cs_get_path
from .ba_algorithm import ba_get_path
from .bi_algorithm import bi_get_path
from .da_algorithm import da_get_path
from .em_algorithm import em_get_path


# Create your views here.
def home(request):
    title = 'Sign Up Now'
    form = SignUpForm(request.POST or None)
    context = {
        "title": title,
        "form": form
    }
    if form.is_valid():
        #form.save()
        instance = form.save(commit=False)
        test_variable = instance
        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name
        instance.save()
        context = {
            "title": "Thank You"
        }

    if request.user.is_authenticated() and request.user.is_staff:
        queryset = SignUp.objects.all().order_by('-timestamp')
        context = {
            "queryset": queryset
        }
    return render(request, "home.html", context)

def test(request):
    # if request.method == 'POST':
    #     test1 = request.POST.get('textfield', None)

    queryset = SignUp.objects.all().order_by('-timestamp')

    user_email = queryset[0]

    profile = SignUp.objects.get(email = user_email)
    quarter = profile.Start_Quarter

    #test = single_quarter_classes(profile, profile.Start_Quarter)
    #test = get_class("2", [], profile.Classes_Per_Quarter, ["None"], "Fall", profile.online, profile.summer)
    if profile.Major == 'Computer Science (Standard Concentration)':
        test = cs_get_path(profile)
    elif profile.Major == 'Information Systems (Business Analysis/Systems Analysis)':
        test = ba_get_path(profile)
    elif profile.Major == 'Information Systems (Business Intelligence Concentration)':
        test = bi_get_path(profile)
    elif profile.Major == 'Information Systems (Database Administration Concentration)':
        test = da_get_path(profile)
    elif profile.Major == 'Information Systems (IT Enterprise Management Concentration)':
        test = em_get_path(profile)
    else:
        test = is_get_path(profile)

    context = {
        "test" : test,
        "quarter" : quarter
    }
    return render(request, "test.html", context)


def contact(request):
    title = 'Contact Us'
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")

        # print email, message, full_name
        subject = 'Site contact form'
        form_email = settings.EMAIL.HOST.USER
        to_email = [form_email, 'youremail@email.com']
        contact_message = "%s: %s via %s"%(
            form_full_name,
            form_message,
            form_email)
        some_html_message = """
        <h1>Hello</h1>
        """

        send_mail(subject,
                  contact_message,
                  form_email,
                  to_email,
                  html_message=some_html_message,
                  fail_silently=True)

    context = {
        "form": form,
        "title": title,
    }
    return render(request, "forms.html", context)

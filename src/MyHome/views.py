from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm, SignUpForm
from .models import SignUp, is_Classes
from .is_algorithm import single_quarter_classes, get_class, get_path
from .cs_algorithm import get_path

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

    profile = SignUp.objects.get(First_Name = "test")
    #test = single_quarter_classes(profile, profile.Start_Quarter)
    #test = get_class("2", [], profile.Classes_Per_Quarter, ["None"], "Fall", profile.online, profile.summer)
    test = get_path(profile)
    context = {
        "test" : test
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

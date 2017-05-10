from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm, SignUpForm
# Create your views here.
def home(request):
    title = 'Welcome'
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

    return render(request, "home.html", context)

def contact(request):
    title = 'Contact Us'
    form = ContactForm(request.POST or None)
    if form.is_valid():
        #for key, value in form.cleaned_data.items():
            #print(key, value)
            #print(form.cleaned_data.get(key))
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
from django import forms
from .models import SignUp

class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['email', 'First_Name', 'Last_Name', 'Major', 'Classes_Per_Quarter', 'Start_Quarter', 'summer', 'online']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        return full_name

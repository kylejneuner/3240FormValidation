from django import forms

from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split('@')
        domain, extension = provider.split('.')
        if not domain == "virginia":
            raise forms.ValidationError("Please use your virginia email")
        if not extension == "edu":
            raise forms.ValidationError("Please use edu email")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        if(any(char.isdigit() for char in full_name)):
        	raise forms.ValidationError("Name cannot contain numbers")
        return full_name

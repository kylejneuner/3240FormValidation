from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.

class fullForm(forms.Form)
	name = forms.CharField(help_text="Please enter your name.")
	email = forms.EmailField(help_text="Please enter your e-mail address.")
	age = forms.IntegerField(help_text="Please enter your age.")

	def clean_name(self):
        data = self.cleaned_data['name']
        
        if len(data) < 0 or len(data) > 30:
            raise ValidationError(_('Invalid name - your name should be between 0-30 characters.'))

        # Remember to always return the cleaned data.
        return data

    def clean_email(self):
    	data = self. cleaned_data['email']

    	return data

    def clean_age(self):
    	data = self.cleaned_data['age']
    	if age < 0 or age > 105:
    		raise ValidationError(_("Invalid age - your age should be between 0 and 105 years old."))
    	return data

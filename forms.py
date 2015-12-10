from django import forms
from .models import contact_us
from django.forms import Textarea
from django.db import models

# Contact us form
class contact_us_form(forms.ModelForm):
	class Meta:
		model = contact_us
		fields = ['fullname', 'email', 'subject', 'message']

	formfield_overrides = {
		models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
	}
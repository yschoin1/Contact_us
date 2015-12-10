from django.contrib import admin
from .models import contact_us
from .forms import contact_us_form

# Contact us admin page display settings
class contact_us_admin(admin.ModelAdmin):
	list_display = ['__unicode__', 'subject', 'timestamp']
	form = contact_us_form

# Registered the change
admin.site.register(contact_us, contact_us_admin)
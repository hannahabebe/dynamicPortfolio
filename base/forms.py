from optparse import OptionContainer
from django.forms import ModelForm
from django.forms import Textarea
from .models import contact


class ContactForm(ModelForm):
    class Meta:
        model = contact
        fields = ["fName", "lName", "country","message"]
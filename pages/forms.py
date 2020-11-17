from django.forms import ModelForm
from .models import feed

class newfeed(ModelForm):
    class Meta:
        model = feed
        fields = '__all__'
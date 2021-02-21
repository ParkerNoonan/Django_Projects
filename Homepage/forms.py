from django import forms
from django.core.exceptions import ValidationError

from .models import Project, Valves

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class ValveForm(forms.ModelForm):
    class Meta:
        model = Valves
        fields = '__all__'
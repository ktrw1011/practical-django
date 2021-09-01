from django import forms
from django.forms import fields

from snippets.models import Snippet

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ('title', 'code', 'description')
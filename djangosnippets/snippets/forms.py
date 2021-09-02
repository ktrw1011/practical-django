from django import forms
from django.forms import fields

from snippets.models import Snippet, Comment

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ('title', 'code', 'description')
        readonly_fields = ('created_at', 'updated_at')

class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput, label='')
    
    class Meta:
        model = Comment
        fields = ('text',)
        readonly_fields = ('commented_at',)

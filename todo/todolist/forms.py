from django.forms import ModelForm
from django import forms

import models

class TodoForm(ModelForm):
  class Meta:
    model = models.Todo
    fields = ('title', 'desc')
    widgets = {
      'desc': forms.Textarea(attrs={'rows':3}),
    }


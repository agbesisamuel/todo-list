from django import forms

from .models import Todo


class TodoForm(forms.Form):
    title = forms.CharField(max_length=200,
                widget=forms.TextInput(
                    attrs={'class': 'form-control',
                    'placeholder': 'What do you want to do?',
                    'aria-label': 'Todo', 
                    'aria-describedby': 'add-btn'}
                ))

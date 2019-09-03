from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PostSearchForm(forms.Form):
    search_word = forms.CharField(
        label='Search Word',
        widget=forms.TextInput(
            attrs={
                'class': 'searchForm',
                'placeholder': 'Type here to search',

            }
        )

    )
from django import forms
from .models import concertModel

class SearchForm(forms.Form):
    ConcertName = forms.CharField(max_length=200,label='نام کنسرت',required=False)

class ConcertForm(forms.ModelForm):
    class Meta:
        model = concertModel
        fields = '__all__'
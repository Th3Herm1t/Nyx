
from django import forms

class MBTIForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

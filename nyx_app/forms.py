
from django import forms

class MBTIForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))


class FeedbackForm(forms.Form):
    feedback_text = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))

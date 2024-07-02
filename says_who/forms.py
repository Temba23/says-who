from django import forms
from .models import Quote
class StarForm(forms.Form):
    name = forms.CharField(
        label="Star name",
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = '__all__'
        labels = {
            'star':'Star',
            'quote':'Quote'
        }
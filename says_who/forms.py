from django import forms
from .models import Quote, Question
class StarForm(forms.Form):
    name = forms.CharField(
        label="Star name",
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['star', 'quote']
        label = {
            'star' : 'Star',
            'quote' : 'Quote'
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        label = {
            'star' : 'Star',
            'quote' : 'Quote'
        }
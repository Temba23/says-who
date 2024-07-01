from django import forms

class StarForm(forms.Form):
    name = forms.CharField(
        label="Star name",
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
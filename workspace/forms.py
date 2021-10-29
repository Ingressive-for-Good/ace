from django import forms

class ContributorForm(forms.Form):
	email = forms.EmailField(max_length=100)
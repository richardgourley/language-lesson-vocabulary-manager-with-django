from django import forms

class SearchEntryForm(forms.Form):
	search_term = forms.CharField(label="Word or sentence:", max_length=100)


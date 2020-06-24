from django import forms

class SearchEntryForm(forms.Form):
	search_term = forms.CharField(label="Enter a search term", max_length=100)

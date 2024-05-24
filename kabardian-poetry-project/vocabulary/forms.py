from django import forms

class AddWordForm(forms.Form):
    word = forms.CharField(label='Word', max_length=250)


class DeleteWordForm(forms.Form):
    vocabulary_entry = forms.CharField(label='Word', max_length=250)

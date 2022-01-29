from django import forms
from .models import Books


class BookForm(forms.ModelForm):
    class Meta:
        model=Books
        fields='__all__'
        widgets = {
        'isbn': forms.TextInput(attrs={'class':'form-fontrol'}),
        'title': forms.TextInput(attrs={'class':'form-fontrol'}),
        'article': forms.TextInput(attrs={'class':'form-fontrol'}),
        'publisher': forms.TextInput(attrs={'class':'form-fontrol'}),
        'price': forms.TextInput(attrs={'class':'form-fontrol'}),
        }
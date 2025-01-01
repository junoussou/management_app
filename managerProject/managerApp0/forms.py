from django import forms
from .models import Book
from datetime import date

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date', 'id': 'published_date'}),
        }
        labels = {
            'title': 'Titre',
            'author': 'Auteur',
            'published_date': 'Date de publication',
        }

    def clean_published_date(self):
        published_date = self.cleaned_data.get('published_date')
        if published_date > date.today():
            raise forms.ValidationError("La date de publication ne peut pas être dans le futur.")
        return published_date

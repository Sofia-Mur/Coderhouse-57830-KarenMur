from django import forms
from myapp.models import Author, Book, Publisher

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)

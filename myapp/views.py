from django.shortcuts import render, get_object_or_404
from myapp.models import Author, Book, Publisher
from myapp.forms import AuthorForm, BookForm, PublisherForm, SearchForm

def author_create(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('author_list')
    return render(request, 'myapp/author_form.html', {'form': form})

def search_books(request):
    form = SearchForm(request.GET or None)
    results = []
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Book.objects.filter(title__icontains=query)
    return render(request, 'myapp/search_results.html', {'form': form, 'results': results})



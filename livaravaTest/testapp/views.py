from django.shortcuts import render

# Create your views here.


def authors(request):
	authors = []

    return render(request, 'index.html', {'authors': authors})

def names(request):
    return render(request, 'names.html')

def years(request):
    return render(request, 'years.html')

def poetry_add(request):
    return render(request, 'poetry_add.html')

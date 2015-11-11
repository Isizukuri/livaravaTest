#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

from models import Author, Verse, Year

# Create your views here.


def authors(request):
    verses = Verse.category().instance.all()
    authors = Author.category().instance.all()
    years = Year.category().instance.all()
    if request.method == 'GET':
        return render(request, 'jinja2/index.html', {'verses': verses,
                                                     'authors': authors,
                                                     'years': years})
    elif request.method == 'POST':
        if request.POST.get('author_name'):
            Author(name=unicode(request.POST['author_name'])).save()
        authors = Author.category().instance.all()
        return render(request, 'jinja2/index.html', {'verses': verses,
                                                     'authors': authors,
                                                     'years': years})


def names(request):
    verses = Verse.category().instance.all()
    authors = Author.category().instance.all()
    years = Year.category().instance.all()
    auth_names = [author.name for author in Author.category().instance.all()]
    year_list = [year.year for year in Year.category().instance.all()]
    if request.method == 'GET':
        return render(request, 'jinja2/names.html', {'verses': verses,
                                                     'authors': authors,
                                                     'years': years})
    elif request.method == 'POST':
        if request.POST.get('name') and request.POST.get('text'):
            verse = Verse(
                name=unicode(request.POST['name']), text=unicode(request.POST['text'])).save()
            if request.POST.get('author'):
                if unicode(request.POST.get('author')) in auth_names:
                    verse.author.connect(
                        Author.index.get(name=request.POST['author']))
                else:
                    Author(name=unicode(request.POST['author'])).save()
                    verse.author.connect(
                        Author.index.get(name=unicode(request.POST['author'])))
            if request.POST.get('year'):
                if int(request.POST.get('year')) in year_list:
                    verse.year.connect(
                        Year.index.get(year=int(request.POST['year'])))
                else:
                    Year(year=request.POST['year']).save()
                    verse.year.connect(
                        Year.index.get(year=int(request.POST['year'])))
        verses = Verse.category().instance.all()
        authors = Author.category().instance.all()
        years = Year.category().instance.all()
        return render(request, 'jinja2/names.html', {'verses': verses,
                                                     'authors': authors,
                                                     'years': years})


def years(request):
    verses = Verse.category().instance.all()
    authors = Author.category().instance.all()
    years = Year.category().instance.all()
    if request.method == 'GET':
        years = Year.category().instance.all()
        return render(request, 'jinja2/years.html', {'verses': verses,
                                                     'authors': authors,
                                                     'years': years})
    elif request.method == 'POST':
        if request.POST.get('year') is not None:
            Year(year=unicode(request.POST['year'])).save()
            years = Year.category().instance.all()
        return render(request, 'jinja2/years.html', {'verses': verses,
                                                     'authors': authors,
                                                     'years': years})


def like(request):
    verse_id = unicode(request.POST.get('id'))
    verse = Verse.index.get(name=verse_id)
    verse.likes += 1
    verse.save()
    return HttpResponse(verse.likes)
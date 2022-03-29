from django import views
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from DictionaryWebpage import models


@csrf_exempt
def index(request):
    if request.method == "GET":
        word = request.GET.get('word', '')
        if 'word' in request.GET:
            b = models.Word.objects.filter(word=word)
            return render(request, 'index.html', {'word': word, 'definition': b[0]})
        else:
            return render(request, 'index.html', {'word': word})

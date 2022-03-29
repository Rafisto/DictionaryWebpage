from django import views
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if request.method == "GET":
        word = request.GET.get('word', '')
        if 'word' in request.GET:
            print(request.GET['word'])
        return render(request, 'index.html', {'word': word})

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'boldmessage': 'Crunchy creamy cupcake yo'
    }
    return render(request, 'rango/index.html', context=context)


def about(request):
    html = "<html><head></head><body>Hi there. <a href='/rango/'>Go back to home page.</a></body></html>"
    return HttpResponse(html)

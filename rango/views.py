from django.shortcuts import render


def index(request):
    context = {
        'boldmessage': 'Crunchy creamy cupcake yo'
    }
    return render(request, 'rango/index.html', context=context)


def about(request):
    return render(request, 'rango/about.html', context={})

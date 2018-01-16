from django.http import HttpResponse


def index(request):
    html = "<html><head></head><body>Hi there. <a href='/rango/about/'>About page</a></body></html>"
    return HttpResponse(html)


def about(request):
    html = "<html><head></head><body>Hi there. <a href='/rango/'>Go back to home page.</a></body></html>"
    return HttpResponse(html)

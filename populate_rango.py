import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
django.setup()
from rango.models import Category, Page


def populate():
    python_pages = [
        {"title": "Official Python Tutorial",
         "url": "https://docs.python.org/2/tutorial/",
         "views": 10},
        {"title": "How to Think like a Computer Scientist",
         "url": "https://www.greenteapress.com/thinkpython",
         "views": 5},
        {"title": "Learn Python in 10 Minutes",
         "url": "https://www.korokithakis.net/tutorials/python/",
         "views": 7}
    ]

    django_pages = [
        {"title": "Official Django Tutorial",
         "url": "https://docs.djangoproject.com/en/1.9/intro/tutorial01/",
         "views": 100},
        {"title": "Django Rocks",
         "url": "https://djangorocks.com/",
         "views": 70},
        {"title": "How to Tango with Django",
         "url": "https://tangowithdjango.com/",
         "views": 10}
    ]

    other_pages = [
        {"title": "Bottle",
         "url": "https://bottlepy.org/docs/dev/",
         "views": 1},
        {"title": "Flask",
         "url": "https://flask.pocoo.org",
         "views": 43}
    ]

    cats = {
        "Python": {"pages": python_pages, "likes": 64, "views": 128},
        "Django": {"pages": django_pages, "likes": 32, "views": 64},
        "Other Frameworks": {
            "pages": other_pages, "likes": 16, "views": 32
        }
    }

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data.get("likes"), cat_data.get("views"))
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"], p["views"])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title, views=views)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name, likes, views):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    c.save()
    return c


if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()

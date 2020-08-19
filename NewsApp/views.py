from django.shortcuts import render
#from django.shortcuts import HttpResponse
from .models import News

def Home(request):
    context = {
        "name":"Jing",
        "number":2323
    }
    return render(request, 'home.html', context)

def NewsP(request):
    obj = News.objects.get(id=1)
    context = {
        #"list":["python", "Java", "C++", "C#"],
        #"mynum":50
        "data":obj
    }
    return render(request, 'news.html', context)

def NewsDate(request, year):
    article_list = News.objects.filter(pub_date__year = year)
    context = {
        'year':year,
        'article_list':article_list
    }
    return render(request, 'newsdate.html', context)



def Contact(request):
    return render(request, 'contact.html')
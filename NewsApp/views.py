from django.shortcuts import render
from django.shortcuts import HttpResponse

def Home(request):
    context = {
        "name":"Jing",
        "number":2323
    }
    return render(request, 'home.html', context)

def News(request):

    context = {
        #"list":["python", "Java", "C++", "C#"],
        #"mynum":50
    }
    return render(request, 'news.html', context)



def Contact(request):
    return render(request, 'contact.html')
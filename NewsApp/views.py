from django.shortcuts import render, redirect
#from django.shortcuts import HttpResponse
from .models import News
from .forms import RegestrationForm
from .models import RegistrationData

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


def register(request):
    context = {
        "form" : RegestrationForm
    }
    return render(request, 'signup.html', context)


def addUser(request):
    form = RegestrationForm(request.POST)

    if form.is_valid():
        myregister = RegistrationData (username = form.cleaned_data['username'],
                                     password=form.cleaned_data['password'],
                                     email=form.cleaned_data['email'],
                                     phone=form.cleaned_data['phone'],
                                     )
        myregister.save()

    return redirect('home')
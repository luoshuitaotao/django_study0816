from django.urls import path
from .views import NewsP, Home, Contact, NewsDate


urlpatterns = [
    path ('', Home, name='home'),
    path('news/', NewsP, name='news'),
    path ('contact/', Contact, name='contact'),
    path ('newsdate/<int:year>', NewsDate, name='newsdate'),

]
from django.urls import path
from .views import NewsP, Home, Contact, NewsDate, register, addUser, modelform, addModalForm


urlpatterns = [
    path ('', Home, name='home'),
    path('news/', NewsP, name='news'),
    path ('contact/', Contact, name='contact'),
    path ('newsdate/<int:year>', NewsDate, name='newsdate'),
    path ('signup/', register, name ='register'),
    path ('addUser/', addUser, name = 'addUser'),
    path ('modalform/', modelform, name = 'form'),
    path('addModalForm/', addModalForm, name = 'addModalForm')

]
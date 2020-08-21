from django.contrib import admin
from .models import Article, Reporter, Place, Restaurant

admin.site.register(Article)
admin.site.register(Reporter)
admin.site.register(Place)
admin.site.register(Restaurant)
from django.contrib import admin
from .models import Movie, Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title',)

    filter_horizontal = ('cast', 'crew')
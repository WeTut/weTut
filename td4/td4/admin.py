from django.contrib import admin
from movies.models import *

class DirectorAdmin(admin.ModelAdmin):
	model = Director

class CountryAdmin(admin.ModelAdmin):
	model = Country

class MovieAdmin(admin.ModelAdmin):
	model = Movie
	date_hierarchy = 'year'


admin.site.register(Director, DirectorAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Movie, MovieAdmin)
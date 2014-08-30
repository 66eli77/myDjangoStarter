from django.contrib import admin

# Register your models here.
from.models import Movie

class MovieAdmin(admin.ModelAdmin):
    class Meta:
        model = Movie
        
admin.site.register(Movie, MovieAdmin)
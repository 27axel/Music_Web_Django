from django.contrib import admin
from .models import Anketa, Price, Cart, Tonal, DrumKit, Genre, Catalog


class PlaylistAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Anketa)
admin.site.register(Price)
admin.site.register(Cart)
admin.site.register(Tonal)
admin.site.register(DrumKit)
admin.site.register(Genre)
admin.site.register(Catalog, PlaylistAdmin)



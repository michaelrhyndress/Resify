from django.contrib import admin
from ATS.models import Keyword, Category

class KeywordAdmin(admin.ModelAdmin):
    # exclude = ('popularity',)
    list_display = ('word', 'num_synonyms', 'popularity',)
    filter_horizontal=('synonyms',)
    search_fields = ['word']
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'num_entries',)
    filter_horizontal=('words',)
    search_fields = ['title']
    
admin.site.register(Keyword, KeywordAdmin)
admin.site.register(Category, CategoryAdmin)

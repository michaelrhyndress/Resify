from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class Keyword(models.Model):
    word=models.CharField(max_length=250, blank=False, unique=True)
    popularity=models.PositiveIntegerField(default=0)
    synonyms=models.ManyToManyField("self", blank=True, null=True)
    word_type=models.CharField(max_length=15, blank=True, unique=False)
    
    class Meta:
        ordering = ['word']
    def __str__(self):
        return self.word
        
    def length(self):
        return len(self.word)
        
    def num_synonyms(self):
        return self.synonyms.count()
        
        
class Category(models.Model):
    """ Class to maintain certain catagories. Such as Computer Science, HealthCare, etc."""
    title = models.CharField(max_length=250, blank=False, unique=True) # one to one with tags
    words = models.ManyToManyField(Keyword,  blank=True)
    
    class Meta:
        ordering = ['title']
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.title
        
    def num_entries(self):
        return self.words.count() 
from django.db import models

# Create your models here.

# TODO: Add default 0 in database for field quantity

class Tovar(models.Model):
    title = models.CharField(max_length=255, unique=True)
    article = models.CharField(max_length=16, null=True, blank=True, unique=True)
    description = models.TextField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0, blank=True)
    group = models.ForeignKey('tovar.Group', on_delete = models.PROTECT, null=True)
    tags = models.ManyToManyField('tovar.Tag')
    
    
    
    def __str__(self):
        if self.article is None:
            return '{2} (---) {0}'.format(self.title, self.pk)
        else:
            return '{2} ({0}) {1}'.format(self.article, self.title, self.pk)
        
        
        
class Group(models.Model):
    title = models.CharField(max_length=120, unique=True)
    code = models.CharField(max_length=10, unique=True)
    skoro = models.NullBooleanField()
    
    @property
    def full_title(self):
        return '({0}) {1}'.format(self.code, self.title)
    
    def __str__(self):
        return self.full_title
        

class Tag(models.Model):
    title = models.CharField(max_length=32, primary_key=True)
    
    def __str__(self):
        return self.title
    
    

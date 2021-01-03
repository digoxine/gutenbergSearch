from django.db import models

# Create your models here.
class Author(models.Model):
    name            = models.CharField(max_length=200, primary_key=True)
    birthDate       = models.DateTimeField('Date of birth')
    deathDate       = models.DateTimeField('Date of death')

class Translator(models.Model):
    name            = models.CharField(max_length=200, primary_key=True)
    birthDate       = models.DateTimeField('Date of birth')
    deathDate       = models.DateTimeField('Date of death')


class Book(models.Model):
    ebookId         = models.CharField(max_length=100, primary_key=True)
    title           = models.CharField(max_length=200)
    translators     = models.ManyToManyField(Translator)
    authors         = models.ManyToManyField(Author)
    releaseDate     = models.DateTimeField('Date of publication')
    language        = models.CharField(max_length=100)
    downloads       = models.IntegerField()
    subject         = models.CharField(max_length=300)
    category        = models.CharField(max_length=100)

    class Meta:
        order_with_respect_to = 'releaseDate'
        


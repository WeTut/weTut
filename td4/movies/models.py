from django.db import models

class Director(models.Model):
    slug = models.SlugField(max_length=200)
    name = models.CharField(max_length=200)
    forename = models.TextField()

    def __unicode__(self):
        return "%s %s" % (self.forename, self.name)


class Country(models.Model):
    slug = models.SlugField(max_length=200)
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return "%s" % (self.name)


class Movie(models.Model):
    slug = models.SlugField(max_length=200)
    title = models.CharField(max_length=200)
    picture = models.ImageField(title, upload_to='img/movies')
    year = models.DateField()
    synopsis = models.CharField(max_length=1000)
    director = models.ForeignKey('director')
    country = models.ForeignKey('country')

    def __unicode__(self):
        return "%s" % (self.title)
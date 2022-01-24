from django.db import models


class Pokemon(models.Model):
    attack = models.CharField(max_length=50)
    number = models.IntegerField()
    featured_image = models.ImageField(null=True, blank=True, default="Pokemon-logo-tumb.jpg")
    pokemon_name = models.CharField(max_length=50)
    tags = models.ManyToManyField('pokemon', blank=True)
    
    def __str__(self):
        return self.pokemon_name


class Type(models.Model):
    TYPE_POKEMONS = (
        ('fire', 'Fire'),
        ('water', 'Water'),
        ('grass', 'Grass')
    )
    type = models.CharField(max_length=50, choices=TYPE_POKEMONS)


class Color(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.color
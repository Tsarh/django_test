from django.db import models

class Author(models.Model):
    name = models.CharField(max_length = 70, unique = True, verbose_name = "Nom")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Auteur"
        verbose_name_plural = "Auteurs"

class Book(models.Model):
    title = models.CharField(max_length = 70, unique = True, verbose_name = "Titre")
    quantity = models.IntegerField(default = 1, verbose_name = "Quantité")
    author = models.ForeignKey(Author, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Livre"
        verbose_name_plural = "Livres"
        permissions = [
            ('apply_promo_code','peut appliquer des réductions')
        ]
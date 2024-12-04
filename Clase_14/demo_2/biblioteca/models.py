from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField()
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
    
    
class Genero(models.Model):
    nombre = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.nombre



class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    fecha_publicacion = models.DateField(("Fecha de publicación"), auto_now=False, auto_now_add=False)
    autor = models.ManyToManyField('Autor')
    genero = models.ForeignKey('Genero', on_delete=models.SET_NULL, null=True)
    

    def __str__(self):
        return self.titulo




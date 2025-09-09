from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=50)
    
    def __str___(self):
        return f'{self.nombre} {self.apellido}'
    
class Libro(models.Model):
    GENEROS = [
        ('ficcon', 'Ficción'),
        ('no_ficcion', 'No Ficción'),
        ('fantasia', 'Fantasía'),
        ('ciencia', 'Ciencia'),
        ('historia', 'Historia'),
    ]
    
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='libros')
    fecha_publicacion = models.DateField()
    genero = models.CharField(max_length=20, choices=GENEROS)
    paginas = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        return self.titulo
    
class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_prestamo = models.DateTimeField(autor_now_add=True)
    fecha_devoluvion = models.DateTimeField(null=True, blank=True)
    devuelto = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.libro.titulo} prestado a {self.usuario.username}'
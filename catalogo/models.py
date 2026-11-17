from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"


class Videojuego(models.Model):
    # Relación 1:N con Categoría (el padre)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='videojuegos'
    )
    # 4 campos variados
    titulo = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_lanzamiento = models.DateField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
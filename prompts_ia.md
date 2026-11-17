# Bitácora de Inteligencia Artificial (RTCF)

## Prompt 1 — Creación del Modelo Relacional
- **Rol:** Eres un desarrollador experto en Django y bases de datos relacionales.
- **Tarea:** Crear dos modelos (Categoria y Videojuego) con una relación de uno a muchos (ForeignKey).
- **Contexto:** Proyecto Django llamado Prueba3 conectado a MySQL. El modelo Videojuego debe tener 4 campos variados: texto (titulo), decimal (precio), fecha (fecha_lanzamiento) y booleano (disponible).
- **Formato:** Código Python limpio para pegar en models.py, incluyendo el método __str__ y la clase Meta para los nombres en español.

## Prompt 2 — Optimización de ListView con select_related
- **Rol:** Eres un desarrollador senior de Django enfocado en rendimiento.
- **Tarea:** Escribir una ListView para mostrar los Videojuegos optimizando la consulta a la base de datos.
- **Contexto:** El modelo Videojuego tiene una ForeignKey hacia Categoria. Al listar los videojuegos en el catálogo, se genera el problema de consultas N+1.
- **Formato:** Código Python para views.py, utilizando `select_related('categoria')` dentro del método `get_queryset` y explicando brevemente por qué soluciona el problema.
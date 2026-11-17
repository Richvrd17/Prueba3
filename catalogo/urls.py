from django.urls import path
from . import views

urlpatterns = [
    path('', views.VideojuegoListView.as_view(), name='lista'),
    path('videojuego/<int:pk>/', views.VideojuegoDetailView.as_view(), name='detalle'),
    path('videojuego/nuevo/', views.VideojuegoCreateView.as_view(), name='crear'),
    path('videojuego/<int:pk>/editar/', views.VideojuegoUpdateView.as_view(), name='editar'),
    path('videojuego/<int:pk>/eliminar/', views.VideojuegoDeleteView.as_view(), name='eliminar'),
]
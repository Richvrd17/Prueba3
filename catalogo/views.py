from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Videojuego
from .forms import VideojuegoForm

class VideojuegoListView(ListView):
    model = Videojuego
    template_name = 'catalogo/lista.html'
    context_object_name = 'videojuegos'

    def get_queryset(self):
        return Videojuego.objects.select_related('categoria').order_by('titulo')

class VideojuegoDetailView(DetailView):
    model = Videojuego
    template_name = 'catalogo/detalle.html'
    context_object_name = 'videojuego'

class VideojuegoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Videojuego
    form_class = VideojuegoForm
    template_name = 'catalogo/form.html'
    success_url = reverse_lazy('lista')
    success_message = "¡Videojuego creado exitosamente!"

class VideojuegoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Videojuego
    form_class = VideojuegoForm
    template_name = 'catalogo/form.html'
    success_url = reverse_lazy('lista')
    success_message = "Videojuego actualizado correctamente."

class VideojuegoDeleteView(LoginRequiredMixin, DeleteView):
    model = Videojuego
    template_name = 'catalogo/confirmar_eliminar.html'
    success_url = reverse_lazy('lista')
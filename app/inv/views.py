from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from .forms import CategoriaForm
from django.urls import reverse_lazy

from .models import Categoria

class CategoriaView(LoginRequiredMixin,ListView):
    model = Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'
    
class CategoriaNew(LoginRequiredMixin,CreateView):
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class= CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')
    login_url = 'bases:login'
    
    def form_valid(self,form):
        form.instance.uc=self.request.user
        return super().form_valid(form)
    
class CategoriaEdit(LoginRequiredMixin,UpdateView):
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class= CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')
    login_url = 'bases:login'
    
    def form_valid(self,form):
        form.instance.um=self.request.user.id
        return super().form_valid(form)
    
class CategoriaDel(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = "inv/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy('inv:categoria_list')
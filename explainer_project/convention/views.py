from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)
class IndexView(CreateView):
    title = 'Test'
    template_name = 'index.html'

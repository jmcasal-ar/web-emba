from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import Carrera, Area
from news.models import News
# Create your views here.
class CarreraListView(ListView):
    model = Carrera
    template_name = 'carreras/carreras_list.html'

class CarreraDetailView(DetailView):
    model = Carrera


class AreaDetailView(DetailView):
    model = Area


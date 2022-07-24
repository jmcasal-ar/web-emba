from django.shortcuts import render, get_object_or_404
from .models import Page
from django.views.generic.detail import DetailView
 
# Create your views here.
class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/page_detail.html'
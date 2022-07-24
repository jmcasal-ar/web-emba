from django.urls import path
from .views import CarreraListView, CarreraDetailView, AreaDetailView


carreras_patterns = ([
    path('', CarreraListView.as_view(), name='carreras_list'),
    path('<int:pk>/<slug:slug>/', CarreraDetailView.as_view(), name='carrera'),
    path('category/<int:pk>/<slug:slug>/', AreaDetailView.as_view(), name='area'),
], "carreras")
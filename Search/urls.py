from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.results, name='results'),
    path('results/prompt/', views.prompt, name='prompt'),
]
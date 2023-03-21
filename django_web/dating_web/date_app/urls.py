from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('match_tester/', views.match_tester, name='match_tester'),
    path('results/', views.results, name="results")
]
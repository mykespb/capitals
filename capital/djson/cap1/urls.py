from django.urls import path

from . import views

urlpatterns = [
    path ('categories/<int:num>/', views.categories, name="categories"),
    path ('categories/', views.categories, name="categories"),
]

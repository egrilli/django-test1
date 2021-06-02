from django.urls import path     
from . import views
urlpatterns = [
    path('', views.root),
    path('blogs', views.index),
    path('blogs/new', views.new),
    path('blogs/create', views.create),
    path('blogs/<int:number1>,<int:number2>',views.show),
    path('blogs/<number>/delete',views.destroy ),
    path('blogs/json',views.bjason)
]
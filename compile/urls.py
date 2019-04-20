from django.urls import path , include
from compile import views

urlpatterns = [
	path('', views.index),
	path('run/', views.run),
]
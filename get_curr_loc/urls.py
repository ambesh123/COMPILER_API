from django.urls import path
from get_curr_loc import views

urlpatterns = [
	path('' , views.index),
]
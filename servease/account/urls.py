from django.urls import path
from . import views 

app_name = 'account'

urlpatterns = [
	path('index/', views.index, name='index'),
	# path('<int:pk>/', views.detail, name="detail"),

]
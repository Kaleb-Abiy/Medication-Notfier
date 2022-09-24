from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:id>', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_medication, name='add_med'),
    path('reminder/', views.reminder, name='reminder')
]
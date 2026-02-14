from django.urls import path
from . import views

urlpatterns = [
    path('', views.toogle_list, name='toogle_list'),

    path('create/', views.toogle_create, name='toogle_create'),

    path('<int:toogle_id>/edit/', views.toogle_edit, name='toogle_edit'),

    path('<int:toogle_id>/delete/', views.toogle_delete, name='toogle_delete'),
   
    path('register/', views.register, name='register'),
   
]
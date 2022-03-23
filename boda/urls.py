from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('confirmacion/', views.confirmacion_create_view, name='confirmacion'),
    path('inscripcion/realizada', views.SuccessForm, name='form_success'),
    path('acceso/', views.password_view, name='password'),
]

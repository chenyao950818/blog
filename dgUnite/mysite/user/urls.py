from django.urls import path
from . import views

urlpatterns=[
    path('reg/', views.reg, name='reg'),
    path('go/', views.go, name='go'),
    path('goout/', views.goout, name='goout'),

]
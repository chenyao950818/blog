from django.urls import path
from . import views

urlpatterns=[
    path('', views.display, name='display'),
    path('write/', views.write, name='write'),
    path('article/', views.article, name='article'),
    path('text_create/', views.text_create, name='text_create'),
    path('text_update/', views.text_update, name='text_update'),
    path('text_delete/', views.text_delete, name='text_delete'),
    path('article_create/', views.article_create, name='article_create'),
    path('article_post/', views.article_post, name='article_post'),
    path('article_del/', views.article_del, name='article_del'),
    path('upload_ajax/', views.upload_ajax, name='upload_ajax'),
]
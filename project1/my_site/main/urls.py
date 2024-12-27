from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('page', views.page, name='page'),
    path('test', views.test, name='test' )
]
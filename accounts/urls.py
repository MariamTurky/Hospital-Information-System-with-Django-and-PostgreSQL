from django.urls import path
from . import views

urlpatterns = [
    path('signa', views.signa, name='signa'),
    path('signd', views.signd, name='signd'),
    path('signn', views.signd, name='signn'),
    path('signp', views.signp, name='signp')
]
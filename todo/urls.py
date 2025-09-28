from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.check,name='check'),
    path('home/',views.display_view,name='home')
]
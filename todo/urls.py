from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.check,name='check'),
    path('home/',views.display_view,name='home'),
    path('add/',views.add_view,name='add'),
    path('edit/<int:pk>/',views.edit_view,name='edit'),
    path('delete/<int:pk>/',views.delete_view,name='delete'),
    path('')
]
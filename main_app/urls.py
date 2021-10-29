from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('handleForm', views.handleForm, name='handleForm'),
    path('delete/<int:widget_id>', views.delete, name="delete")
]